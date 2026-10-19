---
description: Compatibilidad de DocBits con el documento electrónico KSEF
---

# 🇵🇱 KSEF

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte la guía del país para conocer los límites de versión, la configuración que se está utilizando y el vídeo explicativo del país. [Polonia](countries/poland.md). FA2 y FA3 utilizan estructuras diferentes. Confirme el esquema de origen y pruebe la asignación adecuada. Analizar el archivo no envía una factura a KSeF.
{% endhint %}

| Propiedad              | Valor                                    |
| ---------------------- | ---------------------------------------- |
| **País / Región**      | Polonia                                  |
| **Tipos de documento** | Factura, Nota de crédito, Factura rectificativa |
| **Formato**            | XML                                      |
| **Estándar**           | KSeF (Krajowy System e-Faktur)           |

KSeF es el Sistema Nacional de Facturación Electrónica de Polonia, gestionado por el Ministerio de Finanzas. Será obligatorio para todas las empresas polacas registradas a efectos de IVA. DocBits admite las versiones de esquema KSeF FA2 y FA3 para el procesamiento de facturas.

## Estado de compatibilidad

| Componente             | Estado          |
| ---------------------- | --------------- |
| Vista previa           | ✅ Compatible    |
| Extracción de campos   | ✅ Compatible    |
| Transformación         | ✅ Compatible    |

## Vista previa predeterminada

<figure><img src="../../../../../../.gitbook/assets/ksef-preview.png" alt="Vista previa de la factura KSeF en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura KSeF de Polonia</p></figcaption></figure>

## Relacionado

* [Documentos electrónicos compatibles](./)
* [KSeF FA2](ksef-fa2.md)
* [KSeF FA3](ksef-fa3.md)
