# Verpflichtende PDP-/PPF-Kanäle – PEPPOL nur als Transportweg bei Frankreichs E-Rechnung 2026

## PDP oder PPF für inländische B2B-E-Rechnungen erforderlich

Nach der französischen E-Rechnungspflicht ab 2026 können sich Unternehmen für den Austausch inländischer B2B-Rechnungen nicht allein auf das PEPPOL-Netzwerk stützen. Das Gesetz verlangt, dass alle Rechnungen zwischen in Frankreich umsatzsteuerlich registrierten Unternehmen entweder über eine zertifizierte private Plattform (PDP) oder über das staatliche öffentliche Rechnungsportal (PPF) geleitet werden, um die gesetzlichen [Anforderungen](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform) zu erfüllen ￼. Mit anderen Worten: Unternehmen senden Rechnungen künftig nicht mehr direkt an ihre Kunden, sondern müssen sie über eine zugelassene E-Rechnungsplattform (eine PDP) oder über das staatliche [Portal](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html) übermitteln ￼. Dadurch erhält die Steuerbehörde die erforderlichen Daten in Echtzeit. Der bloße Austausch von Rechnungen über PEPPOL ohne Einbindung einer akkreditierten PDP/eines PPF würde die vorgeschriebenen Melde- und Übermittlungspflichten nicht erfüllen.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt=""><figcaption></figcaption></figure>

### Einführung in das Serviceangebot

Der API-Modus ermöglicht es Nutzern, auf alle für sie verfügbaren Funktionen über die bereits in den Partnerstrukturen eingesetzten IT-Werkzeuge zuzugreifen. Es gibt zwei Integrationsmethoden:

### ·       Integration in Informationssysteme (IS):

APIs werden direkt in Informationssysteme oder Verwaltungssoftware der rechnungsstellenden und -empfangenden Parteien oder ihrer Dematerialisierungsdienstleister (ODs) integriert. Nutzer können so direkt aus ihren gewohnten IT-Werkzeugen, intern oder von ihrem OD angeboten, auf die Funktionen der Lösung und deren Erweiterungen zugreifen.

APIs können auch in das IS der PDPs integriert werden, um ihnen mehr Flexibilität (im Vergleich zum EDI-Modus) zu geben; einige APIs sind speziell für deren Nutzung vorgesehen.

### ·       Integration in Software von Drittanbietern:

Softwarehersteller können Software auf Basis der APIs anbieten. Je nach vom Hersteller gewähltem Modus kann die Verbindung dann durch den Hersteller oder durch den Kunden selbst bei der Installation bzw. Bereitstellung in seinem IS hergestellt werden. Diese Drittsoftware ergänzt das Informationssystem des Kunden um eine Kommunikationsschicht zum PPF.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt=""><figcaption></figcaption></figure>

## PEPPOL nur als Interoperabilitätsschicht

Frankreich übernimmt PEPPOL als Teil seiner Infrastruktur, jedoch nur als Transportschicht innerhalb des PDP-Rahmens und nicht als eigenständigen Compliance-Weg.  Die französische Steuerbehörde (DGFiP) wird zur Peppol Authority, um zu vereinheitlichen, wie PDPs sich [vernetzen](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html) . Alle zertifizierten PDPs müssen sich für den Austausch von [Rechnungen](https://nymus.be/fr/facturation-electronique-en-france/) über das PEPPOL-Netzwerk verbinden.  Das bedeutet, dass PEPPOL die Interoperabilität zwischen autorisierten Plattformen erleichtert – es ersetzt diese Plattformen nicht.  In der Praxis kann ein Unternehmen PEPPOL nur nutzen, indem es über eine PDP (oder den PPF in seiner begrenzten Rolle) arbeitet, die PEPPOL zum Senden oder Empfangen von Rechnungen verwendet. Dies wurde in offiziellen Leitlinien bestätigt: Das öffentliche Portal konzentriert sich auf die Datenerfassung, während die Rechnungsverteilung ausschließlich über PDPs erfolgt, die für den [Austausch](https://nymus.be/fr/facturation-electronique-en-france/) Netzwerke wie [PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) nutzen.

\


<figure><img src="../../.gitbook/assets/Picture 2.png" alt=""><figcaption></figcaption></figure>

## Anbindung eines Hubs:

Der Hub stellt seinen Kunden eine Web- oder Anwendungslösung zur Verfügung, mit der sie die verschiedenen API-Aufrufe durchführen können. **Es ist somit der Hub, der die API-Aufrufe im Namen aller seiner Kunden durchführt**. In diesem Fall benötigt jeder Partner ein technisches Konto, aber nur der Hub benötigt eine Anwendung unter PISTE und eine Verbindung zum PPF.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt=""><figcaption></figcaption></figure>



Quelle: Artikel 91 des französischen Finanzgesetzes 2024 (zusammengefasst von EY) schreibt vor, dass E-Rechnungen über eine zertifizierte PDP oder das staatliche Portal versendet werden müssen.  Die Aktualisierungen der französischen Steuerbehörde stellen zudem klar, dass Unternehmen nach den Reformen von 2024 für die B2B-E-Rechnung eine registrierte PDP nutzen müssen (der PPF dient nicht länger als kostenlose Austauschplattform).  PEPPOL wird eingeführt, um diese PDPs miteinander zu verbinden, nicht als alternativer Kanal außerhalb des Systems.  Dies bestätigt, dass die alleinige Nutzung des PEPPOL-Netzwerks nicht ausreicht – die Einhaltung der französischen E-Rechnungsregelung 2026 erfordert die Anbindung an den PPF oder an eine zertifizierte PDP, wobei PEPPOL lediglich als zugrunde liegendes Zustellnetzwerk zwischen diesen Plattformen dient.

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt=""><figcaption></figcaption></figure></div>
