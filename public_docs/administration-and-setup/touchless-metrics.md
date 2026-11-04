# Wskaźniki i obliczenia

### Poprawny odczyt i automatyzacja to różne rzeczy

**DocBits może poprawnie odczytać fakturę, choć rozbieżne dane Infor wymagają pracy.** AP oznacza pracowników zobowiązań, nie asystenta AI. Porównaj oryginał z odczytem sprzed korekt, a następnie z danymi importowanymi. Zielony etap i wysoka pewność nie dowodzą poprawności wszystkich wartości. Wartości po korekcie nie dowodzą początkowego odczytu.

## Co oznacza „touchless”

Każdy zakończony dokument kwalifikujący się do KPI ma jeden wynik:

| Kategoria | Znaczenie | Touchless? |
| --- | --- | --- |
| **Pure Touchless** | Sukces bez ludzkiej ingerencji i zatwierdzenia | Tak |
| **AP Touchless** | Sukces; potrzebne było tylko zatwierdzenie biznesowe | Tak |
| **AP Assisted**, ingerencja AP | Sukces po korekcie, ręcznej walidacji lub ponownym uruchomieniu przez człowieka | Nie |
| **Wyjątek procesu** | Ostateczny błąd, odrzucenie lub odrzucenie ERP sklasyfikowane jako wyjątek | Nie |

Dokumenty w toku i wyłączone nie wchodzą do mianownika. Końcowy wyjątek ma pierwszeństwo przed kategorią sukcesu. AP Assisted opisuje wykonaną pracę, nie jej przyczynę: odczyt mógł być poprawny.

```
rate = (Pure touchless + AP touchless)
       ÷ (Pure touchless + AP touchless + AP assisted + Process exception)
```

AP touchless we wzorze oznacza **tylko zatwierdzenie**. **Łączny wskaźnik AP** obejmuje Pure i zatwierdzenia. Pure i łączny AP nakładają się; nie dodawaj ich procentów. Kategorie wyników dostawcy są rozłączne.

### Przykład obliczeń: 200 dokumentów

| Wynik | Liczba |
| --- | --- |
| Pure | 120 |
| Tylko zatwierdzenie | 30 |
| AP Assisted | 30 |
| Wyjątki | 10 |
| W toku | 8 |
| Wyłączone | 2 |

Mianownik: **190**. Pure: 120 / 190 = **63,2 %**. Tylko zatwierdzenie: 30 / 190 = **15,8 %**. Łączny AP: (120 + 30) / 190 = **78,9 %**. Przy celu 70 % AP jest powyżej celu, a Pure poniżej. Porównuj właściwy wskaźnik.

### Odczyt poprawny w 100 %, AP Touchless 80 %

Załóżmy niezależną kontrolę oryginałów i wartości sprzed korekt: **100 zakończonych, kwalifikujących się faktur odczytano poprawnie**. 70 zakończyło się automatycznie (Pure), 10 wymagało tylko zatwierdzenia (AP Touchless), a 20 miało rozbieżne dane Infor. Po potwierdzeniu ceny poprawiono źródło, sprawdzono import i ręcznie ponownie uruchomiono DocBits; zakończenie było pomyślne (AP Assisted).

Jakość odczytu w tej próbie: **100 %**, Pure: **70 %**, łączny AP: **80 %**. Jakość wynika z niezależnej kontroli o określonym zakresie, nie z dodatkowego KPI panelu. Brak wartości początkowych oznacza brak możliwości oceny. Sama korekta w Infor nie jest automatycznie zdarzeniem DocBits.

**Ingerencja pozostaje zapisana.** Późniejsze automatyczne wykonanie nie usuwa korekt ani ręcznego restartu. Samo czytanie i podgląd nie są ingerencją; ręczna walidacja i restart są. Zatwierdzenie jest osobną kategorią.

<figure><img src="../.gitbook/assets/touchless-report-methodology-pl-20261104.png" alt="Aktualna populacja szkoleniowa: 201 zakończonych, kwalifikujących się faktur; żadna w toku ani wykluczona. 107 całkowicie automatycznych daje 53,2 %; z 11 samymi zatwierdzeniami to 118 i 58,7 %. Te wskaźniki procesu nie mierzą poprawności odczytu."><figcaption><p>Aktualna populacja szkoleniowa: 201 zakończonych, kwalifikujących się faktur; żadna w toku ani wykluczona. 107 całkowicie automatycznych daje 53,2 %; z 11 samymi zatwierdzeniami to 118 i 58,7 %. Te wskaźniki procesu nie mierzą poprawności odczytu.</p></figcaption></figure>

### Które działania AP są ingerencją?

Poniższe wyniki wymagają pomyślnego zakończenia i wymaganego potwierdzenia ERP. Liczy się zdarzenie i wykonawca, nie czas pracy.

| Działanie | Skutek |
| --- | --- |
| Czytanie, filtrowanie, porównanie, podgląd | Same w sobie nie wykluczają Pure |
| Tylko zatwierdzenie biznesowe, także kolejne | AP Touchless bez innych ingerencji |
| Zapis korekty pola lub komórki | AP Assisted; jedna korekta wystarcza |
| Ręczna walidacja lub restart przetwarzania/eksportu | AP Assisted po sukcesie; późniejsza automatyzacja tego nie usuwa |
| Automatyczna ponowna próba lub workflow | Sama nie jest ludzką ingerencją; wcześniejsze ingerencje pozostają |
| Korekta tylko w Infor | Nie jest automatycznie zdarzeniem DocBits; zapisz pracę i sprawdź następny krok |
| Ostateczne odrzucenie ERP | Wyjątek ma pierwszeństwo przed sukcesem |

Zapis bez wykazanej zmiany nie dowodzi korekty; sprawdź też ręczną walidację i restart.

### Dwa znaczenia AP

Procent i liczba na aktualnej karcie AP łączą Pure i samo zatwierdzenie. W przykładzie obliczeń to 150 = 120 + 30 dokumentów i 78,9 %. Na aktualnym zrzucie to 118 = 107 + 11 faktur i 58,7 %. Oddzielna kategoria wyniku, np. grupa MCP `AP_TOUCHLESS`, liczy tylko 11 zatwierdzeń. Aktualna niebieska linia pokazuje wskaźnik łączny z populacją każdego punktu. Pure i łączny AP nakładają się: nie dodawaj ich.

### Aktualność danych

Wyniki są przeliczane co 15 minut. Sprawdź datę aktualności i poczekaj na nowe obliczenia. Potwierdzenie ERP może przyjść później; samo wysłanie nie dowodzi zakończenia.

## FAQ

**Wskaźniki pokazują kreskę (—).**
Żaden dokument nie osiągnął w okresie wyniku końcowego lub zmierzono mniej dokumentów niż wymagane minimum. Dokumenty, które są jeszcze w toku, nie są liczone.

**Brakuje karty.**
Poproś administratora o włączenie modułu i przyznanie Twojej roli karty **Panel analityczny**.

**Dokument jest policzony jako dotknięty, ale tym razem przeszedł bez niczyjej pomocy.**
Został dotknięty we wcześniejszym uruchomieniu (korekta lub restart). Wskaźnik liczy pracę, która się wydarzyła.

**Dlaczego liczba zmienia się po kilku godzinach?**
ERP może potwierdzić eksport kilka godzin po jego wysłaniu. Wynik jest przeliczany co 15 minut.

**Czy AI zmienia cokolwiek samodzielnie?**
Nie. AI pisze tylko wyjaśnienia. Ustawienie zmienia się dopiero po tym, jak administrator wyświetli podgląd i je zastosuje.

## Powiązane strony

* [Touchless Intelligence](touchless-intelligence.md)
* [Korzystanie z panelu](touchless-dashboard.md)
* [Przykłady: cena i ilość](touchless-examples.md)
* [Touchless Intelligence: Diagnoza dostawcy i klastry problemów](touchless-supplier-diagnosis.md)
* [Touchless Intelligence: Diagnoza dopasowania PO](touchless-po-matching-diagnosis.md)
* [Touchless Intelligence: Ślad dokumentu](touchless-document-trace.md)
* [Touchless Intelligence: Propozycje zmian i raporty](touchless-change-proposals.md)
* [Wyjaśnianie i poprawa Touchless przez MCP](touchless-mcp.md)

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow has no screenshot yet. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described.

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
