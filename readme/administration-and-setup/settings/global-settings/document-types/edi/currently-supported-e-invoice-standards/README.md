# Şu Anda Desteklenen E-Fatura Standartları

{% embed url="https://youtu.be/li8KjWO18eU" %}
DocBits EDI Configuration Guide: Structure Descriptors, Transformation & Extraction Paths
{% endembed %}

## Ülkeye Göre Desteklenen Elektronik Belgeler

### 🇦🇷 Arjantin

| Standart | Durum |
|---|---|
| [ARGENTINA AFIP](../supported-electronic-documents/argentina-afip.md) | Destekleniyor |
| [ARGENTINA FACTURA ELECTRONICA](../supported-electronic-documents/argentina-factura-electronica.md) | Destekleniyor |

### 🇧🇷 Brezilya

| Standart | Durum |
|---|---|
| [BRAZIL NF-E](../supported-electronic-documents/brazil-nfe.md) | Destekleniyor |
| [BRAZIL NFC-E](../supported-electronic-documents/brazil-nfce.md) | Destekleniyor |
| [BRAZIL CT-E](../supported-electronic-documents/brazil-cte.md) | Destekleniyor |
| [BRAZIL NFS-E](../supported-electronic-documents/brazil-nfse.md) | Destekleniyor |

### 🇨🇴 Kolombiya

| Standart | Durum |
|---|---|
| [DOCUMENTO SOPORTE](../supported-electronic-documents/colombia-dian.md) | Destekleniyor |
| [FACTURA ELECTRONICA](../supported-electronic-documents/colombia-dian.md) | Destekleniyor |

### 🇩🇰 Danimarka

| Standart | Durum |
|---|---|
| [OIOUBL 2.1](../supported-electronic-documents/denmark-oioubl.md) | Destekleniyor |

### 🇪🇨 Ekvador

| Standart | Durum |
|---|---|
| [FACTURA ELECTRONICA](../supported-electronic-documents/ecuador-sri.md) | Destekleniyor |
| [SRI](../supported-electronic-documents/ecuador-sri.md) | Destekleniyor |
| [SRI 1.0.0](../supported-electronic-documents/ecuador-sri.md) | Destekleniyor |
| [SRI 1.1.0](../supported-electronic-documents/ecuador-sri.md) | Destekleniyor |
| [SRI 2.0.0](../supported-electronic-documents/ecuador-sri.md) | Destekleniyor |
| [SRI 2.1.0](../supported-electronic-documents/ecuador-sri.md) | Destekleniyor |

### 🇪🇸 İspanya

| Standart | Durum |
|---|---|
| [Facturae](../supported-electronic-documents/spain-facturae.md) | Destekleniyor |
| [Facturae 3.2](../supported-electronic-documents/spain-facturae.md) | Destekleniyor |
| [Facturae 3.2.1](../supported-electronic-documents/spain-facturae.md) | Destekleniyor |
| [Facturae 3.2.2](../supported-electronic-documents/spain-facturae.md) | Destekleniyor |

## Desteklenen Formatlar

DocBits aşağıdaki e-fatura formatlarını destekler:

* **FatturaPA**
* **PEPPOL BIS Billing 3.0**
* **Factur-X Basic**
* **EDIFACT INVOIC02**
* **ZUGFeRD 1.0**
* **ZUGFeRD 2.1** 
* **ZUGFeRD 2.3** 
* **XRechnung UBL 1.2**
* **XRechnung UBL 2.1**
* **XRechnung UBL 3.0**

## Beklenen Özelleştirme Kimlikleri

Desteklenen her format için aşağıdaki Özelleştirme Kimlikleri gereklidir:

* **PEPPOL BIS Billing 3.0**
  Beklenen Özelleştirme Kimliği:

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0</cbc:CustomizationID>
```

* **Factur-X Basic**
  Beklenen ram Kimliği:

```xml
<ram:ID>urn:cen.eu:en16931:2017#compliant#urn:factur-x.eu:1p0:basic</ram:ID>
```

* **ZUGFeRD 1.0**
  Beklenen ram Kimliği:

```xml
<ram:ID>urn:ferd:CrossIndustryDocument:invoice:1p0:
```

* **ZUGFeRD 2.1** 
  Beklenen ram Kimlikleri:

```xml
urn:factur-x.eu:1p0:basic</ram:ID>
urn:factur-x.eu:1p0:basicwl</ram:ID>
<ram:ID>urn:cen.eu:en16931:2017</ram:ID>
urn:factur-x.eu:1p0:extended</ram:ID>
urn:factur-x.eu:1p0:minimum</ram:ID>
<ram:ID>urn:cen.eu:en16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_2.1</ram:ID>
```

* **ZUGFeRD 2.3**
  Beklenen ram Kimliği:

```xml
urn:zugferd:2p1:comfort
urn:zugferd:2p1:en16931
urn:zugferd:2p1:extended
urn:zugferd:2p1:basic
```

* **XRechnung UBL 1.2**
  Beklenen Özelleştirme Kimliği:

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_1.X</cbc:CustomizationID>
```

<pre class="language-xml"><code class="lang-xml"><strong> &#x3C;cbc:CustomizationID>urn:cen.eu:de16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_1.X&#x3C;/cbc:CustomizationID>
</strong></code></pre>

* **XRechnung UBL 2.1**
  Beklenen Özelleştirme Kimliği:

<pre class="language-xml"><code class="lang-xml"><strong>&#x3C;cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_2.X&#x3C;/cbc:CustomizationID>
</strong></code></pre>

<pre class="language-xml"><code class="lang-xml"><strong>    &#x3C;cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_2.X&#x3C;/cbc:CustomizationID>
</strong></code></pre>

* **XRechnung UBL 3.0**
  Beklenen Özelleştirme Kimliği:

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.X</cbc:CustomizationID>

```

*   **EDIFACT INVOIC02**

    Beklenen Kimlik:

```xml
<INVOIC02>
```

## Yaklaşan Uygulama Yol Haritası

{% content-ref url="roadmap.md" %}
[roadmap.md](roadmap.md)
{% endcontent-ref %}
