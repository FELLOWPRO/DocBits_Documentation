# Acesso SQL

<figure><img src="../../.gitbook/assets/sql_direct_access_settings.png" alt="Configurações de acesso direto SQL"><figcaption></figcaption></figure>

## Visão geral

No módulo de configurações do DocBits, os administradores podem acessar diretamente o banco de dados de BI usando SQL. Este recurso foi projetado para gerenciamento avançado de dados e necessidades de relatórios personalizados.

### Acessando o SQL Direct Access

Navegue até a seção SQL Direct Access no módulo de configurações. Ali você encontrará as credenciais e os detalhes de acesso, incluindo nome de usuário, senha, nome do banco de dados e informações do host.

* **Nome de usuário:** user\_23f3d6
* **Senha:** _Criptografada_
* **Banco de dados:** demo
* **Host:** veja na captura de tela

## **Exemplo de detalhes de acesso:**

```sql
SELECT
    COUNT(*),
    status,
    invoice_type
FROM dashboard
GROUP BY
    status,
    invoice_type

```

#### Resultados de uma consulta de exemplo

Os resultados a seguir mostram o número de documentos por status e tipo de fatura:

* **Pronto para validação:** 71 faturas, 6 não especificados
* **Aguardando confirmação:** 1 não especificado
* **Concluído:** 3 não especificados, 1 fatura
* **Erro:** 2 não especificados

#### Usando o clickhouse-client para acesso via terminal

Para desenvolvedores que preferem usar o terminal, o acesso pode ser estabelecido por meio do `clickhouse-client`:

```bash
clickhouse-client --host <hostname_or_ip> --port <port> --user <username> --password <your_password> --database <database_name>

```

### Criando views materializadas

Recomendamos criar views materializadas para pré-calcular dados e melhorar o desempenho em ferramentas de análise como o PowerBI:

```sql
SELECT toStartOfWeek(created_on) as week_start, sum(toFloat64OrZero(field_value)) as total_sum
FROM document_extracted_data
WHERE field_name = 'total_amount'
GROUP BY week_start

```

Este exemplo mostra como agrupar os valores totais pela semana em que foram criados, o que é útil para resumos financeiros semanais ou trilhas de auditoria.

## Recursos adicionais

Para obter ajuda adicional ou configurações avançadas, entre em contato com nossa equipe de suporte ou acesse nosso treinamento completo em vídeo na seção de ajuda.
