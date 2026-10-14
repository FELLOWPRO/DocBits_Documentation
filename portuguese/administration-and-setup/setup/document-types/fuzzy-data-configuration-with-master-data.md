# Configuração de Dados Fuzzy com Dados Mestres

## **Visão Geral**

Cada tipo de documento possui suas próprias configurações padrão e deve ser configurado separadamente. Enquanto este exemplo explica a configuração para **Faturas**, o mesmo processo se aplica a todos os tipos de documentos.

## Para configurar Dados Fuzzy, navegue até:

Configurações → Configurações Globais → Tipos de Documento → Fatura → Campos → Configurações de Dados Mestres → Consultar Dados Mestres

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fhnn2NcPGzVkUO0mLQWTy%252Fimage.png%3Falt%3Dmedia%26token%3De2f87385-fc48-4149-9bef-ca917a7328bd\&width=768\&dpr=4\&quality=100\&sign=116ee1da\&sv=2)

## **Consultas Padrão**

Existem **quatro grupos de consulta padrão** para faturas:

1. **Dados da Empresa**
2. **Cabeçalho do Pedido de Compra**
3. **Fornecedor**
4. **Código de Imposto**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4VxYFu8M62dXi6qGsPl3%252Fimage.png%3Falt%3Dmedia%26token%3Db2bc4690-805b-4b19-aa89-73f315889d88\&width=768\&dpr=4\&quality=100\&sign=835f513a\&sv=2)

Cada grupo contém campos específicos. Clique em um grupo para **expandir** e visualizar os campos. Os grupos de consulta padrão são rotulados com uma **tag "Padrão"**.

## **Status da Configuração de Consulta**

* As **configurações ativas** são marcadas com uma **tag "Ativada"**.
* As **configurações desativadas** são marcadas com uma **tag "Desativada"**.

## **Pré-requisito: Importando Dados Mestres**

Para que os Dados Fuzzy funcionem corretamente, os **dados mestres** relevantes devem ser importados. Sem isso, o sistema não tem dados de referência para usar. Aqui está como importar dados mestres:

{% content-ref url="../../../infor-integration-and-configuration/importing-customer-master-data/" %}
[importing-customer-master-data](../../../infor-integration-and-configuration/importing-customer-master-data/)
{% endcontent-ref %}

## **Gerenciando Grupos de Consulta**

Cada grupo de consulta é **ativado por padrão** mas pode ser modificado clicando nos três pontos:

* **Desativar** → Desativa um grupo. _(Disponível apenas para grupos ativados)_
* **Ativar** → Ativa um grupo. _(Disponível apenas para grupos desativados)_
* **Duplicar** → Cria uma cópia que pode ser modificada sem afetar o original.
* **Visualizar** → Exibe informações como o **tipo de documento** ao qual pertence e a **tabela de consulta** que utiliza. _(Disponível apenas para grupos padrão)_
* **Editar** → Disponível para grupos **não padrão**. Permite modificar detalhes do grupo.
* **Excluir** → Remove o grupo completamente. _(Apenas para grupos não padrão)_

## **Criando uma Nova Configuração de Consulta**

Existem **duas maneiras** de criar uma configuração de consulta:

1.  **Duplicar uma consulta existente**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZUlPcWGrx1oITQS3tgZP%252Fimage.png%3Falt%3Dmedia%26token%3D59fb300d-836e-40d0-84b7-4a405cf7f321\&width=768\&dpr=4\&quality=100\&sign=3442db8f\&sv=2)

    * Isso copia todas as informações e campos de um grupo existente.
    * Você só precisa fornecer um **novo nome**.
2.  **Criar uma consulta do zero**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNbEpo2p5Q8D1d7DUchBF%252Fimage.png%3Falt%3Dmedia%26token%3D401314b5-44d0-47df-b3e6-69fea83cce82\&width=768\&dpr=4\&quality=100\&sign=1d0ce322\&sv=2)

    * Clique em **"Criar Configuração de Consulta"**.
    * Preencha os detalhes necessários:
      * **Nome da Configuração**
      * **Tabela de Consulta** (Tabela de Dados Mestres a ser usada)
      * **Manipulador de Conflito** (Escolha um: Melhor Pontuação, Retornar Nenhum, Retornar Primeiro)
      * **Tipo de Contexto** (Cabeçalho ou Linha) precisa de contexto
      * **Corresponder Todos** (Opção de Checkbox) precisa de contexto

## **Gerenciando Campos Dentro de um Grupo de Consulta**

Cada grupo contém campos que podem ser **adicionados, removidos, editados ou visualizados**, dependendo se são campos padrão ou campos personalizados.

### **Campos Padrão**

*   Marcados com uma **tag "Padrão"**.

    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fh37McVpB0tBo5wqiAttR%252Fimage.png%3Falt%3Dmedia%26token%3Dcabce083-83a5-4881-a64f-88a8757df49b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b3739019&#x26;sv=2" alt="" width="375"></div>
* **Apenas pode ser visualizado**, não editado ou excluído.

### **Campos Não Padrão**

* **Podem ser editados ou excluídos** clicando nos três pontos e selecionando **Editar** ou **Remover**.

### **Adicionando um Novo Campo**

**Nota:** Você pode criar campos dentro de configurações de Consulta padrão.

Para adicionar um novo campo dentro de um grupo:

1.  Clique em **"Criar"** dentro do grupo relevante.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvmIXTEQQHKKNbvTJj1b4%252Fimage.png%3Falt%3Dmedia%26token%3D8569867b-9f5b-4865-90bd-f2e41e846979\&width=768\&dpr=4\&quality=100\&sign=603cb7df\&sv=2)
2. Forneça os seguintes detalhes:
   * **Campo de Consulta** → Nome da coluna da tabela de consulta de dados mestres.
   * **Campo de Validação** → Campo correspondente do DocBits.
   * **Campo Pai** → _(Mais detalhes necessários)_
   * **Operador de Busca** → Escolha um:
     * Inteligente
     * Contém
     * Exato
     * Começa com
     * Termina com
   * **Caixas de Seleção:**
     * **Acionador Automático** → Quando ativado, se outro campo em uma configuração de consulta diferente compartilhar a mesma coluna, este campo será atualizado **automaticamente** sempre que o outro campo for atualizado
     * **Pesquisável** → Ativa o campo como um campo **Fuzzy Data**, permitindo pesquisas na consulta de dados mestres (ícone azul na tela de validação).

## **Última Etapa: Adicionando Campos ao Layout**

Após configurar os campos de Dados Fuzzy, **certifique-se de adicioná-los ao layout usando o Construtor de Layout**. Se os campos não forem adicionados ao layout, eles não estarão disponíveis para uso.

{% content-ref url="../../settings/global-settings/document-types/layout-manager/" %}
[layout-manager](../../settings/global-settings/document-types/layout-manager/)
{% endcontent-ref %}

## **Como o DocBits escolhe um fornecedor**

Quando um documento chega, o DocBits procura o fornecedor nos seus dados mestres. Três definições determinam o resultado. Esta secção explica-as passo a passo, com exemplos.

### **Passo 1 — Que campos são usados na pesquisa**

O DocBits só usa um campo na pesquisa quando ambos os pontos são verdadeiros:

* o campo está marcado como **Pesquisável (Searchable)** ou **Auto Trigger** na configuração de consulta, e
* o campo tem um valor no documento.

A origem do valor não importa. Um campo treinado, um campo preenchido pela IA e um valor escrito por um utilizador são tratados da mesma forma.

{% hint style="warning" %}
**Pesquisável faz duas coisas.** Mostra o ícone azul de pesquisa no ecrã de validação **e** acrescenta o campo à pesquisa automática de fornecedor. Um campo que só deve ser pesquisado manualmente fica desmarcado.
{% endhint %}

### **Passo 2 — Uma pesquisa, não uma pesquisa por campo**

O DocBits **não** pesquisa cada campo separadamente. Constrói **uma** pesquisa sobre todos os campos usados. **Corresponder a tudo (Match All)** determina como são combinados:

* **Corresponder a tudo desligado** (predefinição) → "encontrar todos os fornecedores que correspondem ao NIF **OU** ao nome do fornecedor". Isto dá uma lista **mais longa**.
* **Corresponder a tudo ligado** → "encontrar todos os fornecedores que correspondem ao NIF **E** ao nome do fornecedor". Isto dá uma lista **mais curta**.

Tenha em conta que os operadores **Smart** e **Contains** procuram uma parte do texto. O nome "Meier" também encontra "Meier Bau GmbH" e "Meier & Sons Ltd". Por isso um nome de fornecedor encontra muitas vezes vários fornecedores.

### **Passo 3 — O que acontece quando a lista tem mais de um fornecedor**

O **Gestor de conflitos (Conflict Handler)** decide:

* **Best Score** → escolhe o fornecedor que corresponde ao maior número de campos. Nunca deixa o fornecedor vazio.
* **Return None** → deixa o fornecedor vazio, para que um utilizador o escolha.
* **Return First** → escolhe o primeiro fornecedor da lista.

### **Exemplos**

Em todos os exemplos o documento tem um NIF e um nome de fornecedor, e ambos os campos são **Pesquisáveis**.

<table><thead><tr><th width="150">O NIF encontra</th><th width="150">O nome encontra</th><th width="150">Corresponder a tudo desligado + Return None</th><th width="150">Corresponder a tudo ligado + Return None</th><th width="150">Corresponder a tudo desligado + Best Score</th></tr></thead><tbody>
<tr><td>só A</td><td>A e B</td><td>vazio</td><td><strong>A</strong></td><td><strong>A</strong></td></tr>
<tr><td>A e B</td><td>só B</td><td>vazio</td><td><strong>B</strong></td><td><strong>B</strong></td></tr>
<tr><td>A, B e C</td><td>C, D e E</td><td>vazio</td><td><strong>C</strong></td><td><strong>C</strong></td></tr>
<tr><td>A, B e C</td><td>B, C e D</td><td>vazio</td><td>vazio</td><td>B ou C, não fiável</td></tr>
<tr><td>só A</td><td>nada</td><td><strong>A</strong></td><td>vazio</td><td><strong>A</strong></td></tr>
</tbody></table>

Como ler a tabela:

* **As linhas 1 a 3** são o caso normal. Um campo é único, o outro não. Com **Corresponder a tudo desligado** a lista contém vários fornecedores e **Return None** deixa o campo vazio. **Corresponder a tudo ligado** mantém apenas o fornecedor que corresponde aos dois campos e encontra-o.
* **A linha 4** não tem nenhum fornecedor único. Deixar o campo vazio está correto. **Best Score** escolhe um à mesma, e pode ser o errado.
* **A linha 5** é o risco de **Corresponder a tudo ligado**. Ver o aviso abaixo.

{% hint style="warning" %}
**Corresponder a tudo pode perder um fornecedor.** Com **Corresponder a tudo ligado** todos os campos usados têm de corresponder. Se um campo tiver um valor que não existe nos seus dados mestres — um erro de escrita, um nome de empresa antigo, um valor lido da página — a pesquisa inteira não devolve nada e nenhum fornecedor é encontrado, apesar de o NIF sozinho ter encontrado o correto.
{% endhint %}

### **Um fornecedor era reconhecido antes e agora já não é**

Quase sempre há mais um campo que passou a ter valor. Verifique por esta ordem:

1. Abra o documento. Que campo do grupo de consulta tem agora um valor que antes estava vazio?
2. Abra a configuração de consulta. Esse campo está marcado como **Pesquisável** ou **Auto Trigger**? Se sim, passou a participar na pesquisa e torna a lista de resultados mais longa.
3. Escolha uma das três saídas:
   * **O campo não deve participar na pesquisa** → desmarque **Pesquisável** e **Auto Trigger** nesse campo. O campo mantém o seu valor no documento e continua a ser mostrado ao utilizador. É a alteração mais pequena.
   * **O campo deve participar** → ligue **Corresponder a tudo**, mas leia primeiro o aviso acima.
   * **Quer um fornecedor em todos os casos** → coloque o **Gestor de conflitos** em **Best Score**. Aceite que pode escolher o fornecedor errado em vez de deixar o campo vazio.
