"""Correct measured residual loudness after the existing two-pass normalizer."""
import json
import math
from pathlib import Path
from mux import run


def measure(path):
    result=run(['-i',path,'-af','loudnorm=I=-16:TP=-1:LRA=11:print_format=json','-vn','-f','null','-'])
    return json.JSONDecoder().raw_decode(result.stderr[result.stderr.rfind('{'):])[0]


def correct_residual(path):
    path=Path(path)
    before=measure(path)
    integrated=float(before['input_i'])
    peak=float(before['input_tp'])
    if not math.isfinite(integrated) or not math.isfinite(peak):
        raise ValueError('Invalid normalized PCM measurement')
    # Preserve peak headroom for the later AAC encoding. Fail if both targets
    # cannot be met by a constant gain; never weaken the final AAC checks.
    gain=min(-16-integrated,-1.5-peak)
    if abs(integrated+gain+16)>.35:
        raise ValueError('PCM requires a different limiter pass')
    target=path.with_name(path.stem+'.corrected.wav')
    run(['-v','error','-i',path,'-af',f'volume={gain:.6f}dB','-ar','48000','-ac','2','-c:a','pcm_s16le',target])
    target.replace(path)
    return {'before_lufs':integrated,'before_peak_dbtp':peak,'constant_gain_db':round(gain,6),'target_lufs':-16}
