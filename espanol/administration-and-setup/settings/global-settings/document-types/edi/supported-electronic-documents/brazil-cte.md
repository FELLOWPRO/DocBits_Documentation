---
description: Soporte del documento electrónico BRAZIL CT-E en DocBits
---

# 🇧🇷 BRAZIL CT-E

| Propiedad | Valor |
|-----------|-------|
| **País / Región** | Brasil |
| **Tipos de documento** | Factura de transporte (Conhecimento de Transporte Eletrônico) |
| **Formato** | XML |
| **Estándar** | CT-e 3.0 (conocimiento electrónico de flete/transporte) |
| **Idioma** | `pt_BR` |

CT-e (Conhecimento de Transporte Eletrônico, `<mod>57</mod>`) es el documento electrónico de transporte brasileño emitido por empresas de logística y carga. Documenta el servicio de transporte, el valor de la carga, los municipios de origen y destino (`cMunIni` / `cMunFim`) y el precio del flete (`vTPrest`). A diferencia de la NF-e, el CT-e utiliza `cteProc` como elemento raíz y referencia documentos NF-e asociados.

## Estado de soporte

| Componente | Estado |
|------------|--------|
| Vista previa | ✅ Compatible |
| Extracción de campos | ✅ Compatible |
| Transformación | ✅ Compatible |

## Vista previa predeterminada

<figure><img src="brazil-cte-preview.png" alt="Vista previa de Brazil CT-e en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para un documento BRAZIL CT-E</p></figcaption></figure>

## Mapeo de campos

### Campos de cabecera

| Campo DocBits | XPath de origen | Notas |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nCT']` | Número del CT-e |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 con desplazamiento BRT |
| `currency` | Fijo: `BRL` | Siempre Real Brasileño |
| `total_amount` | `//*[local-name()='vPrest']/*[local-name()='vTPrest']` | Valor total del servicio de transporte |
| `net_amount` | `//*[local-name()='vPrest']/*[local-name()='vRec']` | Valor a cobrar |
| `tax_amount` | `//*[local-name()='ICMS']//*[local-name()='vICMS']` | ICMS sobre el servicio de transporte |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Nombre de la transportista (emit) |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` | CNPJ de la transportista |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Nombre del destinatario (dest) |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CNPJ']` | CNPJ del destinatario |

> El CT-e no incluye tabla de líneas — el servicio de transporte es un cargo único a nivel de documento.

## Regla de clasificación

DocBits detecta documentos BRAZIL CT-E mediante:

```
http://www.portalfiscal.inf.br/cte
```

en el namespace XML (elemento raíz `<cteProc>`).

## Relacionados

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Documentos electrónicos compatibles](./)
