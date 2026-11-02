# Fluxo de Execução On-Premise

Para os clientes que executam o Operador DocBits localmente, a sequência a seguir descreve como um documento processado aciona e executa um prompt do Operador por meio do Agente DocBits local.

1. **Upload e Processamento do Documento** Um documento é carregado no DocBits e passa pelo processamento padrão (Extração, validação, etc.).
2. **Acionador do Fluxo de Trabalho** Após a conclusão do processamento, um Fluxo de Trabalho configurado no DocBits avalia suas condições de acionamento. Quando essas condições são atendidas, o Fluxo de Trabalho cria uma nova **Tarefa do Operador**.
3. **Criação e Despacho da Tarefa**
   * O fluxo de trabalho envia o texto do script, variáveis, max-steps, max-retries como carga da tarefa para o Pool de Trabalho compartilhado.
4. **Loop de Verificação do Agente**
   * Um Agente DocBits local (instalado no ambiente do cliente) verifica o Pool de Trabalho a cada 5 minutos. Se nenhuma tarefa for encontrada, o agente permanece inativo e tenta novamente após o intervalo.
5. **Execução da Tarefa**
   * Quando uma tarefa aparece no Pool de Trabalho, o Agente a recupera e inicia a execução.
6. **Geração de Logs**
   * Para cada etapa - sucesso ou falha - o agente registra logs detalhados (ações, status, timestamps). Após a conclusão, ele compila o log completo e o status final.
7. **Retorno e Exibição de Resultados**
   * O agente envia os logs e o status de volta ao DocBits. O histórico de execução do fluxo de trabalho de origem é atualizado, e os usuários podem revisar os detalhes na guia **Logs do Fluxo de Trabalho**.
