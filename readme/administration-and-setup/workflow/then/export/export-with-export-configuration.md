# Exportar com configuração de exportação

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-10e6b7590bc6-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados.</p></figcaption></figure>

## **Objetivo:**

O cartão de fluxo de trabalho **"Exportar documento com configuração de exportação"** foi projetado para exportar um documento usando uma configuração de exportação especificada. Ele fornece flexibilidade para ignorar quaisquer tarefas pendentes associadas ao documento, garantindo um processo de exportação tranquilo, independentemente do seu estado atual.

## **Componentes do cartão:**

1. **Exportar configuração**
   * **Descrição**: Especifica a configuração de exportação a ser usada para processar o documento.
   * **Detalhe**: Esta configuração determina o formato, estrutura e destino do documento exportado.
2. **Ignorar tarefas pendentes**
   * **Descrição**: Determina se as pendências vinculadas ao documento devem ser desconsideradas durante o processo de exportação.
   * **Opções**:
     * **True**: Exporta o documento independentemente das tarefas pendentes.
     * **False**: Garante que as tarefas pendentes sejam concluídas antes da exportação.

## **Funcionalidade:**

* **Avaliação de Condição**: O sistema avalia as condições definidas em **"Quando"** e **"E Seções"** do fluxo de trabalho. Se ambas as condições forem verdadeiras, o processo de exportação será iniciado.
* **Exportação de Documento**: Usando a **Configuração de Exportação** especificada, o documento é processado e exportado no formato e destino definidos.
* **Tratamento de tarefas pendentes**: Se **Ignorar tarefas pendentes** estiver definido como **True**, o processo de exportação ignora quaisquer tarefas pendentes vinculadas ao documento. Se definido como **False**, tarefas pendentes podem impedir a exportação. Resolva-os e organize o gatilho de fluxo de trabalho pretendido ou tente novamente.

## **Instalação e configuração:**

Para configurar este cartão, os usuários precisam:

1. Selecione a **Configuração de Exportação** desejada para definir como o documento será exportado.
2. Escolha se deseja **Ignorar tarefas pendentes** definindo o valor como **True** ou **False.**
3. Certifique-se de que as condições nas seções **"Quando"** e **"E"** estejam definidas corretamente, pois a carta só executa sua ação quando essas condições são verdadeiras.

## **Conclusão:**

O cartão de fluxo de trabalho **"Exportar documento com configuração de exportação"** garante que os documentos sejam exportados de forma eficiente e de acordo com configurações predefinidas. Com capacidade de ignorar tarefas pendentes, este cartão oferece flexibilidade no tratamento de documentos em diversas etapas, reduzindo atrasos e agilizando o processo de exportação.

## Versões atuais e tarefas pendentes

Na v3, escolha também **Status após exportação**: `finished` fecha o documento após uma exportação bem-sucedida; `exported` deixa-o aberto para processamento posterior. Versões anteriores mantêm `finished`. Uma seleção ausente é padronizada como `finished`; uma seleção inválida é rejeitada.

Se as tarefas abertas impedirem a exportação, o cartão informa a recusa. Resolva as tarefas e organize o gatilho pretendido ou tente novamente; a espera e a retomada automáticas não são garantidas por este cartão. O cartão de exportação em fila separado coleta uma configuração para exportação final no final da execução. Consulte [Exportar cartões e status dos resultados](../../cards-overview/export-cards-guide.md).

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Escolha uma configuração de exportação específica para um documento validado.

**Configuração:** Selecione o exportador de demonstração configurado e defina Ignorar tarefas pendentes como `false`. Use um documento com uma tarefa aberta e, em seguida, um teste separado sem tarefas abertas.

**Resultado esperado e contra-exemplo:** O caso de tarefa aberta não deve ser assumido para ser retomado automaticamente. Após resolver a tarefa, acione novamente a exportação pretendida e verifique o resultado do exportador e o status suportado.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
