---
description: Soporte del documento electrónico BRAZIL NFC-E en DocBits
---

# 🇧🇷 BRAZIL NFC-E

| Propiedad | Valor |
|-----------|-------|
| **País / Región** | Brasil |
| **Tipos de documento** | Factura al consumidor (Nota Fiscal de Consumidor Eletrônica) |
| **Formato** | XML |
| **Estándar** | NFC-e 4.0 (factura minorista para el consumidor final) |
| **Idioma** | `pt_BR` |

NFC-e (Nota Fiscal de Consumidor Eletrônica, `<mod>65</mod>`) es la factura electrónica brasileña para ventas minoristas al consumidor final. Utiliza el mismo namespace que NF-e (`http://www.portalfiscal.inf.br/nfe`), pero con el código de modelo 65. El comprador en una NFC-e normalmente tiene un número CPF (identificador fiscal individual) en lugar de CNPJ. En transacciones minoristas simples, las líneas no incluyen impuestos PIS/COFINS.

## Estado de soporte

| Componente | Estado |
|------------|--------|
| Vista previa | ✅ Compatible |
| Extracción de campos | ✅ Compatible |
| Transformación | ✅ Compatible |

## Vista previa predeterminada

<figure><img src="brazil-nfce-preview.png" alt="Vista previa de Brazil NFC-e en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para un documento BRAZIL NFC-E</p></figcaption></figure>

## Mapeo de campos

### Campos de cabecera

| Campo DocBits | XPath de origen | Notas |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nNF']` | Número de Nota Fiscal |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 con desplazamiento BRT |
| `currency` | Fijo: `BRL` | Siempre Real Brasileño |
| `total_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vNF']` | Valor total de la NFC-e |
| `net_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vProd']` | Subtotal de productos |
| `tax_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']` | Importe total del impuesto ICMS |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Nombre del comercio minorista |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` o `CPF` | CNPJ o CPF |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Nombre del consumidor |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CPF']` o `CNPJ` | CPF (persona física) o CNPJ |

### Tabla de líneas (`INVOICE_TABLE`)

Ruta de fila: `//*[local-name()='det']`

| Columna | XPath relativo | Notas |
|---|---|---|
| `POSITION` | `@nItem` | Número de posición secuencial |
| `ITEM_CODE` | `*[local-name()='prod']/*[local-name()='cProd']` | Código de producto |
| `DESCRIPTION` | `*[local-name()='prod']/*[local-name()='xProd']` | Descripción del producto |
| `NCM_CODE` | `*[local-name()='prod']/*[local-name()='NCM']` | Clasificación arancelaria NCM |
| `CFOP_CODE` | `*[local-name()='prod']/*[local-name()='CFOP']` | Código de operación fiscal |
| `UNIT` | `*[local-name()='prod']/*[local-name()='uCom']` | Unidad de medida |
| `QUANTITY` | `*[local-name()='prod']/*[local-name()='qCom']` | Cantidad comercial |
| `UNIT_PRICE` | `*[local-name()='prod']/*[local-name()='vUnCom']` | Precio unitario |
| `TOTAL_AMOUNT` | `*[local-name()='prod']/*[local-name()='vProd']` | Total de línea |
| `ICMS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']` | Impuesto ICMS por línea |
| `VAT_RATE` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | Tasa ICMS (%) |

> La NFC-e no incluye impuestos PIS/COFINS a nivel de línea en transacciones minoristas simples.

## Regla de clasificación

DocBits detecta documentos BRAZIL NFC-E mediante el patrón `<mod>65</mod>` dentro del namespace `http://www.portalfiscal.inf.br/nfe` en el XML.

## Relacionados

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL CT-E](brazil-cte.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Documentos electrónicos compatibles](./)
