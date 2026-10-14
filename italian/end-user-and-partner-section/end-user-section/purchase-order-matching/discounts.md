# Sconti

## **Panoramica**

Se la tua tabella estratta contiene la colonna **Sconto** o **Percentuale di sconto**, **DocBits** applicherà automaticamente lo sconto corrispondente al Prezzo unitario durante l'elaborazione nella [**schermata di abbinamento degli ordini di acquisto**](./).

## Eccezioni

Gli sconti non verranno applicati automaticamente quando viene utilizzata la funzione di abbinamenti multipli. Maggiori informazioni sulla funzione di abbinamenti multipli possono essere trovate [qui](./#abbinamenti-multipli).

## Calcolo dello Sconto

Quando è presente uno **Sconto**, il prezzo unitario scontato viene calcolato sottraendo l'importo dello sconto dal prezzo unitario:

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE - DISCOUNT
```

## Calcolo della Percentuale di Sconto

Quando è presente una **Percentuale di sconto**, il prezzo unitario scontato viene calcolato utilizzando la seguente formula:

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE * (1 - DISCOUNT_PERCENT / 100)
```

## Arrotondamento

Tutti i risultati del prezzo unitario scontato sono arrotondati a quattro decimali per coerenza nell'elaborazione successiva.
