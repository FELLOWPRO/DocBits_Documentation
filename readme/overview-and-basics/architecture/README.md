# Architektura

## **Klient DocBits Cloud**

<figure><img src="../../.gitbook/assets/docbits_cloud_customer_architecture.png" alt="Architektura klienta DocBits Cloud"><figcaption></figcaption></figure>

## DocBits lokalnie

<figure><img src="../../.gitbook/assets/docbits_on_premise_architecture.png" alt="Architektura DocBits On Premise"><figcaption></figcaption></figure>

Doc**Bits** bezproblemowo integruje się z Infor LN/M3 za pośrednictwem ION API, ION Desk i standardowych BOD Infor. Nasza integracja API pozwala nam na eksport danych do Infor oraz przeprowadzanie walidacji danych głównych w Doc**Bits**.

## **Architektura DocBits Operator**

Wszystkie połączenia między komponentami są zabezpieczone przy użyciu standardowych w branży protokołów szyfrowania. SSH, HTTPS i inne bezpieczne kanały zapewniają integralność i poufność danych w całym systemie.

**W siedzibie:**

<figure><img src="../../.gitbook/assets/Operator_On-Prem.png" alt="Diagram architektury Operator On-Prem z DocAgent na komputerze klienckim łączącym się z Prefect API i chmurą DocBits"><figcaption></figcaption></figure>

{% content-ref url="prefect-local-setup-requirements.md" %}
[prefect-local-setup-requirements.md](prefect-local-setup-requirements.md)
{% endcontent-ref %}

**Cloud**:

<figure><img src="../../.gitbook/assets/Operator Cloud .png" alt="Diagram architektury Operator Cloud z rozszerzeniem Chrome, DocBits Operator Cloud, DocFlow i DocBits AI wymieniającymi komunikaty zadań i odpowiedzi"><figcaption></figcaption></figure>

## Eksportowanie danych do Infor

Używamy ION API do wysyłania PDF z atrybutami do IDM oraz BOD Sync.CaptureDocument do ION Desk. W ION Desk przekształcamy [Sync.CaptureDocument](../../infor-integration-and-configuration/exporting-in-docbits/) do docelowych BOD w zależności od przetwarzanego typu dokumentu. Te przekształcone BOD Infor są następnie automatycznie importowane do LN lub M3.

{% hint style="info" %}
Eksport do [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Walidacja danych głównych w DocBits

Aby zidentyfikować dostawcę lub porównać/dopasować linie zamówienia, aktywujemy wyzwalacz w LN/M3, który wysyła BOD Sync.RemitToPartyMaster, Sync.SupplierPartyMaster i Sync.PurchaseOrder do Doc**Bits**. Konfigurujemy ten proces w ION Desk, definiując przepływ danych do konkretnego punktu połączenia z Doc**Bits**.

<figure><img src="../../.gitbook/assets/docbits_architecture (1).png" alt="Diagram architektury DocBits klastra Kubernetes z load balancerem, Redis, PostgreSQL, podami roboczymi i magazynem danych Spaces"><figcaption></figcaption></figure>

{% hint style="info" %}
[Walidacja danych głównych](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

## Import e-mail OAuth Office365

<figure><img src="../../.gitbook/assets/o365_architecture.png" alt="Diagram importu poczty e-mail Office 365 pokazujący, jak Microsoft Graph API wystawia token dostępu dla usługi pocztowej DocBits i systemu głównego"><figcaption></figcaption></figure>
