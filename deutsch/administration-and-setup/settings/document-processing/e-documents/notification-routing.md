# Benachrichtigungsrouting

<figure><img src="../../../../.gitbook/assets/edoc_notification_routing.png" alt="Benachrichtigungs-Routen"><figcaption><p>Zuordnung von Validierungs-Findings zu Agenten</p></figcaption></figure>

Die Seite **Benachrichtigungsrouting** (**E-Dokumente → Aktionen**) ordnet Validierungs-Findings den **KI-Workforce-Agenten** zu. Jedes blockierende Finding löst genau einen Agenten aus – denjenigen, dessen Code-Präfix am längsten übereinstimmt. Alles ohne Treffer fällt auf den Standard-Agenten für Lieferantenbenachrichtigungen zurück.

## Benachrichtigungs-Routen

Legen Sie fest, wer welche Art von Rechnungsproblem bearbeitet. Alles, was nicht aufgeführt ist, geht an den Standard-Agenten:

| Route | Abgedeckte Findings |
|-------|---------------------|
| **Kolumbianische Geschäftsregeln** | Findings zu kolumbianischen Geschäftsregeln. |
| **Deutsche Geschäftsregeln** | Findings zu deutschen Geschäftsregeln. |
| **IBAN-/Bankkonto-Prüfungen** | Findings zu Zahlungsdaten (IBAN-Prüfsumme, Länge, Land). |
| **USt-ID-Prüfungen** | Findings zum Format der USt-IdNr. |
| **Alles andere** | Der Standard-Rückfall für alles, was oben nicht zutrifft. |

Wählen Sie für jede Route den bearbeitenden Agenten aus dem Dropdown. Über **Erweitert (eigene Code-Regeln)** können Sie bei Bedarf nach einem exakten Finding-Code routen.

## Verfügbare Agenten

<figure><img src="../../../../.gitbook/assets/edoc_notification_agents.png" alt="Registry der verfügbaren Agenten"><figcaption><p>Schreibgeschützte Registry der KI-Workforce-Agenten</p></figcaption></figure>

Der Abschnitt **Verfügbare Agenten** ist eine schreibgeschützte Registry der mit Ihrer Installation ausgelieferten KI-Workforce-Agenten, zum Beispiel:

| Agent | Zweck |
|-------|-------|
| **Standard-Lieferantenbenachrichtigung** | Allgemeine Lieferanten-E-Mail; der Auffang-Agent, wenn kein spezifischerer Agent passt. |
| **Banking Bot** | Spezialisierte Vorlage für Zahlungsdaten-Findings (IBAN/BIC-Korrekturen). |
| **Tax Bot** | Lieferantenbenachrichtigung speziell für USt-/Steuer-ID. |
| **Compliance Bot** | Bearbeitet Compliance-Findings. |

Jeder Agent zeigt seinen Celery-Task und die Finding-Code-Präfixe, die er standardmäßig bearbeitet.
