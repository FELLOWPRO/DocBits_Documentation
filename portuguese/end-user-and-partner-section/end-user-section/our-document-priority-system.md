# Nosso Sistema de Prioridade de Documentos

Em nosso sistema de processamento de documentos, lidamos com um grande volume de documentos de múltiplos clientes diariamente. Para garantir que os documentos de cada cliente sejam processados de maneira oportuna, implementamos um sofisticado sistema de prioridade. Este sistema ajusta dinamicamente as prioridades com base no número de documentos pendentes que um cliente possui, garantindo **justiça** e **eficiência**. Vamos explorar como esse sistema de prioridade funciona e quando o contador de tarefas é redefinido.

**Conceitos Chave do Sistema de Prioridade**

Nosso sistema de prioridade gira em torno de alguns conceitos chave:

1. **Documentos Pendentes**: Esta é uma contagem dos documentos que um cliente enviou, mas que ainda não foram processados.
2. **Intervalo de Redefinição**: O sistema redefine periodicamente a contagem de documentos pendentes para zero, garantindo que nenhum cliente possa monopolizar os recursos de processamento indefinidamente.

**Como a Prioridade é Determinada**

Aqui está uma explicação passo a passo de como a prioridade para o processamento de documentos é determinada:

1. **Rastreamento de Documentos Pendentes**: Cada cliente tem uma contagem de documentos pendentes. Essa contagem nos ajuda a saber quantos documentos estão aguardando para serem processados para cada cliente.
2. **Redefinindo a Contagem**: Para manter a justiça, redefinimos a contagem de documentos pendentes para zero se um determinado período de tempo (o intervalo de redefinição) tiver passado desde a última atualização. Este intervalo é definido como 1500 segundos (ou 25 minutos) por padrão.
3. **Atualizando a Contagem**: Se o intervalo de redefinição não tiver passado, reduzimos a contagem de documentos pendentes em um a cada vez que verificamos, simulando o processamento de um documento.
4. **Definindo Prioridades**: A prioridade para o processamento de tarefas é baseada no número de documentos pendentes. Quanto menos documentos pendentes, maior a prioridade, significando que essas tarefas serão processadas mais cedo. Temos limites específicos para atribuir níveis de prioridade de 1 (maior prioridade) a 9 (menor prioridade).

**Níveis de Prioridade**

Os níveis de prioridade são atribuídos com base na contagem de documentos pendentes da seguinte forma:

* **Prioridade 9**: Se a contagem de documentos pendentes for menor que -20
* **Prioridade 8**: Se a contagem de documentos pendentes for menor que -14
* **Prioridade 7**: Se a contagem de documentos pendentes for menor que -12
* **Prioridade 6**: Se a contagem de documentos pendentes for menor que -10
* **Prioridade 5**: Se a contagem de documentos pendentes for menor que -8
* **Prioridade 4**: Se a contagem de documentos pendentes for menor que -6
* **Prioridade 3**: Se a contagem de documentos pendentes for menor que -4
* **Prioridade 2**: Se a contagem de documentos pendentes for menor que -2
* **Prioridade 1**: Se a contagem de documentos pendentes for maior ou igual a -2

{% hint style="info" %}
Em termos mais simples, à medida que o número de documentos pendentes aumenta, o nível de prioridade diminui, significando que esses documentos são processados mais tarde em comparação com outros com prioridades mais altas.
{% endhint %}

**Quando o Contador é Redefinido**

O contador de documentos pendentes é redefinido para zero se mais do que o intervalo de redefinição (**1500** segundos) tiver passado desde a última atualização. Este mecanismo garante que nenhum cliente possa acumular documentos pendentes indefinidamente e monopolizar os recursos do sistema. Ao redefinir periodicamente o contador, garantimos que cada cliente receba uma parte justa do tempo de processamento.
