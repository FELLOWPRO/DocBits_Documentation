# Ignorar a extração de XML de PDFs híbridos

### Visão geral

A configuração **Ignorar a extração de XML de PDFs híbridos** (Skip Hybrid PDF XML Extraction) controla como o DocBits processa **PDFs híbridos** — faturas em PDF que contêm uma fatura eletrônica estruturada incorporada (ZUGFeRD / Factur-X). Ela decide se o **XML estruturado dentro do PDF** é o documento condutor para o processamento automático, ou se o **próprio PDF** é processado por OCR como documento principal.

Esta configuração é especialmente relevante para **clientes dos EUA**. Ao contrário da UE/Alemanha, os Estados Unidos não têm uma obrigação geral de faturação eletrônica B2B, portanto as organizações dos EUA geralmente desejam que o PDF seja tratado como a fatura principal e legível por humanos — mesmo quando uma contraparte envia um arquivo ZUGFeRD/Factur-X com XML incorporado.

### O que faz?

Um arquivo ZUGFeRD/Factur-X é um único PDF que também contém uma fatura XML legível por máquina. Por padrão, o DocBits detecta esse XML incorporado e o utiliza como fonte condutora para a extração (fluxo eletrônico estruturado).

* **Desativada (padrão)** — O DocBits detecta o XML da fatura eletrônica incorporado e processa o documento pelo **fluxo eletrônico estruturado**. O XML é a fatura condutora. Este é o comportamento juridicamente correto para a UE/Alemanha, onde a fatura eletrônica estruturada é a fatura relevante e o PDF é apenas uma visualização / cópia de leitura.
* **Ativada** — O DocBits **ignora o XML incorporado** e encaminha o documento para o **processador de PDF (OCR)**. O PDF torna-se o documento de processamento principal. Esta é a escolha típica para **organizações dos EUA** que desejam um processamento centrado no PDF.

{% hint style="info" %}
Esta configuração afeta apenas os **PDFs híbridos** (ZUGFeRD / Factur-X = um `.pdf` com XML incorporado). Um arquivo XRechnung/EDI puro carregado como `.xml` é sempre processado pelo fluxo eletrônico estruturado — não há PDF que possa se tornar o documento principal.
{% endhint %}

### Auditoria e conformidade — o original é sempre preservado

Ativar esta configuração **não descarta** a fatura eletrônica. O artefato original é sempre preservado:

* O **PDF** ZUGFeRD/Factur-X original — **incluindo seu XML incorporado — permanece armazenado** e disponível para download. Nada é excluído da cópia armazenada do documento.
* O processamento altera apenas **qual conteúdo conduz a extração** (PDF/OCR versus XML incorporado), não o que é arquivado.

Assim, uma organização dos EUA pode processar o PDF como principal enquanto a fatura eletrônica estruturada permanece disponível para auditoria.

{% hint style="warning" %}
Para organizações da UE/Alemanha, deixe esta configuração **desativada**. De acordo com as regras de faturação eletrônica de 2025, uma fatura eletrônica estruturada (ZUGFeRD/Factur-X, XRechnung) é a fatura juridicamente relevante; um PDF simples é apenas uma cópia de leitura. Processar o PDF como principal em vez dos dados estruturados não é apropriado quando há uma fatura eletrônica válida presente.
{% endhint %}

### Como usar

1. **Abrir a configuração**:
   * Vá para **Configurações**.
   * Selecione **Processamento de Documentos**.
   * Selecione **Módulo**.
   * Abra a seção **Tipo de Documento**.
   * Encontre **Ignorar a extração de XML de PDFs híbridos** e acione o botão.
2. **Escolher o modo**:
   * **Organizações dos EUA / centradas em PDF** → ative o botão para que os PDFs ZUGFeRD/Factur-X sejam processados por OCR como documento principal.
   * **Organizações da UE/Alemanha** → deixe o botão desativado para que a fatura eletrônica estruturada continue sendo o documento condutor.
3. **Verificar**:
   * Carregue um PDF ZUGFeRD/Factur-X e verifique o resultado do processamento — com o botão ativado, ele é tratado como um PDF comum (OCR); com ele desativado, os dados da fatura eletrônica incorporada são extraídos.

### Quando usar este recurso

* **Clientes dos EUA / sem obrigação de fatura eletrônica**: ative-o para que o PDF habitual seja o documento de processamento principal enquanto a fatura eletrônica incorporada permanece arquivada.
* **Fluxos de trabalho mistos/centrados em PDF**: ative-o quando os processos posteriores, a validação ou a revisão dependerem do layout do PDF em vez do XML.
* **Conformidade UE/Alemanha**: deixe-o desativado para que os dados estruturados da fatura eletrônica conduzam o processamento, conforme exigido.
