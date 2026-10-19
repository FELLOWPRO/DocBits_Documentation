# eSLOG 1.6 e 2.0

**eSLOG 1.6** e **eSLOG 2.0** aparecem como formatos de fatura eletrônica separados no DocBits. Escolha a versão usada pela sua fatura eslovena recebida. As capturas de tela abaixo mostram a interface atual do Sandbox em inglês, em uma organização de teste da documentação; elas não comprovam que uma fatura de qualquer uma das versões foi processada com sucesso.

## Encontre as configurações

1. Vá para **Settings → Document Types → Invoice → E-Doc**.
2. Expanda **E-SLOG 1.6** ou **E-SLOG 2.0**. Cada formato tem suas próprias três entradas.

<figure><img src="../../../../../.gitbook/assets/dbdc-142-eslog-16-en.png" alt="Formato E-SLOG 1.6 do Sandbox em inglês com as linhas Transformation, Preview e Extraction Paths"><figcaption>E-SLOG 1.6 na lista E-Doc de Invoice.</figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc-142-eslog-20-en.png" alt="Formato E-SLOG 2.0 do Sandbox em inglês com as linhas Transformation, Preview e Extraction Paths"><figcaption>O E-SLOG 2.0 tem configurações separadas para as mesmas três etapas.</figcaption></figure>

| Entrada | O que ela controla | Próximo guia |
| --- | --- | --- |
| **TRANSFORMATION (XSLT)** | Converte os dados de origem do formato em XML estruturado. | [Transformation](edi/edi-transformation-file-guide.md) |
| **PREVIEW (XSLT)** | Define a visualização legível do documento. | [Preview](edi/edi-preview-file-guide.md) |
| **EXTRACTION PATHS (JSON)** | Mapeia valores XML para campos e colunas de tabela do DocBits. | [Extraction Paths](edi/edi-extraction-paths-file-guide.md) |

Clique em uma linha para ver suas versões e a configuração. **Default** identifica a entrada fornecida. **Last Modified At** mostra quando essa entrada foi alterada pela última vez. O botão **New** inicia uma entrada de configuração adicional. O menu de três pontos em uma linha padrão oferece **Customize**, que cria uma cópia específica da organização, e **Delete**; revise com atenção a linha selecionada antes de usar Delete.

Dentro de uma configuração, o lápis ao lado de uma versão ativa cria um rascunho. Verifique um rascunho com o painel de teste **Preview** e o ID de um documento representativo enviado antes de ativá-lo com a marca de seleção. O ícone de lixeira de um rascunho remove esse rascunho. Os nomes reais dos campos e os caminhos XML dependem do seu arquivo eSLOG; use o guia correspondente acima para ver os detalhes do editor.
