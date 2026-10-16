# DocBits (FELLOWPRO AG) — Questionnaire betreffende beveiliging en naleving

**Leverancier:** DocBits door FELLOWPRO AG | **Hosting:** Frankfurt, Duitsland | **ISO 27001 Gecertificeerd** | **Datum:** 2026-03-04

De informatie over de opslag van inloggegevens en TLS bij openbare eindpunten is gecontroleerd op **16 oktober 2026**. De volgende pagina beschrijft de bevestigde reikwijdte en de details die nog per omgeving moeten worden bevestigd. Zie [Veilige opslag van inloggegevens](secure-storage-of-credentials.md).

De informatie over versleuteling van opgeslagen gegevens is op **16 oktober 2026** gecontroleerd aan de hand van beveiligingsdocumentatie van DigitalOcean en metadata van de diensten. Zie [Versleuteling van opgeslagen gegevens](encryption-at-rest.md).

Meer informatie over beveiliging vindt u in [Cookies en browseropslag](cookies-and-browser-storage.md), [Kwetsbaarhedenbeheer](vulnerability-management.md) en [Overige beveiligingsmaatregelen](other-security-controls.md).

---

## Statuslegende

| Symbool | Betekenis |
|---------|-----------|
| ✅ Bevestigd | Antwoord geverifieerd uit officiële DocBits-documentatie of openbare bronnen |
| ✅ Gedeeltelijk | Gedeeltelijk beantwoord; aanvullend detail nodig van DocBits-team |
| ❓ Ter Bevestiging | Geen openbare informatie beschikbaar — moet rechtstreeks met DocBits/FELLOWPRO worden bevestigd |
| ⚠️ Verduidelijking Nodig | Openbare informatie roept vragen of onduidelijkheden op die expliciete verduidelijking van de leverancier vereisen |

---

## 🔹 Gegevenslocatie & Gegevenslokalisatie

### 1. Waar precies wordt de productieomgeving gehost?

**Antwoord:** De EU-productieomgeving wordt gehost op DigitalOcean-cloudinfrastructuur in Frankfurt, Duitsland. DocBits gebruikt DigitalOcean Spaces voor opslag en beheerde PostgreSQL-, OpenSearch- en Valkey-diensten. DocBits is ISO 27001 gecertificeerd. Zie [Versleuteling van opgeslagen gegevens](encryption-at-rest.md) en [Veilige opslag van inloggegevens](secure-storage-of-credentials.md) voor de reikwijdte van de versleuteling.

**Status:** ✅ Bevestigd

**Opmerkingen:** DigitalOcean Frankfurt: de typen beheerde databasediensten zijn op 16 oktober 2026 bevestigd aan de hand van infrastructuurmetadata; het gebruik van Spaces is in deze FAQ beschreven.

---

### 2. Waar wordt de DR-omgeving (Noodherstel) gehost?

**Antwoord:** DR maakt gebruik van een secundaire back-uplokatie in Amsterdam, Nederland (EU). Gecombineerd met de primaire Frankfurt-locatie biedt dit geografische redundantie binnen de EU.

**Status:** ✅ Bevestigd

**Opmerkingen:** Frankfurt (primair) + Amsterdam (secundair). Beide EU-locaties. Vraag naar RTO/RPO-doelstellingen en details over het failover-proces.

---

### 3. Waar worden back-ups opgeslagen?

**Antwoord:** Back-ups opgeslagen op twee EU-locaties:
- **Primair:** Frankfurt, Duitsland
- **Secundair:** Amsterdam, Nederland

Back-upschema: Dagelijkse, wekelijkse, driemaandelijkse en jaarlijkse back-ups.

**Status:** ✅ Bevestigd

**Opmerkingen:** Uitgebreid back-upschema (dagelijks/wekelijks/driemaandelijks/jaarlijks) op twee EU-locaties. Alle gegevens blijven in de EU. Bevestig back-upversleuteling en hoe vaak herstel wordt getest. De versleuteling van door de aanbieder beheerde databaseback-ups staat beschreven in [Versleuteling van opgeslagen gegevens](encryption-at-rest.md); dit verifieert niet elke kopie in het bredere back-upschema.

---

### 4. Zijn er geo-partitioneringsopties beschikbaar (bijv. alleen UK)?

**Antwoord:** Twee datacentregio's beschikbaar:
- **Frankfurt, Duitsland** — voor alle EU-klanten
- **New York, USA** — alleen voor Amerikaanse klanten

Gegevens van EU-klanten worden uitsluitend in Frankfurt gehost. Momenteel is geen optieuitsluiting UK beschikbaar.

**Status:** ✅ Bevestigd

**Opmerkingen:** EU-klanten zijn Frankfurt-only — geen cross-region gegevensmixing. UK-only hosting niet beschikbaar; UK-klanten zouden worden bediend vanuit Frankfurt. Verduidelijk of extra regio's op de routekaart staan.

---

### 5. Zijn gegevens versleuteld in rust en onderweg?

**Antwoord:** De openbare eindpunten `app.docbits.com`, `auth.docbits.com` en `api.docbits.com` ondersteunen HTTPS met TLS 1.2 en TLS 1.3. Bij de controles op 16 oktober 2026 werden TLS 1.0 en TLS 1.1 geweigerd. Inlogwachtwoorden en sleutels uit API-sleutelbeheer worden beschermd met eenrichtingshashes. Hashing is een andere maatregel dan versleuteling van databases, opslag en back-ups.

**Tijdens opslag:** DigitalOcean Managed Databases gebruikt volledige volumeversleuteling met LUKS en AES-256-XTS; de beheerde back-ups gebruiken AES-256-CTR. Spaces gebruikt 256-bits AES-XTS op fysieke schijven. [Versleuteling van opgeslagen gegevens](encryption-at-rest.md) beschrijft methoden, sleutelbeheer en back-updekking.

**Status:** ✅ Gedeeltelijk

**Opmerkingen:** Dit dekt de genoemde beheerde diensten. Aanvullende exports, archieven, back-upkopieën, eventuele versleuteling per veld en elke interne verbinding vereisen bevestiging voor de specifieke omgeving. Opslagversleuteling toont geen toegangsbeperkingen voor medewerkers aan. [Veilige opslag van inloggegevens](secure-storage-of-credentials.md) legt hashing en de verschillen in toegang uit.

---

## 🔹 AI/ML-modelverwerking

### 6. Worden factuurgegevens naar hosts van derden gestuurd (bijv. OpenAI, Azure AI)?

**Antwoord:** AI-modellen worden NIET naar hosts van derden gestuurd. DocBits gebruikt Mistral AI-modellen die in Frankfurt, Duitsland draaien — op dezelfde locatie als de productieomgeving. Er verlaten geen gegevens de Frankfurt-regio voor AI-verwerking.

**Status:** ✅ Bevestigd

**Opmerkingen:** Mistral-modellen gehost in Frankfurt. Geen API-aanroepen van derden voor documentverwerking. Volledig zelfstandig.

---

### 7. Worden geëxtraheerde documenten gebruikt om bredere modellen over klanten heen te trainen?

**Antwoord:** Ja — DocBits gebruikt "AI swarm intelligence" die classificatie- en extractiemodellen over alle klanten heen traint. De technologie werkt echter als een kaart door de gegevens — deze leert de coördinaten/structurele posities van gegevensvelden op documenten, NIET de werkelijke documentinhoud. Onbewerkte documentgegevens worden niet gedeeld tussen huurders.

**Status:** ✅ Bevestigd

**Opmerkingen:** Swarm intelligence leert structurele lay-outpatronen (veldcoördinaten/posities), niet documentinhoud. Dit betekent dat geen klantgegevens (factuurbedragen, leveranciersnamen, enz.) wordt gedeeld tussen huurders — alleen documentstructuurkennis.

---

### 8. Kunt u modeltraining beperken tot uw huurder alleen?

**Antwoord:** Geen per-huurder modelisolatieoptiebeschikbaar. De gedeelde AI-modellen leren echter alleen documentlay-outcoördinaten en structurele patronen — niet werkelijke documentinhoud of bedrijfsgegevens. Klanten kunnen bovendien aangepaste documenttypen trainen die tot hun eigen huurder beperkt zijn.

**Status:** ✅ Bevestigd

**Opmerkingen:** Laag risico: Gedeelde modellen leren alleen positie-/structuurgegevens (coördinaten), niet bedrijfsinhoud. Training van aangepaste documenttypen blijft huurder-gelimiteerd.

---

### 9. Waar worden AI/ML-modellen gehost en uitgevoerd?

**Antwoord:** AI/ML-modellen (Mistral) worden gehost en uitgevoerd in Frankfurt, Duitsland — dezelfde regio als de productieomgeving.

**Status:** ✅ Bevestigd

**Opmerkingen:** Goed: AI-verwerking blijft in Frankfurt. Geen gegevensoverdracht naar externe AI-infrastructuur.

---

### 10. Welke AI/ML-technologieën worden gebruikt (OCR-engine, LLM, NLP)?

**Antwoord:** DocBits gebruikt AI, OCR, machine learning voor extractie. Ondersteunt 120+ talen. Claimt 96%+ nauwkeurigheid. Gebruikt ook Gen AI voor de "AI Tags" functie.

**Status:** ✅ Gedeeltelijk

**Opmerkingen:** Vraag naar specifieke modeldetails: eigendom vs. OCR van derden, welke LLM ondersteunt Gen AI-functies.

---

### 11. Is er een optie voor on-premise AI-modelimplementatie?

**Antwoord:** DocBits-architectuurdocumentatie verwijst naar zowel "DocBits Cloud customer" als "DocBits On premise" implementatieopties.

**Status:** ✅ Gedeeltelijk

**Opmerkingen:** Bevestig bereik van on-premise optie: Omvat het volledige AI-verwerking of alleen documentopslag?

---

## 🔹 Gegevenstoegang & Logboeken

### 12. Wie (ondersteuning/engineers van leverancier) kan toegang krijgen tot onbewerkte documenten en Infor LN-gegevens?

**Antwoord:** FELLOWPRO AG heeft een aangewezen Gegevensbeschermingsfunctionaris (Daniel Jordan). DPA's met subverwerkers zijn ingesteld volgens GDPR. ISO 27001 verplicht toegangscontroles.

**Status:** ✅ Gedeeltelijk

**Opmerkingen:** Vraag DocBits: Exacte lijst van personeelsrollen met toegang tot onbewerkte documenten. Is toegang op basis van behoefte / op aanvraag alleen?

---

### 13. Welke toegangscontroles en logboeken bestaan voor personeelsleden van de leverancier?

**Antwoord:** ISO 27001-certificering vereist gedocumenteerde toegangscontroles, audittrails en beveiligingsmaatregelen. DocBits handhaaft audittrail voor naleving en beoordeling.

**Status:** ✅ Gedeeltelijk

**Opmerkingen:** Vraag naar: RBAC-details, MFA-vereisten, beheersing van bevoorrechte toegang (PAM), en of toegang wordt geregistreerd met onveranderbare audittrails.

---

### 14. Hoe lang worden toegangslogboeken bewaard?

**Antwoord:** Logboeken opgeslagen op DigitalOcean Spaces in Frankfurt en OpenSearch. Logboeken die voor klanten toegankelijk zijn gedurende 30 dagen behouden. Interne logboeken gedurende 3 maanden behouden.

**Status:** ✅ Bevestigd

**Opmerkingen:** DigitalOcean Spaces + OpenSearch in Frankfurt. 30-daagse klantentoegang / 3-maanden interne retentie. Bevestig of logboeken onveranderbaar/tamper-proof zijn.

---

### 15. Hoe lang worden geüploade documenten / geëxtraheerde gegevens bewaard in DocBits?

**Antwoord:** Klanten kunnen gegevensretentie in instellingen configureren. Opties: 30 dagen of 3 maanden. Na de geconfigureerde periode worden documenten en geëxtraheerde gegevens automatisch verwijderd van DocBits-servers.

**Status:** ✅ Bevestigd

**Opmerkingen:** Door klanten configureerbare retentie (30 dagen / 3 maanden). Bevestig: Omvat verwijdering alle kopieën (DigitalOcean Spaces, OpenSearch, AI-trainingsgegevens)?

---

### 16. Kunnen klanten verwijdering van gegevens op aanvraag aanvragen?

**Antwoord:** FELLOWPRO AG voldoet aan GDPR-rechten van gegevensonderwerpen, inclusief wisselsaanvragen. DPO verwerkt deze aanvragen volgens GDPR Art. 17.

**Status:** ✅ Bevestigd

**Opmerkingen:** Bevestig: Omvat verwijdering alle kopieën, inclusief back-ups en AI-trainingsgegevens die afkomstig zijn van de huurder?

---

### 17. Welke subverwerkers hebben toegang tot klantgegevens?

**Antwoord:** Cloudflare wordt gebruikt voor botbeveiliging/DDoS. DPA's zijn ingesteld met alle subverwerkers volgens GDPR-vereisten.

**Status:** ✅ Gedeeltelijk

**Opmerkingen:** Vraag om volledige subprocessorlijst. Cloudflare bevestigd; vraag naar cloud hosting provider, AI-serviceproviders, enz.

---

### 18. Welke certificeringen en compliancekaders heeft DocBits?

**Antwoord:** ISO 27001 gecertificeerd. GDPR-compliant. Handhaaft DPA's met alle subverwerkers. Aangewezen DPO.

**Status:** ✅ Bevestigd

**Opmerkingen:** Vraag: SOC 2 Type II? Penetratietestverslagen? ISO 27701 (privacy)? Jaarlijkse auditschema?

---

## 🔹 Integratieomvang (Infor LN)

### 19. Wat is de exacte lijst van gegevensvelden die uit LN-masters voor validatie worden opgehaald?

**Antwoord:** Mastergegevens geïmporteerd via Infor BOD's:
- **Leveranciers:** Sync.SupplierPartyMaster, Sync.RemitToPartyMaster
- **Inkooporders:** Sync.PurchaseOrder
- **Rekeningschema:** Sync.CodeDefinition (ChartOfAccounts)
- **Flex Dimensions:** Sync.CodeDefinition (FlexDimensions)
- **Belastingcodes:** via BOD publish

**Status:** ✅ Bevestigd

**Opmerkingen:** Vraag DocBits om volledige BOD-lijst en documentatie op veldniveau voor uw specifieke LN-configuratie.

---

### 20. Welke specifieke koptekstvelden worden teruggevoerd naar LN?

**Antwoord:** Koptekst-exportvelden omvatten: SupplierCode, PurchaseType, InvoiceType, InvoiceNumberSupplier, InvoiceDate, InvoiceAmount, InvoiceCurrency, RateDeterminer, RateDate, TaxCountry, TransactionEntryDate, Reference, IDMReference, TaxBaseAmount, InvoiceDocumentType, en meer.

**Status:** ✅ Bevestigd

**Opmerkingen:** Bekijk toewijzingsbestand voor uw specifieke omgeving. Bevestig dat alle statische velden overeenkomen met uw LN-bedrijfsinstelling.

---

### 21. Zijn terugschrijfbewerkingen beperkt tot AP/PO-interfaceobjecten alleen?

**Antwoord:** Export gebruikt Sync.CaptureDocument BOD die wordt omgezet in doel-BOD's (bijv. AP-factuur-BOD's) in ION Desk. Gegevens ook geëxporteerd naar Infor IDM voor documentarchivering.

**Status:** ✅ Gedeeltelijk

**Opmerkingen:** Bevestig: Schrijft DocBits ALLEEN naar AP-factuur- en PO-ontvangstobjecten? Andere LN-modules aangeraakt? Wat is het IDM-schrijfbereik?

---

### 22. Welke integriatiemethode wordt gebruikt (ION API, BOD's, directe DB)?

**Antwoord:** Integratie via Infor ION API, ION Desk en Infor Standard BOD's. Geen directe databasetoegang. Gebruikt ION API-bestanden en serviceaccounts voor authenticatie.

**Status:** ✅ Bevestigd

**Opmerkingen:** Goed: Geen directe DB-toegang. Alle communicatie via standaard integratilaag van Infor.

---

### 23. Welke authenticatie/autorisatie wordt gebruikt voor LN-connectiviteit?

**Antwoord:** Gebruikt ION API Files (OAuth2 client credentials) met ION API Client-ID's en serviceaccounts die in InforOS zijn gemaakt.

**Status:** ✅ Bevestigd

**Opmerkingen:** Zorg ervoor dat serviceaccounts het principe van minste privileges volgen. Bekijk rechten verleend aan de DocBits ION API-gebruiker.

---

### 24. Is gegevensoverdracht tussen DocBits en LN end-to-end versleuteld?

**Antwoord:** De gedocumenteerde ION API-integratie gebruikt HTTPS. Het openbare DocBits-API-eindpunt ondersteunt TLS 1.2 en TLS 1.3. Deze verificatie toont geen versleuteling aan voor elke interne verwerkingsstap of het TLS-beleid van het ERP-eindpunt van de klant.

**Status:** ✅ Gedeeltelijk

**Opmerkingen:** Bevestig het volledige verbindingspad, de TLS-eisen van het ERP-eindpunt en de certificaatvalidatie voor de ingestelde integratie voordat u end-to-end-versleuteling toezegt. Zie [Veilige opslag van inloggegevens](secure-storage-of-credentials.md).

---

### 25. Welke documenttypen worden ondersteund naast AP-facturen?

**Antwoord:** Ondersteunt facturen, afleveringsnotities/facturen, prijsopgaven, orderbevestigingen, contracten en meer. Verwerkt PO en non-PO facturen.

**Status:** ✅ Bevestigd

**Opmerkingen:** Verduidelijk welke documenttypen teruggevoerd naar LN vs. alleen opgeslagen in IDM.

---

## Opslag van inloggegevens en accountherstel

### 26. Kan de leverancier inloggegevens van klanten bekijken en wat gebeurt er als een wachtwoord verloren gaat?

**Antwoord:** DocBits-inlogwachtwoorden worden opgeslagen als eenrichtingshashes met salt. Beheerders en DocBits-support kunnen het oorspronkelijke leesbare wachtwoord niet uit de opgeslagen hash ophalen. Gebruikers die hun wachtwoord vergeten, moeten via de resetprocedure per e-mail een nieuw wachtwoord instellen om weer met een wachtwoord te kunnen inloggen. Ingestelde SSO- of passkey-methoden bieden alternatieve inlogmogelijkheden. Sleutels die via DocBits-API-sleutelbeheer worden aangemaakt, worden slechts één keer getoond en als eenrichtingshashes opgeslagen. Beheerders en DocBits-support kunnen de volledige sleutel daarna niet meer ophalen. Verloren sleutels moeten worden ingetrokken en vervangen.

**Status:** ✅ Gedeeltelijk

**Opmerkingen:** Deze uitspraken gelden voor inlogwachtwoorden en door DocBits uitgegeven sleutels. Bevoegde organisatiebeheerders kunnen accountgegevens bekijken. De dienst die de verbinding maakt, moet mogelijk de inloggegevens voor de integratie kunnen lezen; toegang door medewerkers van de leverancier vereist afzonderlijke bevestiging. Zie [Veilige opslag van inloggegevens](secure-storage-of-credentials.md).
