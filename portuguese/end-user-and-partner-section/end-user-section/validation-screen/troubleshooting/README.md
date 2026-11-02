# Solução de problemas

Se um valor estiver ausente na tela de validação, verifique primeiro se o texto está visível no documento e se o DocBits o reconheceu. Isso ajuda a distinguir um problema de leitura de um problema de campo ou de regra.

1. Abra o documento afetado em **Validation**.
2. Compare o documento original com a **OCR view**. Verifique a mesma página e a mesma área em que o valor deveria aparecer.
3. Se o texto estiver ausente na OCR view, siga [Texto ausente na extração OCR](missing-text-in-ocr-extraction.md).
4. Se o texto estiver presente na OCR view, mas o campo continuar vazio, peça a um administrador que verifique a configuração dos campos do tipo de documento. Informe o tipo de documento, o nome do campo, a página e um exemplo de teste seguro.

<figure><img src="../../../../.gitbook/assets/dbdc238-validation-ocr-en.png" alt="OCR view em inglês de uma fatura sintética em Validation"><figcaption>OCR view atual em inglês no Sandbox de uma fatura sintética Test A. O exemplo serve apenas para orientação; ele não mostra uma falha de extração.</figcaption></figure>

Não inclua documentos de clientes nem dados pessoais em uma captura de tela enviada ao suporte. A [visão geral da Tela de Validação](../README.md) explica os principais controles caso você seja novo nesta tela.
