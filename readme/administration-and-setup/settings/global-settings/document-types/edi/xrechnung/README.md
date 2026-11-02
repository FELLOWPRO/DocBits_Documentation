# Visão geral do XRechnung

## Introdução

XRechnung é um padrão alemão de faturação eletrónica concebido para a administração pública. Baseia-se na norma europeia EN 16931 e existe em dois formatos técnicos: **UBL** (Universal Business Language) e **CII** (Cross Industry Invoice).

O DocBits oferece suporte total para XRechnung, permitindo a extração de dados estruturados e a exportação perfeita para sistemas Infor ERP.

## Versões do XRechnung suportadas (CII)

O DocBits suporta as seguintes versões de XRechnung CII:

* [XRechnung 1.2](versions/xrechnung-1-2.md)
* [XRechnung 2.1](versions/xrechnung-2-1.md)
* [XRechnung 3.0](versions/xrechnung-3-0.md)
* [XRechnung 3.0.1](versions/xrechnung-3-0-1.md)
* [XRechnung 3.0.2](versions/xrechnung-3-0-2.md)

## Fluxo de dados

O fluxo de dados de um documento XRechnung para o seu sistema ERP segue estes passos:

1. **Extração**: o DocBits interpreta os dados XML de acordo com a versão e o formato XRechnung (CII ou UBL).
2. **Mapeamento de campos do DocBits**: os dados extraídos são mapeados para os campos padrão do DocBits.
3. **Alinhamento com o ERP**: os campos do DocBits são mapeados para os campos Infor BOD (Business Object Document), normalmente através do BOD `SyncSupplierInvoice`.
4. **Exportação**: os dados mapeados são exportados para o sistema Infor.

## Padrões de mapeamento

O mapeamento baseia-se nas seguintes normas:
* **UN/CEFACT CII**: base da estrutura XML do XRechnung CII.
* **OAGIS/OASIS**: norma dos BODs da Infor.
* **EN 16931**: norma europeia de faturação eletrónica.

## Guias por país

Consulte os guias por país para obter as designações exatas dos formatos, a sintaxe, os limites das versões e o estado da configuração examinada. [Formatos, versões e guias por país para eDocs](../supported-electronic-documents/README.md).
