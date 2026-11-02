---
description: Wie Sie Stammdaten aus einer XML-Datei in einen Lookup-Datensatz importieren
---

# Stammdaten aus XML importieren

Neben den BOD-Importen kann DocBits Stammdaten aus **jeder beliebigen XML-Datei** in einen Lookup-Datensatz Ihrer Wahl einlesen. Sie geben an, in welchen Datensatz geschrieben werden soll und aus welchem XPath jede Spalte zu lesen ist — das XML muss also überhaupt keinem BOD-Format folgen.

Verwenden Sie das für Stammdaten, die nicht als BOD ankommen — Preislisten, Kostenstellen, Artikelattribute, alles, was Ihr ERP als XML exportieren kann.

## Zwei Wege, das XML zu senden

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-endpoints.png)

| Endpunkt | Wann Sie ihn verwenden |
| --- | --- |
| `/master_data_lookup/xml/import_xml_file` | Sie haben die Daten als **XML-Datei** und möchten sie hochladen. |
| `/master_data_lookup/xml/import_xml_data` | Sie möchten das **XML in den Request einfügen**. Anders als die BOD-Endpunkte nimmt dieser das XML als reinen Text entgegen — ohne JSON-Verpackung. |

Beide werden unten beschrieben. Die Schritte 1 und 2 sind in beiden Fällen gleich.

## Bevor Sie beginnen

Sie benötigen:

* **Einen API Key.** Siehe [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md), falls Sie noch keinen haben.
* **Das XML** — als Datei oder als Inhalt, den Sie einfügen können.
* **Einen Datentyp** — den Namen des Lookup-Datensatzes, in den geschrieben werden soll.
* **Feldzuordnungen** — welcher XPath welche Spalte füllt.
* **Ihre Org ID**, aus **Settings → Integration & SSO** im Abschnitt **ID**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

## Schritt-für-Schritt-Anleitung

### 1. Den API-Link öffnen

Öffnen Sie die API-Testoberfläche für die Umgebung und Region, mit der Sie arbeiten:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Sandbox API (Vereinigte Staaten)](https://us.sandbox.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Production API (Vereinigte Staaten)](https://us.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)

Diese Endpunkte stehen unter **master data lookup** statt unter **import**, weiter unten auf der Seite.

{% hint style="info" %}
Verwenden Sie die Region, in der Ihre Organisation gehostet wird — dieselbe Region, über die Sie sich bei DocBits anmelden. Die europäische und die amerikanische Umgebung sind getrennt, ein Import in die falsche Region taucht in Ihrer Organisation also nicht auf.
{% endhint %}

### 2. Autorisieren

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-lock.png)

Das Autorisieren funktioniert genau wie bei den BOD-Importen: Klicken Sie auf das **Schlosssymbol**, fügen Sie Ihre **Org ID** in **X-ORG-ID** ein, fügen Sie Ihren API Key in **X-API-KEY** ein und klicken Sie jeweils auf **Authorize**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

### 3. Die Felder ausfüllen

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-xml.png)

Klicken Sie auf **Try it out** und füllen Sie dann das Formular aus.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-form.png)

| Feld | |
| --- | --- |
| **data\_type** | Erforderlich. Der Lookup-Datensatz, in den geschrieben werden soll. Er wird automatisch in Kleinbuchstaben umgewandelt, `PriceList` und `pricelist` sind also derselbe Datensatz. |
| **field\_mappings** | Erforderlich. Ein JSON-Objekt, das jede Spalte mit dem XPath verbindet, aus dem sie gelesen wird. Siehe unten. |
| **file** | Erforderlich bei `import_xml_file`. Klicken Sie auf **Choose file** und wählen Sie Ihr XML aus. |
| **xml** | Erforderlich bei `import_xml_data` anstelle der Datei — fügen Sie das XML als reinen Text ein. |
| **org\_id** | Ihre Org ID — derselbe Wert, den Sie in Schritt 2 in **X-ORG-ID** eingetragen haben. |
| **sub\_org\_id** | Nur nötig, wenn Sie in eine bestimmte Unterorganisation importieren. |

#### Feldzuordnungen

`field_mappings` ist ein JSON-Objekt mit einem Eintrag je Spalte. Anders als bei den BOD-Importen, wo die Namen auf `custom_field_1` … `custom_field_5` festgelegt sind, wählen Sie sie hier selbst:

```json
{
  "ID": "//Item/ID",
  "Description": "//Item/Description",
  "Price": "//Item/UnitPrice"
}
```

Die Namen auf der linken Seite werden zu den Spalten des Datensatzes und sind frei wählbar. Die Werte auf der rechten Seite müssen zur Struktur des XML passen, das Sie hochladen — im Beispiel oben greift `//Item/ID` das Element `<ID>` innerhalb jedes `<Item>` ab. Beide Seiten sind unabhängig voneinander: die Zuordnung oben liest `<UnitPrice>` in eine Spalte namens `Price`.

{% hint style="warning" %}
Nur **fehlerhafte** XPaths werden abgelehnt, mit einem `400`, der das Feld benennt. Ein XPath, der gültig ist, aber in Ihrem XML nichts findet, geht stillschweigend durch und lässt diese Spalte einfach leer — ein Tippfehler in einem Pfad sieht deshalb aus wie ein Import, der funktioniert hat, dabei aber eine Spalte verloren hat. Ist es der `ID`-Pfad, der nichts findet, schlägt der Import stattdessen fehl und meldet, dass die Spalte `ID` für diesen Datensatz fehlt.
{% endhint %}

{% hint style="warning" %}
**Eine der Spalten muss `ID` heißen.** Sie identifiziert einen Datensatz: Importieren Sie dieselben Daten erneut, wird die Zeile mit dieser ID aktualisiert statt eine doppelte angelegt. Die Groß- und Kleinschreibung spielt keine Rolle, `ID`, `Id` und `id` funktionieren also alle, aber ein Name wie `ItemID` zählt nicht — der Request wird mit `ID_FIELD_IS_MISSING` abgelehnt und nichts wird geschrieben.
{% endhint %}

{% hint style="warning" %}
**Ein Request importiert einen Datensatz.** Jeder XPath wird einmal gelesen, wenn Ihr XML also mehrere Elemente enthält, wird nur der jeweils erste Treffer verwendet. Um eine Liste zu laden, senden Sie einen Request je Datensatz oder verwenden stattdessen einen CSV-Import.
{% endhint %}

#### Einen Datentyp wählen

`data_type` ist der Schlüssel des Datensatzes, in den Sie schreiben. Er wird in Kleinbuchstaben umgewandelt und getrimmt, `Items` und `items` sind also derselbe Datensatz. Jeder noch nicht vergebene Name legt einen eigenen Datensatz an — `items_example`, `cost_centres`, `price_list` — und ein erneuter Import dorthin aktualisiert ihn.

{% hint style="danger" %}
Manche Namen sind nicht frei: Es sind DocBits' eigene Stammdatentabellen, und ein Import in eine davon schreibt direkt hinein.

| Name | |
| --- | --- |
| `purchase_order_header`, `purchase_order_address` | Werden mit `RESERVED_DATASET_NAME` abgelehnt. |
| `supplier`, `supplier_accounts`, `purchase_order`, `receive_delivery`, `receive_delivery_lines`, `costing_element`, `customer_erp_items`, `supplier_item_price`, `supplier_item_number_mapping` | **Werden angenommen und überschreiben echte Stammdaten.** Verwenden Sie diese nur, wenn Sie genau das beabsichtigen. |

Für alles andere wählen Sie einen eigenen Namen.
{% endhint %}

{% hint style="warning" %}
Prüfen Sie vor dem Ausführen, auf welche Umgebung und welche Organisation Sie zeigen. Ein Import schreibt direkt in die Stammdaten dieser Organisation.
{% endhint %}

### 4. Ausführen

Prüfen Sie vor dem Ausführen das Dropdown **Servers** unten im Formular.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-execute.png)

Klicken Sie auf **Execute**. Ein erfolgreicher Import liefert:

```json
{
  "success": true,
  "message": "Record(s) created/updated successfully"
}
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-response.png)

Anders als die BOD-Importe melden diese Endpunkte Probleme mit einem echten Fehlerstatus statt mit einem `200`, das `"success": false` trägt — ein **400** bedeutet, dass der Request abgelehnt wurde und nichts geschrieben worden ist.

### 5. Prüfen, ob die Daten angekommen sind

* Gehen Sie in DocBits zu **Settings → Document Processing → Lookup Master Data**.
* Wählen Sie links **Imported** und öffnen Sie dann den Tab für Ihren Datentyp.
* Die Spalten sind die Namen, die Sie auf der linken Seite von `field_mappings` verwendet haben.

<!-- SCREENSHOT: Lookup Master Data with Imported selected and the new dataset open -->
