# Przechowywanie, retencja i usuwanie danych

Twoje dane są w dobrych rękach z DocBits. Działamy w dwóch regionach, **Frankfurt am Main (UE)** i **San Francisco (USA)**, a w ustawieniach sam decydujesz, jak długo dokumenty u nas pozostają. Ta strona opisuje lokalizacje przechowywania, okresy retencji i usuwanie danych.

**Stan dokumentacji na dzień: 28 października 2026.**

## W skrócie

- **Region wybierasz Ty:** Frankfurt dla klientów z UE, San Francisco dla klientów z USA.
- **Twoje dane pozostają w Twoim regionie.** Dane z UE są hostowane we Frankfurcie, dane z USA w San Francisco. Dane z różnych regionów nie są ze sobą mieszane.
- **Sam kontrolujesz, jak długo dokumenty są przechowywane** w sekcji **Document Processing → Wygaśnięcie dokumentów** ([przejdź do ustawienia](../administration-and-setup/settings/document-processing/documents-expiry.md)).
- **Tymczasowe pliki OCR** są usuwane automatycznie po 90 minutach.
- **Chętnie pomożemy:** nasz zespół odpowiada na pytania i wnioski o usunięcie danych pod adresem **compliance@fellowpro.com**.

## Gdzie przechowywane są Twoje dane?

| Region | Dla kogo | Lokalizacja | Wykorzystywane usługi |
| --- | --- | --- | --- |
| **UE** | Wszyscy klienci z UE | **Frankfurt am Main, Niemcy** | DigitalOcean Kubernetes (region `fra1`) z zarządzanymi bazami danych PostgreSQL, OpenSearch i Valkey (`fra1`) oraz DigitalOcean Spaces do przechowywania plików |
| **USA** | Klienci z USA | **San Francisco, USA** | DigitalOcean Kubernetes (region `sfo2`) z zarządzanymi bazami danych PostgreSQL, OpenSearch i Valkey (`sfo2`) |

**Kopie zapasowe w UE:** Frankfurt jest podstawową lokalizacją kopii zapasowych, a Amsterdam (Holandia) dodatkową, dzięki czemu Twoje kopie zapasowe również pozostają w UE.

**Połączone systemy:** Jeśli eksportujesz dokumenty do swojego systemu ERP, Infor IDM lub innego systemu docelowego, te kopie są przechowywane w tym systemie, według jego zasad i w jego lokalizacji. To pozostaje w Twoich rękach.

## Jak długo dane są przechowywane?

| Rodzaj danych | Retencja |
| --- | --- |
| **Przesłane dokumenty i wyodrębnione dane** | Kontrolujesz ją Ty za pomocą ustawienia [Wygaśnięcie dokumentów](../administration-and-setup/settings/document-processing/documents-expiry.md) (patrz niżej). |
| **Tymczasowe pliki OCR** | Automatyczne czyszczenie po **90 minutach**. Dotyczy to wyłącznie tymczasowego magazynu OCR, a nie Twojego dokumentu w DocBits. |
| **Logi dostępne dla klienta** (do przeglądania w sekcji [Dziennik aktywności](../administration-and-setup/settings/log-settings/README.md)) | **30 dni** |
| **Logi wewnętrzne** | **3 miesiące** |
| **Codzienne kopie zapasowe baz danych (zarządzane)** | **7 dni**; starsze kopie są usuwane automatycznie. |
| **Dodatkowe codzienne kopie zapasowe (SnapShooter)** | Dla baz danych produkcyjnych i sandbox; retencja jest ustalana osobno dla każdego środowiska. |
| **Pliki cookie i pamięć przeglądarki** | Różni się w zależności od celu, zobacz [Pliki cookie i pamięć przeglądarki](cookies-and-browser-storage.md). |

Wykonujemy też kopie zapasowe codziennie, co tydzień, co kwartał i co rok. Na życzenie chętnie podamy dokładne okresy retencji dla tych rodzajów kopii zapasowych w Twoim środowisku.

## Jak ustawić retencję swoich dokumentów

W Ustawieniach otwórz **Document Processing → Wygaśnięcie dokumentów**. Dostępne są dwa ustawienia:

- **Delete document after:** jak długo dokumenty są przechowywane.
- **Delete finished document after:** jak długo przechowywane są zakończone, w pełni przetworzone i wyeksportowane dokumenty.

Do wyboru są opcje **Default**, **48 Hours**, **1 Week**, **2 Weeks** i **4 Weeks**. **Default** stosuje domyślne ustawienie systemowe. Jeśli chcesz ustalić konkretny okres, po prostu wybierz jedną z opcji czasu. Wszystkie szczegóły znajdziesz w [przewodniku Wygaśnięcie dokumentów](../administration-and-setup/settings/document-processing/documents-expiry.md).

## Co się dzieje po usunięciu danych?

Wygaśnięcie dokumentów automatycznie usuwa Twoje dokumenty po wybranym przez Ciebie okresie. Jest to niezależne od czyszczenia tymczasowych plików OCR, wygasania logów i retencji kopii zapasowych.

Warto wiedzieć:

- **Kopie zapasowe wygasają według własnego harmonogramu.** Usunięcie dokumentu w systemie produkcyjnym nie usuwa więc od razu kopii zapasowych, lecz dopiero z końcem odpowiedniego okresu przechowywania kopii.
- **Wyeksportowane kopie należą do Ciebie.** Gdy DocBits usuwa dokument, kopia w Twoim systemie ERP lub archiwum pozostaje. Zaplanuj tam retencję zgodnie z własnymi wymaganiami.

## Pytania lub wnioski o usunięcie danych? Jesteśmy do Twojej dyspozycji

W sprawie informacji o Twoim wdrożeniu lub wniosku o usunięcie danych napisz do nas na adres **compliance@fellowpro.com**. Podaj swoją organizację, którego środowiska dotyczy sprawa, rodzaj danych i potrzebny zakres. Prosimy nie wysyłać haseł ani kluczy API.

Chętnie potwierdzimy również:

- Twój aktywny region i obowiązujące ustawienia retencji, w tym domyślne ustawienie systemowe.
- Kiedy rozpoczyna się okres usuwania i jak często odbywa się czyszczenie.
- Zakres usuwania dokumentów, wyodrębnionych danych, indeksów wyszukiwania i danych pochodnych.
- Lokalizacje i okresy retencji wszystkich rodzajów kopii zapasowych, także po zakończeniu umowy.

## Więcej informacji o bezpieczeństwie

- [DocBits (FELLOWPRO AG) — Kwestionariusz Bezpieczeństwa i Zgodności](security-and-compliance-faq.md)
- [Szyfrowanie danych w spoczynku](encryption-at-rest.md)
- [Bezpieczne przechowywanie danych uwierzytelniających](secure-storage-of-credentials.md)
- [Pliki cookie i pamięć przeglądarki](cookies-and-browser-storage.md)
