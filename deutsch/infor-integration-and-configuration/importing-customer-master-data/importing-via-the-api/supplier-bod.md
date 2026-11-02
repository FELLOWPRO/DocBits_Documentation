---
description: Wie Sie einen Supplier BOD manuell über die API in DocBits importieren
---

# Lieferanten importieren (Supplier BOD)

Lieferantenstammdaten erreichen DocBits normalerweise automatisch über Ihren ION-Datenfluss. Diese Seite beschreibt, wie Sie einen **Supplier BOD** manuell senden — nützlich, wenn Sie einen Lieferanten erneut importieren, einen Stapel nachladen möchten, der nie angekommen ist, oder eine Feldzuordnung testen wollen, bevor Sie den automatischen Datenfluss einschalten.

## Zwei Wege, denselben BOD zu senden

Es gibt zwei Endpunkte, und sie tun dasselbe. Der einzige Unterschied liegt darin, wie Sie den BOD übergeben:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-supplier-endpoints.png)

| Endpunkt | Wann Sie ihn verwenden |
| --- | --- |
| `/import/supplier_bod` | Sie haben den BOD als **XML-Datei** und möchten sie hochladen. |
| `/import/supplier_bod_xml` | Sie möchten den **XML-Inhalt** im Request senden statt einer Datei. Der BOD muss in JSON verpackt werden, daher eignet sich das für kurzes XML oder für ein anderes System, das die API aufruft — für einen vollständigen BOD von Hand laden Sie besser die Datei hoch. |

Beide werden unten beschrieben. Die Schritte 1 und 2 sind in beiden Fällen gleich.

## Bevor Sie beginnen

Sie benötigen:

* **Einen API Key.** Siehe [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md), falls Sie noch keinen haben.
* **Den BOD** — eine `SyncSupplierPartyMaster`- oder `SyncRemitToPartyMaster`-XML-Datei oder deren Inhalt.
* **Ihre Org ID**, aus **Settings → Integration & SSO** im Abschnitt **ID**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

{% hint style="info" %}
**Sub Org ID** zeigt diejenige Unterorganisation, die in der Kopfzeile ausgewählt ist. Mit **CROSS** — der Ansicht über alle Unterorganisationen hinweg — zeigt sie denselben Wert wie **Org ID**. Wechseln Sie zuerst zu einer bestimmten Unterorganisation, wenn Sie deren ID benötigen.

Wenn Sie nicht in eine bestimmte Unterorganisation importieren, lassen Sie das Feld `sub_org_id` leer.
{% endhint %}

## Schritt-für-Schritt-Anleitung

### 1. Den API-Link öffnen

Öffnen Sie die API-Testoberfläche für die Umgebung und Region, mit der Sie arbeiten:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/import/import_supplier_bod_import_supplier_bod_post)
* [Sandbox API (Vereinigte Staaten)](https://us.sandbox.api.docbits.com/docs#/import/import_supplier_bod_import_supplier_bod_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/import/import_supplier_bod_import_supplier_bod_post)
* [Production API (Vereinigte Staaten)](https://us.api.docbits.com/docs#/import/import_supplier_bod_import_supplier_bod_post)

Klappen Sie den gewünschten Endpunkt durch Anklicken auf.

{% hint style="info" %}
Verwenden Sie die Region, in der Ihre Organisation gehostet wird — dieselbe Region, über die Sie sich bei DocBits anmelden. Die europäische und die amerikanische Umgebung sind getrennt, ein Import in die falsche Region taucht in Ihrer Organisation also nicht auf.

Die Adressen ohne Regionspräfix — `api.docbits.com` und `sandbox.api.docbits.com` — zeigen nach Europa. Sie begegnen Ihnen in älterer Dokumentation und in bestehenden Konfigurationen; es ist dieselbe Umgebung wie die `eu.`-Adressen oben.
{% endhint %}

### 2. Autorisieren

Alles unter **import** ist gesperrt, bis Sie autorisieren. Zwei Dinge sind einzutragen: Ihre Organisation und Ihr API Key.

* Klicken Sie auf das **Schlosssymbol** rechts neben dem Endpunkt.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-supplier-lock.png)

* Der Dialog **Available authorizations** öffnet sich mit zwei Einträgen.
* Fügen Sie Ihre **Org ID** in **X-ORG-ID** ein und klicken Sie auf **Authorize**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid-done.png)

* Scrollen Sie zu **X-API-KEY**, fügen Sie Ihren API Key ein und klicken Sie auf **Authorize**. In DocBits finden Sie ihn unter **Settings → Integration & SSO** im Abschnitt **API Key**, oder Sie [erstellen einen neuen Key](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md#einen-api-key-erstellen).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey-done.png)

* Klicken Sie auf **Close**.

{% hint style="info" %}
Fügen Sie den Key für sich allein ein — schreiben Sie kein `Bearer` davor. Beide Autorisierungen bleiben gesetzt, bis Sie die Seite neu laden oder auf **Logout** klicken.
{% endhint %}

### 3. Die Felder ausfüllen

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout.png)

Klicken Sie auf **Try it out** und füllen Sie dann das Formular für den gewählten Endpunkt aus.

#### Eine Datei hochladen — `/import/supplier_bod`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-supplier-bod-form.png)

| Feld | |
| --- | --- |
| **file** | Erforderlich. Klicken Sie auf **Choose file** und wählen Sie Ihre Supplier-BOD-XML-Datei aus. |
| **org\_id** | Ihre Org ID — derselbe Wert, den Sie in Schritt 2 in **X-ORG-ID** eingetragen haben. Ihn auch hier zu setzen macht den Request eindeutig darüber, in welche Organisation er schreibt. Es muss eine Organisation sein, auf die Ihr API Key Zugriff hat; alles andere wird abgelehnt. |
| **sub\_org\_id** | Nur nötig, wenn Sie in eine bestimmte Unterorganisation importieren. |
| **custom\_fields\_mapping** | Optional. Liest zusätzliche Felder aus dem BOD in die benutzerdefinierten Felder des Lieferanten. Siehe [Benutzerdefinierte Feldzuordnungen](#benutzerdefinierte-feldzuordnungen) unten. |

Ein Feld für Zeilenzuordnungen gibt es hier nicht — Lieferantenstammdaten haben keine Zeilen.

{% hint style="warning" %}
**`string` ist ein Wert, kein Platzhalter.** Swagger füllt die optionalen Felder mit dem Wort `string`, und es wird unverändert gesendet, wenn Sie es stehen lassen — ein Import mit `org_id` auf `string` schlägt fehl.

Leeren Sie jedes optionale Feld, das Sie nicht verwenden möchten. Das Leeren aktiviert das Kontrollkästchen **Send empty value** darunter, das Sie dann anhaken können.
{% endhint %}

#### Benutzerdefinierte Feldzuordnungen

Das Zuordnungsfeld erwartet ein JSON-Objekt. Der **Name auf der linken Seite muss eines von DocBits' eigenen benutzerdefinierten Feldern sein** — `custom_field_1` bis `custom_field_5` für Lieferanten. Jeder andere Name wird ohne Warnung ignoriert, ein Tippfehler hier sieht also genauso aus wie eine Zuordnung, die nicht funktioniert hat.

Der Wert auf der rechten Seite ist der XPath, aus dem gelesen wird. Schreiben Sie ihn ohne Namensraum-Präfixe — DocBits ergänzt diese selbst:

```json
{"custom_field_2": "//SupplierPartyMaster/UserArea/Property/NameValue[@name='User defined 6']/text()"}
```

#### Das XML einfügen — `/import/supplier_bod_xml`

Dieser Endpunkt nimmt den BOD nicht als einfaches Einfügen entgegen. Das Feld **xml** ist ein Objekt, vorbelegt mit `{"xml": "string"}`. Ersetzen Sie `string` durch den Inhalt Ihres BOD und behalten Sie die umgebenden Anführungszeichen und Klammern bei:

```json
{
  "xml": "<SyncSupplierPartyMaster ...>...</SyncSupplierPartyMaster>"
}
```

{% hint style="warning" %}
Der BOD steht innerhalb eines JSON-Strings, jedes doppelte Anführungszeichen im XML muss also als `\"` maskiert werden — und ein BOD ist voll davon. Ist das Ergebnis kein gültiges JSON, schlägt der Request mit einem **422** fehl und es wird nichts importiert.

Für einen echten BOD ist das von Hand mühsam, bevorzugen Sie deshalb das **Hochladen der Datei**.
{% endhint %}

Die Felder `org_id`, `sub_org_id` und `custom_fields_mapping` funktionieren genau wie oben.

{% hint style="warning" %}
Prüfen Sie vor dem Ausführen, auf welche Umgebung und welche Organisation Sie zeigen. Ein Import schreibt direkt in die Stammdaten dieser Organisation.
{% endhint %}

### 4. Ausführen

Prüfen Sie vor dem Ausführen das Dropdown **Servers** unten im Formular. Es entscheidet, an welche Umgebung der Request tatsächlich gesendet wird, und kann von der geöffneten Seite abweichen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-execute.png)

Klicken Sie auf **Execute**. Ein erfolgreicher Import liefert:

```json
{
  "success": true,
  "message": "BOD processed successfully."
}
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-supplier-response.png)

Supplier BODs werden verarbeitet, während Sie warten — wenn Sie diese Meldung sehen, sind die Daten also bereits da.

Wenn am Request etwas nicht stimmte, erhalten Sie `"success": false` zusammen mit einer Meldung, die das Problem beschreibt. Die häufigsten Ursachen sind Inhalte, die kein Supplier BOD sind, und eine Org ID, auf die Ihr API Key keinen Zugriff hat.

### 5. Prüfen, ob die Daten angekommen sind

* Gehen Sie in DocBits zu **Settings → Document Processing → Lookup Master Data**.
* Wählen Sie links **BOD Input Data** und öffnen Sie dann den Tab **Supplier**.
* Suchen Sie nach dem Lieferanten aus Ihrem BOD.

<!-- SCREENSHOT: Lookup Master Data with BOD Input Data selected and the Supplier tab open -->

{% hint style="info" %}
DocBits entscheidet anhand des Typs *innerhalb* des BOD, was damit geschieht — nicht anhand des verwendeten Import-Endpunkts. Wenn Sie hier versehentlich einen Purchase Order BOD senden, wird er als Bestellung importiert statt abgelehnt — prüfen Sie also, ob der Tab, in dem Sie die Daten finden, der erwartete ist.
{% endhint %}
