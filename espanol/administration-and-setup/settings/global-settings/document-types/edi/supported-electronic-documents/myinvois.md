---
description: Compatibilidad de DocBits con el documento electrónico MYINVOIS
---

# 🇲🇾 MYINVOIS

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte la guía del país para conocer los límites de versión, la configuración que se está utilizando y el vídeo explicativo del país. [Malasia](countries/malaysia.md). La ruta de extracción inspeccionada se basa en XML. La plataforma nacional también acepta JSON, pero eso no demuestra la compatibilidad con la importación JSON en esta asignación de DocBits.
{% endhint %}

| Propiedad              | Valor                                                 |
| ---------------------- | ----------------------------------------------------- |
| **País / Región**      | Malasia                                               |
| **Tipos de documento** | Factura, Nota de crédito, Nota de débito, Autofactura |
| **Formato**            | UBL 2.1 XML                                    |
| **Estándar**           | MyInvois (LHDN - Lembaga Hasil Dalam Negeri)          |

MyInvois es el sistema de facturación electrónica de Malasia gestionado por la Agencia Tributaria (LHDN). En vigor desde agosto de 2024 para las grandes empresas, exige que todas las facturas se envíen al portal MyInvois para su validación y reciban un identificador único. El sistema utiliza UBL 2.1 y admite los formatos de envío XML y JSON.

## Estado de compatibilidad

| Componente             | Estado          |
| ---------------------- | --------------- |
| Vista previa           | ✅ Compatible    |
| Extracción de campos   | ✅ Compatible    |
| Transformación         | ✅ Compatible    |

## Vista previa predeterminada

<figure><img src="../../../../../../.gitbook/assets/myinvois-preview.png" alt="Vista previa de la factura MyInvois en DocBits"><figcaption><p>Vista previa predeterminada de DocBits para una factura MyInvois de Malasia</p></figcaption></figure>

## Relacionado

* [Documentos electrónicos compatibles](./)
