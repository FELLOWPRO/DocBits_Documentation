# Erstellen einer IDM-Mapping-Datei

Nachdem Sie die Datei erhalten haben, öffnen Sie sie in Ihrem entsprechenden Datei-Editor Ihrer Wahl. Für diese Anleitung wird VSCode verwendet.

## Mapping-Datei bearbeiten

Überprüfen Sie, ob der Dokumenttypcode wie in DocBits angegeben ist (zum Beispiel sollte er mit dem Namen des Dokumenttyps in der URL der Feldeinstellungen übereinstimmen) und überprüfen Sie auch den Namen des Dokumenttyps, wie er im Dokumenten-Manager (IDM) in Infor sein sollte.

![](https://lh7-us.googleusercontent.com/WHO0vg2W36yVFBq0ay0wBMFVzMfT6pNvHklt0o8N4tqUpM03jXJm2fykuYjyZh0z4wFTO4Eaeh39-D03re3a9utegrdVdsjHBfucmALA3B7YBWd92-9bcYr543G4MWftv0RosvTgFP3J6NNmLZAz5Dc)

**Hinweis**: Es wird angegeben, dass der Name des Dokumenttyps in IDM M3\_SupplierInvoice ist, dies liegt daran, dass es sich um ein Beispiel aus einer M3-Instanz handelt. Dies kann je nach Verwendung von LN oder M3 sowie Ihrer spezifischen IDM-Konfiguration variieren.

Überprüfen Sie die Unternehmens-ID und überprüfen Sie die Entity-ID (SF\_MDS\_EntityType), dieser Wert sollte derselbe sein wie im BOD-Mapping-File.

Stellen Sie sicher, dass IndexFieldFromDocBits=IDMAttributeID ist (überprüfen Sie, ob DocBits in den Feld-Einstellungen links mit IDM in Dokumententyp → Attribute rechts übereinstimmt).

### Dokumenten-Manager in Infor

Gehen Sie zum Dokumenten-Manager und wählen Sie den Namen des aktuellen Dokumenttyps aus, den Sie exportieren möchten, z.B. Lieferantenrechnung.

![](https://lh7-us.googleusercontent.com/EV3uw3R1L6\_RRANB7FRLwtUFMbv\_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Klicken Sie auf das obige Symbol und dann auf Administration → Dokumententyp und finden Sie dann den benötigten Dokumenttyp in der Liste.

![](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j\_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

Wie unten gezeigt, sehen Sie dann den Dokumenttypnamen, wie er in INFOR angezeigt wird.

![](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj\_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW\_dpRfw\_5BXm0WvAnw4HOALmw)

Stellen Sie sicher, dass dies der Name ist, der in der IDM-Mapping-Datei angezeigt wird.

## Datei in DocBits hochladen

Sobald die Datei vorbereitet ist, laden Sie sie in Ihre Exportkonfiguration in DocBits hoch. Dies ist unter Einstellungen → Export verfügbar.

![](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F\_i5mZ42YDnjqZUYKYSJu1Cetc\_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)
