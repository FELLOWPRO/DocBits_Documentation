# Tabelextractie voor kostenelement

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FhfKR7nRoSOXm7ms0X7P2%252FBildschirmfoto%25202024-09-20%2520um%252013.42.20.png%3Falt%3Dmedia%26token%3Dff914785-1bd7-41c5-a6c0-413058dbe9fc\&width=768\&dpr=4\&quality=100\&sign=2616709f\&sv=2)

Om de tabelextractie voor kostenelement in te schakelen, moet je de m3kostenelementtabel in DocBits importeren.

Typ vanaf de M3-startpagina Command + r en zoek de prompt “PPS280”.

Selecteer een van de weergegeven regels. Kies in het volgende menu voor HULPMIDDELEN en “Exporteer naar Excel”.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FI8SYWm-JwpyYRHFUp2obGtXcsa7m_blJ_lTrnhczztRIXIN5gfxCt3eRw6ZI42fH6AwnsKyv4ux5-rhaT505PsyDFFI_anUNvmACFyx_ssgxaqWq25vLt_E5s310HNoiPPLf35qJlYtstjpj5Cc4aB4\&width=768\&dpr=4\&quality=100\&sign=5aa04ccf\&sv=2)

Selecteer “Exporteer alle rijen” en druk vervolgens op EXPORTEREN.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FwtjHI9L4YUhf-yJFjcPGu218Vis_zELtCIfpmkIUKgasfrdfNW-dr_J1DqXlfD-SBrnVduDrMLAIAQh6UTlzBqEP_JPXP48elGMyGj0ByZbX7TpqlnIfRZ4ZoD0pyCo-AKigeKjlHN6cFcdpeClZ9L4\&width=768\&dpr=4\&quality=100\&sign=7cf7a274\&sv=2)

Zodra het is gedownload, moet je het Excel-bestand aanpassen voordat je het in een CSV-bestand converteert.

Je moet het Excel-bestand openen, het zal er ongeveer zo uitzien als hieronder weergegeven.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmR6GtTDYMGf48yc3GCau%252Fimage.png%3Falt%3Dmedia%26token%3Daf52d75f-bdb9-4b18-a4b0-572b76e14309\&width=768\&dpr=4\&quality=100\&sign=57660254\&sv=2)

Van deze Excel-sheet heb je de kolommen A, B, H, J, K en I nodig, pas de Excel-sheet aan zodat het eindresultaat er als volgt uitziet.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FajTC0UO55QZRMDyhBxm1%252Fimage.png%3Falt%3Dmedia%26token%3D5b29b038-8156-4e67-8536-e0bcb65c35ff\&width=768\&dpr=4\&quality=100\&sign=5e46e6c2\&sv=2)

Zodra dit is gedaan, sla het bestand op als een CSV.

Zodra je je CSV-bestand hebt, ga naar de volgende webpagina. Dit hangt af van welke omgeving je gebruikt:

* Prod: http://api.docbits.com/
* Sandbox: http://sandbox.api.docbits.com/
* Stage: http://stage.api.docbits.com/
* Demo: http://demo.api.docbits.com/
* Dev: http://dev.api.docbits.com/

Hier kun je de CostingElement-tabel handmatig uploaden via een API. Klik op de knop Autoriseren.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FtyzOq3BR2QqTguQFKicxo0dE5j5hGsP-BhfVbS81O_mxN5bSVp40jYfgsVJcE_rBLFMDJNvbPkPIdjPqaqoNbHBBM-9hx0i-U4VAH9ISBYhpwKgqQeUEd67VV1E4izwNyxbAwwrhCmrAo1uIKhLherY\&width=768\&dpr=4\&quality=100\&sign=188f5712\&sv=2)

Hier moet je de API-sleutel van je DocBits-omgeving invoeren. Deze bevindt zich in Instellingen onder Integratie.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F4ADnevq6kq_vbxUJpyPbHNcGvRvpO-l9Gwd8ZaYf_vO4uWhSl1jmKNpddmHGc9ZHMMbXCgLOElLDYbNwB3INmBDETecPrDnpI601IUOZQlT7tc7OLSPXwkooOJFNwML2i_gvBPuE8CvfwRpX-ZIlb_g\&width=768\&dpr=4\&quality=100\&sign=dedfcaaf\&sv=2)

Zodra dit is voltooid, zoek naar de API genaamd master\_data\_lookup/import\_data en vul de vereiste informatie in. Zodra dit is voltooid, klik op UITVOEREN om de API te activeren.

### data\_type moet kostenelement zijn

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F8UD4FhFv2dRB4cMjCDL4G9ndjH7laVMKWqdeMaJGgEo48-UVvucB1uOydzNdfFy0yPM5bb66mZB4k9uJR7TTiEREGFaV2EqW01gxJpTyuUfGNh5QmBjySkyhZ56gWV8sYs8WI5RnHcENtXgjTU0vg0Q\&width=768\&dpr=4\&quality=100\&sign=7c9f4dbb\&sv=2)

Als dit correct is gedaan, zou de M3CostingElement-tabel nu in je DocBits-omgeving moeten staan. Tabelextractie voor kostenelementen is nu geconfigureerd voor je omgeving.
