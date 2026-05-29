# Negatief teken instellen voor creditnota's

### Overzicht

De instelling **Negatief teken instellen voor creditnota's** (Set Negative Sign for Credit Notes) zorgt ervoor dat **creditnota's** met **negatieve bedragen** worden opgeslagen. Een creditnota draait een deel van een factuur terug of betaalt het terug, dus in de boekhouding moeten de waarden de totalen verlagen — oftewel negatief zijn. Wanneer deze instelling aan staat, past DocBits dat negatieve teken automatisch toe.

Deze instelling is **standaard ingeschakeld**.

### Wat doet het?

Wanneer een document wordt herkend als een **creditnota**, zet DocBits de bedragen tijdens de verwerking automatisch om in negatieve waarden. Dit betreft de geldvelden, waaronder de nettobedragen, btw-bedragen en totalen (bijvoorbeeld nettobedrag, btw-bedrag, totaal btw-bedrag, totaal nettobedrag en totaalbedrag).

* **Ingeschakeld (standaard)** — Bedragen van creditnota's worden opgeslagen als negatieve waarden (bijvoorbeeld `150,00` wordt `-150,00`). Gewone facturen worden niet beïnvloed.
* **Uitgeschakeld** — De bedragen blijven precies zoals ze uit het document zijn gelezen, zonder tekenwijziging.

{% hint style="info" %}
Dit geldt alleen voor documenten die als **creditnota** zijn geïdentificeerd. Gewone facturen blijven altijd ongewijzigd.
{% endhint %}

### Voordelen

* **Correcte boekhouding**: Creditnota's verlagen saldi, dus negatieve waarden zijn wat uw boekhoud- en ERP-systemen verwachten.
* **Geen handmatig bewerken**: Uw team hoeft het teken niet bij elke creditnota met de hand om te draaien.
* **Consistentie**: Elke creditnota wordt in uw hele organisatie op dezelfde manier behandeld.

### Hoe te gebruiken

1. Ga naar **Instellingen**.
2. Selecteer **Documentverwerking**.
3. Selecteer **Module**.
4. Open de sectie **Documenttype**.
5. Zoek **Negatief teken instellen voor creditnota's** en zet de schakelaar aan of uit.

### Wanneer deze functie gebruiken

* **Laat ingeschakeld** als uw boekhoud- of ERP-systeem verwacht dat creditnota's met negatieve bedragen binnenkomen (dit is de meest voorkomende opzet).
* **Schakel uit** alleen als uw downstream-systeem het teken al zelf afhandelt of verwacht dat bedragen van creditnota's positief blijven.
