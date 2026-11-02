# Sleutelconcept: Tolerantievenster

Voordat we naar operatoren kijken, is het belangrijk om te begrijpen hoe het tolerantievenster wordt berekend.

## Wat is een tolerantievenster?

Het tolerantievenster definieert een bereik van acceptabele datums rond de beloofde leverdatum van de inkooporder.

**Voorbeeld:**

* Inkooporderdatum: **9 januari**
* Tolerantiedagen: **3**
* Tolerantievenster: **6 januari → 12 januari**

> <mark style="color:red;">Alleen de geselecteerde</mark> <mark style="color:red;"></mark><mark style="color:red;">**Toegestane Tolerantiedagen**</mark> <mark style="color:red;"></mark><mark style="color:red;">(weekdagen) worden meegeteld bij het berekenen van dit venster.</mark>

### Visueel Tijdlijnvoorbeeld

```
← Verleden                       Toekomst →
|-----|-----|-----|-----|-----|-----|-----|
     6 jan      9 jan      12 jan
   (Start)    (PO Datum)    (Einde) 
```

### Gedrag van de Operator Uitgelegd met Voorbeelden

* **Is Gelijk Aan (=)**
  * **Betekenis:**
    De leverdatum van het regelitem moet _binnen_ het tolerantievenster vallen.
  * **Geldige Datums:**
    * Elke datum tussen **6 jan en 12 jan** (inclusief)
  * **Ongeldige Datums:**
    * Elke datum **voor 6 jan**
    * Elke datum **na 12 jan**
* **Is Niet Gelijk Aan (≠)**
  * **Betekenis:**
    De leverdatum van het regelitem moet _buiten_ het tolerantievenster vallen.
  * **Geldige Datums:**
    * Elke datum **voor 6 jan**
    * Elke datum **na 12 jan**
  * **Ongeldige Datums:**
    * Datums tussen **6 jan en 12 jan**
* **Groter of Gelijk Aan (≥)**
  * **Betekenis:**
    De leverdatum van het regelitem moet op of na de **start van het tolerantievenster** liggen.
  * **Geldige Datums:**
    * **6 jan → elke toekomstige datum**
  * **Ongeldige Datums:**
    * Elke datum **voor 6 jan**
  * <mark style="color:red;">**Belangrijk:**</mark>
    Deze operator staat datums _binnen_ het tolerantievenster **en daarbuiten** toe.
* **Kleiner of Gelijk Aan (≤)**
  * **Betekenis:**
    De leverdatum van het regelitem moet op of voor het **einde van het tolerantievenster** liggen.
  * **Geldige Datums:**
    * Elke datum in het verleden tot **12 jan**
  * **Ongeldige Datums:**
    * Elke datum **na 12 jan**
* **Groter Dan (>)**
  * **Betekenis:**
    De leverdatum van het regelitem moet _strikt na_ het tolerantievenster liggen.
  * **Geldige Datums:**
    * **13 jan → elke toekomstige datum**
  * **Ongeldige Datums:**
    * Elke datum **op of voor 12 jan**
* **Kleiner Dan (<)**
  * **Betekenis:**
    De leverdatum van het regelitem moet _strikt voor_ het tolerantievenster liggen.
  * **Geldige Datums:**
    * Elke datum **voor 6 jan**
  * **Ongeldige Datums:**
    * Elke datum **op of na 6 jan**

## Hoe "Toegestane Tolerantiedagen" het Tolerantievenster Beïnvloeden

Bij het berekenen van het tolerantievenster worden **alleen de geselecteerde weekdagen meegeteld**.
Dagen die niet zijn geselecteerd (zoals weekenden of uitgesloten weekdagen) worden **volledig overgeslagen**

#### Voorbeeld: Op Weekdagen Gebaseerde Tolerantieberekening

**Configuratie:**

* Inkooporderdatum: **Woensdag, 9 januari**
* Tolerantiedagen: **3**
* Toegestane Tolerantiedagen: **Maandag, Dinsdag, Woensdag, Donderdag, Vrijdag**
* Weekenden (Zaterdag, Zondag): **Niet geselecteerd**

#### Stap-voor-Stap Berekening

Beginnend vanaf de PO-datum (**9 jan**):

**Achteruit tellen (3 tolerantiedagen):**

* Dinsdag, 8 jan → **Dag 1**
* Maandag, 7 jan → **Dag 2**
* Zondag, 6 jan → _Overgeslagen (niet toegestaan)_
* Zaterdag, 5 jan → _Overgeslagen (niet toegestaan)_
* Vrijdag, 4 jan → **Dag 3**

➡ **Tolerantie startdatum: Vrijdag, 4 januari**

**Vooruit tellen (3 tolerantiedagen):**

* Donderdag, 10 jan → **Dag 1**
* Vrijdag, 11 jan → **Dag 2**
* Zaterdag, 12 jan → _Overgeslagen_
* Zondag, 13 jan → _Overgeslagen_
* Maandag, 14 jan → **Dag 3**

➡ **Tolerantie einddatum: Maandag, 14 januari**

#### Resulterend Tolerantievenster

```
4 januari  →  14 januari
```

#### Waarom Dit Belangrijk Is

Als Toegestane Tolerantiedagen onjuist zijn geconfigureerd:

* Kunnen leverdatums **onverwacht geldig of ongeldig** lijken
* Worden vroege of late leveringen mogelijk niet correct gedetecteerd
