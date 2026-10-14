# DocBits Infor na miejscu Klienta

Aby wysłać dane do klienta Infor na miejscu, oferujemy dwa sposoby: Site2Site z IPsec lub [WatchDog](https://docs.docbits.com/administration-and-setup/setup/watchdog)

Wysyłanie danych do klienta Infor na miejscu

Aby wysłać dane do klienta Infor na miejscu, oferujemy dwa sposoby: VPN Site-to-Site z IPsec.

## Konfiguracja VPN Site-to-Site IPsec (Internet Protocol Security)

### 1. Informacje konfiguracyjne:

| **Konfiguracja IPSEC VPN**     |                                                                 |
| ------------------------------ | --------------------------------------------------------------- |
|                                | **Endpoint B**                                                  |
| **Klient**                     | _**FELLOWPRO AG**_                                              |
| **Osoba kontaktowa**           | _**Daniel Lopez**_                                              |
| **E-mail**                     | [daniel.lopez@fellowpro.com](mailto:daniel.lopez@fellowpro.com) |
| **Sprzęt/oprogramowanie endpointu** | _**StrongWAN**_                                            |
| **Lokalizacja zapory**         | _**Frankfurt**_                                                 |
| **IP endpointu**               | _**46.101.133.158**_                                            |
| **Sieć/Host 1**                | _**10.135.0.0/16**_                                             |

### 2. Dla VPN site-to-site IPsec musisz skonfigurować i otworzyć następujące porty:

1\. Port UDP 500: Używany do wymiany kluczy internetowych (IKE) faza 1 i faza 2.

2\. Port UDP 4500: Używany do przechodzenia przez NAT (NAT-T), umożliwiający ruch VPN przechodzenie przez urządzenia NAT (tłumaczenie adresów sieciowych).

## Uzyskiwanie dostępu do Infor OS

• URL uwierzytelniania: https://inforos.CustomerXYZad.net/

• URL danych: https://inforos.CustomerXYZad.net:7443/

## Podsumowanie:

Aby skonfigurować VPN site-to-site IPsec, upewnij się, że powyższe porty i protokoły są skonfigurowane i otwarte.

Użyj podanych adresów URL, aby uzyskać dostęp do Infor OS w celu uwierzytelnienia i danych.
