---
hidden: true
---

# Configuratie van Fuzzy Data met Lijst van Waarden

### **Overzicht**

Elk documenttype heeft zijn eigen Lijst van Waarden (LoV) configuraties, die afzonderlijk moeten worden ingesteld. In tegenstelling tot **Fuzzy Data met Stamgegevens**, komt **Lijst van Waarden** niet met standaard lookup groepen.

### Om Lijst van Waarden te configureren, navigeer naar:

Instellingen → Algemene Instellingen → Documenttypen → Factuur → Velden → Stamgegevens Instellingen → LOV Stamgegevens

### **Een Nieuwe Lijst van Waarden Configuratie Maken**

Er zijn twee manieren om een Lijst van Waarden configuratie te maken:

**1. Dupliceer een Bestaande Lookup**

* Dit kopieert alle informatie en velden van een bestaande groep.
* U hoeft alleen een **nieuwe naam** op te geven.

**2. Maak een Lookup vanaf Nul**

* Klik op **"Lijst van Waarden Maken"**.
* Vul de vereiste details in:
  * **Configuratienaam** → Naam van de Lijst van Waarden.
  * **Lookup Tabel** → De tabel waaruit waarden worden opgehaald.
  * **Conflictafhandelaar** → Kies er een:
    * Beste Score
    * Geen Retourneren
    * Eerste Retourneren
  * **Context Type** → Bepaalt of de LoV van toepassing is op het **Koptekst** of **Regel** niveau.
  * **Match Alles** → _(Meer details nodig)_

### **Velden Beheren Binnen een Lijst van Waarden Groep**

Elke LoV-groep bevat velden die kunnen worden **toegevoegd, verwijderd of bewerkt.**

**Een Nieuw Veld Toevoegen**

Om een nieuw veld binnen een groep toe te voegen:

* Klik op **"Maken"** binnen de relevante groep.
* Geef de volgende details op:
  * **Lookup Veld** → De kolomnaam van de lookup tabel.
  * **Validatie Veld** → Het overeenkomstige DocBits veld.
  * **Bovenliggend Veld** → _(Meer details nodig)_
  * **Zoekoperator** → Kies er een:
    * Slim
    * Bevat
    * Exact
    * Begint met
    * Eindigt met
  * **Selectievakjes:**
    * **Auto Trigger** → Indien ingeschakeld, als een ander veld in een andere lookup configuratie dezelfde kolom deelt, zal dit veld **automatisch** worden bijgewerkt wanneer het andere veld wordt bijgewerkt.
    * **Doorzoekbaar** → Schakelt het veld in als een **Lijst van Waarden** veld, waardoor zoekopdrachten in de lookup tabel mogelijk zijn.

#### **Laatste Stap: Velden Toevoegen aan de Layout**

Na het configureren van Lijst van Waarden velden, **zorg ervoor dat u ze toevoegt aan de layout met behulp van de Layout Builder**. Als velden niet aan de layout worden toegevoegd, zijn ze niet beschikbaar voor gebruik.
