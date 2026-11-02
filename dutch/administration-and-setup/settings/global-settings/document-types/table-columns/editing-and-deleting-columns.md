# Kolommen bewerken en verwijderen

Alles behalve de titel wordt direct in de lijst gewijzigd; er is geen bewerkingsdialoog.

**Waar:** Instellingen → Globale instellingen → Documenttypen → Tabelkolommen

## Een vlag omschakelen

Vink het selectievakje in de rij aan of uit. De wijziging wordt direct opgeslagen (*Successfully saved*).

| Vlag | Aan | Uit |
|---|---|---|
| **Verplicht** | Goedkeuring wordt geblokkeerd zolang de kolom in een rij leeg is; het validatiescherm markeert de cel. | Lege cellen zijn toegestaan. |
| **Alleen-lezen** | De waarde wordt getoond, maar kan niet worden overschreven. Gebruik dit voor waarden die uit een lookup of een script komen. | Gebruikers kunnen de cel bewerken. |
| **Verborgen** | De kolom verdwijnt van het validatiescherm en uit de export. De gegevens blijven bewaard. | De kolom wordt getoond en geëxporteerd. |
| **AI gebruiken** | De AI-tabelextractie vult deze kolom, ook voor leveranciers die getrainde regels hebben. | De kolom wordt gevuld door de getrainde regels, of door de AI wanneer er geen regels bestaan. |

{% hint style="info" %}
Vlaggen gelden voor documenten die **na** de wijziging worden geüpload of opnieuw gestart. Geopende documenten behouden hun huidige tabel totdat ze opnieuw worden gestart.
{% endhint %}

## De titel hernoemen

Klik op het vertaalpictogram in de kolom *Acties* (*Vertaalsleutel bijwerken*), voer het nieuwe label in en bevestig. Het infopictogram ernaast toont welk label momenteel actief is en waar het vandaan komt. Alleen het label verandert; de technische *Kolomnaam* blijft gelijk, zodat scripts, exportmappings en getrainde regels blijven werken.

## Het type of de tabel wijzigen

Niet mogelijk. Verberg de kolom (of verwijder de kolom als het uw eigen kolom is) en voeg een nieuwe kolom met het juiste type toe.

## Een kolom verwijderen

De verwijderactie wordt alleen aangeboden voor kolommen die uw organisatie heeft aangemaakt. Standaardkolommen kunnen niet worden verwijderd; verberg ze.

1. Open het menu met drie puntjes in de kolom *Acties* en kies **Verwijderen**. Bij standaardkolommen ontbreekt deze optie.
2. Bevestig.

Wat er gebeurt:

* De kolom wordt uit de configuratie verwijderd. Documenten die **vanaf nu** worden verwerkt, hebben de kolom niet meer.
* Documenten die al zijn geëxtraheerd, behouden de kolom en de waarden totdat ze opnieuw worden gestart.
* Getrainde regels die deze kolom koppelden, blijven werken voor de andere kolommen; de koppeling voor de verwijderde kolom wordt genegeerd.
* Als er in een exportmapping of een script naar de kolom wordt verwezen, verwijder dan die verwijzing; anders mislukt de export of het script met een fout over een ontbrekende kolom.

## Een verwijdering ongedaan maken

Een verwijderde kolom kan niet vanuit de lijst worden hersteld. Voeg de kolom opnieuw toe met dezelfde titel: de technische naam wordt van de titel afgeleid, dus een kolom die met dezelfde titel wordt aangemaakt, krijgt dezelfde *Kolomnaam* en bestaande mappings kloppen weer.
