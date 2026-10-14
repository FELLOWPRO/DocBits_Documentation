---
description: FACTURX 1.09 - ZUGFERD 2.5 — Compatibilidad con documentos electrónicos en DocBits
---

# 🇫🇷 FACTURX 1.09 - ZUGFERD 2.5

| Propiedad | Valor |
|-----------|-------|
| **País / Región** | Francia / Alemania |
| **Tipos de documento** | Factura, Nota de crédito |
| **Formato** | CII (PDF/A-3 incrustado) |
| **Estándar** | Factur-X 1.09 / ZUGFeRD 2.5 |
| **Basado en** | EN 16931 |

Factur-X 1.09 es la publicación francesa equivalente a ZUGFeRD 2.5 (publicación conjunta FeRD/FNFE-MPE, junio de 2026). Su XML CII utiliza la base D22B de UN/CEFACT, que es compatible con las versiones anteriores de D16B, por lo que el contrato completo de extracción y transformación de Factur-X 1.08 / ZUGFeRD 2.4 sigue siendo válido. El perfil EXTENDED añade nuevos campos para los medios de pago y el BIC, un beneficiario tercero (factor) y el motivo de exención de impuestos de descuentos y recargos.

Se admiten los cinco perfiles: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) y EXTENDED.

## Estado de compatibilidad

| Componente | Estado |
|------------|--------|
| Vista previa | ✅ Compatible |
| Extracción de campos | ✅ Compatible |
| Transformación | ✅ Compatible |

## Relacionados

* [ZUGFeRD 2.5](zugferd-2-5.md)
* [Configuración de ZUGFeRD](../zugferd/configuration.md)
* [Mapeo de campos de ZUGFeRD](../zugferd/README.md)
* [Documentos electrónicos compatibles](./)
