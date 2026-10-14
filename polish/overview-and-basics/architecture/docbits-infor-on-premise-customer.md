# DocBits Infor na miejscu Klienta

Aby wysłać dane do klienta Infor na miejscu, oferujemy dwa sposoby: Site2Site z IPsec lub [WatchDog](https://github.com/Fellow-Consulting-AG/docbits/tree/pl/readme/overview-and-basics/architecture/broken-reference/README.md)

Wysyłanie danych do klienta Infor na miejscu

Aby wysłać dane do klienta Infor na miejscu, oferujemy dwa sposoby: VPN Site-to-Site z IPsec.

## Konfiguracja VPN Site-to-Site IPsec (Internet Protocol Security)

### Dla VPN site-to-site IPsec musisz skonfigurować i otworzyć następujące porty:

1\. Port UDP 500: Używany do wymiany kluczy internetowych (IKE) faza 1 i faza 2.

2\. Port UDP 4500: Używany do przechodzenia przez NAT (NAT-T), umożliwiający ruch VPN przechodzenie przez urządzenia NAT (tłumaczenie adresów sieciowych).

## Uzyskiwanie dostępu do Infor OS

• URL uwierzytelniania: https://inforos.CustomerXYZad.net/

• URL danych: https://inforos.CustomerXYZad.net:7443/

## Podsumowanie:

Aby skonfigurować VPN site-to-site IPsec, upewnij się, że powyższe porty i protokoły są skonfigurowane i otwarte.

Użyj podanych adresów URL, aby uzyskać dostęp do Infor OS w celu uwierzytelnienia i danych.
