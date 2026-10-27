# Verificar a sincronização de dados

Utilize esta vista quando faltar um fornecedor, uma encomenda ou outro dado mestre. Mostra a hora de sincronização registada por tipo na organização atual, não o conteúdo de todos os registos importados.

## Passo a passo

1. Confirme organização, suborganização relevante e empresa de origem do ERP.
2. Abra **Definições → Registo de atividade → Sincronização de dados**. As versões antigas colocam a vista nas definições dos registos.
3. Localize o tipo em **Data Type** e leia **Last Synchronization Time** no formato de data configurado. As atualizações recentes surgem primeiro.
4. Compare a hora com a alteração esperada na origem. Uma atualização recente de fornecedores não comprova encomendas atualizadas.
5. Procure o identificador em falta nos dados mestres ou encomendas. Compare empresa, número de fornecedor/encomenda e identificadores das linhas com a origem.
6. Verifique canal de importação e registos: mensagem de origem, organização de destino, mapeamento e resposta. Corrija a causa na integração; esta vista não tem botão para iniciar ou repetir.
7. Após a atualização corrigida, atualize a vista e volte a abrir a pesquisa ou documento. Verifique hora e valores reais.

## Interpretação

| Observação | Próxima verificação |
| --- | --- |
| Sem linhas | Organização, configuração de importação e sincronizações registadas. Vazio não significa concluído com êxito. |
| Um tipo desatualizado | Analise esse fluxo independentemente das outras linhas. |
| Aviso de dados antigos | O aviso atual pode surgir sem linhas ou se todas as atualizações tiverem mais de duas semanas. O processo pode exigir dados muito mais recentes. |
| Hora recente, registo ausente | Âmbito da origem, identificadores, conteúdo, mapeamento e resposta. A hora não comprova integridade. |

Para suporte, conserve ambiente, organização, tipo, identificador, hora esperada e erro ou ID de rastreio exato com provas relevantes anonimizadas.

Consulte [Importar dados mestres](../../../infor-integration-and-configuration/importing-customer-master-data/README.md), [Registo de atividade](README.md) e [Pesquisa de dados mestres](../document-processing/master-data-lookup.md).
