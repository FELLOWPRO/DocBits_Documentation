# Formatierung von Exportzertifikat-Referenznummern - Skript für DocBits

Dieses Dokument beschreibt das Skript "Formatierung von Exportzertifikat-Referenznummern", das darauf abzielt, Referenznummern auf Exportzertifikaten in DocBits zu standardisieren. Eine ordnungsgemäße Formatierung stellt sicher, dass Referenznummern den Anforderungen externer Systeme oder behördlicher Vorschriften entsprechen.

### Zweck

Das Hauptziel des Skripts ist die Formatierung von Referenznummern auf Exportzertifikaten, um sicherzustellen, dass sie eine vordefinierte Längenanforderung erfüllen, indem sie mit führenden Nullen aufgefüllt werden. Diese Konsistenz hilft, ein standardisiertes Format für alle über DocBits verarbeiteten Exportdokumente aufrechtzuerhalten.

### Skriptübersicht

Das Skript identifiziert das Feld `reference_number` in einem Exportzertifikat, überprüft dessen Länge und füllt die Nummer bei Bedarf mit führenden Nullen auf, um sicherzustellen, dass sie die Mindestlängenanforderung erfüllt.

#### Code-Ausschnitt

```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Sicherstellen, dass die Referenznummer eine Mindestlänge von 10 Zeichen hat
if len(ref_number) < 10:
    ref_number = ref_number.zfill(10)
    set_field_value(fields_dict, 'reference_number', ref_number)
```
