# Architecture

## Client cloud

<figure><img src="../../.gitbook/assets/architecture1.avif" alt=""><figcaption></figcaption></figure>

## Sur site

<figure><img src="../../.gitbook/assets/architecture2.avif" alt=""><figcaption></figcaption></figure>

Doc**Bits** s'intègre parfaitement avec Infor LN/M3 via l'API ION, ION Desk et les BODs standards d'Infor. Notre intégration API nous permet d'exporter des données vers Infor et d'effectuer une validation des données maîtres dans Doc**Bits**.

## Exportation de données vers Infor

Nous utilisons l'API ION pour envoyer le PDF avec les attributs à IDM et le BOD Sync.CaptureDocument à ION Desk. Dans ION Desk, nous transformons le Sync.CaptureDocument vers les BODs cibles souhaités en fonction du type de document traité. Ces BODs Infor transformés sont ensuite automatiquement importés dans LN ou M3.

{% hint style="info" %}
Exporter vers [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Validation des données maîtres dans DocBits

Pour identifier le fournisseur ou comparer/faire correspondre les lignes de commande d'achat, nous activons un déclencheur dans LN/M3 qui envoie les BODs Sync.RemitToPartyMaster, Sync.SupplierPartyMaster et Sync.PurchaseOrder à Doc**Bits**. Nous configurons ce processus dans ION Desk en définissant le flux de données vers un point de connexion spécifique à Doc**Bits**.

<figure><img src="../../.gitbook/assets/architecture3.avif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
[Validation des données maîtres](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

## Importation d'E-mails OAuth Office365

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_architecture.png)
