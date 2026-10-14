# Architektura

## Klient w cloud

<figure><img src="../../.gitbook/assets/architecture1.avif" alt=""><figcaption></figcaption></figure>

## Na miejscu

<figure><img src="../../.gitbook/assets/architecture2.avif" alt=""><figcaption></figcaption></figure>

Doc**Bits** bezproblemowo integruje się z Infor LN/M3 za pośrednictwem ION API, ION Desk i standardowych BOD Infor. Nasza integracja API pozwala nam na eksport danych do Infor oraz przeprowadzanie walidacji danych głównych w Doc**Bits**.

## Eksportowanie danych do Infor

Używamy ION API do wysyłania PDF z atrybutami do IDM oraz BOD Sync.CaptureDocument do ION Desk. W ION Desk przekształcamy Sync.CaptureDocument do pożądanych BOD w zależności od przetwarzanego typu dokumentu. Te przekształcone BOD Infor są następnie automatycznie importowane do LN lub M3.

{% hint style="info" %}
Eksport do [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Walidacja danych głównych w DocBits

Aby zidentyfikować dostawcę lub porównać/dopasować linie zamówienia, aktywujemy wyzwalacz w LN/M3, który wysyła BOD Sync.RemitToPartyMaster, Sync.SupplierPartyMaster i Sync.PurchaseOrder do Doc**Bits**. Konfigurujemy ten proces w ION Desk, definiując przepływ danych do konkretnego punktu połączenia z Doc**Bits**.

<figure><img src="../../.gitbook/assets/architecture3.avif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
[Walidacja danych głównych](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

## Import e-mail OAuth Office365

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_architecture.png)
