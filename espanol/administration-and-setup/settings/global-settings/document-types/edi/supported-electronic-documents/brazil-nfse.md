---
description: Soporte del documento electrónico BRAZIL NFS-E en DocBits
---

# 🇧🇷 BRAZIL NFS-E

| Propiedad | Valor |
|-----------|-------|
| **País / Región** | Brasil |
| **Tipos de documento** | Factura de servicios (Nota Fiscal de Serviços Eletrônica) |
| **Formato** | XML |
| **Estándar** | NFS-e 2.04 (norma nacional ABRASF para facturas municipales de servicios) |
| **Idioma** | `pt_BR` |

NFS-e (Nota Fiscal de Serviços Eletrônica) es la factura electrónica brasileña para servicios, emitida a nivel municipal. DocBits soporta el esquema del estándar ABRASF (Associação Brasileira das Secretarias de Finanças das Capitais). Los documentos NFS-e utilizan una estructura XML diferente a la NF-e: el impuesto principal es ISS (Imposto Sobre Serviços) en lugar de ICMS, y el proveedor/comprador se denominan `PrestadorServico` / `TomadorServico`. El elemento `Discriminacao` contiene la descripción del servicio en texto libre.

## Estado de soporte

| Componente | Estado |
|------------|--------|
| Vista previa | ✅ Compatible |
| Extracción de campos | ✅ Compatible |
| Transformación | ✅ Compatible |

## Vista previa predeterminada

<figure><img src="brazil-nfse-preview.png" alt="Vista previa de Brazil NFS-e en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para un documento BRAZIL NFS-E</p></figcaption></figure>

## Mapeo de campos

### Campos de cabecera

| Campo DocBits | XPath de origen | Notas |
|---|---|---|
| `invoice_id` | `//*[local-name()='Numero']` | Número de la NFS-e |
| `invoice_date` | `//*[local-name()='DataEmissao']` | Fecha de emisión ISO 8601 |
| `currency` | Fijo: `BRL` | Siempre Real Brasileño |
| `total_amount` | `//*[local-name()='ValorServicos']` | Valor bruto del servicio |
| `net_amount` | `//*[local-name()='ValorLiquidoNfse']` | Valor neto tras deducciones |
| `tax_amount` | `//*[local-name()='ValorIss']` | ISS (impuesto municipal sobre servicios) |
| `supplier_name` | `//*[local-name()='PrestadorServico']//*[local-name()='RazaoSocial']` | Nombre del prestador de servicios |
| `supplier_id` | `//*[local-name()='PrestadorServico']//*[local-name()='Cnpj']` | CNPJ del prestador |
| `buyer_name` | `//*[local-name()='TomadorServico']//*[local-name()='RazaoSocial']` | Nombre del tomador de servicios |
| `buyer_id` | `//*[local-name()='TomadorServico']//*[local-name()='Cnpj']` | CNPJ del tomador |

> La NFS-e describe un único servicio en el elemento `Discriminacao` en lugar de líneas de detalle. No se extrae ninguna `INVOICE_TABLE`.

## Regla de clasificación

DocBits detecta documentos BRAZIL NFS-E mediante el namespace:

```
http://www.abrasf.org.br/nfse.xsd
```

## Relacionados

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL CT-E](brazil-cte.md)
- [Documentos electrónicos compatibles](./)
