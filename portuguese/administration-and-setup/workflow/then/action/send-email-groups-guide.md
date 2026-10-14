# Send Email to Groups

Estes cartões ficam no grupo **Then** do Construtor de fluxos de trabalho — as ações executadas assim que as condições When/And são atendidas:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Os cartões são adicionados ao grupo <strong>Then</strong> através de <strong>Add Card</strong>.</p></figcaption></figure>

## Objetivo
Este cartão envia automaticamente notificações por e-mail a grupos de utilizadores. Em vez de atribuir trabalho a pessoas individuais, envia a mensagem a um grupo, e todos os membros desse grupo a recebem.

**Exemplo do mundo real:** Quando chega uma fatura de valor elevado, enviar automaticamente uma notificação por e-mail a todos os membros do grupo "Finance Team" para que tenham conhecimento de que necessita de revisão.

---

## Quando utilizar este cartão

Utilize este cartão quando precisar de:
- Notificar várias pessoas ao mesmo tempo
- Enviar alertas a grupos de equipas
- Difundir atualizações a departamentos
- Notificar grupos sobre alterações de estado de documentos
- Enviar lembretes aos membros de um grupo

**Cenários comuns:**
- Notificar a equipa de aquisições sobre novos fornecedores
- Alertar a equipa financeira sobre faturas de valor elevado
- Notificar a equipa do armazém sobre expedições
- Difundir alterações de estado de documentos

---

## Como funciona

1. **Condition Check**: O fluxo de trabalho verifica as condições "Where" e "And"
2. **Prepare Email**: O sistema prepara o e-mail utilizando o modelo
3. **Get Group Members**: O sistema encontra todos os membros do grupo especificado
4. **Send**: O e-mail é enviado a cada membro do grupo
5. **Log**: O envio do e-mail é registado

---

## Parâmetros explicados

### Email Template
A mensagem de e-mail a enviar

**Opções:**
- Escolher entre os modelos existentes
- Cada modelo tem assunto, corpo e formatação predefinidos
- Os modelos podem incluir marcadores de posição como {document_number}, {supplier_name}

**Modelo de exemplo:**
```
Subject: Document {document_number} requires review

Body:
Dear Team,

A new invoice has arrived and requires review:
- Document: {document_number}
- Supplier: {supplier_name}
- Amount: {amount} {currency}
- Date: {date}

Please login to DocBits to review.

Best regards,
DocBits Automation
```

### Group
O grupo de utilizadores a quem enviar o e-mail

**Grupos de exemplo:**
- Finance Team
- Procurement Team
- Warehouse Team
- Approval Committee
- Management Group

---

## Passos de configuração

### Passo 1: Escolher o modelo de e-mail
1. Clique em "Select Email Template"
2. Escolha o modelo na lista
3. Verifique o assunto e o conteúdo

### Passo 2: Selecionar o grupo
1. Clique em "Select Group"
2. Escolha o grupo que pretende notificar
3. Verifique os membros do grupo (normalmente mostra a contagem)

### Passo 3: Definir as condições
1. Adicione a condição: "When [condition] is true"
2. Exemplo: "When invoice amount is greater than €5000"

### Passo 4: Testar
1. Teste com um documento de amostra
2. Verifique se o e-mail é enviado ao grupo
3. Verifique a apresentação do modelo

---

## Exemplos de modelos de e-mail

### Modelo 1: Alerta de fatura de valor elevado
```
Subject: High-Value Invoice Alert - {document_number}

Body:
Team,

An invoice exceeding €10,000 has been received:

Document Number: {document_number}
Supplier: {supplier_name}
Amount: {amount} EUR
Received Date: {date}
Status: {status}

This requires immediate review and approval.

---
Sent automatically by DocBits
```

### Modelo 2: Alteração do estado do fornecedor
```
Subject: Supplier Status Update - {supplier_name}

Body:
Procurement Team,

The following supplier's status has been updated:

Supplier: {supplier_name}
Supplier Code: {supplier_code}
New Status: {status}
Effective Date: {date}

Please update your systems accordingly.

---
Sent automatically by DocBits
```

### Modelo 3: Documento pronto para exportação
```
Subject: Document Approved for Export - {document_number}

Body:
Export Team,

The following document has been approved and is ready for export:

Document Number: {document_number}
Invoice Number: {invoice_number}
Supplier: {supplier_name}

Please proceed with export to {destination_system}.

---
Sent automatically by DocBits
```

---

## Casos de utilização comuns

### Caso de utilização 1: Alertas de controlo de qualidade
**Acionador:** Quando é encontrada uma discrepância entre a fatura e a PO

**Grupo de e-mail:** Quality Team

**Conteúdo:**
```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### Caso de utilização 2: Notificações de aprovação
**Acionador:** Quando o documento atinge um determinado estado

**Grupo de e-mail:** Approval Committee

**Conteúdo:**
```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### Caso de utilização 3: Notificações de exceção
**Acionador:** Quando as condições não são cumpridas

**Grupo de e-mail:** Managers

**Conteúdo:**
```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### Caso de utilização 4: Atualizações de estado
**Acionador:** Quando o estado do documento muda

**Grupo de e-mail:** Equipa responsável pelo passo seguinte

**Conteúdo:**
```
Document {number} status changed to: {status}
Assigned to: {assigned_user}
Next steps: {next_steps}
```

---

## Resolução de problemas

### "E-mail não recebido"

**Causas possíveis:**
- [ ] Os utilizadores do grupo não têm endereços de e-mail
- [ ] O e-mail foi bloqueado pelo filtro de spam
- [ ] O endereço de e-mail no grupo está incorreto
- [ ] O grupo não tem membros

**Soluções:**
1. Verifique se todos os membros do grupo têm endereços de e-mail
2. Verifique a pasta de spam/lixo
3. Verifique se a composição do grupo está correta
4. Adicione utilizadores ao grupo, caso estejam em falta
5. Confirme com a TI se o serviço de e-mail está a funcionar

### "O modelo não é apresentado corretamente"

**Causa:** Variáveis de marcador de posição não encontradas

**Solução:**
- [ ] Verifique se os nomes dos campos correspondem exatamente
- [ ] Verifique se o campo tem um valor no documento
- [ ] Utilize o formato de marcador de posição correto: {field_name}
- [ ] Teste com um documento de amostra que tenha todos os campos

### "Algumas pessoas recebem o e-mail, outras não"

**Causa:** Composição de grupo incompleta ou e-mails inválidos

**Soluções:**
- [ ] Verifique se todos os membros têm um e-mail válido
- [ ] Verifique se alguns utilizadores optaram por não receber
- [ ] Verifique se a composição do grupo está atualizada
- [ ] Contacte a TI para validar os endereços de e-mail

### "Pretende adicionar/remover pessoas do grupo"

**Solução:**
- Contacte o seu administrador
- Os grupos são geridos nas definições do sistema
- Não podem ser alterados a partir deste cartão
- Solicite alterações à composição do grupo junto da TI

---

## Personalização do modelo de e-mail

### Marcadores de posição disponíveis
```
{document_number} - Document ID
{invoice_number} - Invoice ID
{supplier_name} - Supplier name
{supplier_code} - Supplier code
{amount} - Invoice amount
{currency} - Currency (EUR, USD, etc.)
{date} - Document date
{status} - Current status
{assigned_user} - Assigned person
{assigned_group} - Assigned group
{next_steps} - What needs to happen next
{reason} - Reason for exception/alert
{comment} - Comments or notes
```

### Criar marcadores de posição personalizados
Se precisar de dados adicionais nos e-mails:
1. Contacte o seu administrador
2. Solicite um novo marcador de posição
3. Adicione o campo necessário ao documento
4. Atualize o modelo de e-mail

---

## Boas práticas

✅ **Faça:**
- Mantenha o conteúdo do e-mail breve e claro
- Inclua itens de ação (o que os destinatários devem fazer?)
- Inclua uma ligação ou instruções para aceder ao documento
- Teste o modelo com dados de amostra
- Envie para o grupo certo (não notifique em excesso)
- Utilize modelos para garantir consistência

❌ **Não faça:**
- Enviar demasiados e-mails (fadiga de notificações)
- Incluir dados sensíveis nos e-mails
- Enviar a grupos que não precisam da informação
- Utilizar linhas de assunto pouco claras
- Esquecer-se de incluir como tomar uma ação
- Enviar e-mails a pessoas individuais (utilize antes um grupo)

---

## Notas de desempenho

- Cada e-mail demora cerca de 1 segundo a ser enviado
- Os grupos grandes podem demorar (100 pessoas = ~100 segundos)
- Não crie ciclos que enviem milhares de e-mails
- Monitorize a capacidade do serviço de e-mail
- Considere o envio em lotes se houver muitos documentos

---

## Cartões relacionados

- **ACTION_SEND_EMAIL** - Enviar a uma pessoa individual
- **ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP** - Atribuir uma tarefa em vez de apenas notificar
- **ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL** - Criar uma tarefa e notificar
- **STAUS_CHANGE** - Alterar o estado e notificar

---

## Exemplo de fluxo de trabalho típico

```
Document Arrives
    ↓
Check Condition: "Is amount > €10,000?"
    ↓
YES: Send Email to Finance Team
     "High value invoice alert"
    ↓
Send Email to Procurement Team
     "New invoice from supplier"
    ↓
Workflow Continues
```

---

## Perguntas frequentes

**P: Posso enviar para vários grupos?**
R: Crie cartões separados para cada grupo

**P: E se o e-mail de alguém for devolvido?**
R: O e-mail é registado como falhado; a TI pode investigar

**P: Posso alterar o modelo de e-mail?**
R: Contacte o seu administrador para modificar os modelos

**P: Posso enviar com base em condições?**
R: Sim! Utilize as condições "Where" e "And" para controlar quando os e-mails são enviados

**P: Como sei se o e-mail foi recebido?**
R: Verifique os registos de e-mail no DocBits para conhecer o estado do envio
