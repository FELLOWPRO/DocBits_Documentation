---
description: >-
  Wie Sie die API Keys finden und erstellen, mit denen andere Systeme Zugriff auf
  DocBits erhalten
---

# API Key Management

Ein API Key erlaubt es einem anderen System — Ihrem ERP, einem Skript oder einer Partneranwendung — mit DocBits zu sprechen, ohne dass sich ein Benutzer anmeldet. Ihre Organisation kann so viele Keys halten, wie Sie benötigen, und jeder wird für sich verwaltet: Geben Sie ihm einen eigenen Namen, entscheiden Sie, ob er abläuft, und widerrufen Sie ihn einzeln, falls er jemals offengelegt wird.

Weil jede Integration ihren eigenen Key haben kann, können Sie einen abschalten, ohne einen der anderen zu stören.

## Die API-Key-Verwaltung öffnen

Gehen Sie zu **Settings** und wählen Sie **Integration & SSO** unter **System & Administration**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-settings-overview.png)

Der Abschnitt **API Key** oben auf der Seite listet jeden Key auf, den Ihre Organisation besitzt.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-list.png)

## Die Liste verstehen

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-list-row.png)

| Spalte | Was sie Ihnen sagt |
| --- | --- |
| **Key** | Die ersten Zeichen des Keys, gefolgt von `****`. Der Rest wird nach dem Erstellen nie wieder angezeigt — siehe [Einen API Key erstellen](#einen-api-key-erstellen). |
| **Name** | Der Name, den Sie dem Key gegeben haben, mit seiner Beschreibung darunter. |
| **Expires** | Das Datum, an dem der Key aufhört zu funktionieren, oder **Never**, wenn Sie keines gesetzt haben. |
| **Last Used** | Wann zuletzt eine Anfrage mit diesem Key eingegangen ist. **Never used** bedeutet, dass ihn noch kein System verwendet hat — nützlich, um Keys zu erkennen, die Sie gefahrlos entfernen können. |
| **Status** | **Active** bedeutet, dass der Key funktioniert. Ein widerrufener Key ist dauerhaft abgeschaltet. |
| **Actions** | Das Drei-Punkte-Menü, über das Sie den Key widerrufen können. |

Wenn Sie mehr Keys haben, als auf eine Seite passen, verwenden Sie die Blätterelemente unten in der Liste.

{% hint style="info" %}
**Last Used** ist der schnellste Weg, Keys zu finden, die niemand mehr braucht. Ein Key, der nie verwendet wurde oder seit Monaten nicht mehr, ist ein guter Kandidat zum Widerrufen.
{% endhint %}

## Einen API Key erstellen

1. Klicken Sie oben rechts im Abschnitt API Keys auf **+ Create API Key**.
2. Füllen Sie den Dialog aus:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-create-dialog.png)

| Feld | Was Sie eintragen |
| --- | --- |
| **Key Name** | Erforderlich. Benennen Sie ihn nach dem System, das ihn verwenden wird — `M3 Production`, `Invoice Import Script` — damit Sie später erkennen, zu welcher Integration ein Key gehört. |
| **Description** | Optional. Platz für eine Notiz, wofür der Key da ist oder wer ihn eingerichtet hat. |
| **Expiration** | Wählen Sie ein Ablaufdatum oder belassen Sie es auf **Never expires**. Ein Ablaufdatum ist die sicherere Wahl: Der Key verabschiedet sich von selbst, falls die Integration einmal vergessen wird. |

3. Klicken Sie auf **Create**. DocBits zeigt Ihnen den neuen Key:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-created.png)

4. Kopieren Sie den Key über das Kopiersymbol und fügen Sie ihn direkt in das System ein, das ihn verwenden wird, oder in Ihren Passwortmanager.
5. Haken Sie **I have copied and saved this key** an und klicken Sie auf **Done**.

{% hint style="danger" %}
**Der vollständige Key wird nur ein einziges Mal angezeigt.** DocBits speichert ihn in einer verschlüsselten Form, die sich nicht in das Original zurückverwandeln lässt — niemand kann ihn danach noch nachschlagen, weder Ihre Administratoren noch der DocBits-Support. Wenn Sie ihn verlieren, widerrufen Sie den Key und erstellen einen neuen.
{% endhint %}

Behandeln Sie den Key wie ein Passwort. Wer ihn hat, kann mit den Dokumenten und Daten Ihrer Organisation arbeiten.
