---
hidden: true
noIndex: true
---

# M3\_OLD

## Een API-verbindingssjabloon importeren in Infor M3

Deze handleiding legt uit hoe u een API-verbindingssjabloon importeert om snel belangrijke instellingen te configureren voor de integratie met Infor M3. Met een sjabloon zet u een vooraf gedefinieerde verbindingsconfiguratie op, wat het proces vereenvoudigt en voor consistentie zorgt.

<mark style="color:red;">**Opmerking**</mark>: Voor de gedetailleerde configuratie van specifieke onderdelen zoals Auto Accounting, leveranciersintegratie, inkooporders of Table Extraction voor kostenelementen verwijzen wij naar de bijbehorende documentatie:

* [Auto Accounting](m3/auto-accounting.md)
* [Leveranciers en inkooporder](m3/suppliers-and-purchase-orders.md)
* [Hoe alle leveranciers importeren](m3/how-to-import-all-suppliers.md)
* [Tabelextractie voor kostenelement](m3/table-extraction-for-costing-element.md)

### **Het sjabloon downloaden**

Download vóór het importeren het benodigde verbindingssjabloon via het onderstaande bestand:

{% file src="../../.gitbook/assets/DocBits-Dev-Import-Template (1).xml" %}

### Sjabloon importeren

#### Stappen om een verbindingssjabloon te importeren

1. **Infor ION Desk openen:**
   *   Ga naar **InforOS** → **ION Desk** → **Connect** → **Verbindingspunten**.

       ![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o)
2. **Het sjabloon importeren:**
   *   Klik op de knop **Import**.

       <figure><img src="../../.gitbook/assets/m3_import_2.png" alt=""><figcaption></figcaption></figure>
   * Selecteer het juiste **sjabloonbestand** op uw lokale systeem.
   *   Klik op **OK** om het importproces te starten.

       <figure><img src="../../.gitbook/assets/m3_import_3.png" alt="" width="327"><figcaption></figcaption></figure>
3. **Bevestiging:**
   *   Als de import is geslaagd, verschijnt een bevestigingsmelding.

       <figure><img src="../../.gitbook/assets/m3_import_4.png" alt=""><figcaption></figcaption></figure>
4. **Configuratie na de import:**
   * Na het importeren van het sjabloon kunt u specifieke verbindingsinstellingen naar wens aanpassen.
   * Vergeet niet uw **Service Account** voor authenticatie en toegangsbeheer te importeren of te configureren.

<figure><img src="../../.gitbook/assets/m3_import_5.png" alt=""><figcaption></figcaption></figure>
