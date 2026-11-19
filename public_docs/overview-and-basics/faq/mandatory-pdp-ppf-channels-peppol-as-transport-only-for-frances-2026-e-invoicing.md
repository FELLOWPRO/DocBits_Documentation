# Frankreichs E-Rechnung: zugelassene Plattformen und Peppol

## Aktuelle Regeln und Zeitplan

Für inländische B2B-Rechnungen in Frankreich im Anwendungsbereich der Reform zwischen umsatzsteuerpflichtigen Unternehmen muss der Rechnungsaustausch über eine **zugelassene Plattform (plateforme agréée, PA; früher PDP)** laufen. Das **öffentliche Rechnungsportal (PPF, Portail public de facturation)** übernimmt das öffentliche Verzeichnis und die Erfassung der Steuerdaten; es ist für diese Vorgänge keine alternative Plattform für den Rechnungsaustausch.

* **1. September 2026:** Alle Unternehmen im Anwendungsbereich müssen elektronische Rechnungen empfangen können. Großunternehmen (GE) und mittlere Unternehmen (ETI) müssen ab diesem Datum außerdem elektronische Rechnungen ausstellen und ihre E-Reporting-Pflichten erfüllen.
* **1. September 2027:** Die Pflichten zur Ausstellung und zum E-Reporting gelten für kleine und mittlere Unternehmen (PME) und Kleinstunternehmen.

Welche Pflicht gilt, hängt vom Anwendungsbereich des Vorgangs und der Unternehmenskategorie ab. Lesen Sie die offiziellen [Hinweise zu zugelassenen Plattformen](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees), den [Einführungszeitplan](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation) und die [Antwort des Ministeriums](https://www.senat.fr/questions/base/2026/qSEQ260107185.html).

## Peppol und Interoperabilität

Peppol kann den Transport und die Interoperabilität zwischen verbundenen Systemen und Plattformen bereitstellen. Die Nutzung von Peppol ersetzt nicht die Pflicht, für den Rechnungsaustausch im französischen Mandat eine PA zu verwenden. Betrachten Sie eine Peppol-Anbindung allein nicht als Beleg dafür, dass die französischen Austausch- und Meldepflichten erfüllt sind.

Den Formatkatalog von DocBits finden Sie unter [Überblick der E-Rechnungsstandards](../../administration-and-setup/settings/global-settings/document-types/edi/currently-supported-e-invoice-standards/README.md).

## Historischer technischer Kontext

Die sechs Schaubilder und die folgenden API-Beschreibungen stammen aus früherem PPF-/PDP-Material und dienen dem historischen technischen Verständnis. Sie verwenden die damalige Terminologie und Architektur; sie beschreiben keine aktuelle Möglichkeit, vorgeschriebene B2B-Rechnungen über den PPF auszutauschen. Prüfen Sie die aktuellen Spezifikationen der PA und der öffentlichen Dienste, bevor Sie eine Integration umsetzen.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt="Schaubild des französischen E-Rechnungs-Lebenszyklus über Vorbereitung, Empfang, Validierung und Zahlung mit Lieferanten- und Käuferstatus"><figcaption><p>Historisches Lebenszyklus-Schaubild: Vorbereitung und Ausstellung, Empfang, Validierung/Rückgabe und Zahlung mit den Beschriftungen für Lieferanten- und Käuferstatus auf jeder Stufe.</p></figcaption></figure>

### Historisches API-Servicemodell

Das frühere API-Modell beschrieb den Zugriff auf verfügbare Funktionen aus den IT-Werkzeugen, die Partnerorganisationen betreiben, über zwei Integrationswege:

* **Informationssysteme (IS):** Die APIs wurden als Bestandteil der Systeme von Rechnungsausstellern, Empfängern oder deren Dematerialisierungsoperatoren (OD) beschrieben. Einige APIs waren für PDP-Systeme gedacht und boten eine Alternative zur EDI-Integration.
* **Drittanbieter-Software:** Softwarehersteller konnten eine Kommunikationsschicht in Kundensysteme einfügen. Frühere Verweise auf eine Verbindung zum PPF gehören zu diesem historischen Modell und sind kein aktueller Weg für den Rechnungsaustausch.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt="Schaubild zu Aussteller und Empfänger, die Rechnungen über OD-PDP-Serviceportale und den PPF mit Datenkontrolle und Wiederherstellung austauschen"><figcaption><p>Historisches Verbindungsschaubild: Aussteller und Empfänger sind über Drittanbieter-Software, Serviceportale und OD-/PDP-Blöcke mit dem PPF-Block für Datenkontrolle und Wiederherstellung verbunden.</p></figcaption></figure>

### Historisches Verbindungsschaubild

Dieses Schaubild zeigt den früheren Kontext der Plattform-Vernetzung. Die aktuelle Umsetzung muss den Anforderungen der PA folgen; eine allgemeine Vorgabe, dass jeder Austausch über ein einziges Transportnetz laufen muss, wird hier nicht behauptet.

<figure><img src="../../.gitbook/assets/Picture 2.png" alt="Schaubild zu Flow-, Rechnungs- und Rechnungsdaten-Kontrollen: Einreichungen von Lieferanten durchlaufen technische, Anwendungs- und funktionale Prüfungen mit Zurückweisungen"><figcaption><p>Historisches Kontroll-Schaubild: Technische, Anwendungs- und funktionale bzw. fachliche Prüfungen für manuelle, API- und EDI-Einreichungen, daneben die Ergebnisse unzulässig, zurückgewiesen und abgelehnt.</p></figcaption></figure>

### Historische Hub-Anbindung

Das frühere Hub-Modell beschrieb eine Web- oder Anwendungslösung, bei der **der Hub API-Aufrufe im Namen seiner Kunden ausführte**. Es nannte ein technisches Konto für jeden Partner sowie eine Anwendung unter PISTE und eine PPF-Verbindung für den Hub. Das sind historische Architekturdetails, kein geprüftes aktuelles Integrationsverfahren.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt="Schaubild von Partnern mit technischen Konten, die über einen Hub mit einer Anwendung unter PISTE und einer Verbindung verbunden sind"><figcaption><p>Historisches Hub-Schaubild: Partner mit technischen Konten sind über einen Hub mit einer Anwendung unter PISTE und einer Verbindung verbunden.</p></figcaption></figure>

### Historische Quellen

Das frühere Material nannte [den damaligen Zeitplan und die rechtliche Übersicht](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform), [die Spezifikationen von 2022](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html), [eine Übersicht zur Reform von 2025](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html), [Hintergrund zur Vernetzung der Plattformen](https://nymus.be/fr/facturation-electronique-en-france/), [Hintergrund zu Peppol](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) und [Hintergrund zum Austausch](https://nymus.be/fr/facturation-electronique-en-france/). Diese Links und die übrigen Schaubilder bleiben als historischer Kontext erhalten. Nutzen Sie für aktuelle Pflichten die oben genannten offiziellen Quellen, einschließlich der Unterscheidung zwischen dem Rechnungsaustausch über eine PA und den öffentlichen Funktionen des PPF. Der frühere Verweis auf Artikel 91 des Finanzgesetzes 2024 begründet keine aktuelle Option für einen Austausch über den PPF.

<figure><img src="../../.gitbook/assets/Picture 3.png" alt="Ablaufdiagramm des Ausstellungsprozesses vom EDI-Flow und API-Empfang über Flow-, Anwendungs- und funktionale Prüfungen bis zur ausgestellten Rechnung"><figcaption><p>Historisches Ablaufdiagramm zur Ausstellung: Eingehende EDI- und API-Flows durchlaufen Prüfungen des Flows, der Anwendung und der Funktion, bevor Rechnungsdaten übernommen werden; außerdem sind Pfade für Zurückweisungen, die ausgehenden Flows 1 und 2 sowie Benachrichtigungen zum Lebenszyklus dargestellt.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Picture 4.png" alt="Ablaufdiagramm des Empfangsprozesses vom EDI-Flow und API-Empfang über Prüfungen mit Zurückweisung oder Ablehnung bis zur bereitgestellten Rechnung"><figcaption><p>Historisches Ablaufdiagramm zum Empfang: Technische, Anwendungs- und funktionale Prüfungen umfassen eigene Geschäftsregeln mit Pfaden für Zurückweisung oder Ablehnung; akzeptierte Daten führen zu einer empfangenen und bereitgestellten Rechnung, daneben Empfänger-Flow 2 und Benachrichtigungen zum Lebenszyklus.</p></figcaption></figure>
