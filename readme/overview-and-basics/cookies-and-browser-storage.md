# Cookies e armazenamento do navegador

Verificado em **16 de outubro de 2026** para a pergunta **4.15**. O site público, a aplicação DocBits e esta documentação utilizam cookies e serviços diferentes.

## Política e finalidades

A [Política de Privacidade do DocBits](https://docbits.com/en/privacy-policy/) contém as secções **Cookies** e **Consent with Borlabs Cookie**. Descreve consentimento, funções essenciais, proteção contra bots, Google Analytics, publicidade e Leadfeeder. As análises podem gerar relatórios sobre visitas, páginas, interações e desempenho, mas a recolha não se limita a dados anónimos agregados. A política do site, por si só, não estabelece o inventário de cookies da aplicação.

## Inventário de cookies

**Observado** significa uma nova visita sem iniciar sessão nem selecionar consentimentos opcionais. **Código** significa código ou configurações de infraestrutura analisados; não confirma os atributos de todas as respostas em produção.

| Cookie / âmbito | Finalidade e duração | Evidência e atributos de segurança |
| --- | --- | --- |
| `__cf_bm` / site e aplicação | Proteção Cloudflare contra bots; 30 minutos de inatividade | Observado: `Secure`, `HttpOnly`, `SameSite=None`. A [Cloudflare](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/) cifra as informações sobre bots, exceto as informações temporais. |
| `pll_language` / site | Preferência de idioma; cerca de um ano | Observado: `Secure`, acessível por JavaScript, `SameSite=Lax`. |
| `_lfa` / site | Análise de visitantes e empresas pelo Leadfeeder; cerca de um ano | Observado: acessível por JavaScript, `SameSite=Lax`, **sem atributo `Secure`** nesta visita. |
| Cookie de consentimento Borlabs / site | Guarda consentimentos e revogações | Declarado na política; nome, atributos implementados e duração não verificados nesta visita. |
| `session` / autenticação | Estado de sessão nos fluxos de autenticação | Valores predefinidos do código: `Secure`, `HttpOnly`, `SameSite=None`; dados Flask assinados, não cifrados. As configurações de implementação podem alterá-los. |
| `dbx_td` / autenticação | Recorda um dispositivo de confiança, se escolhido após MFA bem-sucedida; 30 dias | Código: `Secure`, `HttpOnly`, `SameSite=None`; token aleatório cujo hash é guardado no servidor. |
| `prod-sticky` / balanceamento em produção | Encaminha pedidos para o mesmo backend; duração configurada de 300 segundos | Configuração de infraestrutura confirmada; atributos do navegador não verificados. |
| `dontAsk` / aplicação | Guarda uma preferência de aviso; sem validade explícita na chamada analisada | Código: acessível por JavaScript; sem opção explícita `Secure` ou `SameSite` nessa chamada. |

Não foram observados cookies numa nova visita à documentação. É uma observação datada, não um inventário completo de fluxos autenticados, funções opcionais ou conteúdos externos incorporados. A política refere outros serviços analíticos e publicitários cujos cookies não foram confirmados. O inventário completo e a aplicação do consentimento exigem verificações separadas desses fluxos.

## Segurança e análises

`Secure` limita o envio a HTTPS. `HttpOnly` impede a leitura por JavaScript. `SameSite` controla o envio entre sites. Estes atributos não cifram o conteúdo. Não seria correto afirmar que todos os cookies são cifrados ou protegidos de forma idêntica. Os endpoints públicos suportam TLS 1.2 e 1.3; consulte [Armazenamento seguro de credenciais](secure-storage-of-credentials.md).

O armazenamento do navegador também é usado independentemente dos cookies. A configuração Grafana Faro suporta seguimento persistente de sessões, erros, métricas de desempenho e rastreios, com identificadores de utilizador e organização quando disponíveis. A recolha depende da configuração do coletor implementado. Não deve ser descrita como análise de cookies exclusivamente anónima e agregada. As preferências de idioma também usam armazenamento local.

Pode eliminar cookies e armazenamento no navegador, removendo eventualmente preferências e o reconhecimento de dispositivos de confiança. Para inventário atualizado ou questões de privacidade: **compliance@fellowpro.com**.
