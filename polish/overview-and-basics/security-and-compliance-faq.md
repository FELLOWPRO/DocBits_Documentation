# DocBits (FELLOWPRO AG) — Kwestionariusz Bezpieczeństwa i Zgodności

**Dostawca:** DocBits by FELLOWPRO AG | **Hosting:** Frankfurt, Niemcy | **ISO 27001 Certyfikowane** | **Data:** 2026-03-04

---

## Legenda Statusu

| Symbol | Znaczenie |
|--------|---------|
| ✅ Potwierdzone | Odpowiedź zweryfikowana z oficjalnej dokumentacji DocBits lub źródeł publicznych |
| ✅ Częściowe | Częściowo udzielona odpowiedź; wymagane dodatkowe szczegóły od zespołu DocBits |
| ❓ Do Potwierdzenia | Brak publicznych informacji — musi być potwierdzone bezpośrednio z DocBits/FELLOWPRO |
| ⚠️ Wymaga Wyjaśnienia | Publiczne informacje wskazują na obawy lub niejasność wymagającą jawnego wyjaśnienia od dostawcy |

---

## 🔹 Lokalizacja Danych i Rezydencja

### 1. Gdzie dokładnie hostowane jest środowisko produkcyjne?

**Odpowiedź:** Hostowane na infrastrukturze chmury AWS we Frankfurcie w Niemczech. Używa S3 do przechowywania i OpenSearch do indeksowania dzienników. DocBits posiada certyfikat ISO 27001. Wszystkie połączenia zabezpieczone poprzez SSH, HTTPS i standardowe protokoły szyfrowania.

**Status:** ✅ Potwierdzone

**Notatki:** Frankfurt na AWS potwierdzony (S3 + OpenSearch). Zapytaj o konkretny kod regionu AWS (eu-central-1) i czy pojedyncza czy multi-AZ.

---

### 2. Gdzie hostowane jest środowisko DR (Odzyskiwania po Awarii)?

**Odpowiedź:** DR wykorzystuje drugorzędną lokalizację kopii zapasowej w Amsterdamie, Holandia (UE). W połączeniu z głównym stanowiskiem we Frankfurcie zapewnia redundancję geograficzną w obrębie UE.

**Status:** ✅ Potwierdzone

**Notatki:** Frankfurt (główne) + Amsterdam (drugorzędne). Obie lokalizacje w UE. Zapytaj o cele RTO/RPO i szczegóły procesu trybu failover.

---

### 3. Gdzie przechowywane są kopie zapasowe?

**Odpowiedź:** Kopie zapasowe przechowywane w dwóch lokalizacjach UE:
- **Główne:** Frankfurt, Niemcy
- **Drugorzędne:** Amsterdam, Holandia

Harmonogram kopii zapasowych: Codziennie, Co tydzień, Co kwartał i Co roku.

**Status:** ✅ Potwierdzone

**Notatki:** Kompleksowy harmonogram kopii zapasowych (codziennie/co tydzień/co kwartał/co roku) w dwóch lokalizacjach UE. Wszystkie dane pozostają w UE. Potwierdź szyfrowanie kopii zapasowych i częstotliwość testowania przywracania.

---

### 4. Czy dostępne są opcje geo-partycjonowania (np. tylko dla UK)?

**Odpowiedź:** Dostępne dwa regiony centrów danych:
- **Frankfurt, Niemcy** — dla wszystkich klientów UE
- **Nowy Jork, USA** — wyłącznie dla klientów z USA

Dane klientów z UE hostowane są wyłącznie we Frankfurcie. Obecnie niedostępna jest opcja zarezerwowana wyłącznie dla UK.

**Status:** ✅ Potwierdzone

**Notatki:** Klienci z UE są tylko dla Frankfurtu — brak mieszania danych między regionami. Hosting zarezerwowany wyłącznie dla UK niedostępny; klienci z UK byliby obsługiwani z Frankfurtu. Wyjaśnij, czy dodatkowe regiony znajdują się na planie rozwoju.

---

### 5. Czy dane są szyfrowane w spoczynku i w tranzycie?

**Odpowiedź:** Wszystkie połączenia między komponentami są zabezpieczone za pomocą standardowych protokołów szyfrowania (SSH, HTTPS). Certyfikacja ISO 27001 wymaga kontroli szyfrowania.

**Status:** ✅ Potwierdzone

**Notatki:** Potwierdź konkretne standardy szyfrowania (np. AES-256 w spoczynku, TLS 1.2+ w tranzycie).

---

## 🔹 Obsługa Modeli AI/ML

### 6. Czy zawartość faktur jest wysyłana do jakiegoś hostingu modeli trzecich stron (np. OpenAI, Azure AI)?

**Odpowiedź:** Modele AI NIE są wysyłane do hostów trzecich stron. DocBits używa modeli Mistral AI uruchomionych we Frankfurcie w Niemczech — tej samej lokalizacji co środowisko produkcyjne. Żadne dane nie opuszczają regionu Frankfurt w celu przetwarzania AI.

**Status:** ✅ Potwierdzone

**Notatki:** Modele Mistral hostowane we Frankfurcie. Brak połączeń API trzecich stron dla przetwarzania dokumentów. W pełni niezależne.

---

### 7. Czy wyodrębnione dokumenty są używane do trenowania szerszych modeli u wszystkich klientów?

**Odpowiedź:** Tak — DocBits używa "AI swarm intelligence" do trenowania modeli klasyfikacji i ekstrakcji u wszystkich klientów. Jednak technologia działa jak mapa przez dane — nauczy się współrzędnych/pozycji strukturalnych pól danych na dokumentach, a NIE rzeczywistej zawartości dokumentu. Surowe dane dokumentu nie są udostępniane między dzierżawcami.

**Status:** ✅ Potwierdzone

**Notatki:** Swarm intelligence uczy się wzorów rozmieszczenia strukturalnego (współrzędne pól/pozycje), a nie zawartości dokumentu. Oznacza to, że żadne dane klientów (kwoty na fakturach, nazwy dostawców itp.) nie są udostępniane między dzierżawcami — tylko wiedza o strukturze dokumentu.

---

### 8. Czy można ograniczyć trening modelu wyłącznie do twojej dzierżawy?

**Odpowiedź:** Brak opcji izolacji modelu na dzierżawę. Jednak wspólne modele AI nauczają się jedynie współrzędnych rozmieszczenia dokumentu i wzorów strukturalnych — nie rzeczywistej zawartości dokumentu ani danych biznesowych. Klienci mogą dodatkowo trenować niestandardowe typy dokumentów ograniczone do ich własnej dzierżawy.

**Status:** ✅ Potwierdzone

**Notatki:** Niskie ryzyko: Wspólne modele uczą się danych pozycyjnych/strukturalnych (współrzędnych), a nie zawartości biznesowej. Trening niestandardowych typów dokumentów pozostaje w obrębie dzierżawy.

---

### 9. Gdzie hostowane i wykonywane są modele AI/ML?

**Odpowiedź:** Modele AI/ML (Mistral) są hostowane i wykonywane we Frankfurcie w Niemczech — tym samym regionie co środowisko produkcyjne.

**Status:** ✅ Potwierdzone

**Notatki:** Dobrze: Przetwarzanie AI pozostaje w obrębie Frankfurtu. Brak transferu danych do zewnętrznej infrastruktury AI.

---

### 10. Jakie technologie AI/ML są używane (silnik OCR, LLM, NLP)?

**Odpowiedź:** DocBits używa AI, OCR, uczenia maszynowego do ekstrakcji. Obsługuje 120+ języków. Twierdzi dokładność 96%+. Również używa Gen AI dla funkcji "AI Tags".

**Status:** ✅ Częściowe

**Notatki:** Zapytaj o konkretne szczegóły modelu: proprietarny vs. trzeciej strony OCR, który LLM zasilać funkcje Gen AI.

---

### 11. Czy dostępna jest opcja wdrożenia modelu AI na terenie?

**Odpowiedź:** Dokumentacja architektury DocBits odwołuje się zarówno do opcji wdrażania "klienta DocBits Cloud" jak i "DocBits On premise".

**Status:** ✅ Częściowe

**Notatki:** Potwierdź zakres opcji on-premise: Czy obejmuje pełne przetwarzanie AI czy tylko przechowywanie dokumentów?

---

## 🔹 Dostęp do Danych i Logowanie

### 12. Kto (wsparcie dostawcy/inżynierowie) może uzyskać dostęp do surowych dokumentów i danych Infor LN?

**Odpowiedź:** FELLOWPRO AG ma wyznaczonego Inspektora Ochrony Danych (Daniel Jordan). DPA z podprzetwórcami znajdują się w miejscu zgodnie z RODO. ISO 27001 wymaga kontroli dostępu.

**Status:** ✅ Częściowe

**Notatki:** Zapytaj DocBits: Dokładna lista ról personelu z dostępem do surowych dokumentów. Czy dostęp oparty jest na potrzebie / wyłącznie na żądanie?

---

### 13. Jakie kontrole dostępu i logowanie istnieją dla personelu dostawcy?

**Odpowiedź:** Certyfikacja ISO 27001 wymaga udokumentowanych kontroli dostępu, śladów audytu i środków bezpieczeństwa. DocBits utrzymuje ślad audytu dla zgodności i przeglądu.

**Status:** ✅ Częściowe

**Notatki:** Zapytaj o: Szczegóły RBAC, wymagania MFA, zarządzanie dostępem uprzywilejowanym (PAM) i czy dostęp jest logowany z niezmiennikami śladami audytu.

---

### 14. Jak długo przechowywane są dzienniki dostępu?

**Odpowiedź:** Dzienniki przechowywane na AWS S3 we Frankfurcie i OpenSearch. Dzienniki dostępne dla klientów przechowywane przez 30 dni. Dzienniki wewnętrzne przechowywane przez 3 miesiące.

**Status:** ✅ Potwierdzone

**Notatki:** S3 + OpenSearch we Frankfurcie. Przechowywanie dostępu dla klientów przez 30 dni / wewnętrzne przez 3 miesiące. Potwierdź czy dzienniki są niezmienne/zabezpieczone przed manipulacją.

---

### 15. Jak długo przesyłane dokumenty / wyodrębnione dane przechowywane są w DocBits?

**Odpowiedź:** Klienci mogą konfigurować przechowywanie danych w ustawieniach. Opcje: 30 dni lub 3 miesiące. Po skonfigurowanym okresie dokumenty i wyodrębnione dane są automatycznie usuwane z serwerów DocBits.

**Status:** ✅ Potwierdzone

**Notatki:** Przechowywanie konfigurowalne przez klientów (30 dni / 3 miesiące). Potwierdź: Czy usunięcie obejmuje wszystkie kopie (S3, OpenSearch, dane treningu AI)?

---

### 16. Czy klienci mogą zażądać usunięcia danych na żądanie?

**Odpowiedź:** FELLOWPRO AG zgodna z prawami osoby, której dane dotyczą RODO, w tym żądaniami wymazania. DPO przetwarza te żądania zgodnie z RODO Art. 17.

**Status:** ✅ Potwierdzone

**Notatki:** Potwierdź: Czy usunięcie obejmuje wszystkie kopie, w tym kopie zapasowe i dane treningu AI pochodzące z dzierżawy?

---

### 17. Którzy podprzetwórcy mają dostęp do danych klientów?

**Odpowiedź:** Cloudflare jest używany do ochrony przed botami/DDoS. DPA znajdują się w miejscu u wszystkich podprzetwórców zgodnie z wymogami RODO.

**Status:** ✅ Częściowe

**Notatki:** Zażądaj pełnej listy podprzetwórców. Cloudflare potwierdzony; zapytaj o dostawcę hostingu chmury, dostawców usług AI itp.

---

### 18. Jakie certyfikaty i ramy zgodności posiada DocBits?

**Odpowiedź:** ISO 27001 certyfikowane. Zgodne z RODO. Utrzymuje DPA u wszystkich podprzetwórców. Wyznaczony DPO.

**Status:** ✅ Potwierdzone

**Notatki:** Zapytaj: SOC 2 Type II? Raporty testów penetracyjnych? ISO 27701 (prywatność)? Harmonogram audytów rocznych?

---

## 🔹 Zakres Integracji (Infor LN)

### 19. Jaka jest dokładna lista pól danych pobieranych z wzorców LN do walidacji?

**Odpowiedź:** Dane wzorcowe importowane via BOD Infor:
- **Dostawcy:** Sync.SupplierPartyMaster, Sync.RemitToPartyMaster
- **Zamówienia Zakupu:** Sync.PurchaseOrder
- **Plan Kont:** Sync.CodeDefinition (ChartOfAccounts)
- **Wymiary Flex:** Sync.CodeDefinition (FlexDimensions)
- **Kody Podatkowe:** via BOD publish

**Status:** ✅ Potwierdzone

**Notatki:** Zapytaj DocBits o pełną listę BOD i dokumentację mapowania na poziomie pól dla twojej konkretnej konfiguracji LN.

---

### 20. Jakie konkretne pola nagłówka są eksportowane z powrotem do LN?

**Odpowiedź:** Pola eksportu nagłówka obejmują: SupplierCode, PurchaseType, InvoiceType, InvoiceNumberSupplier, InvoiceDate, InvoiceAmount, InvoiceCurrency, RateDeterminer, RateDate, TaxCountry, TransactionEntryDate, Reference, IDMReference, TaxBaseAmount, InvoiceDocumentType i więcej.

**Status:** ✅ Potwierdzone

**Notatki:** Przejrzyj plik mapowania pól dla twojego konkretnego środowiska. Potwierdź że wszystkie pola statyczne odpowiadają twojej konfiguracji firmy LN.

---

### 21. Czy operacje zapisu zwrotnego ograniczone są wyłącznie do obiektów interfejsu AP/PO?

**Odpowiedź:** Eksport używa BOD Sync.CaptureDocument, które jest transformowane do docelowych BOD (np. BOD faktur AP) na ION Desk. Dane są również eksportowane do Infor IDM do archiwizacji dokumentów.

**Status:** ✅ Częściowe

**Notatki:** Potwierdź: Czy DocBits pisze WYŁĄCZNIE do obiektów faktur AP i paragonów PO? Inne moduły LN dotknięte? Co z zakresem zapisu IDM?

---

### 22. Jaka metoda integracji jest stosowana (ION API, BOD, bezpośrednia DB)?

**Odpowiedź:** Integracja poprzez Infor ION API, ION Desk i standardowe BOD Infor. Brak bezpośredniego dostępu do bazy danych. Używa plików ION API i kont serwisowych do uwierzytelniania.

**Status:** ✅ Potwierdzone

**Notatki:** Dobrze: Brak bezpośredniego dostępu do DB. Cała komunikacja poprzez standardową warstwę integracji Infor.

---

### 23. Jakie uwierzytelnianie/autoryzacja jest używane do łączności LN?

**Odpowiedź:** Używa plików ION API (poświadczenia klienta OAuth2) z identyfikatorami klientów ION API i kontami serwisowymi utworzonymi w InforOS.

**Status:** ✅ Potwierdzone

**Notatki:** Upewnij się że konta serwisowe zgodne z zasadą najmniejszych uprawnień. Przejrzyj uprawnienia przyznane użytkownikowi DocBits ION API.

---

### 24. Czy transfer danych między DocBits a LN jest szyfrowany end-to-end?

**Odpowiedź:** Wszystkie połączenia między komponentami zabezpieczone za pomocą standardowych protokołów szyfrowania (SSH, HTTPS).

**Status:** ✅ Potwierdzone

**Notatki:** Komunikacja ION API używa HTTPS/TLS. Potwierdź minimalną wersję TLS (1.2+).

---

### 25. Jakie typy dokumentów obsługiwane są poza fakturami AP?

**Odpowiedź:** Obsługuje faktury, doręczenia/rachunki, wyceny, potwierdzenia zamówień, umowy i więcej. Obsługuje faktury PO i non-PO.

**Status:** ✅ Potwierdzone

**Notatki:** Wyjaśnij które typy dokumentów zapisują się z powrotem do LN vs. są przechowywane wyłącznie w IDM.
