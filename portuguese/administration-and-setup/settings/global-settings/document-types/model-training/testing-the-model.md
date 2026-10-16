# Testando o modelo

## Etapas para executar testes de classificação para avaliar a precisão e a prontidão operacional do modelo

Para testar o modelo treinado e avaliar sua precisão e prontidão operacional, você pode seguir as etapas abaixo:



**Preparação dos dados de teste:**

* Colete uma amostra representativa de dados de teste cobrindo diferentes tipos de documentos e cenários que o modelo encontrará em campo. Certifique-se de que os dados de teste sejam de alta qualidade e estejam rotulados corretamente.



**Execução dos testes de classificação:**

* Execute os testes de classificação nos dados de teste preparados.
* Alimente o modelo com os dados de teste e deixe que ele faça previsões para classificar os documentos.

<figure><img src="../../../../../.gitbook/assets/docbits_remove_user_access.png" alt="Docbits Remove User Access" width="375"><figcaption><p>Configuração</p></figcaption></figure>

* Adicione uma nova regra de classificação ou edite uma existente.

<figure><img src="../../../../../.gitbook/assets/docbits_confirm_user_removal.png" alt="Docbits Confirm User Removal"><figcaption><p>Configurações: Classificação e Extração</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/docbits_save_user_changes.png" alt="Docbits Save User Changes" width="276"><figcaption><p>Configurar Regra de Classificação</p></figcaption></figure>

**Avaliação da precisão do modelo:**

* Compare as previsões do modelo com as classificações reais dos dados de teste. Calcule métricas como exatidão, precisão, recall e pontuação F1 para avaliar o desempenho do modelo. Essas métricas fornecem informações sobre o quão bem o modelo classificou os documentos e o quão confiável ele é.

<figure><img src="../../../../../.gitbook/assets/docbits_model_training_metrics.png" alt="Docbits Model Training Metrics"><figcaption></figcaption></figure>



**Análise de erros:**

* Examine os erros cometidos pelo modelo ao classificar os dados de teste e analise suas causas. Identifique padrões ou tendências nos erros e, se necessário, faça ajustes no modelo para melhorar seu desempenho.



**Otimização do modelo:**

* Com base nos resultados dos testes de classificação e da análise de erros, você pode otimizar o modelo adicionando dados de treinamento, ajustando os parâmetros de treinamento ou alterando a arquitetura do modelo. Repita o processo de teste para verificar se as otimizações melhoraram o desempenho do modelo.



**Documentação dos resultados:**

* Documente os resultados dos testes de classificação e quaisquer ajustes ou otimizações feitos no modelo. Isso o ajudará a acompanhar o progresso do modelo ao longo do tempo e garantirá que ele esteja em constante aprimoramento.

Ao executar regularmente testes de classificação e avaliar o desempenho do seu modelo, você pode garantir que ele seja adequado para uso em produção e forneça resultados precisos.
