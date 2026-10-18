---
description: "Brazylia ma wpisy NF-e, NFC-e, CT-e, NFS-e i SPED NFS-e. NFS-e obejmuje wersje 1.00 i od 2.00 do 2.04; SPED obejmuje 1.00.02 i 1.01."
---

# Brazylia

Skorzystaj z tego przewodnika, aby ustalić skonfigurowaną rodzinę i zakres wersji przed testowaniem pliku źródłowego.

[Wszystkie kraje i zakres obsługi](../README.md)

## Warianty i ograniczenia wersji

Brazylia ma wpisy NF-e, NFC-e, CT-e, NFS-e i SPED NFS-e. NFS-e obejmuje wersje 1.00 i od 2.00 do 2.04; SPED obejmuje 1.00.02 i 1.01.

**Składnia:** XML

Są to różne rodziny dokumentów. Skonfigurowana wersja NFS-e nie certyfikuje każdego schematu gminnego ani każdego krajowego układu faktury za usługi.

Tabele przedstawiają wyniki kontroli katalogu środowiska deweloperskiego z 17 października 2026 i odpowiadającego mu kodu przetwarzania. Opisują dostępne reguły i komponenty konfiguracji, a nie certyfikację każdego pliku, wymogu prawnego czy wdrożenia produkcyjnego. Twoja organizacja może nadpisać ustawienia domyślne.

## Macierz sprawdzonych reguł i komponentów

| Dokładne oznaczenie formatu | Klucz dokumentu reguły | Dostępne komponenty |
| --- | --- | --- |
| `BRAZIL CT-E` | `INVOICE` | C / T / P / E |
| `BRAZIL NF-E` | `INVOICE` | C / T / P / E |
| `BRAZIL NF-E (Import)` | `INVOICE` | C / T / P / E |
| `BRAZIL NFC-E` | `INVOICE` | C / T / P / E |
| `BRAZIL NFS-E` | `INVOICE` | C / T / P / E |
| `BRAZIL NFS-E 1.00` | `INVOICE` | C / T / P / E |
| `BRAZIL NFS-E 2.00` | `INVOICE` | C / T / P / E |
| `BRAZIL NFS-E 2.01` | `INVOICE` | C / T / P / E |
| `BRAZIL NFS-E 2.02` | `INVOICE` | C / T / P / E |
| `BRAZIL NFS-E 2.03` | `INVOICE` | C / T / P / E |
| `BRAZIL NFS-E 2.04` | `INVOICE` | C / T / P / E |
| `BRAZIL SPED NFS-E 1.00.02` | `INVOICE` | C / T / P / E |
| `BRAZIL SPED NFS-E 1.01` | `INVOICE` | C / T / P / E |

C = klasyfikacja, T = Transformation, P = Preview, E = Extraction Paths. Klucz dokumentu służy do wyszukiwania reguł i konfiguracji; nie gwarantuje ostatecznej zapisanej wartości invoice_type. Transformacja może sklasyfikować notę kredytową za pomocą mapowania INVOICE.

Myślnik oznacza, że kontrola statusu nie wykazała dedykowanego komponentu dla tej dokładnej pary formatu i klucza dokumentu. Nie wyklucza to mapowania współdzielonego lub rezerwowego. Zanim oprzesz się na tej ścieżce, sprawdź faktycznie używany mechanizm wyboru mapowania i reprezentatywny plik.

## Znajdź mapowanie w DocBits

<figure><img src="../../../../../../../.gitbook/assets/edocs-support-brazil-pl.png" alt="Brazylia"><figcaption><p>Rzeczywisty interfejs środowiska deweloperskiego: przykładowy format i dostępne komponenty konfiguracji. Pozostałe wersje wymieniono w macierzy.</p></figcaption></figure>

## Film objaśniający dla kraju

Narracja i napisy WebVTT w wybranym języku wyjaśniają wybór formatu, konfigurację i kontrole akceptacyjne.

Ten przegląd bez wprowadzania zmian pokazuje istniejącą konfigurację kraju w DocBits. Sprawdź używane źródło i aktywną wersję, a następnie przetestuj reprezentatywne faktury, noty kredytowe i eksporty we własnej organizacji.

{% file src="../../../../../../../.gitbook/assets/edocs-support-brazil-pl-v2.mp4" %}
Brazylia — Film objaśniający dla kraju
{% endfile %}

{% file src="../../../../../../../.gitbook/assets/edocs-support-brazil-pl-v2.vtt" %}
WebVTT
{% endfile %}

## Kontrole akceptacyjne

Kontrola komponentów potwierdza obecność konfiguracji. Nie jest testem pełnego przetwarzania każdej wersji. Przetestuj dokładną zawartość danych oraz ścieżkę faktury lub noty kredytowej wymaganą przez integrację.

## Sprawdź format w swojej organizacji

1. Zachowaj oryginalny plik XML lub PDF z osadzonym XML. Odczytaj przestrzeń nazw, schemat lub identyfikator dostosowania oraz zadeklarowaną wersję lub profil.

2. Otwórz Ustawienia → Typy dokumentów → E-Doc dla odpowiedniego dokumentu biznesowego. Wyszukaj dokładny format dokumentu elektronicznego podany w przewodniku.

3. Sprawdź faktycznie używane źródło Default lub Custom oraz aktywną wersję konfiguracji. Sprawdź Transformation, Preview i Extraction Paths. Zapisanie wersji roboczej nie powoduje jej aktywowania.

4. Przetestuj reprezentatywne pliki źródłowe dla każdej wymaganej składni, wersji i rodzaju dokumentu biznesowego. Sprawdź kluczowe pola, kwoty, podatek, klasyfikację faktury lub noty kredytowej i eksport do ERP.

5. Osobno potwierdź zasady walidacji i transport. Zachowaj mapowania niestandardowe oraz sprawdź zatwierdzenia i historię eksportu przed ponownym uruchomieniem istniejących dokumentów.

## Powiązana dokumentacja formatu

- [🇧🇷 BRAZIL NF-E](../brazil-nfe.md)
- [🇧🇷 BRAZIL NFC-E](../brazil-nfce.md)
- [🇧🇷 BRAZIL CT-E](../brazil-cte.md)
- [🇧🇷 BRAZIL NFS-E](../brazil-nfse.md)
