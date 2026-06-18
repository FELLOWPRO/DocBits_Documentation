# Pesquisa rápida

A **Pesquisa rápida** no topo do painel é a forma mais rápida de encontrar
documentos. Digite o que procura — um nome, um estado, um valor, uma data — e a
lista filtra-se instantaneamente.

Este guia está organizado tal como a pesquisa se constrói:

1. **Campos padrão** — as colunas que todo documento tem (nome do documento,
   estado, datas). Sempre disponíveis.
2. **Campos de texto completo** — conteúdo extraído (fornecedor, número de
   encomenda, número de fatura, valores, linhas). Disponíveis quando a pesquisa
   de texto completo está ativada.
3. **Operadores, atalhos e receitas** — a referência completa.

> Não precisa de memorizar nada: clique na barra de pesquisa e escolha um campo
> e um valor da lista. Os exemplos abaixo mostram também a forma escrita para
> copiar diretamente.

---

## Como funciona a barra de pesquisa — chips, barra de ferramentas e vista bruta

À medida que completa uma condição (um campo, um operador e um valor), a Pesquisa
rápida transforma-a num **chip** — uma pílula colorida dentro da barra — e inicia
um novo. Um chip mostra o **campo**, o **operador** e o **valor**, com um **×**
para o remover. Os chips têm cores conforme o local onde os dados residem:

| Cor do chip | Tipo de campo |
|-------------|---------------|
| **Azul** | Coluna padrão (nome do documento, estado, datas) |
| **Laranja** | Campo de texto completo / extraído (fornecedor, valor, número de fatura) |
| **Roxo** | Pesquisa vetorial (semântica) |
| **Verde** | Pesquisa de texto OCR |

Clique num chip para o editar; clique em **×** para o eliminar. Vários chips
combinados são lidos como **AND** por predefinição.

**Barra de ferramentas** (à direita da barra): **ⓘ Ajuda** abre a referência
integrada de campos e sintaxe; **Filtros** é um painel rápido de Estado /
Utilizador / Reiniciar; o **anel de índice** mostra que percentagem do índice de
texto completo já está construída (apenas quando a pesquisa de texto completo
está ativada).

**Vista padrão vs. vista bruta:** a barra mostra a sua consulta sob a forma de
chips (padrão). Mude para a **vista bruta** para a ver e editar como texto
simples — prático para copiar ou escrever uma consulta longa. A sua consulta é
memorizada quando recarrega a página.

### Encontrar documentos por subtipo de fatura

```
invoice_sub_type="Cost Invoice"
```

O subtipo de fatura é uma lista fixa (p. ex. **Cost Invoice**, **Purchase
Invoice**), por isso `=` é uma correspondência exata e a barra oferece um seletor
de valores. Use `invoice_sub_type!="Cost Invoice"` para tudo exceto esse subtipo.

## Agrupar resultados

Em vez de uma lista plana, pode **agrupar** os resultados por qualquer campo —
fornecedor, estado, tipo de documento ou um intervalo de datas:

```
group by supplier_name
```

A lista mostra **cabeçalhos de grupo** recolhíveis, cada um com uma **contagem**.
Clique num cabeçalho para o expandir ou recolher; clique dentro de um grupo para
**detalhar** (aplicar esse valor como filtro). O agrupamento combina-se com
qualquer filtro.

<figure><img src="../../../.gitbook/assets/quick_search_16_grouping.png" alt="Resultados agrupados por fornecedor"><figcaption><p><code>group by supplier_name</code> — os resultados recolhem-se num cabeçalho expansível por fornecedor.</p></figcaption></figure>

---

## Parte 1 — Campos padrão

Os campos padrão são as próprias colunas do documento. Estão **sempre
disponíveis**, esteja ou não ativada a pesquisa de texto completo.

### Encontrar documentos por nome

O nome do documento é a pesquisa mais comum. Três formas de corresponder — todas
**sem distinção de maiúsculas/minúsculas**:

#### `=` → começa por

```
filename=invoice
```

Encontra documentos cujo nome **começa por** «invoice». Como ignora maiúsculas,
todos estes correspondem a `filename=invoice`:

```
Invoice.pdf   iNVoice.pdf   iNvoiCE.pdf   INVOICE.pdf
Invoice.xml   iNVoice.xml   iNvoiCE.edi   …
```

**Não** corresponde a `XYZ_Invoice.pdf` (aí «invoice» está no meio — use `:`).

<figure><img src="../../../.gitbook/assets/pt_quick_search_02_filename_starts.png" alt="filename=invoice corresponde apenas a nomes que começam por invoice"><figcaption><p><code>filename=invoice</code> — apenas nomes que <strong>começam por</strong> «invoice», em qualquer capitalização (<code>INVOICE.pdf</code>, <code>iNvoiCE.pdf</code>, <code>iNVoice.pdf</code>, <code>Invoice.pdf</code> correspondem — 7 resultados).</p></figcaption></figure>

#### `:` → contém (em qualquer lugar)

```
filename:invoice
```

Com `:` a palavra corresponde **em qualquer parte** do nome — `2026_Invoice.pdf`,
`XYZ_Invoice ABC.pdf`, `123_Invoice ABC bla bla.pdf`.

<figure><img src="../../../.gitbook/assets/pt_quick_search_03_filename_contains.png" alt="filename:invoice corresponde à palavra em qualquer parte do nome"><figcaption><p><code>filename:invoice</code> — corresponde a «invoice» em qualquer posição do nome (também <code>XYZ_Invoice ABC.pdf</code>).</p></figcaption></figure>

#### `="…"` → começa *ou* termina por

```
filename="invoice"
```

As aspas fazem com que `=` corresponda a nomes que **começam ou terminam** pelo
valor.

> **As três numa linha:** `=` → começa por · `:` → contém · `="…"` → começa ou
> termina por. Todas ignoram maiúsculas/minúsculas.

### Encontrar por estado

```
status=ready_for_validation
```

O estado é uma lista fixa, por isso `=` é uma correspondência **exata** e a barra
oferece um seletor de valores.

### Encontrar por data

```
created_on>2026-05-25
```

Use `>`, `<`, `>=`, `<=` para intervalos de datas. Também datas **relativas**:
`today()`, `today()-7` (últimos 7 dias), `today()+30`.

---

## Parte 2 — Campos de texto completo

Os campos de texto completo pesquisam no **conteúdo extraído** — fornecedor,
número de encomenda, número de fatura, valores, linhas. Aparecem a **laranja** e
exigem a **pesquisa de texto completo ativada**. As regras de correspondência são
idênticas aos campos de texto padrão (`=` começa-por, `:` contém, `="…"`
começa-ou-termina).

### Encontrar documentos de um fornecedor

```
supplier_name=Test
```

Começa-por no nome de fornecedor extraído; `supplier_name:fuji` corresponde em
qualquer parte; `supplier_name:"Ruiz Foods"` coloca entre aspas um valor com
espaços.

### Encontrar por valor

```
total_amount>5000
```

Use `>`, `<`, `>=`, `<=` ou `between 1000 and 5000` para uma janela.

### Encontrar o que falta

```
supplier_name=""
```

`=""` significa «este campo **não está preenchido**»; `supplier_name!=""`
significa «tem qualquer fornecedor». A mesma verificação serve para qualquer
campo, p. ex. `ap_assignment_code=""`.

---

## Filtros inteligentes — um clique

No topo do menu suspenso de pesquisa encontra os **Filtros inteligentes**:
pesquisas prontas com um clique. Cada um é um atalho de uma consulta que também
poderia escrever:

| Filtro inteligente | Encontra | Equivale a |
|--------------------|----------|------------|
| ⚠️ **Vencidos** | Após a data de vencimento | `invoice_due_date<today()` |
| 🕐 **A vencer em breve** | Nos próximos 7 dias | `invoice_due_date<=today()+7` |
| 👤 **Atribuídos a mim** | A aguardar a sua ação | `assigned_to=<você>` |
| 📅 **Caixa de hoje** | Importados hoje | `imported_on>=today()` |
| 📋 **A aguardar validação** | Prontos a validar | `status=ready_for_validation` |
| 🧾 **Documentos eletrónicos** | E-faturas (XML, ZUGFeRD, EDI) | `is_edoc=true` |
| ✅ **Correspondência PO total** | Totalmente conciliado com uma encomenda | `po_match_status=full_matched` |
| ➗ **Correspondência PO parcial** | Parcialmente conciliado | `po_match_status=partial_matched` |
| 📉 **Correspondência PO inferior** | Quantidade ou preço abaixo da encomenda | `po_match_status=under_matched` |

Os três filtros de **correspondência PO** e os campos de texto completo exigem a
pesquisa de texto completo ativada.

---

## Parte 3 — Operadores, conectores, atalhos

### A ajuda integrada

O **ícone de ajuda** na barra de pesquisa abre uma referência completa de todos
os campos, operadores e atalhos do seu espaço de trabalho.

<figure><img src="../../../.gitbook/assets/pt_quick_search_08_help_modal.png" alt="A ajuda integrada de pesquisa do painel com todos os operadores"><figcaption><p>A ajuda integrada <strong>Pesquisa do painel — Campos e sintaxe</strong> lista cada operador e como os valores correspondem (p. ex. «Exato / começa por»).</p></figcaption></figure>

### O que `=` significa por tipo de campo

Toda correspondência de texto ignora maiúsculas/minúsculas.

| Tipo de campo | Exemplo | `=` significa |
|---------------|---------|---------------|
| Texto (nome, fornecedor, encomenda) | `filename=invoice` | **começa por** |
| Texto, em qualquer lugar | `filename:invoice` | **contém** |
| Texto, início *ou* fim | `filename="invoice"` | **começa ou termina por** |
| Estado / tipo / correspondência PO (listas fixas) | `status=finished` | **exato** |
| Identificadores (nº fatura, id fornecedor) | `invoice_number=INV-100` | **exato** |
| Número | `total_amount>5000` | intervalo (`> < >= <= between`) |
| Data | `created_on>2026-01-01` | intervalo + `today()±N` |

### Operadores

| Operador | Significado |
|----------|-------------|
| `=` | começa-por (texto) / exato (lista, número, data) |
| `:` | contém (texto, em qualquer lugar) |
| `="…"` | começa-por ou termina-por (texto) |
| `!=` | o oposto de `=` |
| `>` `<` `>=` `<=` | maior / menor que |
| `between … and …` | intervalo inclusivo |
| `field=""` / `field!=""` | está vazio / está preenchido |
| `today()`, `today()-7`, `today()+30` | datas relativas |

### Conectores

Combine condições com **AND** (ambas), **OR** (uma), **NOT** e parênteses
`( … )` para agrupar:

```
status=ready_for_validation AND supplier_name=Test
(status=error OR status=failed) AND created_on>today()-1
```

### Atalhos

Formas mais curtas para as mesmas consultas:

| Atalho | Equivale a |
|--------|------------|
| `total_amount gt 5000` | `total_amount>5000` (aliases gt/gte/lt/lte) |
| `due_date > today` | `due_date>today()` |
| `imported_on this_week` | esta semana ISO (também `last_week`, `this_month`, …) |
| `ap_assignment_code is empty` | `ap_assignment_code=""` |
| `status:open` | `status=ready_for_validation` (open/closed/failed/done) |
| `total_amount not between 100, 200` | `total_amount<100 OR total_amount>200` |
| `status in (finished, error)` | `status=finished OR status=error` |
| `not status=finished` | `status!=finished` |
| `filename contains rechnung` | `filename:rechnung` |
| `total_amount > 5k` | `total_amount>5000` (`k`=mil, `M`=milhão) |
| `overdue` | `invoice_due_date<today() AND status!=finished` |
| `#INV-1234` | `invoice_id:INV-1234` |
| `@User` | `assigned_to:User` |
| `$5000+` | `total_amount>=5000` |

---

## Parte 4 — Modos de pesquisa avançados

Além da pesquisa por campos, três prefixos pesquisam no próprio conteúdo.

### Pesquisa vetorial (semântica) — `vector:`

Corresponde por **significado**, não por texto exato. Requer o módulo Vector.

```
vector: invoices about office supplies
vector: shipping delays with Hamburg port
```

### Pesquisa de texto OCR — `ocr:`

Pesquisa no **texto das páginas** extraído pelo OCR, não apenas nas colunas.

```
ocr: Versandkosten
ocr: "purchase order PO-12345"
ocr: Hamburg AND doc_type=INVOICE
```

### Pesquisa em linguagem natural (IA) — `ai:`

Descreva em linguagem normal o que procura; a IA lê a frase e extrai filtros
(fornecedor, datas, valores) numa consulta estruturada.

```
ai: invoices from Ruiz over 1000 last quarter
ai: overdue invoices waiting on approval
```

---

### Receitas

| Você quer… | Escreva isto |
|------------|--------------|
| Pronto a validar, totalmente conciliado | `status=ready_for_validation AND po_match_status=full_matched` |
| Este fornecedor, esta semana | `supplier_name=Test AND created_on>today()-7` |
| Faturas vencidas de valor elevado | `total_amount>5000 AND invoice_due_date<today()` |
| Dois fornecedores ao mesmo tempo | `supplier_name=fuji OR supplier_name=acme` |
| Documentos com erro de hoje | `(status=error OR status=failed) AND created_on>today()-1` |
| Por prefixo de número de encomenda | `purchase_order=PO-2026` |

> Os campos laranja (texto completo) e os filtros inteligentes de PO exigem a
> **pesquisa de texto completo** ativada.
