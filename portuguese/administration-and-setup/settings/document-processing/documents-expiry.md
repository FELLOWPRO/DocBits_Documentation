# Validade dos documentos

<figure><img src="../../../.gitbook/assets/document_expiry_settings_overview.png" alt="Configurações de Documents Expiry"><figcaption><p>Configurações de Documents Expiry</p></figcaption></figure>

Em **Document Processing → Documents Expiry** você controla por quanto tempo o DocBits mantém seus documentos antes de excluí-los automaticamente. Isso ajuda a gerenciar o armazenamento, aplicar políticas de retenção de dados e manter a conformidade com regras legais ou organizacionais sobre por quanto tempo os documentos podem ser armazenados.

Duas configurações controlam a exclusão automática:

| Configuração | O que ela controla |
|---------|------------------|
| **Delete document after** | Por quanto tempo qualquer documento processado é mantido antes de ser excluído automaticamente. |
| **Delete finished document after** | Por quanto tempo um documento concluído (totalmente processado e exportado) é mantido antes de ser excluído automaticamente. |

Para cada configuração, você escolhe um período na lista suspensa:

<figure><img src="../../../.gitbook/assets/document_expiry_options.png" alt="Opções de Documents Expiry"><figcaption><p>Períodos de retenção disponíveis</p></figcaption></figure>

| Opção | Significado |
|--------|---------|
| **Default** | Usa o período de retenção padrão do sistema (sem substituição personalizada). |
| **48 Hours** | Exclui 48 horas após o processamento. |
| **1 Week** | Exclui após uma semana. |
| **2 Weeks** | Exclui após duas semanas. |
| **4 Weeks** | Exclui após quatro semanas. |

Ambas as configurações garantem que os documentos não sejam mantidos no sistema por mais tempo do que o necessário. Isso evita o uso desnecessário de armazenamento e mantém o fluxo de documentos organizado. Elas são especialmente importantes para organizações que precisam seguir requisitos regulatórios específicos de retenção de documentos.
