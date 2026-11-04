# DocBits Infor On-Premise-Kunde

Um Daten an Infor On-Premise-Kunden zu senden, bieten wir zwei Möglichkeiten: Site-to-Site mit IPsec oder [WatchDog](../administration-and-setup/setup/watchdog-installation.md)

Daten an Infor On-Premise-Kunden senden

Um Daten an einen Infor On-Premise-Kunden zu senden, bieten wir zwei Möglichkeiten: Site-to-Site VPN mit IPsec.

## IPsec (Internet Protocol Security) Site-to-Site VPN-Konfiguration

### Für ein IPsec Site-to-Site VPN müssen Sie die folgenden Ports konfigurieren und öffnen:

1\. UDP-Port 500: Wird für den Internet Key Exchange (IKE) Phase 1 und Phase 2 verwendet.

2\. UDP-Port 4500: Wird für NAT-Traversal (NAT-T) verwendet, um VPN-Verkehr durch NAT (Network Address Translation) Geräte zu leiten.

## Zugriff auf Infor OS

• Authentifizierungs-URL: https://inforos.CustomerXYZad.net/

• Daten-URL: https://inforos.CustomerXYZad.net:7443/

## Zusammenfassung:

Stellen Sie sicher, dass die oben genannten Ports und Protokolle für die Einrichtung eines IPsec Site-to-Site VPN konfiguriert und geöffnet sind.

Verwenden Sie die bereitgestellten URLs, um auf Infor OS für Authentifizierung und Daten zuzugreifen.
