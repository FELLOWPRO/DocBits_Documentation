---
description: Compatibilidad de DocBits con el documento electrónico THAILAND E-TAX INVOICE
---

# 🇹🇭 THAILAND E-TAX INVOICE

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte la guía del país para conocer los límites de versión, la configuración que se está utilizando y el vídeo explicativo del país. [Tailandia](countries/thailand.md). La etiqueta no indica una publicación. Confirme la estructura XML de origen. La verificación de firmas y la entrega a la plataforma tributaria requieren comprobaciones independientes.
{% endhint %}

| Propiedad              | Valor                                          |
| ---------------------- | ---------------------------------------------- |
| **País / Región**      | Tailandia                                      |
| **Tipos de documento** | Factura fiscal, Recibo                         |
| **Formato**            | XML (incrustado en PDF/A-3)                    |
| **Estándar**           | e-Tax Invoice & e-Receipt (Revenue Department) |

Thailand e-Tax Invoice es el estándar de factura fiscal y recibo electrónicos regulado por el Departamento de Ingresos (Revenue Department). Utiliza un formato híbrido similar a ZUGFeRD, que incrusta datos XML estructurados en un documento PDF/A-3. El sistema exige la firma digital con un certificado emitido por una CA tailandesa.

## Estado de compatibilidad

| Componente             | Estado          |
| ---------------------- | --------------- |
| Vista previa           | ✅ Compatible    |
| Extracción de campos   | ✅ Compatible    |
| Transformación         | ✅ Compatible    |

## Vista previa predeterminada

<figure><img src="../../../../../../.gitbook/assets/thailand-e-tax-invoice-preview.png" alt="Vista previa de Thailand e-Tax Invoice en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una Thailand e-Tax Invoice</p></figcaption></figure>

## Relacionado

* [Documentos electrónicos compatibles](./)
