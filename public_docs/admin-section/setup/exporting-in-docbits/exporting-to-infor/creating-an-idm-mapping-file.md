# Creazione di un file di mapping IDM

Una volta ottenuto, apri il file nel tuo editor di file applicabile preferito. Per questa procedura guidata, verrà utilizzato VSCode.

## Modifica del file di mapping

Controlla che il codice del tipo di documento sia come in DocBits (come nel file di mapping BOD dovrebbe corrispondere al nome del tipo di documento nell'URL delle impostazioni del campo) e controlla anche il nome del tipo di documento come dovrebbe essere in Document Manager (IDM) in Infor.

![](https://lh7-us.googleusercontent.com/WHO0vg2W36yVFBq0ay0wBMFVzMfT6pNvHklt0o8N4tqUpM03jXJm2fykuYjyZh0z4wFTO4Eaeh39-D03re3a9utegrdVdsjHBfucmALA3B7YBWd92-9bcYr543G4MWftv0RosvTgFP3J6NNmLZAz5Dc)

**Nota**: Si specifica che il nome del tipo di documento in IDM è M3\_SupplierInvoice, questo è dovuto al fatto che si tratta di un esempio da un'istanza M3. Questo può variare a seconda che si utilizzi LN o M3, così come la configurazione IDM specifica.

Controlla l'ID aziendale e controlla l'ID entità (SF\_MDS\_EntityType) questo valore dovrebbe essere lo stesso che era nel file di mapping BOD.

Assicurati che IndexFieldFromDocBits=IDMAttributeID (controlla se DocBits a sinistra nelle impostazioni del campo corrisponde a IDM a destra in Tipo di documento → Attributi).

### Document Manager in Infor

Vai a Document Manager e seleziona il nome del tipo di documento attuale che stai cercando di esportare, ad esempio, Fattura del fornitore.

![](https://lh7-us.googleusercontent.com/EV3uw3R1L6\_RRANB7FRLwtUFMbv\_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Clicca sull'icona sopra e poi su Amministrazione → Tipo di documento e quindi trova il tipo di documento di cui hai bisogno nell'elenco

![](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j\_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

Come mostrato di seguito, vedrai quindi il nome del tipo di documento come appare in INFOR

![](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj\_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW\_dpRfw\_5BXm0WvAnw4HOALmw)

Assicurati che questo sia come appare nel file di mapping IDM

## Carica il file su DocBits

Una volta preparato il file, caricalo nella tua configurazione di esportazione in DocBits. Questo è disponibile in Impostazioni → Esporta.

![](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F\_i5mZ42YDnjqZUYKYSJu1Cetc\_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)
