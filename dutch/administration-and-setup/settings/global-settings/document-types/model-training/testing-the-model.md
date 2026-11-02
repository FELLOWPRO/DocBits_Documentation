# Het model testen

## Evalueer met onafhankelijke testdocumenten

<figure><picture><source srcset="../../../../../.gitbook/assets/intro-process-05-modelltest-nl-dark-20261029.png" media="(prefers-color-scheme: dark)"><img src="../../../../../.gitbook/assets/intro-process-05-modelltest-nl-light-20261029.png" alt="Evalueer met onafhankelijke testdocumenten"></picture><figcaption><p>Evalueer met onafhankelijke testdocumenten</p></figcaption></figure>

Trainingsgegevens en testdocumenten dienen verschillende doeleinden. Voor onafhankelijke testdocumenten definieert u de verwachte documenttypen en veldwaarden en vergelijkt u deze vervolgens met de voorspellingen. Registreer de modelversie, de steekproef, afwijkingen en technische storingen. Breng gerichte verbeteringen aan en herhaal de test met hetzelfde evaluatieprotocol. De weergegeven waarden zijn een voorbeeld en geen nauwkeurigheidsmeting.


Test met representatieve documenten die niet voor de training zijn gebruikt. Leg voor elk document de verwachte antwoorden vast: het documenttype en, bij een evaluatie van de extractie, de veldwaarden.

## Test uitvoeren

1. Open de modeltraining voor het te beoordelen documenttype.
2. Kies de classificatietest als je versie die functie biedt.
3. Selecteer de steekproef en start de evaluatie met de beschikbare opties.
4. Wacht op voltooiing en registreer resultaten en fouten. Een technische fout of onvolledige test is geen correcte classificatie.

<figure><img src="../../../../../.gitbook/assets/site-extra-model-training-overview-nl.png" alt="Bediening voor importeren, modeltraining en classificatietests. Deze opname toont geen uitgevoerd trainings- of nauwkeurigheidsresultaat."><figcaption><p>Bediening voor importeren, modeltraining en classificatietests. Deze opname toont geen uitgevoerd trainings- of nauwkeurigheidsresultaat.</p></figcaption></figure>

## Resultaten beoordelen

Vergelijk de voorspellingen met de verwachte antwoorden en onderzoek fouten per type en formaat. Vermeld bij berekeningen van nauwkeurigheid, precisie, recall of F1-score ook de omvang van de steekproef en de beoordeelde categorieën. Schrijf de toepassing geen meetwaarden toe die je versie niet toont; je kunt deze afzonderlijk berekenen uit de geëxporteerde of vastgelegde resultaten.

Classificatie- en extractieregels zijn afzonderlijke instellingen. Controleer hun invloed op de verwerking. Pas een regel niet uitsluitend aan om een fout in de testgegevens te verbergen.

## Verbeteren en opnieuw testen

Corrigeer de trainingsgegevens, labels of daadwerkelijk beschikbare instellingen en train het model zo nodig opnieuw. Herhaal de test met hetzelfde protocol en behoud een onafhankelijke steekproef. Documenteer versie, gegevens, resultaten en regressies. Een goed steekproefresultaat garandeert geen gelijke prestaties bij alle toekomstige documenten.
