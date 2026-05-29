# Negatives Vorzeichen für Gutschriften setzen

### Überblick

Die Einstellung **Negatives Vorzeichen für Gutschriften setzen** (Set Negative Sign for Credit Notes) stellt sicher, dass **Gutschriften** mit **negativen Beträgen** gespeichert werden. Eine Gutschrift storniert oder erstattet einen Teil einer Rechnung, daher sollten ihre Werte in der Buchhaltung die Summen verringern — also negativ sein. Wenn diese Einstellung aktiviert ist, setzt DocBits dieses negative Vorzeichen automatisch.

Diese Einstellung ist **standardmäßig aktiviert**.

### Was bewirkt die Einstellung?

Wird ein Dokument als **Gutschrift** erkannt, wandelt DocBits dessen Beträge bei der Verarbeitung automatisch in negative Werte um. Betroffen sind die Geldfelder, darunter Nettobeträge, Steuerbeträge und Summen (z. B. Nettobetrag, Steuerbetrag, Gesamtsteuerbetrag, Gesamtnettobetrag und Gesamtbetrag).

* **Aktiviert (Standard)** — Gutschriftsbeträge werden als negative Werte gespeichert (z. B. wird aus `150,00` der Wert `-150,00`). Normale Rechnungen sind nicht betroffen.
* **Deaktiviert** — Die Beträge bleiben genau so, wie sie aus dem Dokument ausgelesen wurden, ohne Vorzeichenänderung.

{% hint style="info" %}
Dies gilt nur für Dokumente, die als **Gutschrift** erkannt werden. Normale Rechnungen bleiben immer unverändert.
{% endhint %}

### Vorteile

* **Korrekte Buchhaltung**: Gutschriften verringern Salden, daher sind negative Werte das, was Ihre Buchhaltungs- und ERP-Systeme erwarten.
* **Keine manuelle Bearbeitung**: Ihr Team muss das Vorzeichen nicht bei jeder Gutschrift von Hand ändern.
* **Einheitlichkeit**: Jede Gutschrift wird organisationsweit gleich behandelt.

### Verwendung

1. Gehen Sie zu **Einstellungen**.
2. Wählen Sie **Dokumentverarbeitung**.
3. Wählen Sie **Modul**.
4. Öffnen Sie den Abschnitt **Dokumenttyp**.
5. Finden Sie **Negatives Vorzeichen für Gutschriften setzen** und schalten Sie den Schalter ein oder aus.

### Wann diese Funktion nutzen

* **Aktiviert lassen**, wenn Ihr Buchhaltungs- oder ERP-System erwartet, dass Gutschriften mit negativen Beträgen ankommen (dies ist die häufigste Konfiguration).
* **Deaktivieren** Sie sie nur, wenn Ihr nachgelagertes System das Vorzeichen bereits selbst handhabt oder Gutschriftsbeträge positiv bleiben sollen.
