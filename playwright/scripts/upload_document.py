#!/usr/bin/env python3
"""Upload a document to a DocBits environment and (optionally) wait for it.

Uses the same REST endpoint the web app uses for the dashboard "Upload" button:
``POST {base}/document/process_documents`` (multipart). Authenticates with a
DocBits API key read ONLY from the ``DOCBITS_API_KEY`` env var — never hard-coded
and never accepted on the command line (CLI args leak via shell history and
process listings). This screenshot helper deliberately targets dev/stage only,
never a prod customer org.

This is the reliable upload path for documentation/screenshot automation: the
browser's QFile uploader does not accept programmatically-injected files, and the
HTTP MCP server has no access to the local filesystem.

Example:
    DOCBITS_API_KEY=... python upload_document.py \
        --file ../fixtures/docbits_demo_barcode_invoice.pdf \
        --org-id 23f3d697-7411-4c95-981d-faf089d266be \
        --doc-type INVOICE --wait
"""
from __future__ import annotations

import argparse
import os
import sys
import time

import requests

# dev/stage only by design — never upload demo fixtures to a prod customer org.
ENV_BASES = {
    "dev": "https://dev.api.docbits.com",
    "stage": "https://stage.api.docbits.com",
}


def upload(base: str, api_key: str, file_path: str, org_id: str,
           doc_type: str | None, source: str) -> dict:
    with open(file_path, "rb") as fh:
        files = {"files": (os.path.basename(file_path), fh, "application/pdf")}
        data = {"org_id": org_id, "source": source}
        if doc_type:
            data["doc_type"] = doc_type
        r = requests.post(f"{base}/document/process_documents",
                          headers={"X-API-KEY": api_key}, data=data, files=files,
                          timeout=120)
    r.raise_for_status()
    payload = r.json()
    return payload[0] if isinstance(payload, list) else payload


def wait_ready(base: str, api_key: str, doc_id: str, timeout_s: int = 300) -> str:
    """Poll the document until it leaves the 'running'/'new' states."""
    done = {"ready_for_validation", "pending_user_input", "pending_confirmation",
            "finished", "error", "validated_pending_approval"}
    deadline = time.monotonic() + timeout_s
    last = None
    while time.monotonic() < deadline:
        r = requests.get(f"{base}/document/{doc_id}",
                         headers={"X-API-KEY": api_key}, timeout=30)
        if r.ok:
            doc = r.json()
            doc = doc.get("document", doc) if isinstance(doc, dict) else {}
            last = doc.get("status")
            if last in done:
                return last
        time.sleep(4)
    return last or "timeout"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--file", required=True)
    ap.add_argument("--org-id", required=True)
    ap.add_argument("--env", default="dev", choices=ENV_BASES)
    ap.add_argument("--doc-type", default=None)
    ap.add_argument("--source", default="doc2app")
    ap.add_argument("--wait", action="store_true")
    args = ap.parse_args()

    api_key = os.environ.get("DOCBITS_API_KEY")
    if not api_key:
        sys.exit("No API key: set the DOCBITS_API_KEY env var (not a CLI arg)")

    base = ENV_BASES[args.env]
    res = upload(base, api_key, args.file, args.org_id, args.doc_type, args.source)
    doc_id = res.get("doc_id")
    print(f"uploaded doc_id={doc_id} filename={res.get('filename')}")
    if args.wait and doc_id:
        status = wait_ready(base, api_key, doc_id)
        print(f"final status={status}")


if __name__ == "__main__":
    main()
