# DocBits (FELLOWPRO AG) — Kwestionariusz Bezpieczeństwa i Zgodności

**Dostawca:** DocBits by FELLOWPRO AG | **Hosting:** Frankfurt, Niemcy | **ISO 27001 Certyfikowane** | **Data:** 2026-03-04

Informacje o przechowywaniu danych uwierzytelniających i TLS w publicznych punktach końcowych sprawdzono **16 października 2026 r.** Poniższa strona opisuje potwierdzony zakres oraz kwestie, które wymagają jeszcze potwierdzenia dla danego wdrożenia. Zobacz [Bezpieczne przechowywanie danych uwierzytelniających](secure-storage-of-credentials.md).

Szczegóły szyfrowania w spoczynku zweryfikowano **16 października 2026 r.** na podstawie dokumentacji bezpieczeństwa DigitalOcean i metadanych usług. Zobacz [Szyfrowanie danych w spoczynku](encryption-at-rest.md).

Więcej informacji o bezpieczeństwie można znaleźć na stronach [Pliki cookie i pamięć przeglądarki](cookies-and-browser-storage.md), [Zarządzanie podatnościami](vulnerability-management.md) i [Pozostałe środki bezpieczeństwa](other-security-controls.md).

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

**Odpowiedź:** Środowisko produkcyjne UE jest hostowane w chmurze DigitalOcean we Frankfurcie w Niemczech. DocBits używa DigitalOcean Spaces do przechowywania oraz zarządzanych usług PostgreSQL, OpenSearch i Valkey. DocBits posiada certyfikat ISO 27001. Zakres szyfrowania opisują [Szyfrowanie danych w spoczynku](encryption-at-rest.md) i [Bezpieczne przechowywanie danych uwierzytelniających](secure-storage-of-credentials.md).

**Status:** ✅ Potwierdzone

**Notatki:** DigitalOcean Frankfurt: typy zarządzanych usług baz danych potwierdzono na podstawie metadanych infrastruktury 16 października 2026 r.; użycie Spaces opisano w tym FAQ.

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

**Notatki:** Kompleksowy harmonogram kopii zapasowych (codziennie/co tydzień/co kwartał/co roku) w dwóch lokalizacjach UE. Wszystkie dane pozostają w UE. Potwierdź szyfrowanie kopii zapasowych i częstotliwość testowania przywracania. Szyfrowanie kopii zarządzanych baz danych dostawcy opisano w [Szyfrowanie danych w spoczynku](encryption-at-rest.md); nie potwierdza to każdej kopii w szerszym harmonogramie kopii zapasowych.

---

### 4. Czy dostępne są opcje geo-partycjonowania (np. tylko dla UK)?

**Odpowiedź:** Dostępne dwa regiony centrów danych:
- **Frankfurt, Niemcy** — dla wszystkich klientów UE
- **San Francisco, USA** — wyłącznie dla klientów z USA

Dane klientów z UE hostowane są wyłącznie we Frankfurcie. Obecnie niedostępna jest opcja zarezerwowana wyłącznie dla UK.

**Status:** ✅ Potwierdzone

**Notatki:** Klienci z UE są tylko dla Frankfurtu — brak mieszania danych między regionami. Hosting zarezerwowany wyłącznie dla UK niedostępny; klienci z UK byliby obsługiwani z Frankfurtu. Wyjaśnij, czy dodatkowe regiony znajdują się na planie rozwoju.

---

### 5. Czy dane są szyfrowane w spoczynku i w tranzycie?

**Odpowiedź:** Publiczne punkty końcowe `app.docbits.com`, `auth.docbits.com` i `api.docbits.com` obsługują HTTPS z TLS 1.2 i TLS 1.3. Sprawdzenie 16 października 2026 r. potwierdziło odrzucanie TLS 1.0 i TLS 1.1. Hasła logowania i klucze utworzone w funkcji Zarządzanie kluczami API są chronione jednokierunkowym haszowaniem. Haszowanie jest odrębne od szyfrowania baz danych, magazynów danych i kopii zapasowych.

**W spoczynku:** DigitalOcean Managed Databases stosuje szyfrowanie całych woluminów za pomocą LUKS i AES-256-XTS; zarządzane kopie zapasowe używają AES-256-CTR. Spaces używa 256-bitowego AES-XTS na fizycznych dyskach. [Szyfrowanie danych w spoczynku](encryption-at-rest.md) opisuje metody, zarządzanie kluczami i zakres kopii.

**Status:** ✅ Częściowo potwierdzone

**Notatki:** Dotyczy to wymienionych usług zarządzanych. Dodatkowe eksporty, archiwa, kopie zapasowe, ewentualne szyfrowanie poszczególnych pól i każde połączenie wewnętrzne wymagają osobnego potwierdzenia dla wdrożenia. Szyfrowanie pamięci masowej nie potwierdza ograniczeń dostępu personelu. [Bezpieczne przechowywanie danych uwierzytelniających](secure-storage-of-credentials.md) wyjaśnia haszowanie i różnice w dostępie.

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

**Odpowiedź:** Dzienniki przechowywane na DigitalOcean Spaces we Frankfurcie i OpenSearch. Dzienniki dostępne dla klientów przechowywane przez 30 dni. Dzienniki wewnętrzne przechowywane przez 3 miesiące.

**Status:** ✅ Potwierdzone

**Notatki:** DigitalOcean Spaces + OpenSearch we Frankfurcie. Przechowywanie dostępu dla klientów przez 30 dni / wewnętrzne przez 3 miesiące. Potwierdź czy dzienniki są niezmienne/zabezpieczone przed manipulacją.

---

### 15. Jak długo przesyłane dokumenty / wyodrębnione dane przechowywane są w DocBits?

**Odpowiedź:** Klienci mogą konfigurować przechowywanie danych w ustawieniach. Opcje: 30 dni lub 3 miesiące. Po skonfigurowanym okresie dokumenty i wyodrębnione dane są automatycznie usuwane z serwerów DocBits.

**Status:** ✅ Potwierdzone

**Notatki:** Przechowywanie konfigurowalne przez klientów (30 dni / 3 miesiące). Potwierdź: Czy usunięcie obejmuje wszystkie kopie (DigitalOcean Spaces, OpenSearch, dane treningu AI)?

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

**Odpowiedź:** Udokumentowana integracja ION API używa HTTPS. Publiczny punkt końcowy API DocBits obsługuje TLS 1.2 i TLS 1.3. Weryfikacja ta nie potwierdza szyfrowania na każdym wewnętrznym etapie przetwarzania ani polityki TLS punktu końcowego ERP klienta.

**Status:** ✅ Częściowo potwierdzone

**Notatki:** Przed zapewnieniem szyfrowania end-to-end należy potwierdzić pełną ścieżkę połączenia, wymagania TLS punktu końcowego ERP oraz walidację certyfikatów w skonfigurowanej integracji. Zobacz [Bezpieczne przechowywanie danych uwierzytelniających](secure-storage-of-credentials.md).

---

### 25. Jakie typy dokumentów obsługiwane są poza fakturami AP?

**Odpowiedź:** Obsługuje faktury, doręczenia/rachunki, wyceny, potwierdzenia zamówień, umowy i więcej. Obsługuje faktury PO i non-PO.

**Status:** ✅ Potwierdzone

**Notatki:** Wyjaśnij które typy dokumentów zapisują się z powrotem do LN vs. są przechowywane wyłącznie w IDM.

---

## Przechowywanie danych uwierzytelniających i odzyskiwanie dostępu do konta

### 26. Czy dostawca może przeglądać dane uwierzytelniające klienta i co się dzieje po utracie hasła?

**Odpowiedź:** Hasła logowania DocBits są przechowywane jako jednokierunkowe skróty kryptograficzne z solą. Administratorzy i pomoc techniczna DocBits nie mogą odzyskać oryginalnego hasła w postaci jawnej z zapisanego skrótu. Użytkownicy, którzy zapomnieli hasła, muszą ustawić nowe za pomocą procedury resetowania przez e-mail, aby ponownie logować się hasłem. Skonfigurowane SSO lub klucze dostępu zapewniają alternatywne metody logowania. Klucze utworzone w funkcji Zarządzanie kluczami API DocBits są pokazywane tylko raz i zapisywane jako jednokierunkowe skróty. Ani administratorzy, ani pomoc techniczna DocBits nie mogą później odzyskać pełnego klucza. Utracone klucze należy unieważnić i zastąpić nowymi.

**Status:** ✅ Częściowo potwierdzone

**Notatki:** Te stwierdzenia dotyczą haseł logowania i kluczy wydanych przez DocBits. Upoważnieni administratorzy organizacji mogą przeglądać dane kont. Usługa nawiązująca połączenie może potrzebować dostępu do danych uwierzytelniających integracji; dostęp personelu dostawcy wymaga osobnego potwierdzenia. Zobacz [Bezpieczne przechowywanie danych uwierzytelniających](secure-storage-of-credentials.md).
