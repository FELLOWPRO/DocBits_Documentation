# Export with Export Configuration

<figure><img src="../../../../.gitbook/assets/image (284).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

O cartão de fluxo de trabalho **"Export Document with Export Configuration"** foi concebido para exportar um documento utilizando uma configuração de exportação especificada. Oferece a flexibilidade de ignorar quaisquer tarefas pendentes associadas ao documento, assegurando um processo de exportação fluido independentemente do seu estado atual.

## **Componentes do cartão:**

1. **Export Configuration**
   * **Descrição**: Especifica a configuração de exportação a utilizar no processamento do documento.
   * **Detalhe**: Esta configuração determina o formato, a estrutura e o destino do documento exportado.
2. **Ignore Pending Tasks**
   * **Descrição**: Determina se as tarefas pendentes associadas ao documento devem ser ignoradas durante o processo de exportação.
   * **Opções**:
     * **True**: Exporta o documento independentemente das tarefas pendentes.
     * **False**: Assegura que as tarefas pendentes são concluídas antes da exportação.

## **Funcionalidade:**

* **Avaliação da condição**: O sistema avalia as condições definidas nas secções **"Where"** e **"And Sections"** do fluxo de trabalho. Se ambas as condições forem verdadeiras, o processo de exportação é iniciado.
* **Exportação do documento**: Utilizando a **Export Configuration** especificada, o documento é processado e exportado no formato e destino definidos.
* **Tratamento de tarefas pendentes**: Se **Ignore Pending Tasks** estiver definido como **True**, o processo de exportação ignora quaisquer tarefas por concluir associadas ao documento. Se estiver definido como **False**, a exportação é adiada até que todas as tarefas sejam resolvidas.

## **Configuração:**

Para configurar este cartão, os utilizadores precisam de:

1. Selecionar a **Export Configuration** pretendida para definir como o documento será exportado.
2. Escolher se devem **Ignore Pending Tasks** definindo o valor como **True** ou **False.**
3. Assegurar que as condições nas secções **"Where"** e **"And Sections"** estão corretamente definidas, uma vez que o cartão só executa a sua ação quando estas condições forem verdadeiras.

## **Conclusão:**

O cartão de fluxo de trabalho **"Export Document with Export Configuration"** assegura que os documentos são exportados de forma eficiente e de acordo com configurações predefinidas. Com a capacidade de ignorar tarefas pendentes, este cartão oferece flexibilidade no tratamento de documentos em várias fases, reduzindo atrasos e simplificando o processo de exportação.
