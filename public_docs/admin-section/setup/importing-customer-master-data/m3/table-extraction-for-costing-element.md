# Tabellenextraktion für Kostenelemente

<figure><img src="../../../../.gitbook/assets/docbits_settings_email.png" alt="Einstellungen E-Mail Import Bestellung Tabelle Übersicht"><figcaption></figcaption></figure>

Um den Tabellenextraktion für Kostenelemente zu aktivieren, müssen Sie die m3costingelement-Tabelle in DocBits importieren.

Gehen Sie von der M3-Startseite aus auf Command + r und suchen Sie die Eingabeaufforderung „PPS280“.

Wählen Sie eine der angezeigten Zeilen aus. Wählen Sie im nächsten Menü die OPTIONEN und „In Excel exportieren“.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FI8SYWm-JwpyYRHFUp2obGtXcsa7m_blJ_lTrnhczztRIXIN5gfxCt3eRw6ZI42fH6AwnsKyv4ux5-rhaT505PsyDFFI_anUNvmACFyx_ssgxaqWq25vLt_E5s310HNoiPPLf35qJlYtstjpj5Cc4aB4\&width=768\&dpr=4\&quality=100\&sign=5aa04ccf\&sv=2)

Wählen Sie „Alle Zeilen exportieren“ und drücken Sie dann EXPORTIEREN.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FwtjHI9L4YUhf-yJFjcPGu218Vis_zELtCIfpmkIUKgasfrdfNW-dr_J1DqXlfD-SBrnVduDrMLAIAQh6UTlzBqEP_JPXP48elGMyGj0ByZbX7TpqlnIfRZ4ZoD0pyCo-AKigeKjlHN6cFcdpeClZ9L4\&width=768\&dpr=4\&quality=100\&sign=7cf7a274\&sv=2)

Nach dem Herunterladen müssen Sie die Excel-Datei ändern, bevor Sie sie in eine CSV-Datei umwandeln.

Sie müssen die Excel-Datei öffnen, sie wird ähnlich aussehen wie unten gezeigt.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmR6GtTDYMGf48yc3GCau%252Fimage.png%3Falt%3Dmedia%26token%3Daf52d75f-bdb9-4b18-a4b0-572b76e14309\&width=768\&dpr=4\&quality=100\&sign=57660254\&sv=2)

Von diesem Excel-Blatt benötigen Sie die Spalten A, B, H, J, K und I. Ändern Sie das Excel-Blatt so, dass das Endergebnis wie folgt aussieht.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FajTC0UO55QZRMDyhBxm1%252Fimage.png%3Falt%3Dmedia%26token%3D5b29b038-8156-4e67-8536-e0bcb65c35ff\&width=768\&dpr=4\&quality=100\&sign=5e46e6c2\&sv=2)

Sobald dies erledigt ist, speichern Sie die Datei als CSV.

Sobald Sie Ihre CSV-Datei haben, gehen Sie zu der folgenden Webseite. Dies hängt davon ab, welche Umgebung Sie verwenden:

* Prod: http://api.docbits.com/
* Sandbox: http://sandbox.api.docbits.com/
* Stage: http://stage.api.docbits.com/
* Demo: http://demo.api.docbits.com/
* Dev: http://dev.api.docbits.com/

Hier laden Sie die Kostenelementtabelle manuell über eine API hoch. Klicken Sie auf die Schaltfläche Autorisieren.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FtyzOq3BR2QqTguQFKicxo0dE5j5hGsP-BhfVbS81O_mxN5bSVp40jYfgsVJcE_rBLFMDJNvbPkPIdjPqaqoNbHBBM-9hx0i-U4VAH9ISBYhpwKgqQeUEd67VV1E4izwNyxbAwwrhCmrAo1uIKhLherY\&width=768\&dpr=4\&quality=100\&sign=188f5712\&sv=2)

Hier müssen Sie den API-Schlüssel aus Ihrer DocBits-Umgebung eingeben. Dieser befindet sich in den Einstellungen unter Integration.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F4ADnevq6kq_vbxUJpyPbHNcGvRvpO-l9Gwd8ZaYf_vO4uWhSl1jmKNpddmHGc9ZHMMbXCgLOElLDYbNwB3INmBDETecPrDnpI601IUOZQlT7tc7OLSPXwkooOJFNwML2i_gvBPuE8CvfwRpX-ZIlb_g\&width=768\&dpr=4\&quality=100\&sign=dedfcaaf\&sv=2)

Sobald dies abgeschlossen ist, suchen Sie nach der API mit dem Namen master\_data\_lookup/import\_data und füllen Sie die erforderlichen Informationen aus. Klicken Sie anschließend auf AUSFÜHREN, um die API auszulösen.

### data\_type muss costing\_element sein

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F8UD4FhFv2dRB4cMjCDL4G9ndjH7laVMKWqdeMaJGgEo48-UVvucB1uOydzNdfFy0yPM5bb66mZB4k9uJR7TTiEREGFaV2EqW01gxJpTyuUfGNh5QmBjySkyhZ56gWV8sYs8WI5RnHcENtXgjTU0vg0Q\&width=768\&dpr=4\&quality=100\&sign=7c9f4dbb\&sv=2)

Wenn alles korrekt gemacht wurde, sollte die M3CostingElement-Tabelle jetzt in Ihrer DocBits-Umgebung sein. Der Tabellenextraktion für Kostenelemente wurde nun für Ihre Umgebung konfiguriert.
