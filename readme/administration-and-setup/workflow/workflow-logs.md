# Registos do Fluxo de Trabalho

## **Visão Geral**

Os **Registos do Fluxo de Trabalho** permitem aos usuários analisar quais fluxos de trabalho foram executados para um documento, entender os resultados da execução e aprofundar-se nos detalhes do nível de condição para depuração ou validação.

## **Acessando os Registos do Fluxo de Trabalho**

Para acessar os registos do fluxo de trabalho:

1. Navegue até o **Dashboard**.
2. Clique no **menu de Ações** (ícone de três pontos) ao lado do documento desejado.
3. Selecione **Registos do Fluxo de Trabalho** no menu.
   * <mark style="color:red;">**Nota**</mark>**:** O recurso de workflow deve estar ativado para acessar esta opção.
4.  Um **painel lateral** é aberto mostrando um resumo dos fluxos de trabalho executados.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAlgg3jnSVRVyuYxy4tAp%252Fimage.png%3Falt%3Dmedia%26token%3D4e8fcd63-6113-47eb-95a4-95a7821dc9b9\&width=768\&dpr=4\&quality=100\&sign=9e6ba9f5\&sv=2)

## **Componentes do Painel de Registos do Fluxo de Trabalho**

#### **1. Contadores de Resumo do Fluxo de Trabalho**

Localizados no topo do painel de registos:

* **Azul**: Número total de fluxos de trabalho executados.
* **Vermelho**: Fluxos de trabalho que terminaram em **erros**.
* **Amarelo**: Fluxos de trabalho que **não foram concluídos** devido a incompatibilidades de condição.
* **Verde**: Fluxos de trabalho **executados** com sucesso.

#### **2. Tabela de Execução do Fluxo de Trabalho**

Cada linha na tabela representa uma execução de fluxo de trabalho e inclui:

* **Nome do Fluxo de Trabalho**
* **Timestamp** (Criado Em)
* **Tempo de Execução** (em segundos)
* **Ícone de Resultado**:
  * Marca de seleção verde: Fluxo de trabalho executado com sucesso.
  * Cruz vermelha: Fluxo de trabalho executado com um erro.
  * Traço laranja: A execução foi interrompida devido a uma condição não atendida.

Ao clicar na **seta** à esquerda de cada linha, expande-se a **visualização detalhada do fluxo de trabalho**.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="" width="563"><figcaption></figcaption></figure></div>

### **Visualização Detalhada do Fluxo de Trabalho**

Ao clicar em uma linha de fluxo de trabalho específica, abre-se o **registo de execução detalhado**, mostrando:

#### **Avaliação de Condição**

* Bloco **Quando...**: Condição inicial.
* Bloco(s) **E...**: Condições adicionais.
* Bloco(s) **Então...**: Ações realizadas quando todas as condições são atendidas.

Cada linha de condição mostra:

* Marca de seleção **verde**: Condição foi atendida.
* Traço laranja: Condição não foi atendida.
* Cruz vermelha: Condição falhou **devido a um erro**

### **Nota Comportamental Importante**

Se uma condição em um fluxo de trabalho **não for atendida**, o sistema **para de avaliar quaisquer outras cartas de fluxo de trabalho** dentro desse fluxo de trabalho. Esse comportamento evita processamento desnecessário. Como indicador visual, a carta que **não atendeu à sua condição** é mostrada em **cinza**, e todas as **cartas subsequentes** no mesmo fluxo de trabalho também aparecerão **cinza**, indicando que elas **não foram executadas**.
