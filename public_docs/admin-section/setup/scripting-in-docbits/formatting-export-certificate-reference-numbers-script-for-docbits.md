# Formatierung Exportzertifikat-Referenznummernskript für Docbits

Dieses Dokument beschreibt das Skript "Formatierung Exportzertifikat-Referenznummern", das darauf abzielt, Referenznummern über Exportzertifikate in Docbits zu standardisieren. Eine ordnungsgemäße Formatierung stellt sicher, dass Referenznummern den Anforderungen externer Systeme oder behördlicher Vorschriften entsprechen.

### Zweck

Das Hauptziel des Skripts besteht darin, Referenznummern auf Exportzertifikaten zu formatieren, um sicherzustellen, dass sie eine vordefinierte Längenanforderung erfüllen, indem sie mit führenden Nullen aufgefüllt werden. Diese Konsistenz trägt dazu bei, ein standardisiertes Format für alle Exportdokumente sicherzustellen, die durch Docbits verarbeitet werden.

### Skriptübersicht

Das Skript identifiziert das Feld `reference_number` in einem Exportzertifikat, überprüft dessen Länge und füllt die Nummer bei Bedarf mit führenden Nullen auf, um sicherzustellen, dass sie die Mindestlängenanforderung erfüllt.

#### Code-Schnipsel
```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Ensure the reference number meets a minimum length of 10 characters
if len(ref_number) < 10:
ref_number = ref_number.zfill(10)
set_field_value(fields_dict, 'reference_number', ref_number)
```

