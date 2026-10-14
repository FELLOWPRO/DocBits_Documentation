# Update Document Purchase Order Status

## Overzicht

Wanneer ingeschakeld, wordt de **PO-status** kolom op het dashboard automatisch bijgewerkt wanneer de status van de inkooporder verandert.

## Waar te Activeren

1. Ga naar: **Instellingen** → **Algemene Instellingen** → **Documenttype**
2.  Selecteer het gewenste documenttype en klik op **Meer Instellingen**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fsd3ebb3IETh7wNSA5flh%252Fimage.png%3Falt%3Dmedia%26token%3D6f1d286b-e006-4b23-9866-9ed37bf2bdaa\&width=768\&dpr=4\&quality=100\&sign=b0f0b121\&sv=2)
3.  In de **Inkooporder** sectie, ga naar de optie **Update Document Purchase Order Status**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSsFkQ46Jd4tn0WGqNSjk%252Fimage.png%3Falt%3Dmedia%26token%3D51ee4f2d-76ae-42b4-a748-f0e9d340b329\&width=768\&dpr=4\&quality=100\&sign=e0f4b1af\&sv=2)

## Hoe Het Werkt

Wanneer deze instelling is ingeschakeld, zal de **PO-status** kolom op het dashboard automatisch de huidige status van de inkooporder weergeven. Bijvoorbeeld, als de PO-status wordt bijgewerkt naar _Ontvangen_ of _Gefactureerd_, zal de dashboardkolom dienovereenkomstig worden bijgewerkt om deze nieuwe status weer te geven.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmWZIOi5pqWyeagCfiXgy%252FStatus%2520on%2520Dashboard.jpg%3Falt%3Dmedia%26token%3D3aad59e7-d249-4f07-afa3-c68429128cec&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=6cde440e&#x26;sv=2" alt="" width="375"></div>

## Instellen

1. **Schakel de Instelling In** Ga naar de hierboven genoemde locatie en zet de instelling aan.
2. **Voeg de PO-statuskolom toe (indien niet zichtbaar)** Als de **PO-status** kolom nog niet zichtbaar is op het dashboard:
   *   Ga naar: **Geavanceerde Instellingen** → **Tabelkolommen instellen voor Organisaties**

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn6GyECCtvUeKLYd6FkEH%252Fimage.png%3Falt%3Dmedia%26token%3Da023deba-748f-4140-bb33-17483c91f2cf\&width=768\&dpr=4\&quality=100\&sign=164eb544\&sv=2)
   * Voeg het veld van het documenttype toe door te zoeken naar **PO Status**
3. **Configureer zoekconfiguratie**
   *   Configureer het Statusveld in de Inkooporderkopzoekopdracht als volgt:

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Folrh285NuJO787Udc80C%252Fimage.png%3Falt%3Dmedia%26token%3Def5abe46-fe94-4946-a893-66f7ca21322b\&width=768\&dpr=4\&quality=100\&sign=415e657e\&sv=2)
   * **Opmerking:** **Inkooporder moet op Auto Trigger staan anders kunnen Statusupdates mogelijk niet correct worden bijgewerkt**
   * Weet niet hoe je **Zoekconfiguratie moet configureren? Hier is de** [**zoekconfiguratiegids**](../../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md)
4. **Controleren** Ontvang of factureer een PO, controleer vervolgens het dashboard om te bevestigen dat de status correct is bijgewerkt.
