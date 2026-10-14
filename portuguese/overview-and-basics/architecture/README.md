# Arquitetura

## **Cliente DocBits Cloud**

<figure><img src="../../.gitbook/assets/docbits_cloud_customer_architecture.png" alt="Arquitetura do cliente DocBits Cloud"><figcaption></figcaption></figure>

## DocBits On premise

<figure><img src="../../.gitbook/assets/docbits_on_premise_architecture.png" alt="Arquitetura do DocBits On Premise"><figcaption></figcaption></figure>

Doc**Bits** integra-se perfeitamente com Infor ERP / SAP e M3 por meio da ION API, do ION Desk e dos BODs padrão da Infor. Nossa integração de API nos permite exportar dados para a Infor e realizar a validação de dados mestres no Doc**Bits**.

## **Arquitetura do DocBits Operator**

Todas as conexões entre os componentes são protegidas com protocolos de criptografia padrão do setor. SSH, HTTPS e outros canais seguros garantem a integridade e a confidencialidade dos dados em todo o sistema.

**On Premise:**&#x20;

<figure><img src="../../.gitbook/assets/Operator_On-Prem.png" alt=""><figcaption></figcaption></figure>

{% content-ref url="prefect-local-setup-requirements.md" %}
[prefect-local-setup-requirements.md](prefect-local-setup-requirements.md)
{% endcontent-ref %}

**Cloud**:

<figure><img src="../../.gitbook/assets/Operator Cloud .png" alt=""><figcaption></figcaption></figure>

## Exportando dados para a Infor

Usamos a ION API para enviar o PDF com atributos ao IDM e o BOD Sync.CaptureDocument ao ION Desk. No ION Desk, transformamos o [Sync.CaptureDocument](../../infor-integration-and-configuration/exporting-in-docbits/) nos BODs de destino desejados, com base no tipo de documento processado. Esses BODs da Infor transformados são então importados automaticamente para o LN ou o M3.

{% hint style="info" %}
Exportar para a [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Validação de dados mestres no DocBits

Para identificar o fornecedor ou comparar/combinar linhas de pedidos de compra, ativamos um gatilho no LN/M3 que envia os BODs Sync.RemitToPartyMaster, Sync.SupplierPartyMaster e Sync.PurchaseOrder para o Doc**Bits**. Configuramos esse processo no ION Desk definindo o fluxo de dados para um ponto de conexão específico com o Doc**Bits**.

<figure><img src="../../.gitbook/assets/docbits_architecture (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
[Validação de dados mestres](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

## Importação de e-mail com OAuth Office365

<figure><img src="../../.gitbook/assets/o365_architecture.png" alt=""><figcaption></figcaption></figure>
