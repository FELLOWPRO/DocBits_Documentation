# Editando e Salvando Padrões Regex

## Guia para modificar padrões existentes e a importância de testar essas alterações para garantir que funcionem conforme o esperado sem quebrar a funcionalidade existente.

**Para editar padrões regex existentes e garantir que as alterações funcionem conforme o esperado sem quebrar a funcionalidade existente, você pode seguir o guia abaixo:**

<figure><img src="../../../../../.gitbook/assets/docbits_regex_edit_settings.png" alt="Docbits Regex Edit Settings"><figcaption><p>Configurações: Tipo de Documento</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/docbits_regex_pattern_analysis.png" alt="Docbits Regex Pattern Analysis"><figcaption></figcaption></figure>

**Analise o padrão existente:**

* Examine o padrão regex existente para entender quais dados ele captura e como funciona.
* Identifique as partes do padrão que precisam ser alteradas e o impacto dessas alterações nos dados capturados.

**Por exemplo: O valor da fatura deve ser lido:**

*   (?<=Rechnungsbetrag:)[\s]*((((\d+)[,.]{1,10})+\d{0,2})|(\d+(?!,)))

    Rechnungsbetrag: 100.00
*   Leia o valor com ponto de milhares, mas NÃO passe o ponto

    [\d.]_[\,\d]_

    Caracteres permitidos: 0123456789,
*   O valor "P32180" deve ser lido. A palavra âncora aqui é "Invoice Date".

    (?<=InvoiceDate )[\s]*P\d{5}

    Número do cliente Número da fatura Data da fatura P32180 613976 13/05/2019

<figure><img src="../../../../../.gitbook/assets/docbits_import_start_process.png" alt="Docbits Import Start Process"><figcaption></figcaption></figure>

**Documente as alterações:**

* Faça anotações sobre as alterações que planeja fazer no padrão regex.
* Observe quais novos padrões planeja adicionar e quais partes do padrão existente podem precisar ser alteradas ou removidas.

**Prepare os dados de teste:**

* Colete dados de teste que sejam representativos dos diferentes tipos de dados que o padrão regex normalmente captura.
* Certifique-se de que seus dados de teste cubram casos típicos e extremos para verificar a robustez de suas alterações.

**Faça alterações no padrão regex:**

* Faça as alterações planejadas no padrão regex.
* Isso pode incluir adicionar novos padrões, remover ou ajustar partes existentes ou otimizar o padrão para melhor desempenho.

**Teste as alterações:**

* Aplique o padrão regex atualizado aos seus dados de teste e revise cuidadosamente os resultados.
* Verifique se o padrão ainda captura corretamente os dados desejados e se não há impactos inesperados em outras partes dos dados ou do sistema.

**Depuração e adaptação:**

* Se os resultados do teste não forem os esperados ou ocorrerem problemas inesperados, revise cuidadosamente suas alterações e faça novos ajustes conforme necessário.
* Isso pode incluir reverter certas alterações ou adicionar ajustes adicionais para corrigir o problema.

**Documente as alterações:**

* Atualize a documentação do seu padrão regex para refletir as alterações feitas.
* Descreva os padrões atualizados e os motivos das alterações feitas para ajudar outros desenvolvedores a entender e usar o padrão.

**Salvando as alterações:**

* Quando tiver certeza de que as alterações foram bem-sucedidas e funcionam conforme o esperado, salve o padrão regex atualizado em sua base de código ou arquivos de configuração para garantir que estejam disponíveis para uso futuro.

<figure><img src="../../../../../.gitbook/assets/docbits_model_training_continuous.png" alt="Docbits Model Training Continuous"><figcaption><p>Salvar Alterações</p></figcaption></figure>

Ao seguir estas etapas e testar cuidadosamente as alterações nos padrões regex, você pode garantir que seu padrão regex continue a funcionar corretamente enquanto atende aos novos requisitos.
