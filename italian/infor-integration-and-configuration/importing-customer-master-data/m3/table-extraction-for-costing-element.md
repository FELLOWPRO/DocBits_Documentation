# Estrazione della tabella per l'elemento di costo

<figure><img src="../../../.gitbook/assets/docbits_m3_costing_element_table_it.jpg" alt="Docbits M3 Costing Element Table It"><figcaption></figcaption></figure>

Per attivare l'estrazione della tabella per l'elemento di costo, dovrai importare la tabella m3costingelement in DocBits.

Dalla Homepage di M3, digita Comando + r e cerca il prompt “PPS280”.

Seleziona una delle righe visualizzate. Nel menu successivo, seleziona STRUMENTI e “Esporta in Excel”.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FI8SYWm-JwpyYRHFUp2obGtXcsa7m_blJ_lTrnhczztRIXIN5gfxCt3eRw6ZI42fH6AwnsKyv4ux5-rhaT505PsyDFFI_anUNvmACFyx_ssgxaqWq25vLt_E5s310HNoiPPLf35qJlYtstjpj5Cc4aB4\&width=768\&dpr=4\&quality=100\&sign=5aa04ccf\&sv=2)

Seleziona “Esporta tutte le righe” e poi premi ESPORTA.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FwtjHI9L4YUhf-yJFjcPGu218Vis_zELtCIfpmkIUKgasfrdfNW-dr_J1DqXlfD-SBrnVduDrMLAIAQh6UTlzBqEP_JPXP48elGMyGj0ByZbX7TpqlnIfRZ4ZoD0pyCo-AKigeKjlHN6cFcdpeClZ9L4\&width=768\&dpr=4\&quality=100\&sign=7cf7a274\&sv=2)

Una volta scaricato, dovrai modificare il file Excel prima di convertirlo in un file CSV.

Dovrai aprire il file Excel, che apparirà simile a quanto mostrato di seguito.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmR6GtTDYMGf48yc3GCau%252Fimage.png%3Falt%3Dmedia%26token%3Daf52d75f-bdb9-4b18-a4b0-572b76e14309\&width=768\&dpr=4\&quality=100\&sign=57660254\&sv=2)

Da questo foglio Excel hai bisogno delle colonne A, B, H, J, K e I, modifica il foglio Excel in modo che il risultato finale appaia come segue.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FajTC0UO55QZRMDyhBxm1%252Fimage.png%3Falt%3Dmedia%26token%3D5b29b038-8156-4e67-8536-e0bcb65c35ff\&width=768\&dpr=4\&quality=100\&sign=5e46e6c2\&sv=2)

Una volta fatto, salva il file come CSV.

Una volta che hai il tuo file CSV, vai alla seguente pagina web. Questo dipende dall'ambiente che stai utilizzando:

* Prod: http://api.docbits.com/
* Sandbox: http://sandbox.api.docbits.com/
* Stage: http://stage.api.docbits.com/
* Demo: http://demo.api.docbits.com/
* Dev: http://dev.api.docbits.com/

Qui caricherai manualmente la tabella CostingElement tramite un'API. Clicca sul pulsante Autorizza.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FtyzOq3BR2QqTguQFKicxo0dE5j5hGsP-BhfVbS81O_mxN5bSVp40jYfgsVJcE_rBLFMDJNvbPkPIdjPqaqoNbHBBM-9hx0i-U4VAH9ISBYhpwKgqQeUEd67VV1E4izwNyxbAwwrhCmrAo1uIKhLherY\&width=768\&dpr=4\&quality=100\&sign=188f5712\&sv=2)

Qui dovrai inserire la chiave API dal tuo ambiente DocBits. Questa si trova in Impostazioni sotto Integrazione.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F4ADnevq6kq_vbxUJpyPbHNcGvRvpO-l9Gwd8ZaYf_vO4uWhSl1jmKNpddmHGc9ZHMMbXCgLOElLDYbNwB3INmBDETecPrDnpI601IUOZQlT7tc7OLSPXwkooOJFNwML2i_gvBPuE8CvfwRpX-ZIlb_g\&width=768\&dpr=4\&quality=100\&sign=dedfcaaf\&sv=2)

Una volta completato, cerca l'API chiamata master\_data\_lookup/import\_data e compila le informazioni richieste. Una volta completato, clicca ESEGUI per attivare l'API.

### data\_type deve essere costing\_element

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F8UD4FhFv2dRB4cMjCDL4G9ndjH7laVMKWqdeMaJGgEo48-UVvucB1uOydzNdfFy0yPM5bb66mZB4k9uJR7TTiEREGFaV2EqW01gxJpTyuUfGNh5QmBjySkyhZ56gWV8sYs8WI5RnHcENtXgjTU0vg0Q\&width=768\&dpr=4\&quality=100\&sign=7c9f4dbb\&sv=2)

Se fatto correttamente, la tabella M3CostingElement dovrebbe ora essere nel tuo ambiente DocBits. L'estrazione della tabella per gli elementi di costo è stata ora configurata per il tuo ambiente.
