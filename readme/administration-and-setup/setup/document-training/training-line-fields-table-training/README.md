# Treinar campos de linha e tabelas

## Treino de tabelas: quando e como utilizar

Por predefinição, o DocBits utiliza extração de tabelas por IA em vários fornecedores. Quando precisar de maior controlo sobre a extração dos itens de um fornecedor específico, utilize o **Treino de tabelas** para definir manualmente a estrutura.

#### &#x20;**Importante: treino específico do fornecedor**

O treino de tabelas é **específico de cada fornecedor**. As regras de um layout treinado aplicam-se apenas aos documentos desse fornecedor.\
Os outros fornecedores continuam a utilizar a extração por IA, salvo se forem treinados separadamente.

#### Quando utilizar o treino de tabelas?

Utilize o treino de tabelas **apenas quando o layout for estável** e precisar de uma extração consistente e de qualidade. É particularmente adequado para fornecedores que:

* Utilizam um **formato de fatura fixo** ao longo do tempo.
* Exigem um **mapeamento preciso** dos itens de linha para campos específicos.
* Enviam **grandes volumes de documentos**, para os quais uma automatização consistente tem valor.

#### Quando não utilizar o treino de tabelas

Evite o treino de tabelas se:

* O fornecedor **alterar frequentemente o layout das faturas**, por exemplo a cada dois meses.
* Não receber documentos desse fornecedor regularmente.
* A extração por IA predefinida já funcionar **suficientemente bem** sem treino manual.

Nestes casos, repetir o treino das tabelas seria ineficiente e demorado.



## Como utilizar

O **Modo de treino** ensina o DocBits a extrair corretamente os itens de linha do layout de um fornecedor específico.

No modo de treino, define:

* **Onde se encontra a tabela** no documento.
* **Que áreas correspondem a cada coluna**, como quantidade, descrição ou preço unitário.

Este modo cria um **modelo de extração reutilizável** para o fornecedor. Os documentos futuros com o mesmo layout são processados automaticamente, sem repetir o treino.

**Principais características:**

* **As colunas mapeadas são apenas de leitura**: não pode alterar o texto manualmente.
* **Não pode adicionar nem eliminar linhas**.
* O objetivo é **mapear posições**, e não corrigir valores.
* Depois de mapear a tabela e as colunas, clique em **«Save Rules»** (guardar regras) para aplicar o treino a documentos semelhantes do mesmo fornecedor.



O **Modo de correção** permite **corrigir erros de extração** na tabela do documento atual, depois de o DocBits ter tentado extrair a tabela.

Utilize o modo de correção quando:

* Alguns **valores estiverem em falta ou desalinhados**.
* Tiver sido extraída uma **linha vazia ou duplicada** que deva ser removida.

**O que pode fazer no modo de correção:**

* **Ajustar manualmente os valores** nas colunas mapeadas, por exemplo para corrigir posições incorretas.
* **Eliminar linhas** que não devem fazer parte da tabela.
* **Adicionar linhas** que não foram detetadas na extração.
