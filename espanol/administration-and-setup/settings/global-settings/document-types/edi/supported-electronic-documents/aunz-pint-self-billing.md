---
description: Soporte de documentos electrónicos AUNZ PINT SELF-BILLING en DocBits
---

# 🇦🇺 AUNZ PINT SELF-BILLING

| Propiedad | Valor |
|----------|-------|
| **País / Región** | Australia / Nueva Zelanda |
| **Tipos de documento** | Factura de autofacturación |
| **Formato** | UBL 2.1 XML |
| **Estándar** | PINT A-NZ Self-Billing |
| **Configuración regional** | `en_AU` |

AUNZ PINT Self-Billing es la variante de autofacturación del modelo de facturación Peppol International de A-NZ. En escenarios de autofacturación, el comprador crea la factura en nombre del proveedor. Este tipo de documento sigue la misma estructura PINT A-NZ pero con roles de partes invertidos — la `AccountingCustomerParty` se convierte en la parte emisora de la factura y la `AccountingSupplierParty` es la parte facturada.

## Estado de soporte

| Componente | Estado |
|-----------|--------|
| Vista previa | ✅ Soportado |
| Extracción de campos | ✅ Soportado |
| Transformación | ✅ Soportado |

## Vista previa predeterminada

<figure><img src="aunz-pint-preview.png" alt="Vista previa de factura AUNZ PINT Self-Billing en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura AUNZ PINT Self-Billing</p></figcaption></figure>

## Asignación de campos

La asignación de campos es idéntica a [AUNZ PINT](aunz-pint.md) con la siguiente diferencia clave:

- **Los roles de las partes están invertidos**: En la autofacturación, el comprador es la parte emisora y el proveedor es la parte facturada
- La `CustomizationID` contiene `urn:peppol.org:pint:selfbilling-1@aunz` en lugar de `billing-1@aunz`

Para la tabla completa de asignación de campos, véase [AUNZ PINT](aunz-pint.md#asignacion-de-campos).

## Regla de clasificación

DocBits detecta documentos de autofacturación coincidiendo con la `CustomizationID`:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Tanto los patrones de autofacturación como los de facturación regular se clasifican bajo el tipo de documento electrónico `PINT A-NZ`.

## Relacionado

- [AUNZ PINT](aunz-pint.md)
- [Documentos electrónicos soportados](./)