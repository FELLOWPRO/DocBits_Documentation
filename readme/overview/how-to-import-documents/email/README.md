# Email

Go to the Settings menu and select “Import” under Document Processing.

![](https://lh7-us.googleusercontent.com/W5ed9OceL0beNPMDpWVn-U25OAA6zQsSqnl-GXcg-mjKQTiKNgNYwjxAlWSiLbXfeO-XgI2KI0CDAfDH71bqWO1Y2JRrRznA\_N8DudvQw1yWr3McWJ7yWLGG7kHau5IM2Rmya1SkzsEGQaP53KdtbGA)

Scroll to the bottom of the page and select the NEW button to create a new email import.

![](https://lh7-us.googleusercontent.com/Df5po54NF-aX0zq22r2dcwaP9GmXX26IYOO4yOy6CWMYUzIPc03UObniHGLlUBU6ybBMaaYCIXt2YslnhhZWekGozu4JKo-Kd3CzjVDBNzv7GVR0BnWvAfmfR1izmzhWGIwgzIkk-YGvUVIEvXoNhak)

After pressing NEW, the following menu will be shown to you.

![](https://lh7-us.googleusercontent.com/1m9KmI9T5icR7Ib-URDVvYhEJlXpVDiPaAf7yaqgitgVl1mEmehHvuZRPwzmQU36bbmCui0Nx7xczp789VWsiodtZtuQw6zKxmZDTLQ5DR27AzbkoPX0WwGfW5SZQfCtqH2ohBo28Z2W3fFTKGQVWOI)

Here you can select which Protocol you would like.

![](https://lh7-us.googleusercontent.com/nikZZGemqPpldbGBirUP7d4QAoBikHCay9Ptk8PSVft9zPkZeKuoH9gfK2ar53MpslTjw4GhldbrCw6phn1VV1Y7MMfgaZLnXaXjjERJV8pFUoyIG8Z760P3\_2DjQFUKZYMCagXBzaTm52ii5tPl8C0)

## Desteklenen belge ekleri

Her iki e-posta içe aktarma yöntemi de şu belge eklerini kabul eder:

| Biçim | Dosya uzantıları | Tipik kullanım |
| --- | --- | --- |
| PDF | `.pdf` | Fatura ve diğer PDF belgeler |
| TIFF | `.tif`, `.tiff` | Taranan belgeler |
| XML | `.xml` | Yapılandırılmış elektronik belgeler |
| EDI / sipariş verisi | `.edi`, `.purchaseorder` | Elektronik veri değişimi ve satın alma siparişleri |

Bir iletme hizmeti PDF, TIFF veya XML dosyasını genel (generic) ek olarak etiketlerse, DocBits bu dosyayı içerikten veya bilinen bir dosya uzantısından tanıyabilir. İletilen `.eml` mesajları da desteklenen belgeler içerebilir; DocBits bu iç içe geçmiş ekleri içe aktarmadan önce çıkarır.

PNG, JPG, GIF ve BMP gibi görseller belge olarak içe aktarılmaz. İletilen e-postalardaki imza görselleri ve logolar atlanır. Word, Excel ve PowerPoint gibi Office dosyaları bu e-posta içe aktarma yöntemleri tarafından desteklenmez.

İletilen e-postalarda bir belge eksikse **Inbound Emails** altındaki **Logs** bölümünü kontrol edin. **Notify sender when import fails** etkin olduğunda, gönderene bir açıklama ve bu sayfanın bağlantısı içeren bir bildirim gönderilir. Bağlı bir posta kutusu için [IMAP](imap.md) veya [OAuth (Office 365)](oauth-office365.md) kurulum rehberini kullanın.
