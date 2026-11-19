# Geavanceerde instellingen

In sommige documenten zijn tabelstructuren complex: ze lopen over meerdere regels, bevatten gegroepeerde informatie of hebben overbodige extra rijen. Met de _Geavanceerde instellingen_ in de trainingsmodus stelt u de tabelextractie voor zulke gevallen nauwkeuriger af, wat de nauwkeurigheid en de consistentie ten goede komt.

Om deze instellingen te openen, activeert u de **Trainingsmodus** en klikt u op het tandwiel **Instellingen** in de bovenste actiebalk:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-gear-nl-20261112.png" alt="Tabel Extractie in trainingsmodus met de muis op het tandwiel Instellingen in de bovenste actiebalk."><figcaption><p>Het tandwiel Instellingen in de actiebalk van de trainingsmodus opent de Geavanceerde instellingen.</p></figcaption></figure>

In het venster **Instellingen** staan alle opties die op deze pagina worden beschreven. Klap de sectie **Geavanceerde instellingen** open om bij de groeperingsopties te komen; die blijven ingeklapt tot u ze opent:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-max-rows-nl-20261112.png" alt="Venster Instellingen met Aantal koprijen 2 en de uitgeklapte sectie Geavanceerde instellingen met Minimaal gegroepeerde rijen 2, Maximaal aantal gegroepeerde rijen 3, Verschillende groepskolommen, Omgekeerde groepering en Tekst splitsen."><figcaption><p>De sectie Geavanceerde instellingen met alle groeperingsopties.</p></figcaption></figure>

Elke optie wordt hieronder in een eigen sectie beschreven, samen met het effect ervan op de geëxtraheerde tabel.

### Aantal koprijen

**Gebruik deze instelling om te bepalen uit hoeveel regels de tabelkop bestaat.**

Sommige tabellen hebben een kop over meerdere regels. In dit voorbeeld loopt de kop van de tabel over twee regels:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-two-lines-nl-20261112.png" alt="Factuurtabel waarvan de kop over twee regels loopt (Preis / in EUR en Betrag / in EUR)."><figcaption><p>Een tabelkop die over twee regels loopt.</p></figcaption></figure>

Stel **Aantal koprijen** daarop in:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-row-count-nl-20261112.png" alt="Venster Instellingen met Aantal koprijen ingesteld op 2."><figcaption><p>Aantal koprijen op 2 in het venster Instellingen.</p></figcaption></figure>

#### Waarom is dit belangrijk?

Als u dit niet instelt, kan DocBits de tweede regel als gegevens behandelen in plaats van als deel van de kop, wat tot extractiefouten leidt:

**Voor:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-before-nl-20261112.png" alt="Geëxtraheerde tabel met een onjuist aantal koprijen: de tweede kopregel verschijnt als gegevensrij en de kolomkoppen zijn niet toegewezen."><figcaption><p>Voor: de tweede kopregel wordt als gegevens behandeld.</p></figcaption></figure>

Na:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-after-nl-20261112.png" alt="Geëxtraheerde tabel met Aantal koprijen 2: de kolommen zijn toegewezen aan Positie, Beschrijving, Hoeveelheid, Eenheidsprijs en Nettobedrag en de rijen zijn correct."><figcaption><p>Na: kop- en gegevensrijen zijn correct gescheiden.</p></figcaption></figure>

### Verplaats extra rijen naar Afval

**Gebruik dit om ongewenste regels met doorlopende tekst weg te gooien, zoals omschrijvingen die over meerdere regels lopen.**

In dit voorbeeld loopt de omschrijving door over meerdere regels, terwijl alleen de eerste regel relevant is:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-overflow-doc-nl-20261112.png" alt="Factuurtabel waarin de omschrijving van elk artikel op extra tekstregels onder het artikel doorloopt."><figcaption><p>De omschrijving loopt door over meerdere regels, waarvan alleen de eerste relevant is.</p></figcaption></figure>

Zet **Verplaats extra rijen naar** op **Afval** om de overtollige regels te verwijderen:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-move-extra-rows-nl-20261112.png" alt="Venster Instellingen met Verplaats extra rijen naar ingesteld op Afval."><figcaption><p>Verplaats extra rijen naar ingesteld op Afval.</p></figcaption></figure>

**Resultaat na toewijzen:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-trash-result-nl-20261112.png" alt="Tabel Extractie: in het brondocument loopt de omschrijving van elk artikel door over twee regels, terwijl de geëxtraheerde tabel rechts al één schone rij per artikel bevat."><figcaption><p>Resultaat na toewijzen: de doorlopende regels zijn weg en alleen de relevante rijen blijven over.</p></figcaption></figure>

### Minimaal gegroepeerde rijen

**Gebruik dit wanneer rijen onder één hoofdrij gegroepeerd moeten worden (bijv. artikelregels met meerdere subregels).**

Hier zijn slechts drie van de zes rijen relevant. Twee sleutelkolommen zijn toegewezen (bijv. Positie, Beschrijving), terwijl de andere als aangepaste velden worden behandeld.

Begin met **Aantal koprijen** en **Minimaal gegroepeerde rijen** — het kleinste aantal rijen dat bij een groep moet horen voordat DocBits ze samenvoegt:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-min-grouped-nl-20261112.png" alt="Venster Instellingen met Aantal koprijen 2 en de uitgeklapte sectie Geavanceerde instellingen met Minimaal gegroepeerde rijen ingesteld op 2."><figcaption><p>Aantal koprijen en Minimaal gegroepeerde rijen ingesteld in het venster Instellingen.</p></figcaption></figure>

Zet daarnaast **Verplaats extra rijen naar** op **Afval** om irrelevante gegevens op te ruimen:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-min-grouped-trash-nl-20261112.png" alt="Venster Instellingen met Aantal koprijen 2, Verplaats extra rijen naar Afval en Minimaal gegroepeerde rijen 2."><figcaption><p>Ook Verplaats extra rijen naar is ingesteld op Afval.</p></figcaption></figure>

Definieer vervolgens de groeperingssleutelkolom, bijv. _Positie_, door het kolommenu van die kolom te openen en **Groepsrijen** te kiezen:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-group-key-nl-20261112.png" alt="Geëxtraheerde tabel met het geopende kolommenu van de kolom Pos. met Kolom verwijderen, Groepsrijen en Regex."><figcaption><p>Kies Groepsrijen in het kolommenu van de groeperingssleutelkolom (Positie).</p></figcaption></figure>

Groeperen zelf en de andere kolomhulpmiddelen die ermee samenwerken (handmatige rijselectie, kolomtoewijzing en regex) worden stap voor stap behandeld in [Tabellen structureren en de tabelextractie in DocBits verbeteren](improving-table-extraction-with-regex.md).

**Resultaat:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-grouped-result-nl-20261112.png" alt="Tabel Extractie: het brondocument bevat zes fysieke regels, twee per artikel, en de geëxtraheerde tabel rechts toont één gegroepeerde rij per artikel."><figcaption><p>Resultaat: de zes fysieke regels zijn gegroepeerd tot drie artikelregels.</p></figcaption></figure>

#### Maximaal aantal gegroepeerde rijen

**Gebruik dit om te beperken hoeveel rijen één groep mag bevatten.** De tooltip ervan vraagt: _Hoeveel rijen heeft uw gegroepeerde kolom maximaal?_ Het is de tegenhanger van Minimaal gegroepeerde rijen: een groep die meer rijen nodig zou hebben dan dit aantal, wordt niet samengevoegd.

Laat het leeg wanneer groepen willekeurig groot mogen zijn. Stel het in wanneer een document artikelen met veel subregels bevat en u wilt dat DocBits uitzonderlijk grote blokken niet groepeert, zodat u ze zelf kunt controleren.

U stelt het in hetzelfde deel van het venster in als Minimaal gegroepeerde rijen, direct daaronder:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-max-rows-nl-20261112.png" alt="Venster Instellingen met Minimaal gegroepeerde rijen ingesteld op 2 en Maximaal aantal gegroepeerde rijen ingesteld op 3; Verschillende groepskolommen, Omgekeerde groepering en Tekst splitsen zijn niet aangevinkt."><figcaption><p>Maximaal aantal gegroepeerde rijen (hier 3) staat direct onder Minimaal gegroepeerde rijen.</p></figcaption></figure>

#### Verschillende groepskolommen

**Gebruik dit om alleen unieke waarden in de groeperingssleutelkolom te behouden.**

De tooltip van de optie vraagt: _Wilt u alleen unieke waarden voor uw gegroepeerde kolom?_ Schakel de optie in wanneer meerdere groepen dezelfde waarde in de groeperingssleutelkolom zouden krijgen en u wilt dat DocBits die waarde maar één keer behoudt, zodat de herhaalde groepen een lege sleutel tonen in plaats van de dubbele waarde.

Het is een selectievakje in dezelfde sectie als Minimaal gegroepeerde rijen:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-distinct-split-nl-20261112.png" alt="Venster Instellingen met het selectievakje Verschillende groepskolommen aangevinkt onder Maximaal aantal gegroepeerde rijen."><figcaption><p>Verschillende groepskolommen is het selectievakje onder Maximaal aantal gegroepeerde rijen.</p></figcaption></figure>

#### Omgekeerde groepering

**Gebruik dit wanneer de groeperingsrij pas _na_ de rijen staat die erbij gegroepeerd moeten worden.**

De tooltip van de optie vraagt: _Wilt u alle rijen boven het gegroepeerde kenmerk combineren?_ Schakel de optie in wanneer de rij met de groeperingssleutel (bijvoorbeeld de positie of het bedrag) _onder_ de bijbehorende vervolgregels staat, zodat DocBits de rijen boven de sleutel in de groep samenvoegt in plaats van de rijen eronder:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-doc-nl-20261112.png" alt="Factuurtabel waarin de omschrijvingsregel boven de regel staat met positie, hoeveelheid en bedragen."><figcaption><p>De groeperingsrij staat na de rijen die erbij gegroepeerd moeten worden.</p></figcaption></figure>

Schakel **Omgekeerde groepering** in, groepeer op een hoofdkolom (bijv. Nettobedrag) en stel indien nodig **Verplaats extra rijen naar** in op **Afval**:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-dialog-nl-20261112.png" alt="Venster Instellingen met Omgekeerde groepering aangevinkt, Verplaats extra rijen naar Afval en Aantal koprijen 2."><figcaption><p>Omgekeerde groepering ingeschakeld samen met Verplaats extra rijen naar Afval.</p></figcaption></figure>

**Eindresultaat:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-result-nl-20261112.png" alt="Geëxtraheerde tabel met drie rijen na omgekeerde groepering op de kolom met bedragen."><figcaption><p>Eindresultaat met omgekeerde groepering.</p></figcaption></figure>

#### Tekst splitsen

**Gebruik dit om celtekst precies op het kolomscheidingsteken te splitsen.**

De tooltip van de optie vraagt: _Wilt u de tekst precies op het punt van de kolomscheidingsteken splitsen?_ Schakel de optie in wanneer één geëxtraheerde cel de tekst van twee kolommen bevat die door het tabelscheidingsteken niet zijn gescheiden. DocBits extraheert de tabel dan opnieuw en knipt elke waarde af op de positie van het door u bepaalde scheidingsteken, in plaats van beide waarden in één cel op te slaan.

Omdat het splitsen de extractie opnieuw uitvoert, vraagt DocBits eerst om bevestiging: de bevestiging verschijnt zodra u het selectievakje aanvinkt, en de splitsing wordt pas toegepast nadat u op **Doorgaan** hebt geklikt.

Het selectievakje is de laatste optie in de sectie Geavanceerde instellingen:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-distinct-split-nl-20261112.png" alt="Venster Instellingen met het selectievakje Tekst splitsen aangevinkt als laatste optie van de sectie Geavanceerde instellingen."><figcaption><p>Tekst splitsen is het laatste selectievakje van de sectie.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-split-confirm-nl-20261112.png" alt="Bevestigingsvenster met de vraag 'Weet je het zeker? De tabel wordt opnieuw opgehaald.' en de knoppen Annuleren en Doorgaan."><figcaption><p>Het aanvinken van Tekst splitsen opent deze bevestiging; alleen Doorgaan past de splitsing toe.</p></figcaption></figure>

### Samenvatting

Gebruik de _Geavanceerde instellingen_ om DocBits te leren hoe het complexere of inconsistente tabelstructuren nauwkeurig verwerkt. Deze instellingen verbeteren de extractieprecisie door rekening te houden met:

* koppen over meerdere regels
* omschrijvingen over meerdere rijen
* gegroepeerde artikelregels
* omgekeerde volgorde van gegroepeerde gegevens
* tekst die op een kolomscheidingsteken gesplitst moet worden

Als u deze opties tijdens de training inschakelt, onthoudt DocBits de juiste lay-out voor toekomstige documenten van dezelfde leverancier. Zodra de extractie goed uitziet, slaat u de configuratie op met de actie **Regels opslaan**, die wordt beschreven in [Regels opslaan en verwijderen](save-and-delete-rules.md).
