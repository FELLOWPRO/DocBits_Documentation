# Infrastruktura

Strona **Infrastructure** daje administratorom aktualny obraz tego, gdzie działa każda część platformy (EU lub US) i czy przetwarzanie jest w dobrym stanie. Jest tylko do odczytu, więc niczego tu nie konfiguruje się.

> **Access:** Infrastructure to strona wyłącznie dla administratorów. Otwórz **Settings → Organization & Access → Infrastructure**.

Strona ma trzy karty. Każda ładuje swoje dane przy pierwszym otwarciu, więc przełączanie między nimi nie pobiera wszystkiego od nowa.

| Tab | Answers |
|-----|---------|
| **Topology** | Gdzie działa każdy komponent i jak dokument przechodzi przez DocBits? |
| **Processing** | Czy etapy przetwarzania dokumentów działają i czy praca się kumuluje? |
| **Scheduled Tasks** | Czy cykliczne zadania w tle uruchamiają się zgodnie z harmonogramem? |

## Topology

**Topology** otwiera się domyślnie. Widok pokazuje platformę w dwóch odsłonach: **Architecture** i **Process**. Przełącznik nad diagramem pozwala przechodzić między nimi; wskaźnik obok pokazuje **live**, dopóki widok transmituje swój stan.

Baner nad diagramem podsumowuje kontrolę regionów:

* **Green**: wszystkie komponenty działają w regionie Twojej organizacji, a baner podaje nazwę tego regionu (na przykład **EU**).
* **Red**: komponent oznaczony jako krytyczny działa poza regionem Twojej organizacji.
* **Amber**: komunikat wskazuje komponenty znajdujące się w innym regionie, mimo że ogólna kontrola jest zaliczona. To różnica regionów, a nie awaria.

### Widok architektury

Widok architektury przedstawia platformę jako pasy kart komponentów, na przykład Edge / Web, Core API, Import, Background Services i Modules. Strzałki pokazują połączenia między kartami.

Każda karta pokazuje nazwę komponentu, oznaczenie regionu oraz, w przypadku komponentów krytycznych, kropkę stanu, która zmienia kolor na zielony, gdy komponent odpowiada, i pokazuje jego opóźnienie w milisekundach, gdy zgłaszana jest wartość.

| Badge | Meaning |
|-------|---------|
| **EU ✓** / **US ✓** | Komponent działa w regionie Twojej organizacji. |
| **SHARED** | Komponent globalny, taki jak CDN, bez jednego regionu. To jest oczekiwane. |
| **EU ⓘ** / **US ⓘ** | Komponent działa w innym regionie i jest zgłaszany jako uwaga. |
| **EU ⚠** / **US ⚠** | Komponent działa w innym regionie i jest zgłaszany jako błąd. Zgłoś to do pomocy technicznej. |
| Szare oznaczenie, bez znaku | Region tego komponentu nie jest znany. |

### Widok procesu

Widok procesu animuje pojedynczy dokument w potoku: źródła wejściowe **Email**, **FTP** i **Web** zbiegają się w **API**, a następnie przechodzą przez **OCR**, **Extraction**, **PO matching**, **Auto Accounting** i **Export**. Każdy etap łączy się z paskiem magazynów danych z **Postgres** i magazynem plików. Podpis wskazuje etap aktualnie animowany, a przycisk odtwarzania wstrzymuje animację lub ją wznawia.

PO matching i Auto Accounting są opcjonalne. Gdy jedno z nich jest wyłączone dla Twojej organizacji, jego etap jest wyszarzony, a animacja go pomija.

### Moduły opcjonalne

Moduły opcjonalne (Full-Text Search, DocFlow, Auto-Accounting, DocNet i PO Matching) mają na swojej karcie oznaczenie **active** lub **inactive**. Wyłączony moduł oferuje przycisk **Activate**, który prowadzi do strony, na której można go włączyć: ustawienia Modules dla większości modułów albo **Document Types** dla PO Matching, który włącza się dla każdego typu dokumentu.

## Processing

Karta **Processing** wylicza etapy przetwarzania dokumentów dla Twojej organizacji i informuje, czy praca płynie, czy się kumuluje.

| Column | Description |
|--------|-------------|
| **Process** | Etap przetwarzania: Document Processing, OCR, TR-OCR, Barcode Split, Barcode Extraction, Extraction i PO Match. |
| **Last run** | Jak dawno temu etap był ostatnio uruchamiany. Najedź kursorem, aby zobaczyć dokładny znacznik czasu. **Never run** oznacza, że żaden dokument nie dotarł jeszcze do tego etapu. |
| **Status** | Jedno lub więcej oznaczeń (patrz poniżej). |

Oznaczenia stanu są niezależnymi sygnałami:

* Czerwone oznaczenie **Errors (N)**: `N` dokumentów niedawno nie powiodło się na tym etapie.
* Bursztynowe oznaczenie z liczbą: `N` dokumentów jest teraz przetwarzanych przez ten etap.
* Zielone oznaczenie **OK**: brak niedawnych błędów i nic nie czeka.

Ponieważ błędy i trwająca praca są liczone osobno, etap może pokazywać oba jednocześnie, więc awaria pozostaje widoczna, podczas gdy inne dokumenty są nadal przetwarzane.

## Scheduled Tasks

Karta **Scheduled Tasks** wylicza cykliczne zadania w tle, które utrzymują DocBits w działaniu, na przykład odświeżanie pamięci podręcznej, alerty stanu, limity czasu dokumentów i synchronizacje wychodzące. Każdy wiersz pokazuje, czy zadanie uruchamia się na czas.

| Column | Description |
|--------|-------------|
| **Task** | Nazwa zadania zaplanowanego, w której separatory zastąpiono spacjami. |
| **Last run** | Jak dawno temu zadanie zostało uruchomione. Najedź kursorem, aby zobaczyć dokładny znacznik czasu. **Never run** oznacza, że nie zostało jeszcze uruchomione. |
| **Status** | Stan harmonogramu (patrz poniżej). |

| Status | Meaning |
|--------|---------|
| **On schedule** (zielone) | Zadanie działa w oczekiwanym interwale. |
| **Delayed** (czerwone) | Zadanie nie zostało uruchomione w oczekiwanym czasie. Zbadaj to lub zgłoś do pomocy technicznej. |
| **Unknown** (szare) | Nie udało się ustalić stanu harmonogramu. |

Obie tabele mają przycisk **Refresh**, który na żądanie ponownie ładuje aktualne wartości.
