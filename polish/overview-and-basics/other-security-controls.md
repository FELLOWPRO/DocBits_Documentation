# Pozostałe środki bezpieczeństwa

Zweryfikowano **16 października 2026 r.** dla pytania **4.17**. Rozróżniamy opublikowane dowody audytowe i aktualną inwentaryzację infrastruktury.

| Środek | Udokumentowany zakres |
| --- | --- |
| Zapory sieciowe | Raport SOC 2 opisuje filtry VPC/security groups DigitalOcean oraz nadzór bezpieczeństwa IT nad zmianami. Aktualne kontrole tylko do odczytu potwierdzają aktywne zapory chmurowe, w tym reguły dla zasobów Kubernetes. |
| Zapora aplikacji internetowych (WAF) | Audyt RODO dokumentuje WAF chroniącą produkt. Nie zweryfikowano niezależnie aktualnych reguł zarządzanych, wyjątków ani zakresu dla każdej nazwy hosta. Zaobserwowane cookie Cloudflare chroniące przed botami same nie potwierdzają reguł WAF. |
| Równoważenie obciążenia | Aktualny spis DigitalOcean potwierdza aktywne produkcyjne load balancery we Frankfurcie z kontrolami stanu. Routing i przywiązanie sesji są funkcjami infrastruktury. Zobacz [Pliki cookie i pamięć przeglądarki](cookies-and-browser-storage.md). |
| Listy dozwolonych IP | Reguły infrastruktury umożliwiają filtrowanie źródeł. Nie potwierdzono listy per tenant konfigurowanej przez klienta, jej zakresu ani wyjątków. Wymagane ograniczenie wdrożenia należy uzgodnić z FELLOWPRO. |
| Testy lokalne i sandbox | [Strategia cyklu wydań](docbits-release-lifecycle-strategy.md) opisuje rozwój, QA/UAT i ocenę sandbox przed produkcją. Lokalne testy integracyjne wymagają określonego środowiska i odpowiednich danych. Dostęp do sandboxa sam nie zezwala na testy penetracyjne. |
| Maszyny wirtualne i Kubernetes | Raport SOC opisuje standardy utwardzania, dostęp, ograniczone porty i poprawki systemu/sieci. Spis potwierdza zarządzane klastry Kubernetes. Nie gwarantuje jednakowych ustawień dla każdego obciążenia. |
| Urządzenia końcowe i mobilne | Raport SOC opisuje antimalware, automatyczne skany, aktualizacje sygnatur i kontrolę poprawek. Raport ISO wskazuje MDM jako możliwość poprawy. Powszechne MDM, zdalne kasowanie i zasady mobile/BYOD wymagają aktualnego potwierdzenia. Klienci zabezpieczają własne urządzenia z przeglądarką. |
| Polityki i procedury | Raport SOC opisuje formalne polityki bezpieczeństwa, ocenę ryzyka, dostęp, zmiany, incydenty i szkolenia. Aktualne polityki i ich zakres udostępnia kontakt ds. zgodności. |

## Dowody i dalsze informacje

[Certyfikaty](architecture/certifications.md) zawierają raporty i okresy. Historyczne audyty potwierdzają środki w ocenionym zakresie; spis potwierdza obecność zasobów w dniu weryfikacji, nie jest pełnym audytem konfiguracji.

Zobacz [Bezpieczne przechowywanie danych uwierzytelniających](secure-storage-of-credentials.md), [Szyfrowanie danych w spoczynku](encryption-at-rest.md) i [Zarządzanie podatnościami](vulnerability-management.md).

Ograniczenia wdrożenia, wymagania mobilne i aktualne polityki: **compliance@fellowpro.com**.
