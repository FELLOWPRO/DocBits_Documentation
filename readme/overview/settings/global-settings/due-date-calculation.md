# Obračun roka dospeća

<figure><img src="../../../.gitbook/assets/due_date_calc_overview.png" alt="Podešavanja obračuna roka dospeća"><figcaption><p>Podešavanja obračuna roka dospeća</p></figcaption></figure>

Stranica **Obračun roka dospeća** (**Obrada dokumenata → Obračun roka dospeća**) kontroliše kako DocBits obračunava rokove dospeća faktura, rokove dospeća popusta (Skonto) i uslove plaćanja na osnovu kodova uslova plaćanja pronađenih na fakturama.

## Prikaži obračunata polja

Omogućite **Prikaži obračunata polja** da bi se automatski obračunata polja fakture — rok dospeća, rok dospeća popusta, uslovi plaćanja i AP kod dodele — pojavila u Podešavanjima polja i kao promenljive u Brzoj pretrazi i šablonima e-pošte. Prilagođeni tipovi dokumenata nikada nisu obuhvaćeni.

## Obračun roka dospeća fakture

### Postupanje s vikendima

<figure><img src="../../../.gitbook/assets/due_date_calc_weekend_options.png" alt="Opcije konvencije za vikend"><figcaption><p>Opcije konvencije za vikend</p></figcaption></figure>

Izaberite kako se prilagođava rok dospeća koji pada u subotu ili nedelju. Ovo se odnosi **i** na rok dospeća fakture **i** na rok dospeća popusta (Skonto).

| Konvencija | Efekat |
|------------|--------|
| **Nijedna** | Zadrži kalendarski datum (bez prilagođavanja). |
| **Sledeća** | Pomeri sub./ned. na sledeći ponedeljak. |
| **Prethodna** | Pomeri sub./ned. na prethodni petak. |
| **Najbliža** | Subota → petak, nedelja → ponedeljak. |
| **Izmenjena sledeća** | Sledeći ponedeljak, osim ako pređe u sledeći mesec; tada prethodni petak. |

### AP kod dodele

Povežite uslove plaćanja dobavljača sa AP kodovima dodele za automatsko usmeravanje faktura tako što ćete izabrati **polje AP koda dodele**.

## Zamene uslova popusta

<figure><img src="../../../.gitbook/assets/due_date_calc_mappings.png" alt="Zamene uslova popusta"><figcaption><p>Zamene uslova popusta</p></figcaption></figure>

Koristite **Zamene uslova popusta** da biste povezali određeni prefiks sa procentom popusta i brojem dana. Kliknite na **+ Dodaj mapiranje** da biste dodali red sa poljima **Prefiks**, **Procenat** i **Dani**.

## Podržani formati

<figure><img src="../../../.gitbook/assets/due_date_calc_formats.png" alt="Podržani formati uslova plaćanja i popusta"><figcaption><p>Podržani formati uslova plaćanja i popusta</p></figcaption></figure>

DocBits prepoznaje sledeće kodove uslova plaćanja i popusta.

**Podržani formati uslova plaćanja**

| Format | Primer | Značenje |
|--------|--------|----------|
| Infor M3 | `N90`, `N30` | Neto 90 / 30 dana |
| Infor M3 | `NET` | Plativo po prijemu |
| Infor M3 | `M20` | 20. u sledećem mesecu |
| Infor M3 | `E15` | Kraj meseca + 15 dana |
| Infor LN | `030`, `30` | Neto 30 dana |
| Reversed | `14N`, `30N` | Neto 14 / 30 dana |
| Tekstualni kodovi | `REC`, `DUE`, `COD` | Plativo po prijemu |

**Format uslova popusta** — uslovi popusta kodiraju popuste za rano plaćanje kao trocifrene kodove: prva cifra je procenat popusta, poslednje dve su dani u okviru kojih treba platiti.

| Kod | Značenje |
|-----|----------|
| `210` | 2% popusta ako se plati u roku od 10 dana |
| `130` | 1% popusta ako se plati u roku od 30 dana |
| `545` | 5% popusta ako se plati u roku od 45 dana |
| `0` | Bez popusta |
