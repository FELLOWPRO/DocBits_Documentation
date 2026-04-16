---
description: DocBits'te BRAZIL NFS-E elektronik belge desteği
---

# 🇧🇷 BRAZIL NFS-E

| Özellik | Değer |
|---------|-------|
| **Ülke / Bölge** | Brezilya |
| **Belge Türleri** | Hizmet Faturası (Nota Fiscal de Serviços Eletrônica) |
| **Format** | XML |
| **Standart** | NFS-e 2.04 (belediye hizmet faturaları için ABRASF ulusal standardı) |
| **Yerel Ayar** | `pt_BR` |

NFS-e (Nota Fiscal de Serviços Eletrônica), belediye düzeyinde düzenlenen Brezilya elektronik hizmet faturasıdır. DocBits, ABRASF (Associação Brasileira das Secretarias de Finanças das Capitais) standart şemasını desteklemektedir. NFS-e belgeleri, NF-e'den farklı bir XML yapısı kullanır: ana vergi ICMS yerine ISS (Imposto Sobre Serviços) olup tedarikçi/alıcı `PrestadorServico` / `TomadorServico` olarak adlandırılır. `Discriminacao` öğesi, serbest metin biçiminde hizmet açıklamasını içerir.

## Destek Durumu

| Bileşen | Durum |
|---------|-------|
| Önizleme | ✅ Destekleniyor |
| Alan Çıkarımı | ✅ Destekleniyor |
| Dönüşüm | ✅ Destekleniyor |

## Varsayılan Önizleme

<figure><img src="brazil-nfse-preview.png" alt="DocBits'te Brazil NFS-e önizlemesi"><figcaption><p>BRAZIL NFS-E belgesi için varsayılan DocBits önizlemesi</p></figcaption></figure>

## Alan Eşlemesi

### Başlık Alanları

| DocBits Alanı | Kaynak XPath | Notlar |
|---|---|---|
| `invoice_id` | `//*[local-name()='Numero']` | NFS-e numarası |
| `invoice_date` | `//*[local-name()='DataEmissao']` | ISO 8601 düzenleme tarihi |
| `currency` | Sabit: `BRL` | Her zaman Brezilya Reali |
| `total_amount` | `//*[local-name()='ValorServicos']` | Brüt hizmet değeri |
| `net_amount` | `//*[local-name()='ValorLiquidoNfse']` | Kesintilerden sonra net değer |
| `tax_amount` | `//*[local-name()='ValorIss']` | ISS (belediye hizmet vergisi) |
| `supplier_name` | `//*[local-name()='PrestadorServico']//*[local-name()='RazaoSocial']` | Hizmet sağlayıcı adı |
| `supplier_id` | `//*[local-name()='PrestadorServico']//*[local-name()='Cnpj']` | Sağlayıcı CNPJ |
| `buyer_name` | `//*[local-name()='TomadorServico']//*[local-name()='RazaoSocial']` | Hizmet alan taraf adı |
| `buyer_id` | `//*[local-name()='TomadorServico']//*[local-name()='Cnpj']` | Alan taraf CNPJ |

> NFS-e, kalem satırları yerine `Discriminacao` öğesinde tek bir hizmet açıklamaktadır. `INVOICE_TABLE` çıkarımı yapılmaz.

## Sınıflandırma Kuralı

DocBits, BRAZIL NFS-E belgelerini şu ad alanı aracılığıyla tespit eder:

```
http://www.abrasf.org.br/nfse.xsd
```

## İlgili Belgeler

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL CT-E](brazil-cte.md)
- [Desteklenen Elektronik Belgeler](./)
