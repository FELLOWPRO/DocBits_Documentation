# Web search

With web search the Knowledge Assistant can look up **public information on the internet** in addition to your own documents, for example the current address of a company or the current base interest rate. An administrator switches it on per organization. It is **off by default**.

{% hint style="warning" %}
Web search is a **best-effort** function. Results are links with a short text snippet from public websites. They are not verified and do not replace a lookup in an official register. Check every value on the page the result points to.
{% endhint %}

{% hint style="info" %}
The examples on this page are generic. We measured the behavior described here on our DocBits Local test installation on 28 November 2026. How reliably web search works with your questions and in your environment is not covered by this page.
{% endhint %}

## Switch on web search (administrator)

1. Open **Settings** → **Module** → **Document Integration**.
2. Open the card **Knowledge Assistant** and go to **Functions**.
3. Switch on **Web search**.

The setting applies to the whole organization. If web search is off, the assistant tells you that an administrator can switch it on under **Functions**.

The notice on the screen says: "The assistant may search the internet. Search queries leave DocBits." Only switch web search on if this is allowed in your company.

### Search without confirmation

Under **Functions** there is a second switch, **Web search without confirmation**. It needs web search to be on and is off by default.

* **Off (default):** before every search the assistant shows you the search text and asks for your confirmation (**Send** or **Don't send**). Nothing leaves DocBits until you confirm.
* **On:** a search text that comes from your question is sent without asking. According to the notice on the screen, search texts that the assistant formulated itself are still always confirmed.

## What a search looks like

1. You ask a question in **Chat** that needs public information, for example: "What is the registered address of this supplier?"
2. The assistant proposes a search text. Unless **Web search without confirmation** is on, you see the text with the question "This search text will be sent to the web search:" and choose **Send** or **Don't send**.
3. The assistant receives the results and answers with the sources it used. Web results are links to public pages.

The screen notes that web search runs in the mode Smart Reasoning and is off in Quick Answer. See [Choose the right agent](choose-the-right-agent.md).

## How the search works

By default, web search runs **through DocBits**. You do not need a key or an account with a search provider.

* The search goes through DocBits **without a key**. It is marked **Best effort**: with automated queries it can be blocked or inaccurate, and then a search returns no result or a poor one.
* A result consists of a **link and a short text snippet**, not the text of the page. Values such as an interest rate or an exchange rate are therefore not always part of the snippet. If a value is missing, the assistant says so; open the linked page and read the value there.
* The provider cannot be changed on screen. The use of your own search provider with your own key is planned, but it is **not yet available** in the interface.

## Data protection

* **No long numbers in the search text.** The assistant may not write longer number sequences, such as invoice numbers, account numbers or IBANs, into a search text. The search text is checked before it is sent. If it contains characters or numbers that are not sent for data protection reasons, the search is not sent and you see a message.
* **Search texts are not logged.**
* **Web results are unverified web content** with a source. The assistant names the source; you decide whether you trust it.

## Limits

* **At most 3 searches per question.** Rejected searches (**Don't send**) do not count toward the 3, up to 10 rejections.

## Typical uses

* **Check a supplier:** company name and address of a supplier whom you want to compare with the data on an invoice.
* **Current reference rates:** for example the current base interest rate when you check a default interest clause from your contract.

In both cases the web result is a **hint**. Compare it with the original source before you use it.

## Honest limits

* Web search is **not a register lookup**. For commercial register, tax number or VAT ID checks, use the official register.
* Web search gives **no legal advice** and makes no approval or payment decision.
* A search can return no result, an old result or a wrong one. Pages can block automated queries.
* The assistant does not read whole websites; it works with links and short snippets.

## Messages you may see

| Message | What it means | What to do |
| --- | --- | --- |
| Web search is not switched on for your organisation. An administrator can switch it on under Functions. | The switch is off. | Ask your administrator. |
| The search text contains characters or numbers that are not sent for data protection reasons. | The search text contained a long number sequence or other characters. | Ask without the number, for example only with the company name. |
| The web search was not sent because it was not confirmed. | You chose **Don't send** or did not confirm. | Ask again and confirm the search text. |
| Web search is not available right now. / The web search did not deliver a result. Please try again later. | The search service did not answer or returned nothing. This can happen with best-effort search. | Try again later or look the value up directly on the website. |
| Too many web searches in a short time. | The number of searches is limited. | Wait a moment. |
| Web search is not allowed for this account. | Your account may not use it. | Ask your administrator. |

See also: [Tasks and where to find them](tasks-and-where-to-find-them.md), [Choose the right agent](choose-the-right-agent.md) and [What it can and cannot do](what-it-can-and-cannot-do.md).
