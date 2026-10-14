# Run DocOperator Prompt (Automation Script)

Estes cartões ficam no grupo **Then** do Construtor de fluxos de trabalho — as ações executadas assim que as condições When/And são atendidas:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Os cartões são adicionados ao grupo <strong>Then</strong> através de <strong>Add Card</strong>.</p></figcaption></figure>

## Objetivo
Este cartão executa uma ação de navegador automatizada ou um script utilizando o DocOperator. Pense nele como um robô que pode interagir com sites ou sistemas exatamente como um humano faria - clicando em botões, preenchendo formulários, extraindo dados, etc.

**Exemplo do mundo real:** A sua empresa utiliza um sistema de compras baseado na Web. Este cartão pode iniciar sessão automaticamente, procurar um produto, verificar a disponibilidade e obter o preço atual - tudo sem que ninguém o faça manualmente.

---

## Quando utilizar este cartão

Utilize este cartão quando precisar de:
- Automatizar tarefas em sites que não têm APIs
- Extrair dados de páginas web
- Preencher formulários automaticamente
- Iniciar sessão em sistemas e obter informações
- Automatizar tarefas manuais repetitivas
- Interagir com sistemas antigos que não estão integrados

**Cenários comuns:**
- Iniciar sessão em sites de fornecedores e obter o inventário em tempo real
- Preencher automaticamente formulários em sistemas externos
- Extrair dados de páginas web que não oferecem APIs
- Verificar o estado da entrega em sites de transportadoras
- Obter preços de sistemas sem acesso à API

---

## Como funciona

1. **Card Triggered**: O fluxo de trabalho chega a este cartão e as condições são cumpridas
2. **Script Starts**: O bot do DocOperator começa a executar o seu script de automação
3. **Bot Actions**: O bot realiza ações como clicar, escrever, deslocar e extrair
4. **Data Extraction**: O bot recolhe informações das páginas web
5. **Return Data**: Os dados voltam ao DocFlow para serem utilizados nos cartões seguintes
6. **Timeout Handling**: Se o script demorar demasiado, para e devolve o que tem

---

## Parâmetros explicados

### DocOperator Prompt/Script
O script de automação que indica ao DocOperator exatamente o que fazer

**Exemplo (em linguagem corrente):**
```
1. Go to https://supplier.com/login
2. Enter username: myuser
3. Enter password: mypass
4. Click Login button
5. Search for product "ABC123"
6. Extract the price
7. Return the price
```

### Variables
Dados que pretende passar PARA DENTRO do script

**Exemplo:**
```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

Estas variáveis podem ser utilizadas no script da seguinte forma:
```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Maximum Steps
Quantas ações o bot está autorizado a realizar

**Valores típicos:**
- Tarefa simples (como obter um preço): 10-20 passos
- Complexidade média (preencher formulário + extrair): 20-50 passos
- Fluxo de trabalho complexo (iniciar sessão + procurar + validar): 50-100 passos

**Porque é importante:** Evita ciclos infinitos e scripts de execução muito longa

### Maximum Retries
Se o bot falhar uma ação, quantas vezes deve voltar a tentar?

**Exemplos:**
- 1: Tenta uma vez; se falhar, avança
- 3: Tenta 3 vezes antes de desistir
- 5: Muito persistente - tenta 5 vezes

---

## Exemplo passo a passo

### Cenário: Obter preços de fornecedor a partir de um site

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

**Script utilizando variáveis:**
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

---

## Tipos de ações que o DocOperator pode realizar

### Navegação
- Ir para um URL
- Clicar em ligações
- Premir botões
- Deslocar a página

### Preenchimento de formulários
- Escrever texto em campos
- Selecionar opções de listas pendentes
- Marcar/desmarcar caixas
- Clicar em botões

### Extração de dados
- Ler texto da página
- Extrair números
- Obter dados de tabelas
- Copiar informações

### Espera
- Aguardar o carregamento da página
- Aguardar o aparecimento de elementos
- Aguardar conteúdo dinâmico

### Lógica condicional
- Se algo existir, fazer isto
- Se o texto corresponder, então...
- Contar resultados e agir em conformidade

---

## Casos de utilização comuns

### 1. Obter preços em tempo real
**Cenário:** O fornecedor não tem API, mas o site mostra os preços

**Script:**
```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Verificar a disponibilidade em inventário
**Cenário:** É necessário saber se o fornecedor tem stock

**Script:**
```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Submissão automática de formulários
**Cenário:** É necessário preencher um formulário num site externo

**Script:**
```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. Verificação de introdução de dados
**Cenário:** Verificar se os dados coincidem em dois sistemas diferentes

**Script:**
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

---

## Passos de configuração

### Passo 1: Criar o script
1. Defina o que pretende alcançar
2. Divida-o em pequenos passos
3. Escreva cada passo com clareza
4. Teste primeiro manualmente (abra o site, faça-o você mesmo)
5. Documente exatamente onde clica, onde escreve e o que extrai

### Passo 2: Identificar as variáveis
1. Que dados mudarão entre documentos?
2. O que deve ser passado para o script?
3. Defina os nomes das variáveis
4. Especifique onde as variáveis são utilizadas no script

### Passo 3: Definir os parâmetros
- **Maximum Steps**: Com base na complexidade do script
- **Maximum Retries**: Quão persistente deve ser o bot?
- **Timeout**: Quanto tempo deve aguardar pelas páginas?

### Passo 4: Testar
1. Teste com dados de amostra
2. Verifique se o bot consegue aceder ao site
3. Verifique se a extração está correta
4. Verifique se as variáveis funcionam corretamente

---

## Dicas para escrever scripts

### Linguagem clara
✅ **Faça:**
```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **Não faça:**
```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Seletores específicos
✅ **Faça:**
```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **Não faça:**
```
Click somewhere
Type in a field
```

### Tratamento de erros
✅ **Faça:**
```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **Não faça:**
```
Click "Next" (assumes it's always there)
```

---

## Resolução de problemas

### "Script Timed Out"
**Causa:** O script demorou demasiado a concluir

**Soluções:**
- [ ] Reduza o número de ações
- [ ] Aumente o valor de "Maximum Steps"
- [ ] Otimize o script para uma execução mais rápida
- [ ] Simplifique aquilo que está a tentar extrair

### "Element Not Found"
**Causa:** O DocOperator não conseguiu encontrar o botão/campo que especificou

**Soluções:**
- [ ] Verifique se o nome do botão/campo está exatamente correto
- [ ] Verifique se a disposição do site mudou
- [ ] Adicione um tempo de espera antes de clicar
- [ ] Verifique se o botão só aparece sob determinadas condições

### "Login Failed"
**Causa:** A autenticação falhou

**Soluções:**
- [ ] Verifique se o nome de utilizador/palavra-passe estão corretos
- [ ] Verifique se a palavra-passe tem caracteres especiais
- [ ] Verifique se a conta não está bloqueada
- [ ] Verifique se o processo de início de sessão mudou

### "Data Not Extracted Correctly"
**Causa:** O script foi executado, mas extraiu informações erradas

**Soluções:**
- [ ] Verifique se o campo correto foi selecionado
- [ ] Verifique se os dados estão na localização esperada
- [ ] Teste a lógica de extração manualmente
- [ ] Adicione passos de depuração para verificar o que está na página

### "Script Runs Slowly"
**Causa:** Demasiados passos ou site lento

**Soluções:**
- [ ] Remova passos desnecessários
- [ ] Otimize os tempos de espera
- [ ] Verifique a ligação à Internet
- [ ] Considere se existe uma alternativa de API

---

## Boas práticas

✅ **Faça:**
- Teste os scripts exaustivamente antes de os implementar
- Mantenha os scripts simples e focados
- Adicione comentários a explicar cada passo
- Utilize nomes de variáveis significativos
- Monitorize o desempenho dos scripts
- Tenha uma alternativa para quando os scripts falham

❌ **Não faça:**
- Criar scripts extremamente longos (>100 passos)
- Colocar palavras-passe sensíveis nos registos
- Confiar em coordenadas exatas (os sites mudam)
- Criar ciclos sem condições de saída
- Ignorar as mensagens de erro

---

## Dicas de desempenho

- **Remova passos não utilizados** - Cada passo demora tempo
- **Combine ações semelhantes** - Agrupe cliques relacionados
- **Otimize as esperas** - Utilize apenas os atrasos necessários
- **Coloque dados em cache** - Não extraia os mesmos dados duas vezes
- **Processamento paralelo** - Execute vários scripts, se possível

---

## Considerações de segurança

⚠️ **Importante:**
- Não armazene palavras-passe no DocFlow
- Utilize métodos seguros para passar credenciais
- Não registe dados sensíveis
- Monitorize aquilo que está a ser extraído
- Garanta que a atividade do bot é registada e auditável

---

## Exemplo de variáveis

### Variáveis disponíveis que pode utilizar:
```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### Script utilizando variáveis:
```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

---

## Comparação: quando utilizar o DocOperator vs API

| Situação | Utilizar DocOperator | Utilizar API |
|-----------|-----------------|---------|
| O site tem API | ❌ Não | ✅ Sim |
| O site é interativo | ✅ Sim | ❌ Não |
| Requer início de sessão | ✅ Sim | Depende |
| É necessário muita rapidez | ❌ Não | ✅ Sim |
| Fluxo de trabalho complexo | ✅ Sim | ❌ Talvez não |
| Os dados mudam diariamente | ✅ Sim | ✅ Sim |

---

## Cartões relacionados

- **CALL_API** - Utilizar quando existe uma API em alternativa
- **ACTION_HTTPS_REQUEST** - Pedidos mais simples
- **ACTION_SET_FIELD_TO_TEXT** - Utilizar dados extraídos
- **CONDITION_HTTPS_REQUEST_STATUS** - Verificar o estado do pedido
