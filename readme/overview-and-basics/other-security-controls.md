# Outros controlos de segurança

Verificado em **16 de outubro de 2026**. Distinguem-se as evidências de auditorias publicadas e o inventário atual da infraestrutura.

| Controlo | Âmbito documentado |
| --- | --- |
| Firewalls de rede | O relatório SOC 2 descreve filtros VPC/security groups da DigitalOcean e supervisão das alterações pela segurança informática. As verificações atuais apenas de leitura confirmam firewalls ativos, incluindo regras associadas a recursos Kubernetes. |
| Web Application Firewall (WAF) | A auditoria RGPD documenta uma WAF de proteção do produto. Regras geridas atuais, exclusões e cobertura de cada hostname não foram verificadas independentemente. Foram observados cookies Cloudflare contra bots no site e aplicação; isso, por si só, não comprova as regras WAF. |
| Balanceadores de carga | O inventário DigitalOcean confirma balanceadores de produção ativos em Frankfurt com verificações de integridade configuradas. Encaminhamento e afinidade de sessão são funções de infraestrutura. Consulte [Cookies e armazenamento do navegador](cookies-and-browser-storage.md). |
| Listas de IPs permitidos | As regras de infraestrutura suportam filtragem por origem. Não foram confirmados uma lista por tenant configurável pelo cliente, a cobertura ou exceções. Acorde a restrição necessária para a implementação com a FELLOWPRO. |
| Testes locais e sandbox | A [Estratégia do ciclo de versões](docbits-release-lifecycle-strategy.md) documenta desenvolvimento, QA/UAT e avaliação em sandbox antes da produção. Testes locais de integração exigem ambiente definido e dados adequados. O acesso à sandbox não autoriza por si só testes de intrusão. |
| Máquinas virtuais e Kubernetes | O relatório SOC descreve normas de hardening, acessos, portas limitadas e patches de sistemas/rede. O inventário confirma clusters Kubernetes geridos. Isso não garante configurações idênticas para todas as cargas. |
| Dispositivos e móveis | O relatório SOC descreve antimalware, verificações automáticas, atualização de assinaturas e monitorização de patches. O relatório ISO indica MDM como oportunidade de melhoria. MDM universal, eliminação remota e regras de móveis/BYOD exigem confirmação atual. Os clientes protegem os seus próprios dispositivos de navegação. |
| Políticas e procedimentos | O relatório SOC descreve políticas formais, avaliação de riscos, acessos, alterações, incidentes e formação. Solicite as políticas vigentes e o âmbito ao contacto de conformidade. |

## Evidências e mais informações

[Certificações](architecture/certifications.md) disponibiliza relatórios e períodos. As auditorias históricas sustentam os controlos no âmbito avaliado; o inventário confirma recursos presentes na data da revisão e não constitui auditoria completa da configuração.

Consulte [Armazenamento seguro de credenciais](secure-storage-of-credentials.md), [Cifragem em repouso](../security/encryption-at-rest.md) e [Gestão de vulnerabilidades](vulnerability-management.md).

Para restrições da implementação, requisitos móveis ou políticas atuais: **compliance@fellowpro.com**.
