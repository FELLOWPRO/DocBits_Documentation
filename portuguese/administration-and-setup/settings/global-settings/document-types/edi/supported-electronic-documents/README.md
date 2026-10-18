---
description: "Identifique a família eDocs, a sintaxe, a versão e o perfil configurados antes de testar o processamento de documentos."
---

# Formatos, versões e guias por país para eDocs

Comece pelo documento de origem e pelo guia do país correspondente. O nome de um país, por si só, não identifica um formato de ficheiro. Uma designação de versão, uma sintaxe XML e um perfil de negócio descrevem aspetos diferentes.

{% hint style="info" %}
As tabelas registam uma verificação do catálogo de desenvolvimento realizada em 17 de outubro de 2026 e o código de processamento correspondente. Descrevem as regras e os componentes de configuração disponíveis; não certificam todos os ficheiros, requisitos legais ou implementações em produção. A sua organização pode sobrepor-se às predefinições.
{% endhint %}

## Interpretar corretamente a matriz de suporte

- Família: o formato de documento eletrónico, como XRechnung, Factur-X, KSeF ou CFDI.
- Sintaxe: o conteúdo efetivo, como XML UBL, XML CII ou um PDF com XML incorporado. Um PDF digitalizado, uma exportação JSON ou uma imagem de código QR não equivalem a um conteúdo XML.
- Versão: a edição da publicação ou do esquema declarada no documento. Uma designação genérica de família não comprova o suporte de todas as versões.
- Perfil: um subconjunto de requisitos de negócio ou de dados, como BASIC, EN16931, EXTENDED ou autofaturação. Um perfil não é uma versão da publicação.
- Regra e componentes: a classificação, Transformation, Preview e Extraction Paths são elementos distintos. Um perfil configurado não tem necessariamente uma regra de classificação própria.
- Validação e transmissão: apresentar ou extrair dados de um ficheiro não verifica, por si só, todas as regras legais, assinaturas, aprovações fiscais ou entregas através da rede.

## Guias por país

| País / região | Famílias e âmbito das versões | Resultado no catálogo |
| --- | --- | --- |
| [Áustria](countries/austria.md) | ebInterface 4.3, 5.0, 6.0 e 6.1 têm entradas distintas. | Entradas encontradas |
| [Dinamarca](countries/denmark.md) | OIOUBL 2.1 é a entrada dinamarquesa identificada. | Entradas encontradas |
| [Finlândia](countries/finland.md) | Finvoice 1.3, 2.0, 2.01 e 3.0 têm entradas distintas. TEAPPSXML é outra família. | Entradas encontradas |
| [França](countries/france.md) | Factur-X tem entradas genéricas e específicas de cada edição, incluindo 1.0.05, 1.08 e 1.09. VRBL FR CIUS 1.0 é uma entrada distinta. | Entradas encontradas |
| [Alemanha](countries/germany.md) | XRechnung tem treze designações de versão, de 1.0 a 3.0.2, cada uma em CII e UBL. ZUGFeRD inclui perfis antigos e entradas 2.5 em CII e UBL. | Entradas encontradas |
| [Itália](countries/italy.md) | FatturaPA é a família italiana configurada. | Entradas encontradas |
| [Países Baixos](countries/netherlands.md) | SI-UBL 2.0 tem uma entrada dedicada. | Entradas encontradas |
| [Noruega](countries/norway.md) | EHF Invoice 3.0 está listado juntamente com EHF Order, Order Response e Despatch Advice. | Entradas encontradas |
| [Polónia](countries/poland.md) | KSeF tem entradas genéricas, FA2 e FA3. | Entradas encontradas |
| [Eslovénia](countries/slovenia.md) | e-SLOG 1.6 e 2.0 têm entradas distintas. | Entradas encontradas |
| [Espanha](countries/spain.md) | Facturae tem entradas genéricas, 3.2, 3.2.1 e 3.2.2. | Entradas encontradas |
| [Suécia](countries/sweden.md) | Svefaktura 1.0 é a entrada sueca identificada. | Entradas encontradas |
| [Austrália](countries/australia.md) | PINT A-NZ tem entradas de regras para faturas e notas de crédito partilhadas com a Nova Zelândia. | Entradas encontradas |
| [Nova Zelândia](countries/new-zealand.md) | PINT A-NZ tem entradas de regras para faturas e notas de crédito partilhadas com a Austrália. | Entradas encontradas |
| [Índia](countries/india.md) | India GST E-Invoice e GST CreditNote têm entradas distintas. | Entradas encontradas |
| [Indonésia](countries/indonesia.md) | Indonesia E-Faktur é a família configurada. | Entradas encontradas |
| [China](countries/china.md) | O catálogo inclui Fapiao, E-Fapiao, General VAT Invoice e Special VAT Invoice. | Entradas encontradas |
| [Japão](countries/japan.md) | JP PINT e JP PINT Self-Billing são entradas distintas. | Entradas encontradas |
| [Coreia do Sul](countries/korea.md) | Korea E-Tax Invoice e Korea NTS são famílias configuradas. | Entradas encontradas |
| [Malásia](countries/malaysia.md) | MyInvois tem entradas de regras para faturas e notas de crédito. | Entradas encontradas |
| [Filipinas](countries/philippines.md) | Philippines EIS é a família configurada. | Entradas encontradas |
| [Singapura](countries/singapore.md) | InvoiceNow tem entradas para faturas e notas de crédito; InvoiceNow SG é outra designação configurada. | Entradas encontradas |
| [Taiwan](countries/taiwan.md) | Taiwan eGUI é a família configurada. | Entradas encontradas |
| [Tailândia](countries/thailand.md) | Thailand E-Tax Invoice é a família configurada. | Entradas encontradas |
| [Vietname](countries/vietnam.md) | Vietnam E-Invoice é a família configurada. | Entradas encontradas |
| [Argentina](countries/argentina.md) | Argentina AFIP e Factura Electronica são designações configuradas. | Entradas encontradas |
| [Brasil](countries/brazil.md) | O Brasil tem entradas NF-e, NFC-e, CT-e, NFS-e e SPED NFS-e. NFS-e inclui as versões 1.00 e 2.00 a 2.04; SPED inclui 1.00.02 e 1.01. | Entradas encontradas |
| [Chile](countries/chile.md) | Chile DTE tem entradas para faturas, notas de crédito e guias de expedição. | Entradas encontradas |
| [Colômbia](countries/colombia.md) | Colombia Factura Electronica e Documento Soporte têm entradas distintas. | Entradas encontradas |
| [Costa Rica](countries/costa-rica.md) | A documentação anterior menciona a Costa Rica, mas não foi encontrada nenhuma entrada de classificação ou de configuração correspondente no catálogo de desenvolvimento examinado. | Não confirmado |
| [Equador](countries/ecuador.md) | Ecuador SRI tem entradas genéricas, 1.0.0, 1.1.0, 2.0.0 e 2.1.0. A retenção na fonte é um tipo de documento distinto. | Entradas encontradas |
| [México](countries/mexico.md) | Mexico CFDI 3.3 e 4.0 têm entradas distintas. | Entradas encontradas |
| [Paraguai](countries/paraguay.md) | Paraguay DTE, SIFEN e SIFEN 150 são designações configuradas. | Entradas encontradas |
| [Peru](countries/peru.md) | Peru CPE tem entradas genéricas, UBL 2.0 e UBL 2.1. Factura Electronica é outra designação. | Entradas encontradas |
| [Uruguai](countries/uruguay.md) | Uruguay CFE tem entradas genéricas, 24 e 25. E-Factura e E-Nota Credito também estão listadas. | Entradas encontradas |
| [Cazaquistão](countries/kazakhstan.md) | Kazakhstan ESF é a família configurada. | Entradas encontradas |
| [Arábia Saudita](countries/saudi-arabia.md) | ZATCA Fatoorah, Reporting, Simplified e Tax Invoice têm entradas distintas. | Entradas encontradas |
| [Turquia](countries/turkey.md) | Turkey E-Fatura e E-Arsiv são famílias configuradas distintas. | Entradas encontradas |
| [Emirados Árabes Unidos](countries/united-arab-emirates.md) | UAE VAT Invoice é a designação configurada. | Entradas encontradas |
| [Internacional](countries/international.md) | As entradas internacionais incluem Peppol BIS 3.0, UBL 2.1, CII puro, EDI, INVOIC02, cXML, OCI, BOD e SPS Commerce RSX 7.7.4. | Entradas encontradas |

## Factur-X / ZUGFeRD: não inventar uma versão da publicação

Um Guideline ID CII harmonizado pode identificar uma família e um perfil, embora várias edições partilhem o mesmo marcador 1p0. Factur-X XMP Version 1.0 é um marcador de esquema, não uma edição da publicação como 1.08 ou 1.09. O XMP do ZUGFeRD pode declarar a sua versão. Se não existirem metadados fiáveis, mantenha o resultado da família genérica e confirme o ficheiro original com o remetente.

MINIMUM e BASIC WL podem omitir informações de linhas de detalhe necessárias nas etapas seguintes. BASIC, EN16931/COMFORT e EXTENDED oferecem diferentes coberturas de dados. Um perfil mais abrangente pode incluir campos que o seu mapeamento de extração não utiliza. Verifique os campos obrigatórios com exemplos reais.

## Verificar um formato na sua organização

1. Conserve o XML original ou o PDF com o XML incorporado. Consulte o espaço de nomes, o esquema ou o identificador de personalização e a versão ou o perfil declarados.

2. Abra Definições → Tipos de documento → E-Doc para o documento de negócio aplicável. Procure o formato de documento eletrónico exato indicado no guia.

3. Verifique a origem efetiva, Default ou Custom, e a respetiva versão de configuração ativa. Examine Transformation, Preview e Extraction Paths. Guardar um rascunho não o ativa.

4. Teste ficheiros de origem representativos de cada sintaxe, versão e documento de negócio de que necessita. Verifique os campos principais, os montantes, os impostos, a classificação como fatura ou nota de crédito e a exportação para o ERP.

5. Confirme separadamente a política de validação e a transmissão. Preserve os mapeamentos personalizados e verifique as aprovações e o histórico de exportação antes de reiniciar documentos existentes.

[Verificações de aceitação](../credit-note-recognized-as-invoice.md)
