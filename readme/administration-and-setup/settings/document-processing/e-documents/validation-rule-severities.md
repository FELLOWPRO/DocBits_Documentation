# Regel-Schweregrade

Jede Validierungsregel hat einen Schweregrad. Sie können den Schweregrad jeder Regel für Ihre Organisation ändern. Diese Seite gehört zur [E-Rechnungs-Prüfung](validation-rules.md). Nur Organisationsadministratoren können die Schweregrade ändern.

<figure><img src="../../../../.gitbook/assets/einvoice-rule-table-de.png" alt="Die Validierungsregel-Tabelle"><figcaption><p>Die vollständige Regeltabelle mit Schweregrad-Override pro Regel</p></figcaption></figure>

Die Regeltabelle listet jede Validierungsregel auf (insgesamt über 1.600). Filtern Sie nach **Ebene (Layer)**, **Profil** oder **Version** oder suchen Sie nach Code oder Feld. Für jede Regel können Sie den **Schweregrad** über das Dropdown überschreiben, um ihn an die Richtlinien Ihrer Organisation anzupassen – zum Beispiel eine Regel von `ERROR` auf `WARNING` herabstufen, damit sie das Dokument nicht mehr ablehnt.

Die Bedeutung von **FATAL**, **ERROR**, **WARNING** und **INFO** ist unter [Validierungs-Setup und akzeptierte Versionen](validation-setup.md#akzeptierte-profile-und-schweregrad-modell) erklärt. Ein geänderter Schweregrad erscheint außerdem im [Prüfbericht](validation-report.md) in der Spalte **Ihre Organisation**.
