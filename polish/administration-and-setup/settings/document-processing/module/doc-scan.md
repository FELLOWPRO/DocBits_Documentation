---
description: Twórz dokumenty w DocBits za pomocą lokalnego skanera i Doc Scan.
---

# Doc Scan

## Pobierz i zainstaluj oprogramowanie skanera

Na pulpicie DocBits kliknij Scan Document.

<figure><img src="../../../../.gitbook/assets/image (203).png" alt="Przycisk Scan Document na pulpicie DocBits"><figcaption></figcaption></figure>

Jeśli lokalne oprogramowanie skanera nie jest zainstalowane, DocBits wyświetli monit o pobranie. Wybierz plik dla swojego systemu operacyjnego.

<figure><img src="../../../../.gitbook/assets/image (204).png" alt="Monit o pobranie lokalnego oprogramowania skanera"><figcaption></figcaption></figure>

Otwórz pobrany plik instalacyjny. Przedstawiony instalator jest przeznaczony dla macOS; postępuj zgodnie z instrukcjami dla swojego systemu operacyjnego.

<figure><img src="../../../../.gitbook/assets/image (205).png" alt="Uruchomienie instalatora oprogramowania skanera"><figcaption></figcaption></figure>

W przedstawionym instalatorze kliknij Continue, zaakceptuj licencję oprogramowania za pomocą Agree i kontynuuj. Sprawdź miejsce instalacji i wymaganą ilość miejsca, a następnie kliknij Install. Wyświetlone 33,6 MB dotyczy tej wersji instalatora; wymagana ilość miejsca może zmieniać się w zależności od wersji.

Po zakończeniu instalacji zamknij instalator.

<figure><img src="../../../../.gitbook/assets/image (206).png" alt="Zakończona instalacja oprogramowania skanera"><figcaption></figcaption></figure>

Otwórz https://local.polydocs.io:12500/ w przeglądarce, aby przetestować usługę lokalną. Jeśli przeglądarka nie może się z nią połączyć i używasz FRITZ!Box, sprawdź opisane poniżej ustawienia ochrony przed DNS rebinding.

<figure><img src="../../../../.gitbook/assets/image (207).png" alt="Błąd przeglądarki podczas testowania lokalnej usługi skanera"><figcaption></figcaption></figure>

Gdy pojawi się strona usługi lokalnej, kliknij DocBits, aby otworzyć DocBits.

<figure><img src="../../../../.gitbook/assets/image (208).png" alt="Strona lokalnej usługi skanera po udanym połączeniu"><figcaption></figcaption></figure>

Zaloguj się na stronie logowania DocBits, aby otworzyć swój pulpit.

<figure><img src="../../../../.gitbook/assets/image (209).png" alt="Strona logowania DocBits otwarta z usługi lokalnej"><figcaption></figcaption></figure>

Włącz Doc Scan w ustawieniach, w sekcji Moduły.

<figure><img src="../../../../.gitbook/assets/image (210).png" alt="Ustawienie modułu Doc Scan"><figcaption></figcaption></figure>

## Ustawienia sieciowe FRITZ!Box

Jeśli https://local.polydocs.io:12500/ jest niedostępny, ponieważ FRITZ!Box blokuje odpowiedzi DNS z adresami prywatnymi, przeglądarka może zgłosić przekroczenie czasu oczekiwania DNS. FRITZ!Box stosuje tę ochronę przed DNS rebinding. Dodaj wyjątek nazwy hosta dla tej usługi lokalnej:

1. W niemieckim interfejsie FRITZ!Box otwórz Heimnetz (sieć domowa), a następnie Netzwerk (sieć).
2. Otwórz kartę Netzwerkeinstellungen (ustawienia sieciowe).
3. W sekcji DNS-Rebind-Schutz (ochrona przed DNS rebinding) dodaj local.polydocs.io do wyjątków nazw hostów.
4. Kliknij Übernehmen (zastosuj) i ponownie przetestuj usługę lokalną.

## Odinstaluj Doc2Scan Service Manager

Aby odinstalować Doc2Scan Manager w macOS, wykonaj:

```bash
sudo bash /Library/doc2scan/uninstall.sh
```

## Zgodność skanerów

sane-airscan to backend SANE dla Apple AirScan/eSCL i Microsoft WSD (WS-Scan, Web Services for Devices). Są to protokoły skanowania sieciowego.

Sprawdź [aktualizowane informacje o zgodności sane-airscan](https://github.com/alexpevzner/sane-airscan), aby poznać zgłoszone wsparcie urządzeń i protokołów. Dostępność protokołu lub zgłoszenie dotyczące sane-airscan nie gwarantuje, że każda funkcja urządzenia działa w Doc Scan. Przetestuj skaner w wymaganym procesie pracy z Doc Scan.
