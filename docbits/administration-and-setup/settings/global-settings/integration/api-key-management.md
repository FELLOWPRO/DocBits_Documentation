---
description: >-
  How to find and create the API keys that give other systems access to DocBits
---

# API Key Management

An API key lets another system — your ERP, a script, or a partner application — talk to DocBits without a user logging in. Your organization can hold as many keys as you need, and each one is managed separately: give it its own name, decide whether it expires, and revoke it on its own if it is ever exposed.

Because each integration can have its own key, you can switch one off without disturbing any of the others.

## Opening API key management

Go to **Settings** and select **Integration & SSO** under **System & Administration**.

<figure><img src="../../../../.gitbook/assets/prior-t020-en.png" alt="Access to API-key management."><figcaption><p>Access to API-key management.</p></figcaption></figure>

The **API Key** section at the top of the page lists every key your organization has.

<figure><img src="../../../../.gitbook/assets/prior-t017-en.png" alt="API-key list with keys and associated names hidden."><figcaption><p>API-key list with keys and associated names hidden.</p></figcaption></figure>

## Understanding the list

<figure><img src="../../../../.gitbook/assets/s150-api-key-list-row.png" alt="API key list with keys and account details hidden."><figcaption><p>API key list with keys and account details hidden.</p></figcaption></figure>

| Column | What it tells you |
| --- | --- |
| **Key** | The first few characters of the key, followed by `****`. The rest is never shown again after you create it — see [Creating an API key](#creating-an-api-key). |
| **Name** | The name you gave the key, with its description underneath. |
| **Expires** | The date the key stops working, or **Never** if you did not set one. |
| **Last Used** | When a request last arrived with this key. **Never used** means no system has used it yet — useful for spotting keys you can safely remove. |
| **Status** | **Active** means the key works. A revoked key is switched off permanently. |
| **Actions** | The three-dot menu, where you can revoke the key. |

If you have more keys than fit on one page, use the paging controls at the bottom of the list.

{% hint style="info" %}
**Last Used** is the quickest way to find keys nobody needs any more. A key that has never been used, or has not been used in months, is a good candidate for revoking.
{% endhint %}

## Creating an API key

1. Click **+ Create API Key** at the top right of the API Keys section.
2. Fill in the dialog:

<figure><img src="../../../../.gitbook/assets/prior-t018-en.png" alt="Create API key dialog before saving."><figcaption><p>Create API key dialog before saving.</p></figcaption></figure>

| Field | What to enter |
| --- | --- |
| **Key Name** | Required. Name it after the system that will use it — `M3 Production`, `Invoice Import Script` — so you can tell later which integration a key belongs to. |
| **Description** | Optional. Room for a note about what the key is for or who set it up. |
| **Expiration** | Choose an expiry date, or leave it on **Never expires**. An expiry date is the safer choice: the key retires itself if the integration is ever forgotten. |

3. Click **Create**. DocBits shows you the new key:


4. Copy the key with the copy icon and paste it straight into the system that will use it, or into your password manager.
5. Tick **I have copied and saved this key** and click **Done**.

{% hint style="danger" %}
**The full key is shown only once.** DocBits stores a one-way hash of the key and a short identifying prefix. Neither your administrators nor DocBits support can retrieve the original full key from that hash. If you lose it, revoke the key and create a new one.
{% endhint %}

Treat the key like a password. Anyone who has it can act on your organization's documents and data.

For password hashing, TLS, vendor visibility, and the distinction between DocBits keys and credentials for connected systems, see [Secure Storage of Credentials](../../../../security/secure-storage-of-credentials.md).


The complete API key is shown only once after creation. Copy it into approved secure storage, confirm that it has been saved, and close the dialog. The key list shows its identifying information rather than revealing the complete secret again.
