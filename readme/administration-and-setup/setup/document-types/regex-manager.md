# Regex Manager

Deze functie van DocBits is een alternatief voor modelclassificatie: u kunt doorzoekbare reguliere expressies voor een documenttype schrijven, voor classificatie en andere doeleinden.

**Documenttype:** Met de Regex Manager schrijft u reguliere expressies, en DocBits zoekt het document op deze expressies. Als een document overeenkomt met de regex van een gedefinieerd document, wordt het in het bijbehorende documenttype ingedeeld. Schrijft u bijvoorbeeld een reguliere expressie die „Gutschrift” vindt, dan classificeert DocBits elk document met deze term als creditnota.

**Herkomst van het document:** Hiermee weet DocBits via reguliere expressies uit welk land een document afkomstig is. Als de reguliere expressie voor een Spaans document bijvoorbeeld de term „Factura” bevat en DocBits vindt deze term in een document, dan weet DocBits dat het document Spaans van oorsprong is en classificeert het dienovereenkomstig.

## De Regex Manager openen

Om deze functie te gebruiken, gaat u naar Instellingen → Documenttypen en klikt u op „Nieuw”. Voer in de wizard „Nieuw documenttype maken” een naam in voor het documenttype en selecteer als extractiemethode „Regex” in plaats van „Auto”; ga daarna verder met „Volgende”.

<figure><img src="../../../.gitbook/assets/regex-manager-create-nl-20261006.png" alt="De DocBits-wizard om een nieuw documenttype te maken, met de ingevulde naam en de geselecteerde optie „Regex”."><figcaption><p>De wizard „Nieuw documenttype maken” met de naam van het documenttype en de keuze tussen „Auto” en „Regex”.</p></figcaption></figure>

## Regex toevoegen en verwijderen

De Regex-stap toont een tabel met de bestaande reguliere expressies, met Oorsprong en Patroon, en de knop „Toevoegen” om nieuwe regex-regels te maken.

<figure><img src="../../../.gitbook/assets/regex-manager-list-nl-20261006.png" alt="De tabel van de Regex Manager met de bestaande reguliere expressies per oorsprong en patroon."><figcaption><p>De Regex-stap met de tabel van bestaande reguliere expressies en de knop „Toevoegen”.</p></figcaption></figure>
