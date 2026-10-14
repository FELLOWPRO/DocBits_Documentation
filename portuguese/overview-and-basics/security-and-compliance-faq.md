# DocBits (FELLOWPRO AG) — Questionário de Segurança e Conformidade

**Fornecedor:** DocBits by FELLOWPRO AG | **Hosting:** Frankfurt, Alemanha | **ISO 27001 Certificado** | **Data:** 2026-03-04

---

## Legenda de Status

| Símbolo | Significado |
|--------|---------|
| ✅ Confirmado | Resposta verificada a partir da documentação oficial do DocBits ou fontes públicas |
| ✅ Parcial | Parcialmente respondido; detalhes adicionais necessários da equipe DocBits |
| ❓ Confirmar | Nenhuma informação pública disponível — deve ser confirmado diretamente com DocBits/FELLOWPRO |
| ⚠️ Necessita Esclarecimento | Informações públicas levantam dúvidas ou ambiguidades que requerem esclarecimento explícito do fornecedor |

---

## 🔹 Localização de Dados e Residência

### 1. Onde exatamente o ambiente de produção está hospedado?

**Resposta:** Hospedado na infraestrutura de nuvem AWS em Frankfurt, Alemanha. Utiliza S3 para armazenamento e OpenSearch para indexação de logs. DocBits é certificado ISO 27001. Todas as conexões são seguras via SSH, HTTPS e protocolos de criptografia padrão da indústria.

**Status:** ✅ Confirmado

**Notas:** AWS Frankfurt confirmado (S3 + OpenSearch). Solicite o código de região AWS específico (eu-central-1) e se é single ou multi-AZ.

---

### 2. Onde o ambiente de DR (Disaster Recovery) está hospedado?

**Resposta:** DR utiliza localização de backup secundária em Amsterdã, Países Baixos (EU). Combinado com o site principal de Frankfurt, isso fornece redundância geográfica dentro da EU.

**Status:** ✅ Confirmado

**Notas:** Frankfurt (primário) + Amsterdã (secundário). Ambos localizados na EU. Solicite detalhes sobre objetivos RTO/RPO e processo de failover.

---

### 3. Onde os backups estão armazenados?

**Resposta:** Backups armazenados em duas localizações da EU:
- **Primário:** Frankfurt, Alemanha
- **Secundário:** Amsterdã, Países Baixos

Cronograma de backup: Backups diários, semanais, trimestrais e anuais.

**Status:** ✅ Confirmado

**Notas:** Cronograma de backup abrangente (diário/semanal/trimestral/anual) em duas localizações da EU. Todos os dados permanecem dentro da EU. Confirme criptografia de backup e frequência de testes de restauração.

---

### 4. Existem opções de geo-particionamento (ex: apenas UK)?

**Resposta:** Duas regiões de data center disponíveis:
- **Frankfurt, Alemanha** — para todos os clientes da EU
- **Nova York, EUA** — apenas para clientes dos EUA

Dados de clientes da EU são hospedados exclusivamente em Frankfurt. Nenhuma opção apenas para UK disponível atualmente.

**Status:** ✅ Confirmado

**Notas:** Clientes da EU estão apenas em Frankfurt — sem mistura de dados entre regiões. Hosting apenas para UK não disponível; clientes do UK seriam atendidos a partir de Frankfurt. Esclareça se regiões adicionais estão no roadmap.

---

### 5. Os dados estão criptografados em repouso e em trânsito?

**Resposta:** Todas as conexões entre componentes são protegidas usando protocolos de criptografia padrão da indústria (SSH, HTTPS). A certificação ISO 27001 impõe controles de criptografia.

**Status:** ✅ Confirmado

**Notas:** Confirme padrões de criptografia específicos (ex: AES-256 em repouso, TLS 1.2+ em trânsito).

---

## 🔹 Tratamento de Modelos de IA/ML

### 6. Os conteúdos de faturas são enviados para qualquer host de modelo de terceiros (ex: OpenAI, Azure AI)?

**Resposta:** Modelos de IA NÃO são enviados para hosts de terceiros. DocBits utiliza modelos Mistral AI rodando em Frankfurt, Alemanha — mesma localização do ambiente de produção. Nenhum dado sai da região de Frankfurt para processamento de IA.

**Status:** ✅ Confirmado

**Notas:** Modelos Mistral hospedados em Frankfurt. Nenhuma chamada de API de terceiros para processamento de documentos. Totalmente independente.

---

### 7. Documentos extraídos são usados para treinar modelos mais amplos entre clientes?

**Resposta:** Sim — DocBits utiliza "inteligência enxame de IA" que treina modelos de classificação e extração em todos os clientes. No entanto, a tecnologia funciona como um mapa através dos dados — ela aprende as coordenadas/posições estruturais de campos de dados em documentos, NÃO o conteúdo real do documento. Dados brutos de documentos não são compartilhados entre tenants.

**Status:** ✅ Confirmado

**Notas:** Inteligência enxame aprende padrões de layout estrutural (coordenadas de campos/posições), não conteúdo de documento. Isso significa que nenhum dado de cliente (valores de faturas, nomes de fornecedores, etc.) é compartilhado entre tenants — apenas conhecimento de estrutura de documento.

---

### 8. Você pode restringir o treinamento de modelo apenas para seu tenant?

**Resposta:** Nenhuma opção de isolamento de modelo por tenant. No entanto, os modelos de IA compartilhados apenas aprendem coordenadas de layout de documento e padrões estruturais — não conteúdo real de documento ou dados de negócio. Clientes podem treinar adicionalmente tipos de documento personalizados com escopo para seu próprio tenant.

**Status:** ✅ Confirmado

**Notas:** Risco baixo: Modelos compartilhados aprendem apenas dados posicionais/estruturais (coordenadas), não conteúdo de negócio. Treinamento de tipo de documento personalizado permanece com escopo de tenant.

---

### 9. Onde modelos de IA/ML estão hospedados e executados?

**Resposta:** Modelos de IA/ML (Mistral) estão hospedados e executados em Frankfurt, Alemanha — mesma região do ambiente de produção.

**Status:** ✅ Confirmado

**Notas:** Bom: Processamento de IA permanece dentro de Frankfurt. Nenhuma transferência de dados para infraestrutura de IA externa.

---

### 10. Quais tecnologias de IA/ML são utilizadas (mecanismo OCR, LLM, NLP)?

**Resposta:** DocBits utiliza IA, OCR, aprendizado de máquina para extração. Suporta 120+ idiomas. Alega precisão de 96%+. Também utiliza Gen AI para recurso "AI Tags".

**Status:** ✅ Parcial

**Notas:** Solicite detalhes específicos do modelo: OCR proprietário vs. terceiros, qual LLM potencializa recursos Gen AI.

---

### 11. Existe uma opção para implantação de modelo de IA no local?

**Resposta:** Documentação de arquitetura DocBits faz referência a ambas as opções de implantação "DocBits Cloud customer" e "DocBits On premise".

**Status:** ✅ Parcial

**Notas:** Confirme escopo da opção no local: Inclui processamento completo de IA ou apenas armazenamento de documento?

---

## 🔹 Acesso e Registro de Dados

### 12. Quem (suporte do fornecedor/engenheiros) pode acessar documentos brutos e dados Infor LN?

**Resposta:** FELLOWPRO AG tem um Data Protection Officer designado (Daniel Jordan). DPAs com subprocessadores estão em vigor conforme GDPR. ISO 27001 impõe controles de acesso.

**Status:** ✅ Parcial

**Notas:** Solicite ao DocBits: Lista exata de funções de pessoal com acesso a documentos brutos. O acesso é apenas por necessidade / sob demanda?

---

### 13. Quais controles de acesso e registros existem para pessoal do fornecedor?

**Resposta:** Certificação ISO 27001 requer controles de acesso documentados, trilhas de auditoria e medidas de segurança. DocBits mantém trilha de auditoria para conformidade e revisão.

**Status:** ✅ Parcial

**Notas:** Solicite: Detalhes RBAC, requisitos de MFA, gerenciamento de acesso privilegiado (PAM), e se o acesso é registrado com trilhas de auditoria imutáveis.

---

### 14. Quanto tempo os logs de acesso são retidos?

**Resposta:** Logs são armazenados em AWS S3 em Frankfurt e OpenSearch. Logs acessíveis ao cliente retidos por 30 dias. Logs internos retidos por 3 meses.

**Status:** ✅ Confirmado

**Notas:** S3 + OpenSearch em Frankfurt. 30 dias de acesso do cliente / retenção interna de 3 meses. Confirme se logs são imutáveis/à prova de manipulação.

---

### 15. Quanto tempo documentos enviados / dados extraídos são retidos no DocBits?

**Resposta:** Clientes podem configurar retenção de dados em configurações. Opções: 30 dias ou 3 meses. Após o período configurado, documentos e dados extraídos são automaticamente deletados dos servidores DocBits.

**Status:** ✅ Confirmado

**Notas:** Retenção configurável pelo cliente (30 dias / 3 meses). Confirme: Exclusão inclui todas as cópias (S3, OpenSearch, dados de treinamento de IA)?

---

### 16. Clientes podem solicitar exclusão de dados sob demanda?

**Resposta:** FELLOWPRO AG está em conformidade com direitos de sujeitos de dados GDPR incluindo solicitações de exclusão. DPO processa essas solicitações conforme GDPR Art. 17.

**Status:** ✅ Confirmado

**Notas:** Confirme: Exclusão cobre todas as cópias incluindo backups e dados de treinamento de IA derivados do tenant?

---

### 17. Quais subprocessadores têm acesso aos dados do cliente?

**Resposta:** Cloudflare é utilizado para proteção contra bot/DDoS. DPAs estão em vigor com todos os subprocessadores conforme requisitos GDPR.

**Status:** ✅ Parcial

**Notas:** Solicite lista completa de subprocessadores. Cloudflare confirmado; solicite sobre provedor de hospedagem em nuvem, provedores de serviço de IA, etc.

---

### 18. Quais certificações e frameworks de conformidade o DocBits possui?

**Resposta:** Certificado ISO 27001. Conforme GDPR. Mantém DPAs com todos os subprocessadores. DPO designado.

**Status:** ✅ Confirmado

**Notas:** Solicite: SOC 2 Type II? Relatórios de teste de penetração? ISO 27701 (privacidade)? Cronograma de auditoria anual?

---

## 🔹 Escopo de Integração (Infor LN)

### 19. Qual é a lista exata de campos de dados extraídos de mestres LN para validação?

**Resposta:** Dados mestres importados via Infor BODs:
- **Fornecedores:** Sync.SupplierPartyMaster, Sync.RemitToPartyMaster
- **Ordens de Compra:** Sync.PurchaseOrder
- **Plano de Contas:** Sync.CodeDefinition (ChartOfAccounts)
- **Dimensões Flex:** Sync.CodeDefinition (FlexDimensions)
- **Códigos de Imposto:** via publicação BOD

**Status:** ✅ Confirmado

**Notas:** Solicite ao DocBits lista completa de BODs e documentação de mapeamento em nível de campo para sua configuração LN específica.

---

### 20. Quais campos de cabeçalho específicos são exportados de volta para LN?

**Resposta:** Campos de exportação de cabeçalho incluem: SupplierCode, PurchaseType, InvoiceType, InvoiceNumberSupplier, InvoiceDate, InvoiceAmount, InvoiceCurrency, RateDeterminer, RateDate, TaxCountry, TransactionEntryDate, Reference, IDMReference, TaxBaseAmount, InvoiceDocumentType, e outros.

**Status:** ✅ Confirmado

**Notas:** Revise arquivo de mapeamento de campo para seu ambiente específico. Confirme todos os campos estáticos correspondem à configuração da sua empresa LN.

---

### 21. Operações de gravação de volta estão com escopo apenas para objetos de interface AP/PO?

**Resposta:** Exportação utiliza Sync.CaptureDocument BOD que é transformado em BODs alvo (ex: BODs de fatura AP) em ION Desk. Dados também exportados para Infor IDM para arquivo de documento.

**Status:** ✅ Parcial

**Notas:** Confirme: DocBits escreve APENAS para objetos de fatura AP e recebimento PO? Qualquer outro módulo LN afetado? E quanto ao escopo de gravação IDM?

---

### 22. Qual método de integração é utilizado (ION API, BODs, DB direto)?

**Resposta:** Integração via Infor ION API, ION Desk e Infor Standard BODs. Sem acesso direto a banco de dados. Utiliza arquivos ION API e contas de serviço para autenticação.

**Status:** ✅ Confirmado

**Notas:** Bom: Sem acesso direto a DB. Toda comunicação via camada de integração Infor padrão.

---

### 23. Qual autenticação/autorização é utilizada para conectividade LN?

**Resposta:** Utiliza ION API Files (credenciais OAuth2 client) com IDs de Cliente ION API e contas de serviço criadas no InforOS.

**Status:** ✅ Confirmado

**Notas:** Garanta que contas de serviço sigam princípio de menor privilégio. Revise permissões concedidas ao usuário DocBits ION API.

---

### 24. Transferência de dados entre DocBits e LN é criptografada de ponta a ponta?

**Resposta:** Todas as conexões entre componentes são protegidas utilizando criptografia padrão da indústria (SSH, HTTPS).

**Status:** ✅ Confirmado

**Notas:** Comunicação ION API utiliza HTTPS/TLS. Confirme versão TLS mínima (1.2+).

---

### 25. Quais tipos de documento são suportados além de faturas AP?

**Resposta:** Suporta faturas, notas de entrega/comprovantes, cotações, confirmações de pedido, contratos e outros. Manipula faturas com e sem PO.

**Status:** ✅ Confirmado

**Notas:** Esclareça quais tipos de documento são gravados de volta em LN vs. apenas armazenados em IDM.
