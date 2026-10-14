# Architecture

## **Client DocBits Cloud**

<figure><img src="../../.gitbook/assets/docbits_cloud_customer_architecture.png" alt="Architecture client DocBits Cloud"><figcaption></figcaption></figure>

## DocBits sur site

<figure><img src="../../.gitbook/assets/docbits_on_premise_architecture.png" alt="Architecture DocBits sur site"><figcaption></figcaption></figure>

Doc**Bits** s'intègre parfaitement avec Infor LN/M3 via l'API ION, ION Desk et les BODs standards d'Infor. Notre intégration API nous permet d'exporter des données vers Infor et d'effectuer une validation des données maîtres dans Doc**Bits**.

## **Architecture de DocBits Operator**

Toutes les connexions entre les composants sont sécurisées par des protocoles de chiffrement conformes aux standards de l'industrie. SSH, HTTPS et d'autres canaux sécurisés garantissent l'intégrité et la confidentialité des données dans l'ensemble du système.

**Sur site :**&#x20;

<figure><img src="../../.gitbook/assets/Operator_On-Prem.png" alt=""><figcaption></figcaption></figure>

{% content-ref url="prefect-local-setup-requirements.md" %}
[prefect-local-setup-requirements.md](prefect-local-setup-requirements.md)
{% endcontent-ref %}

**Cloud** :

<figure><img src="../../.gitbook/assets/Operator Cloud .png" alt=""><figcaption></figcaption></figure>

## Exportation de données vers Infor

Nous utilisons l'API ION pour envoyer le PDF avec les attributs à IDM et le BOD Sync.CaptureDocument à ION Desk. Dans ION Desk, nous transformons le [Sync.CaptureDocument](../../infor-integration-and-configuration/exporting-in-docbits/) vers les BODs cibles souhaités en fonction du type de document traité. Ces BODs Infor transformés sont ensuite automatiquement importés dans LN ou M3.

{% hint style="info" %}
Exporter vers [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Validation des données maîtres dans DocBits

Pour identifier le fournisseur ou comparer/faire correspondre les lignes de commande d'achat, nous activons un déclencheur dans LN/M3 qui envoie les BODs Sync.RemitToPartyMaster, Sync.SupplierPartyMaster et Sync.PurchaseOrder à Doc**Bits**. Nous configurons ce processus dans ION Desk en définissant le flux de données vers un point de connexion spécifique à Doc**Bits**.

<figure><img src="../../.gitbook/assets/docbits_architecture (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
[Validation des données maîtres](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

## Importation d'e-mails OAuth Office365

<figure><img src="../../.gitbook/assets/o365_architecture.png" alt=""><figcaption></figcaption></figure>
