# Smart Search Ranking

Smart Search Ranking mette i documenti che intendi in cima a una ricerca nella dashboard. Una ricerca per parola chiave trova ogni documento che contiene la tua parola; Smart Search Ranking aggiunge un passo: un'IA legge i risultati migliori e mette per primi i documenti che parlano davvero della tua ricerca. Le corrispondenze esatte — numeri di fattura, numeri d'ordine, nomi dei fornitori — restano sempre in cima.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/features/smart-search-ranking/preview/it.mp4" %}
Smart Search Ranking nella dashboard (narrazione in italiano). [Player con sottotitoli](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/features/smart-search-ranking/preview/it.html) · [Trascrizione](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/features/smart-search-ranking/preview/it.txt)
{% endembed %}

## Cosa cambia

| | Ordine per parola chiave | Con Smart Search Ranking |
| --- | --- | --- |
| Quali documenti vengono trovati | Gli stessi | Gli stessi |
| Ordine dei risultati | Per corrispondenza della parola chiave | Prima i documenti che parlano della tua ricerca |
| Corrispondenze esatte (numero fattura, numero ordine, fornitore) | Prime | Prime |
| Ordinamento per colonna, ricerche `ocr:` e per campo | Invariati | Invariati — mantengono il proprio ordine |

## Esempio

Otto fatture di prova contengono la parola *vite*: viti in acciaio inox, un set di cacciaviti, la manutenzione di un compressore a vite, bottiglie con tappo a vite, una pianta di vite, raccoglitori a vite, frenafiletti e una valigetta assortimento di viti.

* Cerca **vite**. Nell'ordine per parola chiave il set di cacciaviti è il primo risultato e la fattura delle viti è quinta. Con Smart Search Ranking le viti passano in cima — prima l'assortimento, poi le viti inox — e il set di cacciaviti scende al quarto posto.
* Cerca **cacciavite**. Nell'ordine per parola chiave il set di cacciaviti è primo. Con Smart Search Ranking i cacciaviti professionali salgono al primo posto e il set resta subito dietro, perché questa volta sono proprio cacciaviti; cocktail e giocattolo scendono.

## Dove si applica

* Nella [Ricerca rapida](quick-search.md) della dashboard con testo semplice (non nei chip di campo `campo:`).
* Viene riordinata la parte alta dell'elenco dei risultati; più in basso, gli elenchi lunghi mantengono l'ordine per parola chiave.
* Se il servizio di ordinamento non risponde entro il suo tempo, la ricerca mostra il normale ordine per parola chiave. Nulla viene nascosto, nessun risultato viene rimosso.

## Come si attiva

Smart Search Ranking viene attivato da DocBits per ogni organizzazione. Chiedi al tuo referente DocBits di attivarlo. Vale per tutti gli utenti dell'organizzazione entro un minuto, senza cambiare il modo in cui cerchi.
