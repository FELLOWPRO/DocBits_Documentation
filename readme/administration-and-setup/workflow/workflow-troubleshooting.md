---
description: "Diagnosticar workflows com eventos, dados de entrada, percursos escolhidos e resultados reais."
---

# Diagnosticar problemas de workflow sistematicamente

Comece por uma execução afetada. Registe organização e ambiente, nome e revisão guardada do workflow, referência documental, momento e fuso horário e mensagem exata do nó. Nas respostas de teste utilize também `execution_id`. Exclua chaves de acesso e dados de clientes desprotegidos das evidências partilhadas.

## Do sintoma à verificação

| Sintoma | Evidência | Correção e novo teste |
| --- | --- | --- |
| Sem execução | Licença, módulo, ativação, filtros temporais e evento | Corrigir entrada e filtros; repetir o evento real. Start manual não o demonstra. |
| Ação cinzenta | Resultado anterior e saída ligada | Seguir o percurso escolhido. Um nó ignorado não falhou por si. |
| Condição laranja | Chave, tipo, valor e operador lidos | Distinguir resultado negativo e erro. Testar abaixo, no limite e acima. |
| Nó vermelho | Primeiro erro e dados necessários | Corrigir dados ou configuração; repetir falha e sucesso. |
| Wait ALL não continua | Cada origem e saída de resultado ligada | Não exigir percursos exclusivos em conjunto. Demonstrar um caminho possível por origem necessária. |
| Tarefas ou exports duplicados | Repetições, eventos, estados e Run Workflow | Limitar condições e transições; testar o mesmo caso duas vezes. Verificar proteção adequada contra processamento simultâneo no destino. |
| Variável afeta outros workflows | Variável partilhada da organização | Rever dependências. Alterações persistem fora do canvas; testar novamente os workflows afetados. |
| Teste passa, efeito ausente | O que foi comparado ou simulado? | Verificar atribuição no documento, tarefa na área respetiva e receção no destino. O estado só não basta. |
| Exportação iniciada sem receção | Histórico, resposta e dados do destinatário | Diagnosticar antes de repetir; confirmar se o primeiro pedido já foi processado. |

## Interpretar mensagens

No [exemplo Advanced](advanced-workflow-case-study.md), um montante ausente segue vermelho para correção. Tratamento e OR podem ter sucesso enquanto o conjunto mantém o erro original. Uma condição normalmente falsa segue laranja e pode terminar corretamente no percurso padrão.

Duas ligações da mesma origem não são duas aprovações independentes. As uniões avaliam resultados ligados das origens. Verifique o fluxo completo: um teste parcial a partir de um nó intermédio pode omitir predecessores necessários.

## Demonstrar a correção

1. Conservar o problema original e a expectativa funcional.
2. Alterar dados ou configuração de forma específica. Mudar expectativas só quando o requisito mudar.
3. Repetir falha, caso positivo e limites afetados com o [pacote](workflow-training-kit.md).
4. Guardar a regra e verificar a ativação separadamente.
5. Comparar uma execução real nova com a anterior. Os registos antigos continuam a descrever a revisão original.

Registe causa, correção, resultado demonstrado e limitações restantes. Separe espera e execução: uma duração total elevada não identifica, por si só, um nó lento.

## WF-04: Exercício e aceitação

Comece com invalid-number. Guarde primeiro erro amount e resultado error. Repita com above e compare novas provas. Conserve o registo antigo; tratar bem o erro não basta.

[Percurso](workflow-learning-path.md)

## Repetir testes de cartão com âmbito explícito

No designer Dev analisado, repetir um teste iniciado num nó selecionado mudou para o grafo completo. Abra novamente o teste no menu de contexto do cartão pretendido e confirme os nós realmente visitados. Um resultado com seis nós não comprova um teste isolado de vazio. O contador de ações falhadas pode incluir uma condição não satisfeita: leia também a saída escolhida, o registo e o resultado global.
