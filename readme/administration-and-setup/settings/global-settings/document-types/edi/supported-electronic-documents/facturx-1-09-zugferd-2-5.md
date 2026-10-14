---
description: Compatibilidad de DocBits con el documento electrónico FACTURX 1.09 - ZUGFERD 2.5
---

# 🇫🇷 FACTURX 1.09 - ZUGFERD 2.5

| Propiedad | Valor |
|----------|-------|
| **País / Región** | Francia / Alemania |
| **Tipos de documento** | Factura, Nota de crédito |
| **Formato** | CII (incrustado en PDF/A-3) |
| **Estándar** | Factur-X 1.09 / ZUGFeRD 2.5 |
| **Basado en** | EN 16931 |

Factur-X 1.09 es la publicación francesa equivalente a ZUGFeRD 2.5 (publicación conjunta de FeRD/FNFE-MPE, junio de 2026). Su XML CII utiliza la base UN/CEFACT D22B, que es retrocompatible con D16B, por lo que el contrato completo de extracción y transformación de Factur-X 1.08 / ZUGFeRD 2.4 sigue siendo válido. El perfil EXTENDED añade nuevos campos para los medios de pago y el BIC, un beneficiario tercero (factor) y el motivo de exención de impuestos de descuentos y cargos.

Se admiten los cinco perfiles: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) y EXTENDED.

## Estado de compatibilidad

| Componente | Estado |
|-----------|--------|
| Vista previa | ✅ Compatible |
| Extracción de campos | ✅ Compatible |
| Transformación | ✅ Compatible |

## Relacionado

- [ZUGFeRD 2.5](zugferd-2-5.md)
- [Configuración de ZUGFeRD](../zugferd/configuration.md)
- [Asignación de campos de ZUGFeRD](../zugferd/README.md)
- [Documentos electrónicos compatibles](./)
