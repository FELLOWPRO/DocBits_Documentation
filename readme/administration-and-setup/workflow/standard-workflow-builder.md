# Standard Workflow

**Standard Workflow** alat za izradu je linearni editor zasnovan na karticama za automatizaciju obrade dokumenata. Radni tok se sastoji od tri grupe kartica — **When** (okidač), **And** (dodatni uslovi) i **Then** (akcije koje se izvršavaju). Kada dokument ispuni When/And uslove, Then akcije se izvršavaju automatski.

## Kako pristupiti

Otvorite **Workflow Dashboard → Workflow List**, zatim kliknite na **Add Workflow** da kreirate novi Standard radni tok, ili kliknite na postojeći radni tok da ga izmenite.

<figure><img src="../../.gitbook/assets/workflow_list.png" alt="Workflow List sa tipom, redosledom izvršavanja i okidačem"><figcaption><p>Workflow List — svaki red je radni tok koji možete otvoriti, uključiti/isključiti ili izmeniti.</p></figcaption></figure>

## When / And / Then model

<figure><img src="../../.gitbook/assets/workflow_designer_cards.png" alt="Standard Workflow platno sa When, And i Then karticama"><figcaption><p>Standard Workflow platno. Ovaj primer se pokreće na fakturama u pod-organizaciji i dodeljuje ih korisniku.</p></figcaption></figure>

- **When** — okidač koji pokreće radni tok (npr. *Document type is Invoice*).
- **And** — dodatni uslovi koji takođe moraju biti ispunjeni (npr. *Document is part of sub-organization*). Ostavite prazno da bi se izvršavao na svakom poklapanju When kartice.
- **Then** — akcije koje treba izvršiti (npr. *Assign the document to the user*, kreiranje zadatka, poziv API-ja, slanje e-pošte).

## Dodavanje kartica

Kliknite na **Add Card** u bilo kojoj grupi da otvorite biblioteku kartica. Kartice su organizovane po kategorijama tako da lako pronađete građevni blok koji vam je potreban:

<figure><img src="../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card biblioteka grupisana po kategorijama"><figcaption><p><strong>Add Card</strong> biblioteka — kartice uslova, kartice poređenja, kartice akcija i još mnogo toga, grupisane po kategorijama.</p></figcaption></figure>

Sačuvajte pomoću **Save Workflow**, ili sačuvajte raspored kao šablon za ponovnu upotrebu pomoću **Save Template**.

## Sledeći koraci

- Pogledajte šta svaka kartica radi u odeljku **Cards**.
- Kombinujte kartice u proverena rešenja pomoću **Workflow Pattern Guides**.
- Za tokove sa grananjem i paralelnim putanjama (Wait ALL / Wait ANY / OR), koristite **Advanced Workflow** alat za izradu.
