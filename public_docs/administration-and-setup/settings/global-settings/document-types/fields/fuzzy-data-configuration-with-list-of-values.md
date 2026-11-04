---
hidden: true
---

# Fuzzy gegevensconfiguratie met waardenlijst

### **Overzicht**

Elk documenttype heeft zijn eigen configuraties voor de waardenlijst (List of Values, LoV), die afzonderlijk moeten worden ingesteld. In tegenstelling tot **Fuzzy gegevens met stamgegevens** (Master Data), wordt de **Waardenlijst** niet geleverd met standaard lookup-groepen.

### Om de waardenlijst te configureren, navigeert u naar:

Instellingen → Globale instellingen → Documenttypen → Factuur → Velden → Stamgegevensinstellingen → LOV-stamgegevens

### **Een nieuwe waardenlijstconfiguratie maken**

Er zijn twee manieren om een waardenlijstconfiguratie te maken:

**1. Een bestaande lookup dupliceren**

* Hiermee worden alle informatie and velden van een bestaande groep gekopieerd.
* U hoeft alleen een **nieuwe naam** op te geven.

**2. Een lookup vanaf nul maken**

* Klik op **"Waardenlijst maken"**.
* Vul de vereiste gegevens in:
  * **Configuratienaam** → Naam van de waardenlijst.
  * **Lookup-tabel** → De tabel waaruit de waarden worden opgehaald.
  * **Conflictbehandelaar** → Kies er een:
    * Beste score
    * Geen teruggeven
    * Eerste teruggeven
  * **Contexttype** → Bepaalt of de LoV van toepassing is op het **Kop-** of **Regelniveau**.
  * **Alles matchen** → _(Meer details nodig)_

### **Velden beheren binnen een waardenlijstgroep**

Elke LoV-groep bevat velden die kunnen worden **toegevoegd, verwijderd of bewerkt.**

**Een nieuw veld toevoegen**

Om een nieuw veld binnen een groep toe te voegen:

* Klik op **"Maken"** binnen de relevante groep.
* Geef de volgende details op:
  * **Lookup-veld** → De kolomnaam uit de lookup-tabel.
  * **Validatieveld** → Het overeenkomstige DocBits-veld.
  * **Bovenliggend veld** → _(Meer details nodig)_
  * **Zoekoperator** → Kies er een:
    * Slim
    * Bevat
    * Exact
    * Begint met
    * Eindigt met
  * **Selectievakjes:**
    * **Automatische trigger** → Indien ingeschakeld, als een ander veld in een andere lookup-configuratie dezelfde kolom deelt, zal dit veld **automatisch** worden bijgewerkt wanneer het andere veld wordt bijgewerkt.
    * **Zoekbaar** → Schakelt het veld in als een **Waardenlijst**-veld, waardoor zoekopdrachten in de lookup-tabel mogelijk zijn.

#### **Laatste stap: Velden toevoegen aan de lay-out**

Na het configureren van de waardenlijstvelden, **zorgt u ervoor dat u ze toevoegt aan de lay-out met de Layout Builder**. Als velden niet aan de lay-out worden toegevoegd, zijn ze niet beschikbaar voor gebruik.
