---
description: "Ustal skonfigurowaną rodzinę eDocs, składnię, wersję i profil przed testowaniem przetwarzania dokumentów."
---

# Formaty eDocs, wersje i przewodniki krajowe

Zacznij od dokumentu źródłowego i odpowiedniego przewodnika krajowego. Sama nazwa kraju nie określa formatu pliku. Oznaczenie wersji, składnia XML i profil biznesowy opisują różne rzeczy.

{% hint style="info" %}
Tabele przedstawiają wyniki kontroli katalogu środowiska deweloperskiego z 17 października 2026 i odpowiadającego mu kodu przetwarzania. Opisują dostępne reguły i komponenty konfiguracji, a nie certyfikację każdego pliku, wymogu prawnego czy wdrożenia produkcyjnego. Twoja organizacja może nadpisać ustawienia domyślne.
{% endhint %}

## Jak prawidłowo odczytywać macierz obsługi

- Rodzina: format dokumentu elektronicznego, na przykład XRechnung, Factur-X, KSeF lub CFDI.
- Składnia: rzeczywista zawartość danych, na przykład UBL XML, CII XML lub PDF z osadzonym XML. Skan PDF, eksport JSON czy obraz kodu QR nie są równoważną zawartością XML.
- Wersja: zadeklarowane wydanie publikacji lub schematu. Ogólne oznaczenie rodziny nie potwierdza obsługi każdego wydania.
- Profil: podzbiór reguł biznesowych lub danych, na przykład BASIC, EN16931, EXTENDED lub samofakturowanie. Profil nie jest wersją publikacji.
- Reguła i komponenty: klasyfikacja, Transformation, Preview i Extraction Paths są odrębne. Skonfigurowany profil nie musi mieć własnej reguły klasyfikacji.
- Walidacja i przesyłanie: wyświetlenie pliku lub wyodrębnienie danych samo w sobie nie weryfikuje wszystkich reguł prawnych, podpisów, zatwierdzenia podatkowego ani dostarczenia przez sieć.

## Przewodniki krajowe

| Kraj / region | Rodziny i zakres wersji | Wynik kontroli katalogu |
| --- | --- | --- |
| [Austria](countries/austria.md) | ebInterface 4.3, 5.0, 6.0 i 6.1 mają osobne wpisy. | Znaleziono wpisy |
| [Dania](countries/denmark.md) | OIOUBL 2.1 jest wymienionym duńskim wariantem. | Znaleziono wpisy |
| [Finlandia](countries/finland.md) | Finvoice 1.3, 2.0, 2.01 i 3.0 mają osobne wpisy. TEAPPSXML to inna rodzina. | Znaleziono wpisy |
| [Francja](countries/france.md) | Factur-X ma wpisy ogólne i przypisane do konkretnych wydań, w tym 1.0.05, 1.08 i 1.09. VRBL FR CIUS 1.0 jest odrębny. | Znaleziono wpisy |
| [Niemcy](countries/germany.md) | XRechnung ma trzynaście oznaczeń wersji od 1.0 do 3.0.2, każde w CII i UBL. ZUGFeRD obejmuje starsze profile oraz wpisy 2.5 dla CII i UBL. | Znaleziono wpisy |
| [Włochy](countries/italy.md) | FatturaPA jest skonfigurowaną włoską rodziną. | Znaleziono wpisy |
| [Niderlandy](countries/netherlands.md) | SI-UBL 2.0 ma dedykowany wpis. | Znaleziono wpisy |
| [Norwegia](countries/norway.md) | EHF Invoice 3.0 jest wymieniony obok EHF Order, Order Response i Despatch Advice. | Znaleziono wpisy |
| [Polska](countries/poland.md) | KSeF ma wpisy ogólne oraz FA2 i FA3. | Znaleziono wpisy |
| [Słowenia](countries/slovenia.md) | e-SLOG 1.6 i 2.0 mają osobne wpisy. | Znaleziono wpisy |
| [Hiszpania](countries/spain.md) | Facturae ma wpisy ogólne oraz 3.2, 3.2.1 i 3.2.2. | Znaleziono wpisy |
| [Szwecja](countries/sweden.md) | Svefaktura 1.0 jest wymienionym szwedzkim wariantem. | Znaleziono wpisy |
| [Australia](countries/australia.md) | PINT A-NZ ma wpisy reguł faktur i not kredytowych współdzielone z Nową Zelandią. | Znaleziono wpisy |
| [Nowa Zelandia](countries/new-zealand.md) | PINT A-NZ ma wpisy reguł faktur i not kredytowych współdzielone z Australią. | Znaleziono wpisy |
| [Indie](countries/india.md) | India GST E-Invoice i GST CreditNote mają osobne wpisy. | Znaleziono wpisy |
| [Indonezja](countries/indonesia.md) | Indonesia E-Faktur jest skonfigurowaną rodziną. | Znaleziono wpisy |
| [Chiny](countries/china.md) | Katalog obejmuje Fapiao, E-Fapiao, General VAT Invoice i Special VAT Invoice. | Znaleziono wpisy |
| [Japonia](countries/japan.md) | JP PINT i JP PINT Self-Billing to osobne wpisy. | Znaleziono wpisy |
| [Korea Południowa](countries/korea.md) | Korea E-Tax Invoice i Korea NTS to skonfigurowane rodziny. | Znaleziono wpisy |
| [Malezja](countries/malaysia.md) | MyInvois ma wpisy reguł faktur i not kredytowych. | Znaleziono wpisy |
| [Filipiny](countries/philippines.md) | Philippines EIS jest skonfigurowaną rodziną. | Znaleziono wpisy |
| [Singapur](countries/singapore.md) | InvoiceNow ma wpisy faktur i not kredytowych; InvoiceNow SG to kolejne skonfigurowane oznaczenie. | Znaleziono wpisy |
| [Tajwan](countries/taiwan.md) | Taiwan eGUI jest skonfigurowaną rodziną. | Znaleziono wpisy |
| [Tajlandia](countries/thailand.md) | Thailand E-Tax Invoice jest skonfigurowaną rodziną. | Znaleziono wpisy |
| [Wietnam](countries/vietnam.md) | Vietnam E-Invoice jest skonfigurowaną rodziną. | Znaleziono wpisy |
| [Argentyna](countries/argentina.md) | Argentina AFIP i Factura Electronica to skonfigurowane oznaczenia. | Znaleziono wpisy |
| [Brazylia](countries/brazil.md) | Brazylia ma wpisy NF-e, NFC-e, CT-e, NFS-e i SPED NFS-e. NFS-e obejmuje wersje 1.00 i od 2.00 do 2.04; SPED obejmuje 1.00.02 i 1.01. | Znaleziono wpisy |
| [Chile](countries/chile.md) | Chile DTE ma wpisy faktur, not kredytowych i dokumentów wysyłkowych. | Znaleziono wpisy |
| [Kolumbia](countries/colombia.md) | Colombia Factura Electronica i Documento Soporte mają osobne wpisy. | Znaleziono wpisy |
| [Kostaryka](countries/costa-rica.md) | Starsza dokumentacja wymienia Kostarykę, ale w sprawdzonym katalogu środowiska deweloperskiego nie znaleziono pasującego wpisu klasyfikacji ani konfiguracji. | Niepotwierdzone |
| [Ekwador](countries/ecuador.md) | Ecuador SRI ma wpisy ogólne oraz 1.0.0, 1.1.0, 2.0.0 i 2.1.0. Withholding (podatek u źródła) jest osobnym typem dokumentu. | Znaleziono wpisy |
| [Meksyk](countries/mexico.md) | Mexico CFDI 3.3 i 4.0 mają osobne wpisy. | Znaleziono wpisy |
| [Paragwaj](countries/paraguay.md) | Paraguay DTE, SIFEN i SIFEN 150 to skonfigurowane oznaczenia. | Znaleziono wpisy |
| [Peru](countries/peru.md) | Peru CPE ma wpisy ogólne oraz UBL 2.0 i UBL 2.1. Factura Electronica to kolejne oznaczenie. | Znaleziono wpisy |
| [Urugwaj](countries/uruguay.md) | Uruguay CFE ma wpisy ogólne oraz 24 i 25. Wymienione są też E-Factura i E-Nota Credito. | Znaleziono wpisy |
| [Kazachstan](countries/kazakhstan.md) | Kazakhstan ESF jest skonfigurowaną rodziną. | Znaleziono wpisy |
| [Arabia Saudyjska](countries/saudi-arabia.md) | ZATCA Fatoorah, Reporting, Simplified i Tax Invoice mają osobne wpisy. | Znaleziono wpisy |
| [Turcja](countries/turkey.md) | Turkey E-Fatura i E-Arsiv to osobne skonfigurowane rodziny. | Znaleziono wpisy |
| [Zjednoczone Emiraty Arabskie](countries/united-arab-emirates.md) | UAE VAT Invoice jest skonfigurowanym oznaczeniem. | Znaleziono wpisy |
| [Międzynarodowe](countries/international.md) | Wpisy międzynarodowe obejmują Peppol BIS 3.0, UBL 2.1, czysty CII, EDI, INVOIC02, cXML, OCI, BOD i SPS Commerce RSX 7.7.4. | Znaleziono wpisy |

## Factur-X / ZUGFeRD: nie zakładaj wersji publikacji

Zharmonizowany CII Guideline ID może identyfikować rodzinę i profil, mimo że kilka wydań używa tego samego znacznika 1p0. Factur-X XMP Version 1.0 jest znacznikiem schematu, a nie publikacją taką jak 1.08 czy 1.09. ZUGFeRD XMP może deklarować swoją wersję. Gdy brakuje miarodajnych metadanych, zachowaj ogólny wynik rozpoznania rodziny i potwierdź oryginalny plik z nadawcą.

MINIMUM i BASIC WL mogą pomijać dane pozycji potrzebne w dalszym przetwarzaniu. BASIC, EN16931/COMFORT i EXTENDED zapewniają różny zakres danych. Szerszy profil może zawierać pola, których mapowanie ekstrakcji nie wykorzystuje. Sprawdź wymagane pola na rzeczywistych przykładach.

## Sprawdź format w swojej organizacji

1. Zachowaj oryginalny plik XML lub PDF z osadzonym XML. Odczytaj przestrzeń nazw, schemat lub identyfikator dostosowania oraz zadeklarowaną wersję lub profil.

2. Otwórz Ustawienia → Typy dokumentów → E-Doc dla odpowiedniego dokumentu biznesowego. Wyszukaj dokładny format dokumentu elektronicznego podany w przewodniku.

3. Sprawdź faktycznie używane źródło Default lub Custom oraz aktywną wersję konfiguracji. Sprawdź Transformation, Preview i Extraction Paths. Zapisanie wersji roboczej nie powoduje jej aktywowania.

4. Przetestuj reprezentatywne pliki źródłowe dla każdej wymaganej składni, wersji i rodzaju dokumentu biznesowego. Sprawdź kluczowe pola, kwoty, podatek, klasyfikację faktury lub noty kredytowej i eksport do ERP.

5. Osobno potwierdź zasady walidacji i transport. Zachowaj mapowania niestandardowe oraz sprawdź zatwierdzenia i historię eksportu przed ponownym uruchomieniem istniejących dokumentów.

[Kontrole akceptacyjne](../credit-note-recognized-as-invoice.md)

[Konfigurowanie DocBits przez Claude lub Codex](../../../../../../advanced-functions-and-tools/docbits-mcp/configuration-with-claude-or-codex.md): połączenie, prompty, podglądy, wersjonowane zmiany, kontrole i cofnięcie.
