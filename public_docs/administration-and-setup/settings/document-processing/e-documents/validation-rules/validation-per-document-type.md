# Prüfung je Dokumenttyp

Administratoren legen für jeden Dokumenttyp fest, ob DocBits eingehende E-Rechnungen prüft und ob eine fehlgeschlagene Prüfung das Dokument blockiert. Jede Änderung wird bestätigt und im [Änderungsprotokoll](validation-change-log.md) festgehalten.

> Nur **Organisationsadministratoren** können diese Einstellungen ändern. Andere Benutzer sehen die Tabelle nur lesend oder gar nicht.

## Die Tabelle

Gehen Sie zu **Settings → E-Documents → E-Invoice Validation**. Der Tab **Rules and policy** beginnt mit der Tabelle **Validation for each document type**.

<figure><img src="../../../../../.gitbook/assets/einvoice-validation-settings-de-20261104.png" alt="Prüfung und Blockierung je Dokumenttyp. Konfigurierte Namen sind ausgeblendet. Beispiel aus Dev."><figcaption><p>Prüfung und Blockierung je Dokumenttyp. Konfigurierte Namen sind ausgeblendet. Beispiel aus Dev.</p></figcaption></figure>

| Schalter | Was er bewirkt |
| --- | --- |
| **Enabled** | DocBits prüft jede eingehende E-Rechnung dieses Dokumenttyps und speichert einen [Prüfbericht](validation-report.md). |
| **Blocking** | Ein Prüfhinweis mit dem Schweregrad Fehler stoppt das Dokument. Es erhält den Status **Error**. Ist Blockierend aus, speichert DocBits den Bericht und das Dokument läuft weiter. **Blocking** können Sie nur einschalten, wenn **Enabled** eingeschaltet ist. |

Hat ein Dokumenttyp Überschreibungen für Untertypen, zeigt die Tabelle einen Hinweis dazu.

## Eine Einstellung ändern

1. Wählen Sie den Schalter, den Sie ändern möchten.
2. DocBits zeigt **Confirm validation change** mit dem Dokumenttyp und der Änderung, zum Beispiel *QUOTE: Enabled → On*.

<figure><img src="../../../../../.gitbook/assets/einvoice-validation-confirm-de.png" alt="Bestätigung einer Einstellungsänderung. Die Änderung wurde für diese Aufnahme abgebrochen."><figcaption><p>Bestätigung einer Einstellungsänderung. Die Änderung wurde für diese Aufnahme abgebrochen.</p></figcaption></figure>

3. Lesen Sie den Hinweis: **Bereits gespeicherte Prüfberichte bleiben unverändert.** Die Änderung gilt nur für neue Prüfungen, auch bei einem Neustart der Verarbeitung eines Dokuments.
4. Wählen Sie **Confirm change** oder **Cancel**, um die alte Einstellung zu behalten.

Fehlt Ihnen die Berechtigung, zeigt DocBits eine Meldung, dass ein Organisationsadministrator erforderlich ist, und nichts ändert sich.

## Verwandte Seiten

* [E-Rechnungs-Prüfung](./)
* [Änderungsprotokoll](validation-change-log.md)
* [Validierungs-Setup und akzeptierte Versionen](validation-setup.md)
* [Prüfbericht](validation-report.md)
* [E-Rechnungs-Validierung aktivieren oder deaktivieren](../#e-rechnungs-validierung-aktivieren-oder-deaktivieren)
