# Een BOD-mappingbestand maken

Download een BOD Mapping File en open het in de gewenste bestandseditor om het te bewerken. Voor deze walkthrough wordt VSCode gebruikt.

## Het mappingbestand bewerken

Wijzig het bedrijf in het juiste bedrijf (SFV\_AccountingEntityID) en bewerk indien nodig locatie ID.

![BOD-mappingbestand geopend in VSCode met SFV_AccountingEntityID en andere SyncCaptureDocumentType-sleutel-waardetoewijzingen](https://lh7-us.googleusercontent.com/eJQI1CKlxEkS_Pwp0VH2hgS220b-q8NSFG5iJKpLOL457qTN3CbUB8IHTw1lRinbB_kP00UUNgepWNsbh3_Ko-SExObePjqmxP7ee_lQnADTtDmxEtRM_S7AONMbcpjwtnHTakYd1Q06GVm2G0o-UDA)

Controleer de documentcode door naar de veldinstellingen te gaan van het documenttype dat u probeert te exporteren (te vinden in URL van de lokale instellingen van het documenttype in DocBits zoals hieronder

![DocBits-veldinstellingenpagina voor het factuurdocumenttype in de browser met de URL die de documentcode toont](https://lh7-us.googleusercontent.com/AhU3i27qFS7BMCgpNQnmLWAjcIWHXHOlxMKqd2Yob5RQKa8qysQQsSsacr6zao4cnAh3DISPgYu1GnjubIJpgtAdiBR_0vy3WJZXPY-HeEfVQkWnlRI9UEJWMPQ7DbWYLQhz339BOlbd4KgxU9B_CPE)

Bewerk ten slotte de SFV\_LogicalID die u kunt vinden in INFOR ION DESK → Verbinden → Verbindingspunten en selecteer het DocBits\_Export of vergelijkbaar verbindingspunt en op die pagina vindt u de logische ID die u nodig hebt.

![Connect-pagina in ION Desk met de Connection Points-lijst en DocBits-Prod-Export geselecteerd](https://lh7-us.googleusercontent.com/f50i7pzRuZULJ6shehba0lWIWFBTsPZyip-LQxAYJpYDXK66SlzdGOpdEG-wqLQfqXMgMMhm5SAvj57UOCvF6xf2OMCXtFiEEKr9yiQr4xtv8vbV-NGcLuJwuQ9zHMBBKfTktAp1nSfBJhdPeAu3RWc)

![Pagina Connection Point DocBits-Prod-Export in ION Desk met API Client Id en Logical ID infor.ims.docbits-prod-export](https://lh7-us.googleusercontent.com/qyEt4iYRIjOZCCrVbImeK6EdZGun2YrAy8li8u3tulcD8bwzl_sl1TiEXKqbik-4MxnbV_MCwltvuA2WAgzzvDpTVd7W52he9QD9IK0qijoz3ZihUYcWJlqlD5kbcsRTj3SfP1CDqcyhoFfBeiE1Xfo)

## Een logische ID maken (verbindingspunt)

Als dit Aansluitpunt nog niet bestaat, moet u er een aanmaken.

Ga eerst naar ION Desk → Verbinden → Verbindingspunten en klik op de knop “+ Add”

![ION Desk-menu Connect met de navigatie Connection Points, Mappings en File Templates open](https://lh7-us.googleusercontent.com/fQPmV8KgffyWhM0i0cQlyh7fyQe37p8uR6C_pVD5SboEx2emIJX2212GXqk_KT71DfYMKSjkfYFFTARqgLLxoOPNQFXHxUOo9vMXH2pmDN469VgbQkV-JjRtCevZJsbvS8vbfUtasN83xN25tX6_S5U)

Selecteer vervolgens de optie “IMS via API Gateway”

![Lijst Connection Points in ION Desk met de gemarkeerde optie IMS via API Gateway tussen de beschikbare connectionpoint-typen](https://lh7-us.googleusercontent.com/uPLiiLHp6Z3jPCzYBOzHVuI8sGY5XQuUfv66fZYH0HndSBL7yvzFHh3lJjEMxteJfXsVMhUe3U_38xZHDRFSn0jeiMZUQBJJLzZ2oaIQAixY7wUPd6D0PJwg7wvC8XBeZxPmjNoiUvP3ImoG_aOhFmY)

![Dialoog Infor Application Connection Point voor IMS via API Gateway met de secties Authorization en IMS Endpoint](https://lh7-us.googleusercontent.com/VhyMDEuglPfxeX-3cATu6ZFB_Mz2Y7C-yJ99EvBvrhD8IoVzGd4ksjrWAE0mIPub2PX5_Zua10ZHQeWI82QbJ8ZgJKN-tVpVrYGvMdfQOj3Uco5efsPT6JYkDyPu_lkeR9aTGhh5-q2bzZztXuTUixM)

U wordt naar het bovenstaande scherm gebracht waar u nu de benodigde informatie moet invullen, de naam moet ongeveer “DocBits\_export” of iets dergelijks zijn.

Voor “ION API Client ID” voert u dezelfde Client ID in die u eerder heeft verkregen voor het ION Mapping File.

Selecteer vervolgens het tabblad Document van het menu Verbindingspunt aanmaken en voeg de volgende documenten toe door op het teken “+” te drukken. Dit wordt pas later nuttig.

![Infor Application Connection Point-pagina DocBits-Sandbox-Export met Logical ID infor.ims.docbits-sandbox-export](https://lh7-us.googleusercontent.com/GtHlTliePV-JIDLP9YNGlXELKuWIU2VSlUt4mvWO4q_XM54MSL9zTmtxPMdeOl24VFtNC0pQ-nbXyHb9PaeMkKvgzpCOo5kLdL3A8Bw54ILniwIdTyfxFhPuzRUGKs2hRi5ioKvfkdsPMgq4x6EHOtM)

Zodra u dit Verbindingspunt opslaat, verkrijgt u de Logische ID zoals hieronder weergegeven

![Pagina voor het aanmaken van een Connection Point met de naam DocBits-Sandbox en het veld Logical ID Type](https://lh7-us.googleusercontent.com/P7cihsQT2Qcq_XGL08dTV2jHMUK7YCMQyXsJudkVDXDh73GZ-hS61IoAKSHptPyX4C5e_xPKP0yZGzpQOwCFw6BppPlzZuFWZ_VGIrOUmJH2egxaCEXMoVBHBM6lkZeb3gPYWYdMYpuNqFFPC-4Qol0)

Voeg vervolgens deze logische ID in de juiste sectie van het BOD-toewijzingsbestand in en sla het bestand op.

## Bestand uploaden naar DocBits

Sleep het bestand naar uw exportconfiguratie in DocBits. Dit is beschikbaar via Instellingen → Exporteren.

![DocBits-pagina Export Settings met de kolommen Title, Document Type, Sub-Organizations, Export Method en Actions](https://lh7-us.googleusercontent.com/AqCo7QgC-kaAxbaIJD8MYeKGLBXbwGVJPGx9_2yfUp3R2MYxJPowVAjnO80uxQ9qMDxNoXy1eY3WH-mEpaeWwatwi91edm_0lS9Hg93FSAjQGtDAR5y7Ptce-ARfetSiXIBJKiGwujSggVXXHUhG77U)
