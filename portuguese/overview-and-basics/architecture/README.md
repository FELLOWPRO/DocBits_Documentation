# Arquitetura

## Cliente em cloud

<figure><img src="../../.gitbook/assets/architecture1.avif" alt=""><figcaption></figcaption></figure>

## Local

<figure><img src="../../.gitbook/assets/architecture2.avif" alt=""><figcaption></figcaption></figure>

Doc**Bits** integra-se perfeitamente com Infor LN/M3 através da API ION, ION Desk e BODs Padrão da Infor. Nossa integração de API nos permite exportar dados para a Infor e realizar validação de dados mestres no Doc**Bits**.

## Exportando Dados para a Infor

Usamos a API ION para enviar o PDF com atributos para IDM e o BOD Sync.CaptureDocument para o ION Desk. No ION Desk, transformamos o Sync.CaptureDocument nos BODs de destino desejados com base no tipo de documento que está sendo processado. Esses BODs da Infor transformados são então importados automaticamente para LN ou M3.

{% hint style="info" %}
Exportar para [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Validação de Dados Mestres no DocBits

Para identificar o fornecedor ou comparar/combinar linhas de pedidos de compra, ativamos um gatilho no LN/M3 que envia os BODs Sync.RemitToPartyMaster, Sync.SupplierPartyMaster e Sync.PurchaseOrder para o Doc**Bits**. Configuramos esse processo no ION Desk definindo o fluxo de dados para um ponto de conexão específico com o Doc**Bits**.

<figure><img src="../../.gitbook/assets/architecture3.avif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
[Validação de Dados Mestres](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

## Importação de E-mails OAuth Office365

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_architecture.png)
