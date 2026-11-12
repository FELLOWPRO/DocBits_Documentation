# Lieferanten und Bestellungen aus Infor M3

Dieses Beispiel verbindet die BODs für Lieferanten und Bestellungen aus M3 über Infor ION mit DocBits. Die fünfzehn Infor-Bilder auf dieser Seite sind historische Beispiele aus einem Kundenmandanten und belegen nicht, dass Ihre M3-Einrichtung aktuell funktioniert. Lassen Sie vom Infor-Administrator die BOD-Namen, Quelltabellen, Firma, Division, API-Call-Namen und das Zielsystem bestätigen, bevor Sie einen Job starten. Für diese Überarbeitung wurde kein M3-Initial-Load und kein DocBits-Import ausgeführt.

Der [Initial-Load-Leitfaden von Infor](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html) erklärt die Definitionen in EVS006, den BOD-Verb mit der Auswahl, das Absenden und den Verlauf. Wählen Sie zuerst eine kleine Auswahl; ein uneingeschränkter Lauf kann sehr viele Ereignisse erzeugen.

## **Verbindungspunkt**

Sie müssen den DocBits-API-Verbindungspunkt anlegen, um später den Datenfluss erstellen zu können.

Navigieren Sie in InforOS zu ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o" alt="Historische ION-Desk-Navigation mit aufgeklappter Gruppe Connect und hervorgehobenen Connection Points."><figcaption><p>Historische Navigation: ION Desk → Connect → Connection Points.</p></figcaption></figure>

Dort angekommen legen Sie einen neuen Verbindungspunkt an.

<figure><img src="https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE_WQj-0ONoE7McRl-f6_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI" alt="Historische Seite Connection Points mit einem grünen Pfeil auf Add."><figcaption><p>Historische Aktion Add zum Anlegen eines Verbindungspunkts.</p></figcaption></figure>

**Wählen Sie API**

Geben Sie dem Verbindungspunkt einen Namen und eine Beschreibung, die seinen Zweck und seine Umgebung wiedergeben. Importieren Sie unter dem Reiter „Connection" das Service-Konto, das Sie für die Umgebung angelegt haben, mit der Sie arbeiten.

<figure><img src="https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0" alt="Historischer Verbindungspunkt DocBits-DEV-Demo-Import mit ausgewähltem Reiter Connection und einem Service-Konto Import."><figcaption><p>Historischer Reiter Connection. Die gezeigten Namen gehören zur Beispielumgebung; verwenden Sie Ihr eigenes Service-Konto.</p></figcaption></figure>

Wechseln Sie anschließend zum Reiter „Documents". Fügen Sie dem Verbindungspunkt die folgenden BODs hinzu. Nicht alle sind für die Stammdaten zu Lieferanten und Bestellungen nötig, sie werden aber gebraucht, wenn weitere Funktionen wie Auto Accounting eingerichtet werden.

<figure><img src="https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8" alt="Historischer Reiter Documents mit den BODs Acknowledge.SupplierInvoice, Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster und Sync.SupplierPartyMaster."><figcaption><p>Historische Liste der empfangenen Dokumente. Der gezeigte Lieferanten-BOD heißt Sync.RemitToPartyMaster, ohne das Suffix Data.</p></figcaption></figure>

Diese historische Einrichtung verwendet Sync.RemitToPartyMaster, Sync.SupplierPartyMaster und Sync.PurchaseOrder. Bestätigen Sie, welche BODs Ihr DocBits-Mapping benötigt; die Einrichtung kann je nach Mandant und Funktion abweichen.

* Sync.RemitToPartyMaster und Sync.SupplierPartyMaster

Das folgende historische Bild zeigt Sync.SupplierPartyMaster. Konfigurieren Sie jeden benötigten Lieferanten-BOD mit dem API-Call-Namen und der empfangenden Operation, die für Ihre Umgebung bestätigt wurden; die zweite Lieferantenroute ist nicht abgebildet.

<figure><img src="https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk" alt="Historischer Reiter ION API mit der Auswahl Send to API, dem API Call Name Sync.SupplierPartyMaster und der Operation POST."><figcaption><p>Historische Route SupplierPartyMaster. Das Bild zeigt eine Lieferantenroute; bestätigen Sie die empfangende Operation für jeden benötigten BOD separat.</p></figcaption></figure>

* Sync.PurchaseOrder

Das folgende historische Bild zeigt eine empfangende Operation für Bestellungen. Bestätigen Sie den aktuellen Endpunkt und das Anforderungsformat für Ihre Umgebung.

<figure><img src="https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4" alt="Historischer Reiter ION API mit der Auswahl Send to API für Sync.PurchaseOrder und der Operation POST."><figcaption><p>Historische Route PurchaseOrder. Der gezeigte alte API-Gateway-Pfad ist ein Beispiel und keine allgemeingültige DocBits-Adresse.</p></figcaption></figure>

Sind diese BODs konfiguriert, speichern Sie den Verbindungspunkt über das Symbol direkt rechts neben der Zurück-Schaltfläche.

## **Datenfluss**

Dieser historische Datenfluss ist ein möglicher Aufbau; prüfen Sie Routen und empfangende Organisation in Ihrem eigenen Mandanten.

<figure><img src="https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8" alt="Historischer Ablauf von M3 über einen Ja- oder Nein-Filter und eine Parallelverzweigung zu vier DocBits-API-Knoten mit Zusammenführung und Endknoten."><figcaption><p>Historischer Ablauf. Der Nein-Zweig endet vor den API-Knoten; der Ja-Zweig erreicht die vier Beispielumgebungen.</p></figcaption></figure>

Die mehreren DocBits-API-Knoten stehen in diesem Beispiel für getrennte Umgebungen. Ihr Aufbau kann abweichen; stellen Sie sicher, dass Testnachrichten die Produktion nicht erreichen.

Die vier Umgebungen sind nur ein Beispiel.

### **M3**

Der Beginn des Datenflusses ist Ihre M3-Anwendung

### **Filter**

Die Konfiguration des Filters sieht wie folgt aus

<figure><img src="https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374_T2V0q__QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY" alt="Historischer Bereich Filter Properties mit ausgewähltem Reiter Properties sowie Name und Description jeweils auf Division."><figcaption><p>Historischer Filtername und Beschreibung. Der Name Division allein sagt nicht, welche Datensätze gefiltert werden.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA" alt="Historischer Reiter Attributes im Bereich Filter Properties mit AccountingEntityID-Pfaden für ChartOfAccounts, PurchaseOrder, RemitToPartyMaster und SupplierPartyMaster."><figcaption><p>Historische Attribute: Jeder BOD hat einen Pfad AccountingEntityID. Prüfen Sie den Pfad für jedes Dokument in Ihrem Mandanten.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3_2DPj96aV0vLdZk2tzw" alt="Historischer Reiter Conditions im Bereich Filter Properties mit dem Dokument ChartOfAccounts, der Bedingung Not Filtered und einem Beispielausdruck für AccountingEntityID_3."><figcaption><p>Historisches Beispiel für Conditions. Used Condition zeigt Not Filtered, obwohl ein Ausdruck eingetragen ist; prüfen Sie die gewählte Bedingung und ihre Wirkung, statt von einem aktiven Ausdruck auszugehen.</p></figcaption></figure>

(Die Buchungskreis-ID (Accounting Entity ID) ist selbstverständlich für Ihre Organisation einzigartig.)

### **DocBits-API**

Hier fügen Sie eine Anwendung hinzu und wählen die zuvor angelegte(n) DocBits-API(s) aus

### **Dokumente**

Wählen Sie die Dokumente aus, die dem M3-Quellknoten und den empfangenden Knoten zugeordnet sind. Prüfen Sie, dass die Filterattribute und die empfangenden Routen jedes benötigte Dokument abdecken.

<figure><img src="https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY" alt="Historischer M3-Ablauf mit hervorgehobenem Dokument-Symbol und einem Bereich Documents mit Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster und Sync.SupplierPartyMaster."><figcaption><p>Historische Dokumentauswahl für den M3-Ablauf. Das ist eine BOD-Dokumentliste, keine Konfiguration eines Datei-Knotens.</p></figcaption></figure>

## **M3-BODs auslösen**

Öffnen Sie die Infor-M3-Anwendung

Öffnen Sie in M3 das Steuerelement **Search and Start**, geben Sie **EVS006** ein und bestätigen Sie das Programm. Verwenden Sie die Navigation, die Ihr M3-Client unterstützt.

<figure><img src="https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr_o" alt="Historischer Dialog Search and Start in M3 mit dem Eintrag evs006 und der Schaltfläche OK."><figcaption><p>Historische Programmsuche: EVS006 in Search and Start eingeben.</p></figcaption></figure>

Legen Sie in EVS006 die BOD-Nouns an, die Ihr freigegebenes Mapping benötigt. Das historische Beispiel verwendet SupplierPartyMaster, RemitToPartyMaster und PurchaseOrder. Bestätigen Sie deren M3-Tabellennamen in Ihrer Version, bevor Sie eine Initial-Load-Definition anlegen.

BOD Noun: SupplierPartyMaster

Table: CIDMAS

BOD Noun: RemitToPartyMaster

Table: CIDMAS

BOD Noun: PurchaseOrder

Table: MPHEAD

Verwenden Sie für jede freigegebene Definition die Aktion zum Hinzufügen. Prüfen Sie Firma und Division, bevor Sie fortfahren.

<figure><img src="https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN_ZlPk3W_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k_94_pYjt6Uw" alt="Historischer Ausschnitt der EVS006-Werkzeugleiste mit hervorgehobenem Add über leeren Feldern für BOD noun, BOD variant, BOD und Table."><figcaption><p>Historische Aktion Add in EVS006. Dieser Ausschnitt zeigt keine ausgefüllten Initial-Load-Definitionen.</p></figcaption></figure>

Nachdem Sie alle BODs hinzugefügt haben, klicken Sie mit der rechten Maustaste auf das BOD Noun des BOD und wählen Sie Related → Run

<figure><img src="https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH_eIYzFj22XgFHZccEM9g2nVQ_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo" alt="Historisches Kontextmenü mit aufgeklapptem Related und hervorgehobenem Run; darunter ist History aufgeführt."><figcaption><p>Historische Aktion Related → Run. Mit History prüfen Sie später das Ergebnis des Initial Load.</p></figcaption></figure>

Die verknüpfte Aktion **Run** öffnet EVS007. Wählen Sie **Sync** nur, wenn der empfangende ION-Ablauf es erwartet. Prüfen Sie Auswahl und Filter vor dem endgültigen Absenden; das Wechseln zum nächsten Bildschirm ist kein Beleg für eine Zustellung.

<figure><img src="https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD_ka--G1SFdzIhBAp7dq63_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA" alt="Historischer Bildschirm EVS007 Initial Load Job für CIDMAS und SupplierPartyMaster mit Status Pending, geöffnetem BOD-Verb-Menü und markiertem Sync, während Show noch angezeigt wird."><figcaption><p>Historische Verb-Auswahl in EVS007 vor der Ausführung. Das Bild zeigt einen wartenden Job und eine markierte Sync-Option; es belegt nicht, dass Sync gewählt oder Daten importiert wurden.</p></figcaption></figure>

Eine Absendebestätigung zeigt, dass der Job angefordert wurde. Prüfen Sie in EVS006 unter **History** die verarbeitete Anzahl und die Fehler. Kontrollieren Sie anschließend Nachricht und Ziel in Infor ION.

## Prüfung in DocBits

Öffnen Sie in der vorgesehenen DocBits-Organisation **Einstellungen → Dokumentenverarbeitung → Stammdaten → BOD Eingangsdaten → Lieferant**. Wählen Sie im Feld **Suche nach Spalten** das Feld für die Kennung, geben Sie in **Suche Zeichenfolge** eine bekannte Lieferantennummer oder einen Namen ein und starten Sie die Suche mit dem Lupensymbol. Öffnen Sie danach **Bestellung** und suchen Sie eine bekannte Bestellnummer; prüfen Sie bei getrennten Kopf- und Positionsdaten zusätzlich **Purchase Order Header** (dieser Eintrag wird auch in der deutschen Oberfläche englisch angezeigt). Vergleichen Sie Kennungen und Firma mit der M3-Quelle. Eine erfolgreiche EVS007-Anforderung allein belegt nicht, dass alle Datensätze angekommen sind.

<figure><img src="../../../.gitbook/assets/dbdc-1136-supplier-de-20261112.png" alt="Deutsche DocBits-Ansicht Stammdaten mit dem Reiter Lieferant, den Suchfeldern Suche nach Spalten und Suche Zeichenfolge sowie zehn erfundenen Lieferzeilen von SUP-1001 bis SUP-1010."><figcaption><p>Lieferantenansicht in der Sandbox-Version 11.27.7 mit erfundenen Beispieldaten. Suchen Sie eine bekannte Testkennung und vergleichen Sie sie mit M3 und ION.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/dbdc-1136-purchase-order-de-20261112.png" alt="Deutsche DocBits-Ansicht Bestellung mit den offenen Reitern Lieferant und Bestellung, denselben Suchfeldern und zehn erfundenen Bestellzeilen von PO-4500 bis PO-4509."><figcaption><p>Bestellansicht in der Sandbox-Version 11.27.7 mit erfundenen Beispieldaten. Die Zeilen belegen keinen M3-Import.</p></figcaption></figure>

Die Bilder in diesem Abschnitt stammen aus der ausgelieferten Sandbox-Oberfläche (Version 11.27.7) mit erfundenen Beispieldaten. Es wurde kein M3-Job gestartet, keine Datei importiert und kein Stammdatum geändert; die Bilder zeigen, wo Sie prüfen, nicht einen abgeschlossenen Transfer. Fehlt ein erwarteter Datensatz, prüfen Sie den EVS006-Verlauf, das ION-Routing, das BOD-Mapping und die DocBits-Organisation, bevor Sie erneut starten.
