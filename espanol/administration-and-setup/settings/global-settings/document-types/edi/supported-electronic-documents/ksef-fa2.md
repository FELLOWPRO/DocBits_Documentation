---
description: Compatibilidad de DocBits con el documento electrónico KSEF FA2
---

# 🇵🇱 KSEF FA2

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte la guía del país para conocer los límites de versión, la configuración que se está utilizando y el vídeo explicativo del país. [Polonia](countries/poland.md). FA2 y FA3 utilizan estructuras diferentes. Confirme el esquema de origen y pruebe la asignación adecuada. Analizar el archivo no envía una factura a KSeF.
{% endhint %}

| Propiedad              | Valor                           |
| ---------------------- | ------------------------------- |
| **País / Región**      | Polonia                         |
| **Tipos de documento** | Factura, Factura rectificativa  |
| **Formato**            | XML                             |
| **Estándar**           | KSeF FA(2)                      |

KSeF FA2 es la segunda versión del esquema del Sistema Nacional de Facturación Electrónica de Polonia. Define la estructura XML de las facturas estructuradas (faktury), incluidos los datos del vendedor y del comprador, las líneas de detalle, los tipos de IVA y las condiciones de pago exigidos por la legislación fiscal polaca.

## Estado de compatibilidad

| Componente             | Estado          |
| ---------------------- | --------------- |
| Vista previa           | ✅ Compatible    |
| Extracción de campos   | ✅ Compatible    |
| Transformación         | ✅ Compatible    |

## Vista previa predeterminada

<figure><img src="../../../../../../.gitbook/assets/ksef-preview.png" alt="Vista previa de la factura KSeF FA(2) en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura KSeF FA(2) de Polonia</p></figcaption></figure>

## Relacionado

* [Documentos electrónicos compatibles](./)
