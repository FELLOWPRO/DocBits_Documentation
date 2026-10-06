# Regex-Manager

Diese Funktion von DocBits ist eine Alternative zur Modell-Klassifizierung: Sie können durchsuchbare reguläre Ausdrücke für einen Dokumenttyp schreiben, für die Klassifizierung und andere Zwecke.

**Dokumenttyp:** Mit dem Regex-Manager schreiben Sie reguläre Ausdrücke, und DocBits sucht das Dokument nach diesen Ausdrücken ab. Findet das Dokument eine Übereinstimmung mit dem Regex eines definierten Dokuments, wird es dem entsprechenden Dokumenttyp zugeordnet. Schreiben Sie zum Beispiel einen regulären Ausdruck, der „Gutschrift“ findet, so stuft DocBits ein Dokument, das diesen Begriff enthält, als Gutschrift ein.

**Dokumentenherkunft:** Damit weiß DocBits über reguläre Ausdrücke, aus welchem Land ein Dokument stammt. Enthält zum Beispiel der reguläre Ausdruck für ein spanisches Dokument den Begriff „Factura“ und DocBits findet diesen Begriff in einem Dokument, erkennt DocBits die spanische Herkunft und ordnet das Dokument entsprechend ein.

## Zugriff auf den Regex-Manager

Um diese Funktion zu nutzen, gehen Sie zu Einstellungen → Dokumenttypen und klicken Sie auf „Neu“. Geben Sie im Assistenten „Neue Dokumentart erstellen“ einen Namen für den Dokumenttyp ein und wählen Sie als Extraktionsmethode „Regex“ statt „Automatisch“, fahren Sie dann mit „Weiter“ fort.

<figure><img src="../../../.gitbook/assets/regex-manager-create-de-20261006.png" alt="Der DocBits-Assistent zum Erstellen einer neuen Dokumentart mit ausgefülltem Namen und ausgewählter Option „Regex“."><figcaption><p>Der Assistent „Neue Dokumentart erstellen“ mit dem Namen des Dokumenttyps und der Wahl zwischen „Automatisch“ und „Regex“.</p></figcaption></figure>

## Regex hinzufügen und entfernen

Der Regex-Schritt zeigt eine Tabelle der vorhandenen regulären Ausdrücke mit Herkunft und Muster sowie die Schaltfläche „hinzufügen“, um neue Regex-Einträge zu erstellen.

<figure><img src="../../../.gitbook/assets/regex-manager-list-de-20261006.png" alt="Die Tabelle des Regex-Managers mit den vorhandenen regulären Ausdrücken nach Herkunft und Muster."><figcaption><p>Der Regex-Schritt mit der Tabelle der vorhandenen regulären Ausdrücke und der Schaltfläche „hinzufügen“.</p></figcaption></figure>
