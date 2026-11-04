# Execute o prompt do DocOperator (script de automação)

***

Adicione este cartão ao grupo **Então** do Workflow Builder — as ações que são executadas quando as condições Quando/E correspondem:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-pt.png" alt="Exemplo não guardado com cartões Quando, E e Então. Configure todos os campos antes da execução. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real."><figcaption><p>Exemplo não guardado com cartões Quando, E e Então. Configure todos os campos antes da execução. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

***

## 📌 Informações da versão

**Versão atual:** v3 (mais recente e recomendado) **Estado:** ✅ Ativo

**Histórico de versões:**

* v2 → Implementação original do DocOperator
* **v3 → CURRENT** (parâmetro de controle de execução adicionado)
* v4 → Obsoleto (recursos revertidos)

**O que mudou:** v3 adicionou o parâmetro opcional "Executar o prompt" para maior controle. v4 tentou reverter isso, mas foi descontinuado.

📖 [Histórico e alterações da versão](../../release.md) | [Banco de dados completo do cartão](../../cards-overview/export-cards-guide.md)

***

## Objetivo

Este cartão executa uma ação ou script automatizado do navegador usando DocOperator. Pense nele como um robô que pode interagir com sites ou sistemas exatamente como um ser humano faria – clicando em botões, preenchendo formulários, extraindo dados, etc.

**Exemplo do mundo real:** Sua empresa usa um sistema de compras baseado na web. Este cartão pode fazer login automaticamente, pesquisar um produto, verificar a disponibilidade e obter o preço atual - tudo sem que ninguém faça isso manualmente.

***

## Quando usar este cartão

Use este cartão quando precisar:

* Automatize tarefas em sites que não possuem APIs
* Extraia dados de páginas da web
* Preencha formulários automaticamente
* Faça login nos sistemas e recupere informações
* Automatize tarefas manuais repetitivas
* Interaja com sistemas legados que não estão integrados

**Cenários comuns:**

* Faça login nos sites dos fornecedores e obtenha inventário em tempo real
* Preencher formulários automaticamente em sistemas externos
* Extraia dados de páginas da web que não oferecem APIs
* Verifique o status da entrega em sites de correio
* Obtenha preços de sistemas sem acesso à API

***

## Como funciona

1. **Cartão acionado**: O fluxo de trabalho chega a este cartão e as condições são atendidas
2. **O script começa**: O bot DocOperator começa a executar seu script de automação
3. **Ações de bot**: O bot realiza ações como clicar, digitar, rolar, extrair
4. **Extração de dados**: Bot coleta informações de páginas da web
5. **Dados de retorno**: Os dados voltam ao DocFlow para uso nos próximos cartões
6. **Manipulação de tempo limite**: Se o script demorar muito, ele para e retorna o que possui

***

## Parâmetros explicados

### Prompt/Script do DocOperator

O script de automação que informa ao DocOperator exatamente o que fazer

**Exemplo (inglês simples):**

```
1. Go to https://supplier.com/login
2. Enter username: myuser
3. Enter password: mypass
4. Click Login button
5. Search for product "ABC123"
6. Extract the price
7. Return the price
```

### Variáveis

Dados que você deseja passar para o script

**Exemplo:**

```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

Essas variáveis ​​podem ser usadas no script como:

```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Máximo de etapas

Quantas ações o bot pode realizar

**Valores típicos:**

* Tarefa simples (como conseguir um preço): 10 a 20 etapas
* Complexidade média (preencher formulário + extrair): 20-50 etapas
* Fluxo de trabalho complexo (login + pesquisa + validação): 50-100 etapas

**Por que é importante:** Evita loops infinitos e scripts de execução muito longa

### Máximo de tentativas

Se o bot falhar em uma ação, quantas vezes ele deverá tentar novamente?

**Exemplos:**

* 1: Tente uma vez, se falhar, siga em frente
* 3: Tente 3 vezes antes de desistir
* 5: Muito persistente – tente 5 vezes

***

## Exemplo passo a passo

### Cenário: Obtenha preços do fornecedor no site

**Definição do script:**

```
Step 1: Open website https://prices.supplier-xyz.com
Step 2: Click on "Product Lookup"
Step 3: Enter product code: ABC-123
Step 4: Click "Search"
Step 5: Wait for results to load (3 seconds)
Step 6: Extract price from the page
Step 7: Extract available quantity
Step 8: Return both values
```

**Variáveis passadas:**

```
product_code = "ABC-123"
supplier_name = "Supplier XYZ"
```

**Script usando variáveis:**

```
Open website https://prices.{supplier_name}.com
Enter product code: {product_code}
Extract price and quantity
```

**Resultado esperado:**

```
price: 45.50
quantity_available: 500
```

***

## Tipos de ações que o DocOperator pode realizar

### Navegação

* Ir para URL
* Clique nos links
* Pressione botões
* Rolar página

### Preenchimento de formulário

* Digite texto nos campos
* Selecione as opções suspensas
* Marque/desmarque caixas
* Clique nos botões

### Extração de dados

* Leia o texto da página
* Extrair números
* Obtenha dados da tabela
* Copiar informações

### Esperando

* Aguarde a página carregar
* Espere que os elementos apareçam
* Aguarde pelo conteúdo dinâmico

### Lógica Condicional

* Se algo existe, faça isso
* Se o texto corresponder, então...
* Conte os resultados e aja de acordo

***

## Casos de uso comuns

### 1. Obtenha preços em tempo real

**Cenário:** Fornecedor não possui API, mas site mostra preços

**Roteiro:**

```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Verifique a disponibilidade do estoque

**Cenário:** Necessidade de saber se o fornecedor tem estoque

**Roteiro:**

```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Envio automático de formulário

**Cenário:** Necessidade de preenchimento de formulário em site externo

**Roteiro:**

```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. Verificação de entrada de dados

**Cenário:** Verifique as correspondências de dados em dois sistemas diferentes

**Roteiro:**

```
1. Go to System A
2. Search for Order #123
3. Extract order amount
4. Go to System B
5. Search for Order #123
6. Extract order amount
7. Compare amounts
8. Return true/false if they match
```

***

## Etapas de configuração

### Etapa 1: crie o script

1. Defina o que você deseja realizar
2. Divida-o em pequenos passos
3. Escreva cada etapa claramente
4. Teste manualmente primeiro (abra o site, faça você mesmo)
5. Documente exatamente o que você clica, onde digita e o que extrai

### Etapa 2: identificar variáveis

1. Quais dados serão alterados entre documentos?
2. O que deve ser passado para o script?
3. Definir nomes de variáveis
4. Especifique onde as variáveis são usadas no script

### Etapa 3: definir parâmetros

* **Etapas Máximas**: Baseado na complexidade do script
* **Máximo de novas tentativas**: Quão persistente deve ser o bot?
* **Tempo limite**: Quanto tempo deve esperar pelas páginas?

### Etapa 4: teste

1. Teste com dados de amostra
2. Verifique se o bot pode acessar o site
3. Verifique se a extração está correta
4. Verifique se as variáveis funcionam corretamente

***

## Dicas para escrever roteiros

### Linguagem clara

✅ **Fazer:**

```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **Não:**

```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Seletores Específicos

✅ **Fazer:**

```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **Não:**

```
Click somewhere
Type in a field
```

### Tratamento de erros

✅ **Fazer:**

```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **Não:**

```
Click "Next" (assumes it's always there)
```

***

## Solução de problemas

### "Tempo limite do script esgotado"

**Causa:** O script demorou muito para ser concluído

**Soluções:**

* [] Reduzir o número de ações
* [] Aumentar o valor de "Passos Máximos"
* [] Otimize o script para uma execução mais rápida
* [] Simplifique o que você está tentando extrair

### "Elemento não encontrado"

**Causa:** DocOperator não conseguiu encontrar o botão/campo que você especificou

**Soluções:**

* [] Verifique se o nome do botão/campo está exatamente correto
* [] Verifique se o layout do site mudou
* [] Adicionar tempo de espera antes de clicar
* [] Verifique se o botão só aparece sob certas condições

### "Falha no login"

**Causa:** Falha na autenticação

**Soluções:**

* [] Verifique se o nome de usuário/senha estão corretos
* [] Verifique se a senha possui caracteres especiais
* [] Verifique se a conta não está bloqueada
* [] Verifique se o processo de login foi alterado

### "Dados não extraídos corretamente"

**Causa:** O script foi executado, mas extraiu informações erradas

**Soluções:**

* [] Verifique se o campo correto foi selecionado
* [] Verifique se os dados estão no local esperado
* [] Testar a lógica de extração manualmente
* [] Adicione etapas de depuração para verificar o que está na página

### "O script é executado lentamente"

**Causa:** Muitas etapas ou site lento

**Soluções:**

* [] Remova etapas desnecessárias
* [] Otimize os tempos de espera
* [] Verifique a conexão com a internet
* [] Considere se existe alternativa de API

***

## Melhores Práticas

✅ **Fazer:**

* Teste os scripts completamente antes de implantar
* Mantenha os scripts simples e focados
* Adicione comentários explicando cada etapa
* Use nomes de variáveis significativos
* Monitore o desempenho do script
* Tenha um substituto para quando os scripts falharem

❌ **Não:**

* Crie scripts extremamente longos (>100 etapas)
* Coloque senhas confidenciais em logs
* Confie em coordenadas exatas (mudança de sites)
* Crie loops sem condições de saída
* Ignorar mensagens de erro

***

## Dicas de desempenho

* **Remover etapas não utilizadas** - Cada etapa leva tempo
* **Combinar ações semelhantes** - Agrupar cliques relacionados
* **Otimizar esperas** - Use apenas atrasos necessários
* **Cache de dados** - Não extraia os mesmos dados duas vezes
* **Processamento paralelo** - Execute vários scripts, se possível

***

## Considerações de segurança

⚠️ **Importante:**

* Não armazene senhas no DocFlow
* Use métodos seguros para passar credenciais
* Não registre dados confidenciais
* Monitore o que está sendo extraído
* Garanta que a atividade do bot seja registrada e auditável

***

## Exemplo de variáveis

### Variáveis disponíveis que você pode usar:

```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### Script usando variáveis:

```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

***

## Comparação: quando usar DocOperator vs API

| Situação              | UsarDocOperator | Usar API     |
| ---------------------- | --------------- | ----------- |
| Site tem API        | ❌ Não            | ✅ Sim       |
| O site é interativo | ✅ Sim           | ❌ Não        |
| Requer login         | ✅ Sim           | Depende     |
| Muito rápido necessário       | ❌ Não            | ✅ Sim       |
| Fluxo de trabalho complexo       | ✅ Sim           | ❌Talvez não |
| Os dados mudam diariamente     | ✅ Sim           | ✅ Sim       |

***

## Cartões Relacionados

* **CALL\_API** - Use quando a API estiver disponível
* **ACTION\_HTTPS\_REQUEST** - Solicitações mais simples
* **ACTION\_SET\_FIELD\_TO\_TEXT** - Use dados extraídos
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Verifique o status da solicitação
