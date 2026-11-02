# DocBits Infor On-Premise-Kunde

Um Daten an einen Infor-On-Premise-Kunden zu senden, bieten wir zwei Wege an: Site-to-Site mit IPsec oder [WatchDog](https://docs.docbits.com/administration-and-setup/setup/watchdog)

Daten an einen Infor-On-Premise-Kunden senden

Um Daten an einen Infor-On-Premise-Kunden zu senden, bieten wir zwei Wege an: Site-to-Site-VPN mit IPsec.

## Konfiguration eines IPsec-(Internet Protocol Security-)Site-to-Site-VPN

### 1. Konfigurationsinformationen:

| **IPSEC-VPN-Einrichtung**      |                                                                 |
| ------------------------------ | --------------------------------------------------------------- |
|                                | **Endpunkt B**                                                  |
| **Kunde**                      | _**FELLOWPRO AG**_                                              |
| **Name des Ansprechpartners**  | _**Daniel Lopez**_                                              |
| **E-Mail**                     | [daniel.lopez@fellowpro.com](mailto:daniel.lopez@fellowpro.com) |
| **Endpunkt-Hardware/-Software**| _**StrongWAN**_                                                 |
| **Standort der Firewall**      | _**Frankfurt**_                                                 |
| **Endpunkt-IP**                | _**46.101.133.158**_                                            |
| **Netzwerk/Host 1**            | _**10.135.0.0/16**_                                             |

### 2. Für ein IPsec-Site-to-Site-VPN müssen Sie die folgenden Ports konfigurieren und öffnen:

1\. UDP-Port 500: Wird für Phase 1 und Phase 2 des Internet Key Exchange (IKE) verwendet.

2\. UDP-Port 4500: Wird für NAT-Traversal (NAT-T) verwendet, wodurch VPN-Datenverkehr durch NAT-Geräte (Network Address Translation) geleitet werden kann.

## Zugriff auf Infor OS

• Authentifizierungs-URL: https://inforos.CustomerXYZad.net/

• Daten-URL: https://inforos.CustomerXYZad.net:7443/

## Zusammenfassung:

Stellen Sie für die Einrichtung eines IPsec-Site-to-Site-VPN sicher, dass die oben genannten Ports und Protokolle konfiguriert und geöffnet sind.

Verwenden Sie die angegebenen URLs, um für die Authentifizierung und den Datenaustausch auf Infor OS zuzugreifen.
