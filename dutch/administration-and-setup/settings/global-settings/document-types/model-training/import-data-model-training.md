# Gegevens importeren voor modeltraining

## Opstellen, importeren en controleren van voorbeelddocumenten

<figure><img src="../../../../../.gitbook/assets/intro-process-04-trainingsimport-nl-20261028.png" alt="Opstellen, importeren en controleren van voorbeelddocumenten"><figcaption><p>Opstellen, importeren en controleren van voorbeelddocumenten</p></figcaption></figure>

Kies representatieve voorbeelddocumenten, bereid de beschikbare importopties voor en controleer de importstatus. Alleen succesvol geïmporteerde voorbeelden zijn klaar voor verdere training. Los importfouten op vóór de volgende stap en houd onafhankelijke testdocumenten gescheiden van de trainingsdataset.


Bereid documenten voor die representatief zijn voor de formaten, talen en documenttypen van de organisatie. Gebruik alleen bestandsformaten die je installatie accepteert. Vermijd duplicaten en houd trainingsdocumenten gescheiden van de documenten voor de evaluatie.

## Import openen

Open de modeltraining bij het gewenste documenttype en kies de importfunctie.

<figure><img src="../../../../../.gitbook/assets/site-extra-model-training-overview-nl.png" alt="Bediening voor importeren, modeltraining en classificatietests. Deze opname toont geen uitgevoerd trainings- of nauwkeurigheidsresultaat."><figcaption><p>Bediening voor importeren, modeltraining en classificatietests. Deze opname toont geen uitgevoerd trainings- of nauwkeurigheidsresultaat.</p></figcaption></figure>

## Formaat en bestanden kiezen

Kies het getal- en datumformaat dat bij de bestanden past en selecteer vervolgens de documenten. `1.234,56` en `1,234.56` gebruiken bijvoorbeeld verschillende scheidingstekens. Ook een datum zoals `05/06/2026` moet volgens het gekozen formaat worden geïnterpreteerd.

<figure><img src="../../../../../.gitbook/assets/model-training-import-dialog-nl.png" alt="Documentimport met de keuze voor bedrag- en datumnotatie; er is geen bestand geüpload."><figcaption><p>Documentimport met de keuze voor bedrag- en datumnotatie; er is geen bestand geüpload.</p></figcaption></figure>

Controleer de selectie voordat je de import start. Wacht tot de verwerking klaar is en controleer fouten en het toegewezen documenttype. Corrigeer onjuiste classificaties en extracties voordat je de voorbeelden voor training gebruikt.

## Trainen en evalueren

Train het model met de functies en rechten die je versie biedt. Evalueer het resultaat vervolgens met een afzonderlijke steekproef. Meer trainingsdocumenten garanderen op zichzelf geen betere nauwkeurigheid. Zie [Het model testen](testing-the-model.md).
