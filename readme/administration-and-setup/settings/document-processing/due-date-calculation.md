# Fälligkeitsberechnung

<figure><img src="../../../.gitbook/assets/core6846-due-date-calculation-de.png" alt="Einstellungen der Fälligkeitsberechnung"><figcaption><p>Einstellungen der Fälligkeitsberechnung</p></figcaption></figure>

Die Seite **Fälligkeitsberechnung** (**Dokumentenverarbeitung → Fälligkeitsberechnung**) steuert, wie DocBits Fälligkeitsdaten von Rechnungen, Skonto-Fälligkeitsdaten und Zahlungsbedingungen aus den auf Rechnungen gefundenen Zahlungsbedingungs-Codes berechnet.

Die Karte **Invoice Due Date Calculation** enthält die allgemeinen Einstellungen. Speichern Sie Änderungen über **Speichern** in ihrer Kopfzeile. Darunter finden Sie die Tabellen für Skonto- und Zahlungsbedingungs-Überschreibungen sowie eine Übersicht der unterstützten Formate.

## Berechnete Felder anzeigen

Aktivieren Sie **Berechnete Felder anzeigen**, damit die automatisch berechneten Rechnungsfelder – Fälligkeitsdatum, Skonto-Fälligkeitsdatum, Zahlungsbedingungen und AP-Zuordnungscode – in den Feldeinstellungen sowie als Variablen in der Schnellsuche und in E-Mail-Vorlagen erscheinen. Benutzerdefinierte Dokumenttypen sind nie betroffen.

## Rechnungsfälligkeitsdatum-Berechnung

### Wochenend-Behandlung

Wählen Sie die **Wochenend-Behandlung**, um festzulegen, wie ein Fälligkeitsdatum angepasst wird, das auf einen Samstag oder Sonntag fällt. Dies gilt **sowohl** für das Rechnungsfälligkeitsdatum als auch für das Skonto-Fälligkeitsdatum.

| Konvention | Wirkung |
|------------|---------|
| **Keine** | Kalenderdatum beibehalten (keine Anpassung). |
| **Folgend** | Sa/So auf den nächsten Montag verschieben. |
| **Vorausgehend** | Sa/So auf den vorherigen Freitag verschieben. |
| **Nächste** | Samstag → Freitag, Sonntag → Montag. |
| **Modifiziert Folgend** | Nächster Montag, außer er fällt in den nächsten Monat – dann vorheriger Freitag. |

### AP-Zuordnungscode

Ordnen Sie Lieferanten-Zahlungsbedingungen AP-Zuordnungscodes für die automatisierte Rechnungsweiterleitung zu, indem Sie das **AP-Zuordnungscode-Feld** auswählen.

## Skonto-Überschreibungen

<figure><img src="../../../.gitbook/assets/core6846-discount-term-overwrites-de.png" alt="Skonto-Überschreibungen"><figcaption><p>Skonto-Überschreibungen</p></figcaption></figure>

Verwenden Sie **Skonto-Überschreibungen**, um ein bestimmtes Präfix einem Skonto-Prozentsatz und einer Anzahl von Tagen zuzuordnen. Klicken Sie auf **Zuordnung hinzufügen**, um eine Zeile mit **Präfix**, **Prozentsatz** und **Tagen** hinzuzufügen. Um eine bestehende Zuordnung zu ändern oder zu entfernen, verwenden Sie das Menü (⋮) am Zeilenende.

## Zahlungsbedingungs-Überschreibungen

<figure><img src="../../../.gitbook/assets/core6846-payment-term-overwrites-de.png" alt="Zahlungsbedingungs-Überschreibungen"><figcaption><p>Zahlungsbedingungs-Überschreibungen</p></figcaption></figure>

Verwenden Sie **Zahlungsbedingungs-Überschreibungen**, um einem Zahlungsbedingungs-Code einen Typ, eine Anzahl Tage und eine Beschreibung zuzuordnen. Klicken Sie auf **Zuordnung hinzufügen**, um eine Zeile anzulegen, und verwenden Sie das Menü (⋮) am Zeilenende, um eine Zuordnung zu ändern oder zu entfernen.

## Unterstützte Formate

<figure><img src="../../../.gitbook/assets/core6846-supported-formats-de.png" alt="Unterstützte Zahlungsbedingungs- und Skonto-Formate"><figcaption><p>Unterstützte Zahlungsbedingungs- und Skonto-Formate</p></figcaption></figure>

DocBits erkennt die folgenden Zahlungsbedingungs- und Skonto-Codes.

**Unterstützte Zahlungsbedingungs-Formate**

| Format | Beispiel | Bedeutung |
|--------|----------|-----------|
| Infor M3 | `N90`, `N30` | Netto 90 / 30 Tage |
| Infor M3 | `NET` | Zahlbar bei Erhalt |
| Infor M3 | `M20` | 20. des Folgemonats |
| Infor M3 | `E15` | Monatsende + 15 Tage |
| Infor LN | `030`, `30` | Netto 30 Tage |
| Reversed | `14N`, `30N` | Netto 14 / 30 Tage |
| Text-Codes | `REC`, `DUE`, `COD` | Zahlbar bei Erhalt |

**Skonto-Format** – Skonto-Bedingungen kodieren Frühzahlerrabatte als 3-stellige Codes: die erste Ziffer ist der Skonto-Prozentsatz, die letzten beiden sind die Tage, innerhalb derer gezahlt werden muss.

| Code | Bedeutung |
|------|-----------|
| `210` | 2 % Skonto bei Zahlung innerhalb von 10 Tagen |
| `130` | 1 % Skonto bei Zahlung innerhalb von 30 Tagen |
| `545` | 5 % Skonto bei Zahlung innerhalb von 45 Tagen |
| `0` | Kein Skonto |
