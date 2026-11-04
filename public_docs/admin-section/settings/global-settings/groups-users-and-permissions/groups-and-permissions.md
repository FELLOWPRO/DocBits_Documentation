# Gruppen und Berechtigungen

<figure><img src="../../../../.gitbook/assets/docbits_groups_permissions_overview.png" alt="Docbits Groups Permissions Overview"><figcaption></figcaption></figure>

#### Komponenten des Abschnitts Gruppen und Berechtigungen

1. **Gruppen und Berechtigungen aktivieren/deaktivieren**: Ein Schalter, der es dem Systemadministrator ermöglicht, die Verwendung von Gruppen und Berechtigungen plattformweit zu aktivieren oder zu deaktivieren. Wenn dies deaktiviert ist, kann das System auf ein weniger granulares Zugriffssteuerungsmodell zurückgreifen.
2. **Gruppenliste**: Zeigt die Liste der verfügbaren Benutzergruppen innerhalb der Organisation an. Jede Gruppe kann mit spezifischen Berechtigungen konfiguriert werden. Administratoren können neue Gruppen hinzufügen, indem sie auf die Schaltfläche "+ Neu" klicken.
3. **Berechtigungstabelle**:

- Wird angezeigt, sobald eine Gruppe ausgewählt oder eine neue Gruppe konfiguriert wird.
- Listet alle vom System erkannten Dokumententypen auf (z. B. RECHNUNG, GUTSCHRIFT, LIEFERSCHEIN).
- Für jeden Dokumententyp gibt es Kontrollkästchen für verschiedene Berechtigungen:
  - **Anzeigen**: Berechtigung, das Dokument zu sehen.
  - **Aktualisieren**: Berechtigung, das Dokument zu ändern.
  - **Löschen**: Berechtigung, das Dokument aus dem System zu entfernen.
  - **Erste Genehmigung**: Berechtigung, die erste Genehmigung des Dokuments durchzuführen.
  - **Zweite Genehmigung**: Berechtigung, eine sekundäre Genehmigungsstufe durchzuführen (falls zutreffend).

<figure><img src="../../../../.gitbook/assets/docbits_second_approval_permission.png" alt="Docbits Second Approval Permission"><figcaption></figcaption></figure>

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2486" %}
