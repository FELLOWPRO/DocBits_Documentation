# Guia de Diagnóstico de Exportação da API M3

### 1. Configuração Inicial

Antes de começar a solucionar problemas, certifique-se de estar familiarizado com as entradas esperadas para o endpoint M3 com o qual está trabalhando.

#### 1.1 Acessar a Documentação da API M3

* Faça login no **M3**.
* Acesse a **Seção API → Documentação da API**.
* Localize e selecione o endpoint relevante (por exemplo, `APS450MI` para exportações relacionadas a faturas).
* Escolha a função apropriada (por exemplo, `Add`).

#### 1.2 Compreender os Requisitos da API

* Revise todos os **campos obrigatórios** na documentação da API.
* Preste atenção a campos importantes como:
  * `DIVI`
  * `ACDT` (data contábil)
  * `CUCD` (código de moeda)
  * `SINO` (número da fatura do fornecedor)
* Confirme os **tipos de dados** dos campos, **maiúsculas e minúsculas**, e **regras de formatação** (por exemplo, `AAAA-MM-DD` para datas).

### 2. Testando Chamadas de API Diretamente no M3

Este passo verifica se a API M3 se comporta conforme o esperado usando entradas manuais.

#### 2.1 Gerar uma Solicitação de Teste no M3

* Na ferramenta de Documentação da API M3:
  * Preencha os dados de teste para os campos obrigatórios.
  * Clique em **Executar** para fazer a solicitação.
  * Copie o **cURL** resultante e o **corpo JSON**.

#### 2.2 Depurar Usando o Postman

* Abra o **Postman** e crie uma nova solicitação **POST**.
* Cole o corpo JSON ou cURL.
* Adicione cabeçalhos necessários (por exemplo, autorização).
* Clique em **Enviar** e observe o resultado:
  * `200 OK`: A solicitação foi bem-sucedida.
  * Erro: Revise a mensagem para detalhes sobre o que deu errado.

### 3. Comparando a API M3 com o Mapeamento do DocBits

Depois de confirmar que a API funciona com dados de teste, compare com o que o DocBits está realmente enviando.

#### 3.1 Exportar Dados de Amostra do DocBits

*   Abra a **documentação da API DocBits**:

    Use o endpoint **/export/get\_infor\_export\_api\_json**.
* Insira o **ID do Documento** de um documento problemático.
* Execute a exportação para visualizar a **carga JSON** que o DocBits enviará para o M3.

#### 3.2 Comparar Cargas da API

* Coloque o **JSON de teste do M3** e o **JSON de exportação do DocBits** lado a lado.
* Verifique:
  * **Nomes dos Campos**: Garanta que os nomes correspondam _exatamente_, incluindo maiúsculas e minúsculas (`DIVI` ≠ `divi`).
  * **Tipos de Dados**: Verifique se as strings, números e datas estão formatados corretamente.
  * **Campos Ausentes**: Identifique quaisquer campos presentes na solicitação do M3, mas ausentes no DocBits.

### 4. Solução de Problemas de Problemas Comuns

| Problema                                          | Causa Provável                                   | Solução                                                                 |
| ------------------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------- |
| Erro de campo ausente                             | Um campo obrigatório não está mapeado no DocBits | Adicione o campo ausente na configuração de exportação do DocBits.      |
| Incompatibilidade de maiúsculas do campo (`DIVI`) | O M3 é sensível a maiúsculas e minúsculas        | Use a maiúscula correta no mapeamento do campo.                         |
| Formato inválido de `accountingDate`              | Data errada ou ausente                           | Ajuste para o formato esperado pelo M3 (por exemplo, `AAAA-MM-DD`).     |
| Erro de API inesperado                            | Campos extras ou não reconhecidos                | Compare com cargas de trabalho conhecidas e limpe dados desnecessários. |

### 5. Se os Problemas Persistirem

Se o problema não for resolvido após seguir os passos acima:

1. **Documente** o problema:
   * Mensagem de erro e código de status
   * Solicitação de teste do M3 e JSON de exportação do DocBits
2. **Resuma** sua solução de problemas:
   * O que você tentou
   * Diferenças-chave observadas entre testes e cargas falhas
3. **Escale** para um desenvolvedor:
   * Inclua todos os dados e descobertas
   * Destaque áreas de problema suspeitas
