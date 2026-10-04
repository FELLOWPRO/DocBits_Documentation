# Email

Go to the Settings menu and select “Import” under Document Processing.

![](https://lh7-us.googleusercontent.com/W5ed9OceL0beNPMDpWVn-U25OAA6zQsSqnl-GXcg-mjKQTiKNgNYwjxAlWSiLbXfeO-XgI2KI0CDAfDH71bqWO1Y2JRrRznA\_N8DudvQw1yWr3McWJ7yWLGG7kHau5IM2Rmya1SkzsEGQaP53KdtbGA)

Scroll to the bottom of the page and select the NEW button to create a new email import.

![](https://lh7-us.googleusercontent.com/Df5po54NF-aX0zq22r2dcwaP9GmXX26IYOO4yOy6CWMYUzIPc03UObniHGLlUBU6ybBMaaYCIXt2YslnhhZWekGozu4JKo-Kd3CzjVDBNzv7GVR0BnWvAfmfR1izmzhWGIwgzIkk-YGvUVIEvXoNhak)

After pressing NEW, the following menu will be shown to you.

![](https://lh7-us.googleusercontent.com/1m9KmI9T5icR7Ib-URDVvYhEJlXpVDiPaAf7yaqgitgVl1mEmehHvuZRPwzmQU36bbmCui0Nx7xczp789VWsiodtZtuQw6zKxmZDTLQ5DR27AzbkoPX0WwGfW5SZQfCtqH2ohBo28Z2W3fFTKGQVWOI)

Here you can select which Protocol you would like.

![](https://lh7-us.googleusercontent.com/nikZZGemqPpldbGBirUP7d4QAoBikHCay9Ptk8PSVft9zPkZeKuoH9gfK2ar53MpslTjw4GhldbrCw6phn1VV1Y7MMfgaZLnXaXjjERJV8pFUoyIG8Z760P3\_2DjQFUKZYMCagXBzaTm52ii5tPl8C0)

## Podržani prilozi u imejlovima

Oba načina uvoza putem imejla prihvataju sledeće priloge dokumenta:

| Format | Ekstenzije datoteka | Uobičajena namena |
| --- | --- | --- |
| PDF | `.pdf` | Fakture i drugi PDF dokumenti |
| TIFF | `.tif`, `.tiff` | Skenirani dokumenti |
| XML | `.xml` | Strukturirani elektronski dokumenti |
| EDI / podaci o narudžbenici | `.edi`, `.purchaseorder` | Elektronska razmena podataka i narudžbenice |

Ako servis za prosleđivanje označi PDF, TIFF ili XML datoteku kao generički prilog, DocBits može da je prepozna na osnovu sadržaja datoteke ili poznate ekstenzije. Prosleđene `.eml` poruke takođe mogu da sadrže podržane dokumente; DocBits izdvaja te unutrašnje priloge pre uvoza.

Slike kao što su PNG, JPG, GIF i BMP se ne uvoze kao dokumenti. Slike potpisa i logotipi u prosleđenim imejlovima se preskaču. Office datoteke, kao što su Word, Excel i PowerPoint, nisu podržane za ove načine uvoza putem imejla.

Kod prosleđenih imejlova proverite **Logs** (Evidentiju) u odeljku **Inbound Emails** (Dolazni imejlovi) ako dokument nedostaje. Kada je omogućena opcija **Notify sender when import fails** (Obavesti pošiljaoca kada uvoz ne uspe), pošiljalac dobija objašnjenje i link ka ovoj stranici. Za povezano sanduče pošte koristite vodič za podešavanje [IMAP](imap.md) ili [OAuth (Office 365)](oauth-office365.md).
