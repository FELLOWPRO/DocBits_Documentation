# Settings Assistant

The **Settings Assistant** is a chat panel inside the Settings area. You ask a question in plain language, and it reads the configuration of your organisation, answers, and takes you straight to the right setting. It can also warn you when something in your setup has stopped working, and, with your confirmation, change a setting for you.

It helps most when you know **what** you want ("stop splitting documents on barcodes") but not **where** the setting lives, or when you wonder **why** something does not happen ("Why isn't PO matching active?").

<figure><img src="../../../../.gitbook/assets/settings-assistant-panel-open.png" alt="The Settings Assistant panel on the right side of the Settings area, with a finding card, a greeting and three example questions"><figcaption><p>The Settings Assistant on the Company Information page: a finding at the top, a greeting for the current page, three example questions and the question field.</p></figcaption></figure>

The assistant is **off by default**. This page shows where to turn it on and how to open it. What you can ask it, and what it can change, is described on the page [Settings Assistant: What the Chat Can Do](settings-assistant-chat.md).

## Who can use it

* The **organisation administrator** switches the assistant on or off for the whole organisation.
* Once it is on, every administrator who can open **Settings** can show or hide the panel for themselves.
* Changes (applying a recommendation, switching off or deleting an import connection, creating a rule) are limited to **organisation administrators**. Other users get the message *Available to administrators only.*

## Turn it on

1. Go to **Settings → Global Settings → Company Information**. The page header shows **Company Settings**.
2. Open the **Assistants** section.
3. Turn on **Enable the settings assistant**.

<figure><img src="../../../../.gitbook/assets/settings-assistant-org-switch.png" alt="The Assistants section in Company Information with the switches for the settings assistant, the validation assistant and the explainer voice-over"><figcaption><p>The Assistants section. The settings assistant has its own switch. The validation assistant and the explainer voice-over are separate features.</p></figcaption></figure>

A short message confirms **Settings assistant enabled**. The setting is off by default. While it is off, the panel and its button do not appear anywhere.

{% hint style="warning" %}
The **Validation assistant** in the same section is a different feature. It explains blocking fields inside a document and cannot change any setting. Switching one of the two does not affect the other.
{% endhint %}

## Open and close the panel

On every page of the Settings area you find a small **genie-lamp button** next to the settings search field. Click it to **show** or **hide** the assistant.

* The panel remembers your choice per user, so it stays open the next time you come back.
* On a wide screen (1280 pixels and more) it sits next to the page. You can drag its edge to change the width.
* On a narrow screen it opens as an overlay. **Esc** or a click outside closes it.
* **New chat** (the speech-bubble icon in the header) clears the conversation. The conversation also survives a page reload, but not a closed browser tab.

## What to do next

* Ask your first question: see [Settings Assistant: What the Chat Can Do](settings-assistant-chat.md).
* The assistant runs on the **Fast** AI tier. There is no organisation setting to choose a different model.

## Troubleshooting

| Problem | Cause and solution |
| --- | --- |
| There is no genie-lamp button in the Settings area | The organisation switch is off. An organisation administrator turns it on under **Company Information → Assistants** |
| The section **Assistants** is missing in Company Information | Only organisation administrators see it |
| The panel says **The assistant is being set up** | The feature is not yet available in your environment |
| The panel is there, but answers say *Available to administrators only.* | Your account is not an organisation administrator |

## Related pages

* [Settings Assistant: What the Chat Can Do](settings-assistant-chat.md)
* [Company Preferences](company-preferences.md)
