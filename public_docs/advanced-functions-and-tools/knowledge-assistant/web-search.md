# Websuche

Mit der Websuche kann der Wissensassistent zusätzlich zu Ihren eigenen Dokumenten **öffentliche Informationen im Internet** nachschlagen, zum Beispiel die aktuelle Adresse einer Firma oder den aktuellen Basiszinssatz. Ein Administrator schaltet sie pro Organisation ein. Sie ist **standardmäßig aus**.

{% hint style="warning" %}
Die Websuche ist eine Funktion nach dem Prinzip **Best Effort**. Treffer sind Links mit einem kurzen Textauszug aus öffentlichen Webseiten. Sie sind nicht geprüft und ersetzen keine Abfrage in einem amtlichen Register. Prüfen Sie jeden Wert auf der Seite, auf die der Treffer verweist.
{% endhint %}

{% hint style="info" %}
Die Beispiele auf dieser Seite sind allgemein gehalten. Das hier beschriebene Verhalten haben wir am 28. November 2026 auf unserer DocBits-Local-Testinstallation gemessen. Wie zuverlässig die Websuche mit Ihren Fragen und in Ihrer Umgebung arbeitet, sagt diese Seite nicht.
{% endhint %}

## Websuche einschalten (Administrator)

1. Öffnen Sie **Einstellungen** → **Module** → **Dokumentenintegration**.
2. Öffnen Sie die Karte **Wissensassistent** und gehen Sie zu **Funktionen**.
3. Schalten Sie **Websuche** ein.

Die Einstellung gilt für die ganze Organisation. Ist die Websuche aus, weist der Assistent darauf hin, dass ein Administrator sie unter **Funktionen** einschalten kann.

Der Hinweis auf dem Bildschirm lautet: „Der Assistent darf im Internet suchen. Die Suchanfragen verlassen DocBits.“ Schalten Sie die Websuche nur ein, wenn Ihr Unternehmen das erlaubt.

### Suche ohne Rückfrage

Unter **Funktionen** gibt es einen zweiten Schalter, **Websuche ohne Rückfrage**. Er setzt voraus, dass die Websuche an ist, und ist standardmäßig aus.

* **Aus (Standard):** Vor jeder Suche zeigt der Assistent Ihnen den Suchtext und fragt nach Ihrer Bestätigung (**Senden** oder **Nicht senden**). Ohne Ihre Bestätigung verlässt nichts DocBits.
* **An:** Ein Suchtext, der aus Ihrer Frage stammt, wird ohne Rückfrage gesendet. Suchtexte, die der Assistent selbst formuliert hat, werden laut Hinweis auf dem Bildschirm weiterhin immer bestätigt.

## So läuft eine Suche ab

1. Sie stellen im **Chat** eine Frage, die öffentliche Informationen braucht, zum Beispiel: „Wie lautet die eingetragene Adresse dieses Lieferanten?“
2. Der Assistent schlägt einen Suchtext vor. Ist **Websuche ohne Rückfrage** nicht an, sehen Sie den Text mit der Frage „Diese Suchanfrage wird an die Websuche gesendet:“ und wählen **Senden** oder **Nicht senden**.
3. Der Assistent erhält die Treffer und antwortet mit den Quellen, die er genutzt hat. Treffer aus dem Web sind Links auf öffentliche Seiten.

Laut Hinweis auf dem Bildschirm läuft die Websuche im Modus Smart Reasoning und ist im Modus Quick Answer aus. Siehe [Den richtigen Agenten wählen](choose-the-right-agent.md).

## Wie die Suche arbeitet

Standardmäßig läuft die Websuche **über DocBits**. Sie brauchen weder einen Schlüssel noch ein Konto bei einem Suchanbieter.

* Die Suche läuft **ohne Schlüssel** über DocBits. Sie ist als **Best Effort** gekennzeichnet: Bei automatisierten Abfragen kann sie gesperrt oder ungenau sein, dann liefert eine Suche kein oder ein schlechtes Ergebnis.
* Ein Treffer besteht aus einem **Link und einem kurzen Textauszug**, nicht aus dem Text der Seite. Werte wie ein Zinssatz oder ein Kurs stehen daher nicht immer im Textauszug. Fehlt ein Wert, sagt der Assistent das; öffnen Sie dann die verlinkte Seite und lesen Sie den Wert dort ab.
* Den Anbieter können Sie auf dem Bildschirm nicht ändern. Ein eigener Suchanbieter mit eigenem Schlüssel ist geplant, aber in der Oberfläche **noch nicht verfügbar**.

## Datenschutz

* **Keine langen Zahlen im Suchtext.** Der Assistent darf keine längeren Zahlenfolgen, etwa Rechnungs-, Konto- oder IBAN-Nummern, in einen Suchtext schreiben. Der Suchtext wird vor dem Senden geprüft. Enthält er Zeichen oder Zahlen, die aus Datenschutzgründen nicht gesendet werden, wird die Suche nicht gesendet und Sie sehen eine Meldung.
* **Suchtexte werden nicht protokolliert.**
* **Treffer sind ungeprüfte Webinhalte** mit Quellenangabe. Der Assistent nennt die Quelle; ob Sie ihr vertrauen, entscheiden Sie.

## Grenzen

* **Höchstens 3 Suchen pro Frage.** Abgelehnte Suchen (**Nicht senden**) zählen nicht mit, bis zu 10 Ablehnungen.

## Typische Anwendungen

* **Lieferanten prüfen:** Firmenname und Adresse eines Lieferanten, die Sie mit den Angaben auf einer Rechnung vergleichen möchten.
* **Aktuelle Referenzzinssätze:** zum Beispiel der aktuelle Basiszinssatz, wenn Sie eine Verzugszinsklausel aus Ihrem Vertrag prüfen.

In beiden Fällen ist der Treffer aus dem Web ein **Hinweis**. Vergleichen Sie ihn mit der Originalquelle, bevor Sie ihn verwenden.

## Ehrliche Grenzen

* Die Websuche ist **keine Registerabfrage**. Für Handelsregister, Steuernummer oder USt-IdNr. nutzen Sie das amtliche Register.
* Die Websuche gibt **keine Rechtsberatung** und trifft keine Freigabe- oder Zahlungsentscheidung.
* Eine Suche kann kein, ein altes oder ein falsches Ergebnis liefern. Webseiten können automatisierte Abfragen sperren.
* Der Assistent liest keine ganzen Webseiten; er arbeitet mit Links und kurzen Textauszügen.

## Meldungen, die Sie sehen können

| Meldung | Bedeutung | Was Sie tun können |
| --- | --- | --- |
| Die Websuche ist für Ihre Organisation nicht eingeschaltet. Ein Administrator kann sie unter Funktionen einschalten. | Der Schalter ist aus. | Fragen Sie Ihren Administrator. |
| Die Suchanfrage enthält Zeichen oder Zahlen, die aus Datenschutzgründen nicht gesendet werden. | Der Suchtext enthielt eine lange Zahlenfolge oder andere Zeichen. | Fragen Sie ohne die Zahl, zum Beispiel nur mit dem Firmennamen. |
| Die Websuche wurde nicht gesendet, weil sie nicht bestätigt wurde. | Sie haben **Nicht senden** gewählt oder nicht bestätigt. | Fragen Sie erneut und bestätigen Sie den Suchtext. |
| Die Websuche ist gerade nicht verfügbar. / Die Websuche hat kein Ergebnis geliefert. Bitte versuchen Sie es später erneut. | Der Suchdienst hat nicht geantwortet oder nichts geliefert. Das kann bei einer Best-Effort-Suche vorkommen. | Versuchen Sie es später erneut oder schlagen Sie den Wert direkt auf der Webseite nach. |
| Zu viele Websuchen in kurzer Zeit. | Die Zahl der Suchen ist begrenzt. | Warten Sie einen Moment. |
| Die Websuche ist für dieses Konto nicht erlaubt. | Ihr Konto darf sie nicht nutzen. | Fragen Sie Ihren Administrator. |

Siehe auch: [Aufgaben und wo Sie sie finden](tasks-and-where-to-find-them.md), [Den richtigen Agenten wählen](choose-the-right-agent.md) und [Was er kann und was nicht](what-it-can-and-cannot-do.md).
