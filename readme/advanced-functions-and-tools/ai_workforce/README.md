# AI Workforce

<figure><img src="../../.gitbook/assets/docnet-agents-infographic-en.png" alt="AI Workforce Agents Infographic"><figcaption><p>DocBits Multi-Agenten-System für die autonome Dokumentenverarbeitung</p></figcaption></figure>

## Überblick

**AI Workforce** ist die Orchestrierungsebene innerhalb von DocBits, die eingehende Arbeit in koordinierte KI-Agenten verwandelt. Anstatt dass eine Person jeden Schritt von Hand durchläuft, nimmt AI Workforce eine Einheit eingehender Arbeit entgegen – eine E-Mail, eine Chat-Nachricht in Microsoft Teams oder Discord, eine manuelle Aktion in der Oberfläche oder einen API-Aufruf – und führt sie bis zum Abschluss: Klassifizierung des Dokuments, Extraktion und Validierung von Feldern, Abgleich mit Bestellungen und Stammdaten sowie Export in das ERP, mit menschlicher Beteiligung an den entscheidenden Stellen.

Betrachten Sie es als ein Team, das Sie führen, und nicht als ein Werkzeug, das Sie bedienen. Jede Arbeit durchläuft dieselbe feste Struktur:

* Ein **Orchestrator** erhält eine **Mission** (eine Arbeitseinheit), plant sie und delegiert.
* Der Plan wird in **Issues** (einzelne Aufgaben) unterteilt, die jeweils von einem **Spezialisten-Agenten** oder einem **Menschen** bearbeitet werden.
* Die Spezialisten melden ihre Ergebnisse zurück, und der Orchestrator führt das Gesamtergebnis zusammen.

Die _Agenten_, die diese Rollen ausfüllen, sind nicht festgelegt: DocBits liefert einen einsatzbereiten **DocBits Orchestrator** und zwei Standard-Spezialisten mit, und Sie können eigene erstellen (siehe [Agenten](./#agents)).

Ein typischer Durchlauf von Anfang bis Ende: Eine Rechnung trifft per E-Mail ein → eine Mission wird erstellt → der Orchestrator plant sie und verteilt Issues an die Spezialisten (klassifizieren, extrahieren, validieren, PO-Abgleich) → ein sensibler Schritt pausiert im **Posteingang**, damit ihn ein Mensch genehmigt → nach der Genehmigung wird das Dokument exportiert und die Mission abgeschlossen. Das gesamte Geschehen verfolgen Sie über das **Dashboard**, halten zusammengehörige Durchläufe in **Projekten** zusammen und greifen über den **Posteingang** und die **Issues** ein, wann immer eine menschliche Entscheidung erforderlich ist.

## Aktivierung

AI Workforce wird pro Organisation über die Haupteinstellungen aktiviert.

1. Gehen Sie zu **Einstellungen → Module**.
2. Aktivieren Sie das Modul **AI Workforce**.
3. Bestätigen Sie das Abonnement im daraufhin angezeigten Dialog.

Nach der Aktivierung erscheint **AI Workforce** in der Hauptnavigationsleiste, und der Arbeitsbereich steht Ihrer Organisation zur Verfügung.

## Dashboard

Das **Dashboard** ist Ihre Übersicht über die AI Workforce – KPIs, Diagramme und Aktivitätslisten auf einen Blick. Sie wählen selbst, welche Kennzahlen angezeigt werden.

Um die aktiven Kennzahlen zu konfigurieren, öffnen Sie die **Einstellungen** (Zahnradsymbol) und verwenden Sie das Panel **Dashboard-Widgets**. Schalten Sie jedes Widget ein oder aus und klicken Sie auf **Speichern**; Ihre Auswahl wird als persönliche Einstellung gespeichert, sodass jeder Benutzer seine eigene Ansicht anpassen kann.

Zu den verfügbaren Widgets gehören:

* **Flottenüberwachung** – Live-Status all Ihrer Agenten.
* **KPI-Karten** – Offene Issues, Aktive Missionen, Aktivierte Agenten, Läufe heute, Token-Nutzung und Ausstehende Genehmigungen.
* **Diagramme** – Issue-Verlauf über die Zeit, Missionen nach Status, E-Mail-Eingang, Issues nach Priorität, Läufe pro Tag und Token-Nutzung nach Agent.
* **Listen** – aktive Missionen, letzte Aktivitäten, ausstehende Genehmigungen, Ihre offenen Issues, Agenten bei der Arbeit und blockierte Elemente.

## Posteingang

Der **Posteingang** ist der Ort, an dem Arbeit auf **menschliche Aufmerksamkeit** wartet. Wenn ein Agent im Begriff ist, ein Tool auszuführen, das eine Freigabe erfordert, pausiert er die Aufgabe und stellt hier eine **Genehmigungsanfrage**. Dies ist Human-in-the-Loop (HITL): Die Aktion wird erst ausgeführt, wenn ein Mensch entscheidet. Ob ein bestimmtes Tool eine Freigabe benötigt, wird durch den **Genehmigungsmodus** des Agenten und die **Kritisch**-Markierungen seiner Tools bestimmt (siehe [Agenteneinstellungen](./#agent-settings)).

Jedes Posteingangs-Element zeigt den Titel der Anfrage, den Agenten, der sie ausgelöst hat, und eine kurze Beschreibung dessen, was eine Entscheidung erfordert. Von einem Element aus können Sie:

* **Genehmigen** – den Agenten mit der Aktion fortfahren lassen.
* **Ablehnen** – die Aktion stoppen.
* **Kommentieren / eine Nachricht senden** – dem Agenten alternative Anweisungen geben, bevor er fortfährt.
* **Mission öffnen** – zur Mission springen, zu der dieses Element gehört, um den vollständigen Kontext zu erhalten.

Elemente sind **Ausstehend**, bis jemand darauf reagiert, und werden dann **Erledigt** (oder **Verworfen**, wenn das Element ohne Entscheidung beiseitegelegt wird – zum Beispiel, wenn seine Mission abgebrochen wird). Der Navigationseintrag Posteingang zeigt ein Abzeichen mit der Anzahl der ausstehenden Genehmigungen, damit nichts Wichtiges übersehen wird.

## Missionen

Eine **Mission** ist die oberste Arbeitseinheit und der Agenten-Durchlauf, der ein einzelnes Ziel verfolgt. Jede Mission kann mehrere Aufgaben umfassen und wird von einem **Orchestrator-Agenten** koordiniert, der die Arbeit plant, sie als Issues an Spezialisten delegiert, die Ergebnisse überwacht und das Endergebnis zusammenführt.

Eine Mission wird aus ihrer **Quelle** erstellt – E-Mail, Chat (Microsoft Teams oder Discord), Mission Control (manuell) oder der API – und trägt diesen Kontext über ihre gesamte Lebensdauer mit sich. Sie können selbst eine über **Mission Control** starten, indem Sie in einfacher Sprache beschreiben, was erledigt werden soll; den Rest übernimmt der Orchestrator.

Missionen durchlaufen die folgenden Status:

| Status                          | Bedeutung                                                                       |
| ------------------------------- | ------------------------------------------------------------------------------- |
| **Planung**                     | Der Orchestrator analysiert die Anfrage und erstellt einen Plan.                |
| **In Bearbeitung** _(Aktiv)_    | Spezialisten-Agenten führen die geplanten Issues aus.                           |
| **Warten auf Genehmigung**      | Die Mission ist pausiert und wartet auf eine menschliche Entscheidung im Posteingang. |
| **Abgeschlossen**               | Alle Issues sind erledigt und das Ziel der Mission ist erreicht.                |

Missionen können außerdem **Pausiert** oder **Abgebrochen** sein. In der Detailansicht einer Mission können Sie ihren **Fortschritt** verfolgen, die verknüpften **Issues** prüfen, den Zeit- und Token-Verbrauch einsehen, die **Zeitleiste** der Ereignisse öffnen und die Mission **neu starten**, **bearbeiten** oder **löschen**.

## Issues

Ein **Issue** ist eine einzelne Aufgabe, die erstellt wird, um einen Teil des Missionsziels zu erreichen – zum Beispiel _ein Dokument importieren_, _eine Antwort an den Absender senden_ oder _einen Schritt manuell genehmigen_. Issues werden von **Spezialisten-Agenten** und **Menschen** bearbeitet, die gemeinsam an derselben Aufgabe arbeiten.

Jedes Issue trägt den Kontext, den sein Bearbeiter benötigt, und durchläuft seinen eigenen Lebenszyklus (To Do / In Bearbeitung → In Prüfung → Fertig, oder Fehler / Abgebrochen). Issues können einem Agenten oder einer Person zugewiesen, mit einer Priorität versehen (Kritisch, Hoch, Mittel, Niedrig), mit einer Mission verknüpft und über Kommentare diskutiert werden.

Sie können alle Issues anzeigen, sie nach Status, Priorität, Bearbeiter oder Mission filtern, sie nach Status, Priorität oder Bearbeiter gruppieren und **Meine Issues** einsehen – die Ihnen zugewiesenen Aufgaben. Durch das manuelle Erstellen eines Issues können Sie Arbeit für einen Agenten oder einen Kollegen direkt in eine Mission einfügen.

## Projekte

**Projekte** sind Ordner, die zusammengehörige **Missionen** gruppieren – zum Beispiel _alle Rechnungen eines bestimmten Lieferanten in Q1_, dann ein weiteres Projekt für _Q2_ und so weiter. Sie halten eine große Zahl von Agenten-Ausführungen organisiert und leicht auffindbar.

Wenn Sie ein Projekt erstellen, geben Sie ihm:

* einen **Namen** – z. B. _„Acme Rechnungen Q1"_;
* eine optionale **Beschreibung** – worum es in dem Projekt geht und welches Ergebnis Sie erwarten;
* ein optionales **Fälligkeitsdatum** – das Datum, bis zu dem das Projekt aktiv bleiben soll.

Ein Projekt ist **Aktiv** oder **Abgeschlossen**. Ein Projekt mit einem Fälligkeitsdatum **bleibt aktiv, bis dieses Datum erreicht ist**, und wird dann automatisch abgeschlossen – so schließt sich eine vierteljährliche Sammlung am Ende des Quartals von selbst (die Prüfung läuft einmal täglich). Ein Projekt ohne Fälligkeitsdatum bleibt aktiv, bis Sie es selbst abschließen. Sie können ein Projekt außerdem jederzeit manuell abschließen oder wieder öffnen. Von einem Projekt aus sehen Sie, wie viele Missionen es enthält, und können ihm weitere Missionen zuordnen.

## Agenten

Agenten sind die Arbeitskräfte. Jeder Agent hat eine **Rolle**, die bestimmt, was er im Ablauf Orchestrator → Missionen → Issues tut:

* **Orchestrator** – koordiniert die Arbeit über mehrere Agenten hinweg. Er erhält eine Mission, plant sie, delegiert die Schritte als Issues und führt die Ergebnisse zusammen. Für die Ausführung von Missionen ist ein Orchestrator erforderlich.
* **Spezialist** – führt eine bestimmte Aufgabe aus, etwa das Importieren eines Dokuments oder das Senden einer E-Mail-Antwort, und meldet sich bei seinem Orchestrator zurück.

DocBits liefert die AI Workforce einsatzbereit mit diesen Standard-Agenten:

* **DocBits Orchestrator** – der Standard-Orchestrator.
* **Document Processor** – importiert und verarbeitet hochgeladene Dokumente.
* **Email Reply** – verfasst und sendet Antworten an den Absender.

Dies sind **Systemagenten**: Sie können Teile davon konfigurieren, aber Sie können sie nicht löschen. Zusätzlich dazu können Sie eigene Orchestratoren und Spezialisten erstellen.

### Hierarchie- und Aktivierungsregeln

Da für die Ausführung jeder Mission ein Orchestrator erforderlich ist, folgt die Aktivierung einigen Regeln:

* **Orchestratoren** haben einen **Aktivieren/Deaktivieren**-Schalter, aber ein Orchestrator kann **nur dann deaktiviert werden, wenn mindestens zwei Orchestratoren vorhanden sind** – das System lässt Sie niemals den letzten abschalten, da dann nichts mehr übrig wäre, um Missionen zu koordinieren.
* Wenn **mehr als ein Orchestrator aktiv ist**, wird der **System Router** automatisch aktiv. Seine Aufgabe ist es, jede eingehende Mission zu betrachten und sie an den richtigen Orchestrator zu delegieren. Bei einem einzelnen Orchestrator wird der Router nicht benötigt und hält sich im Hintergrund.
* **Spezialisten haben keinen Aktivieren/Deaktivieren-Schalter.** Stattdessen steuern Sie, wo sie arbeiten können, indem Sie sie **Orchestratoren zuweisen** (siehe _Agent Pool_ weiter unten). Ein Spezialist, der keinem Orchestrator zugewiesen ist, ist überhaupt nicht verfügbar – er bleibt im Verzeichnis, aber kein Orchestrator kann ihm Arbeit delegieren, daher muss jeder Spezialist mindestens einem Orchestrator zugewiesen sein, um genutzt zu werden.

Sie können diese Beziehungen im **Org Chart** ansehen und neu anordnen, das Router → Orchestratoren → Spezialisten darstellt.

### Agenteneinstellungen

Jeder Agent – ob System- oder benutzerdefinierter Agent – verfügt über ein Einstellungsmenü mit den folgenden Abschnitten:

* **Prompt** – der Basis-Systemprompt des Agenten. _Bei Systemagenten schreibgeschützt._
* **Einstellungen** – das **Modell** des Agenten und sein **Reasoning Effort**. Die AI Workforce läuft auf einem einzigen reasoning-fähigen Modell (**DocBits Pro**), daher gibt es statt Detailreglern nur einen Regler – **Reasoning Effort** –, der steuert, wie intensiv der Agent nachdenkt (und damit, wie viel er kostet):
  * **None** – am schnellsten und günstigsten; kein Reasoning.
  * **Low** – schnelle Aufgaben, leichtes Reasoning.
  * **Medium** _(Standard)_ – ausgewogenes Verhältnis von Qualität und Kosten.
  * **High** – tiefgründiges Reasoning für schwierigere Aufgaben; höhere Kosten.
  * **X-High** – maximales Reasoning; höchste Kosten.
* **Genehmigungsmodus** – wie viel der Arbeit des Agenten eine menschliche Freigabe im [Posteingang](./#inbox) erfordert:
  * **None** – der Agent führt jedes Tool automatisch aus; nichts wird zur Genehmigung geschickt.
  * **Critical** _(Standard)_ – nur als **kritisch** markierte Tools erfordern eine Genehmigung; alles andere läuft automatisch. Kritische Tools sind die sensiblen, schreibenden/externen Aktionen (zum Beispiel _Dokument hochladen/importieren_, _Dokumentfelder aktualisieren_, _auf E-Mail antworten_, _Benachrichtigung senden_). In diesem Modus löst ein kritisches Tool **immer** eine Genehmigungsanfrage im Posteingang aus. Sie können einzelne Tools feinabstimmen (ein normalerweise sicheres Tool als genehmigungspflichtig markieren oder ein kritisches freigeben) – diese Überschreibungen pro Tool gelten nur im Critical-Modus.
  * **All** – jedes Tool, das der Agent ausführt, erfordert eine Genehmigung.
*   **Benutzerdefinierte Anweisungen** – Freitext, in dem Sie die Arbeitsgewohnheiten des Agenten beschreiben (dies ist auch bei Systemagenten bearbeitbar). Die Standardvorlage sieht so aus:

    > **Klassifizierung:** Verwenden Sie den Klassifizierer von DocBits für das hochgeladene Dokument. Verlassen Sie sich nur dann auf E-Mail-Betreff/-Text, wenn kein Dokument angehängt war.
    >
    > **Feldüberschreibungen:** keine – Extraktionswerte unverändert übernehmen.
    >
    > **Genehmigung:** nicht konfiguriert. (Um für bestimmte Aktionen eine menschliche Genehmigung zu verlangen, benennen Sie die Aktion und den Schwellenwert.)
    >
    > **Projektzuordnung:** gegen Projektbeschreibungen abgleichen; lassen Sie die Mission lieber nicht zugeordnet, als eine schlechte Zuordnung zu erzwingen. (Zum Überschreiben nennen Sie Schlüsselwörter oder Absendermuster: z. B. `supplier@acme.com → Acme Onboarding`.)
* **Skills** – die Tools, die der Agent verwenden darf (zum Beispiel _Dokumente hochladen_ oder _Benutzer auflisten_). Jedes Tool ist entweder **kritisch** (sensible schreibende/externe Aktionen) oder nicht kritisch, was das oben beschriebene Genehmigungsverhalten steuert. _Bei Systemagenten nicht bearbeitbar._
* **Agent Pool** – _nur für Orchestratoren._ Eine Liste der verfügbaren Agenten, in der Sie auswählen, an welche Spezialisten dieser Orchestrator Arbeit delegieren darf. Ein Spezialist muss hier (oder einem anderen Orchestrator) einem Orchestrator zugewiesen sein, um überhaupt Arbeit zu erledigen; einer, der überall nicht zugewiesen ist, ist gar nicht verfügbar.

### Erstellen benutzerdefinierter Agenten

Über die Standardagenten hinaus können Sie eigene **Orchestratoren** und **Spezialisten** erstellen, die zu Ihren Prozessen passen. Öffnen Sie **Agenten → Agent erstellen**, um den Assistenten zu starten, der durch dieselbe oben beschriebene Konfiguration führt: Wählen Sie die **Rolle** (Orchestrator oder Spezialist), geben Sie dem Agenten einen **Namen** und eine klare **Beschreibung** (ein Orchestrator wird anhand dieses Textes ausgewählt, und ein Orchestrator wählt seine Spezialisten anhand deren Beschreibungen aus), schreiben Sie seinen Prompt, wählen Sie seine Skills, legen Sie sein Reasoning Effort fest und – bei Orchestratoren – wählen Sie die Spezialisten in seinem Agent Pool aus. Benutzerdefinierte Agenten können jederzeit vollständig bearbeitet oder gelöscht werden.
