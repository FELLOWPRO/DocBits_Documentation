---
description: DocBits'te BRAZIL CT-E elektronik belge desteği
---

# 🇧🇷 BRAZIL CT-E

| Özellik | Değer |
|---------|-------|
| **Ülke / Bölge** | Brezilya |
| **Belge Türleri** | Taşıma Faturası (Conhecimento de Transporte Eletrônico) |
| **Format** | XML |
| **Standart** | CT-e 3.0 (elektronik yük/nakliye konşimentosu) |
| **Yerel Ayar** | `pt_BR` |

CT-e (Conhecimento de Transporte Eletrônico, `<mod>57</mod>`), lojistik ve nakliye şirketleri tarafından düzenlenen Brezilya elektronik taşıma belgesidir. Taşıma hizmetini, kargo değerini, menşe ve varış belediyelerini (`cMunIni` / `cMunFim`) ve navlun fiyatını (`vTPrest`) belgelemektedir. NF-e'den farklı olarak CT-e, kök öğe olarak `cteProc` kullanır ve ilişkili NF-e belgelerine referans verir.

## Destek Durumu

| Bileşen | Durum |
|---------|-------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarımı | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="brazil-cte-preview.png" alt="DocBits'te Brazil CT-e önizlemesi"><figcaption><p>BRAZIL CT-E belgesi için varsayılan DocBits önizlemesi</p></figcaption></figure>

## Alan Eşlemesi

### Başlık Alanları

| DocBits Alanı | Kaynak XPath | Notlar |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nCT']` | CT-e numarası |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | BRT ofseti ile ISO 8601 |
| `currency` | Sabit: `BRL` | Her zaman Brezilya Reali |
| `total_amount` | `//*[local-name()='vPrest']/*[local-name()='vTPrest']` | Toplam nakliye hizmeti değeri |
| `net_amount` | `//*[local-name()='vPrest']/*[local-name()='vRec']` | Tahsil edilecek tutar |
| `tax_amount` | `//*[local-name()='ICMS']//*[local-name()='vICMS']` | Taşıma hizmetine uygulanan ICMS |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Taşıyıcı (transportadora) adı |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` | Taşıyıcı CNPJ |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Konsinyatör (destinatário) adı |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CNPJ']` | Konsinyatör CNPJ |

> CT-e, kalem satırı tablosu içermez — taşıma hizmeti belge düzeyinde tek bir ücret olarak ifade edilir.

## Sınıflandırma Kuralı

DocBits, BRAZIL CT-E belgelerini XML ad alanındaki şu ifade aracılığıyla tespit eder:

```
http://www.portalfiscal.inf.br/cte
```

(kök öğe `<cteProc>`).

## İlgili Belgeler

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Desteklenen Elektronik Belgeler](./)
