# Tabellenzeilen neu aufbauen

[Zurück zum vollständigen Praxisüberblick](praxisueberblick.md)

Tabelle INVOICE_TABLE · clear_rows → add_row am Ende · POSITION=001, QUANTITY=1, NET_AMOUNT aus header.total_net_amount.

## Vorgehen im Editor

1. Den vorgesehenen Dokumenttyp öffnen und den Geltungsbereich wählen.
2. Ziel und gegebenenfalls eine getrennte Quelle einstellen.
3. Die unten beschriebenen Schritte in der passenden Reihenfolge konfigurieren.
4. Eingabe und Gegenfall in der Vorschau prüfen und mit dem Servertest vergleichen.
5. Eine gespeicherte Regel erneut öffnen; die Dokumentwirkung mit einem isolierten Beleg prüfen.

<figure><img src="../../../../../.gitbook/assets/transformation-series-08-steps-de-20261028.png" alt="Konfiguration der Schritte – Tabellenzeilen neu aufbauen"><figcaption><p>Konfiguration der Schritte. Originalaufnahme der deutschen Oberfläche. Die Vorschau verändert keine gespeicherten Dokumente.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/transformation-series-08-preview-de-20261028.png" alt="Live-Vorschau mit Schulungswert – Tabellenzeilen neu aufbauen"><figcaption><p>Live-Vorschau mit Schulungswert. Originalaufnahme der deutschen Oberfläche. Die Vorschau verändert keine gespeicherten Dokumente.</p></figcaption></figure>

## 1. Zeilen aufbauen

Alle Zeilen löschen entfernt die vorhandenen Zeilen der ausgewählten Tabelle. Zeile hinzufügen baut anschließend eine neue Zeile auf. Für jede Spalte wähle ich entweder einen festen Wert oder den Wert eines Kopffelds. In meinem Beispiel entsteht eine Gesamtposition mit Menge eins und einem Nettobetrag aus dem Rechnungskopf. Nicht befüllte Spalten bleiben leer. Die neue Zeile kann am Anfang oder am Ende stehen. Das ist keine automatische Gruppierung oder Summierung ausgewählter vorhandener Positionen.

## 2. Schrittreihenfolge

Die Reihenfolge ist entscheidend. Löschen und danach hinzufügen ergibt die gewünschte neue Zeile. Hinzufügen und danach löschen entfernt auch die gerade erzeugte Zeile. Ohne vorausgehendes Löschen würde ein weiterer Durchlauf noch eine Zeile anhängen. Dafür verlangt die Regel eine passende Einmalausführung. Eine Vorschau mit einer Zeilenzahl prüft die Struktur, ersetzt aber noch keinen Test mit einer echten extrahierten Tabelle. Ich kontrolliere die Spaltenwerte und die Zeilenzahl nach dem Speichern.

## 3. Bestellabgleich getrennt prüfen

Eine Tabellenregel läuft vor den Spaltenregeln. Eine nachgelagerte Spaltenregel kann deshalb auch neu hinzugefügte Zeilen bereinigen. Das Neuaufbauen von Positionen kann bestehende Zeilenkennungen und Bestellzuordnungen verändern. Für eine Rechnung, die bewusst auf den Gesamtbetrag abgeglichen wird, brauche ich zusätzlich die passende Bestellabgleichsregel. Die Transformation allein bestätigt keinen vollständigen Abgleich. Ich teste das nur mit einem isolierten Beleg und prüfe nach erneutem Speichern die Zeilenzahl und den Abgleichsstatus getrennt.


## Abnahme

Prüfen Sie einen passenden Fall, einen Gegenfall, einen leeren Wert und ein bereits verarbeitetes Ergebnis. Wiederholen Sie den Dokument-Speichervorgang. Prüfen Sie PO-Abgleich und ERP-Empfang zusätzlich, wenn sie zum fachlichen Ziel gehören.
