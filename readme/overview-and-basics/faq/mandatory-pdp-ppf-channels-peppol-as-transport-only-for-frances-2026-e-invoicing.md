# Frankreichs E-Rechnung: zugelassene Plattformen und Peppol

## Zugelassene Plattformen für den Rechnungsaustausch

Für inländische B2B-E-Rechnungen im Anwendungsbereich der französischen Reform ist eine **zugelassene Plattform** erforderlich: französisch **plateforme agréée (PA)**, früher **PDP**. Das öffentliche Portal **PPF (Portail public de facturation)** ist keine Alternative für das Senden und Empfangen dieser Rechnungen. Es übernimmt insbesondere das öffentliche Verzeichnis und die Bündelung der an die Verwaltung zu übermittelnden Daten. Die Rollen erläutern die [französische Steuerverwaltung](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees) und die [Ministeriumsantwort vom 12. Februar 2026 beim französischen Senat](https://www.senat.fr/questions/base/2026/qSEQ260107185.html).

## Einführungsfristen

Für Unternehmen im Anwendungsbereich gelten folgende Fristen:

* **Seit dem 1. September 2026:** Empfang elektronischer Rechnungen für alle betroffenen Unternehmen; Ausstellung elektronischer Rechnungen für Großunternehmen und mittelgroße Unternehmen (GE/ETI).
* **Ab dem 1. September 2027:** Ausstellung elektronischer Rechnungen für kleine und mittlere Unternehmen sowie Kleinstunternehmen (PME/micro).

Maßgeblich sind die [offiziellen Angaben zum Einführungszeitplan](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation) und der jeweilige Anwendungsbereich der Reform.

## Peppol als Interoperabilitäts- und Transportnetz

Peppol kann den Austausch zwischen zugelassenen Plattformen unterstützen. Eine alleinige Peppol-Anbindung ersetzt die erforderliche PA jedoch nicht. Insbesondere lässt sich aus der Nutzung des Transportnetzes keine pauschale Zusage ableiten, dass sämtliche französischen Rechnungs- und Meldepflichten erfüllt sind.

Für die praktische Integration ist deshalb zu klären, welche zugelassene Plattform den Rechnungsaustausch übernimmt und wie die eingesetzte Software an diese Plattform angebunden ist. Die konkrete Schnittstelle richtet sich nach der gewählten Plattform.

## Historische Schaubilder zur PPF-API-Anbindung

Die folgenden Schaubilder stammen aus der früheren Beschreibung des API-Serviceangebots und der Hub-Anbindung an den PPF. Sie veranschaulichen diesen technischen Kontext und sind **keine aktuelle Anleitung für den B2B-Rechnungsaustausch über den PPF**. Für den heutigen Rechnungsaustausch gilt die oben beschriebene Rolle der zugelassenen Plattformen.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt="Diagramm des Lebenszyklus einer Rechnung vom Lieferanten über die Zustände Submitted, Received by the platform und Made available bis zu den Ergebnissen Rejected, Refused, Disputed, Partially approved, In hand und Completed"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/Picture 6.png" alt="Diagramm eines Issuer OD-PDP und eines Receiver OD-PDP, die über Serviceportale und Drittanbietersoftware verbunden sind, mit einem Datenkontroll- und Wiederherstellungsschritt dazwischen"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/Picture 2.png" alt="Diagramm der drei nummerierten Kontrollebenen – technische Kontrollen, Anwendungskontrollen sowie funktionale und geschäftliche Kontrollen – die jeweils in einen nachfolgenden Prozessschritt einfließen"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/Picture 5.png" alt="Diagramm des Hub-Modells mit einem Partner, einem technischen Konto, dem Hub, einer Anwendung unter PISTE und einer Verbindung"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/Picture 3.png" alt="Diagramm des Empfangs eines EDI-Flusses und von Flow 2 via API, die funktionale Kontrollen für semantisches Format, Verzeichnis und Datenkonsistenz durchlaufen, bevor die Rechnungsdaten eingebunden werden und die Rechnung als eingereicht resultiert"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/Picture 4.png" alt="Diagramm eines EDI-Flusses und eines API-Flusses, die funktionale Kontrollen und spezifische Geschäftsregeln durchlaufen, bevor die Rechnung abgelehnt oder zurückgewiesen wird oder als empfangen und verfügbar gemacht resultiert"><figcaption></figcaption></figure>
