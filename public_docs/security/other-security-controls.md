# Altri controlli di sicurezza

Verificato il **16 ottobre 2026**. Le evidenze degli audit pubblicati sono distinte dall'inventario attuale dell'infrastruttura.

| Controllo | Ambito documentato |
| --- | --- |
| Firewall di rete | Il report SOC 2 descrive filtri VPC/security group DigitalOcean e supervisione delle modifiche da parte della sicurezza IT. Le verifiche attuali in sola lettura confermano firewall cloud attivi, incluse regole associate a risorse Kubernetes. |
| Web Application Firewall (WAF) | L'audit GDPR documenta una WAF a protezione del prodotto. Regole gestite attuali, esclusioni e copertura di ogni hostname non sono state verificate indipendentemente. Cookie Cloudflare contro i bot sono stati osservati sul sito e nell'app; questo da solo non dimostra il set di regole WAF. |
| Bilanciatori di carico | L'inventario DigitalOcean conferma bilanciatori di produzione attivi a Francoforte con controlli di integrità configurati. Instradamento e affinità di sessione sono funzioni infrastrutturali. Vedere [Cookie e archiviazione del browser](cookies-and-browser-storage.md). |
| Liste IP consentiti | Le regole infrastrutturali consentono il filtraggio per origine. Non sono confermati una lista per tenant configurabile dal cliente, la copertura o le eccezioni. Concordare con FELLOWPRO le restrizioni del deployment. |
| Test locali e sandbox | La [Strategia del ciclo di rilascio](../overview-and-basics/docbits-release-lifecycle-strategy.md) descrive sviluppo, QA/UAT e valutazione sandbox prima della produzione. I test locali di integrazione richiedono ambiente definito e dati adeguati. L'accesso sandbox non autorizza da solo penetration test. |
| Macchine virtuali e Kubernetes | Il report SOC descrive standard di hardening, accessi, porte limitate e gestione patch di sistema/rete. L'inventario conferma cluster Kubernetes gestiti. Non garantisce impostazioni identiche per ogni carico di lavoro. |
| Dispositivi e mobili | Il report SOC descrive antimalware, scansioni automatiche, aggiornamenti delle firme e monitoraggio patch. Il report ISO indica MDM come opportunità di miglioramento. MDM universale, cancellazione remota e regole mobili/BYOD richiedono conferma attuale. I clienti gestiscono la sicurezza dei propri dispositivi di navigazione. |
| Politiche e procedure | Il report SOC descrive politiche formali, valutazione dei rischi, controlli di accesso, gestione di modifiche e incidenti e formazione. Richiedere politiche vigenti e ambito al referente compliance. |

## Evidenze e ulteriori informazioni

[Certificazioni](../overview-and-basics/architecture/certifications.md) contiene i report e i periodi esaminati. Gli audit storici sostengono i controlli per l'ambito valutato; l'inventario conferma risorse presenti alla data della verifica, non un audit completo della configurazione.

Vedere [Archiviazione sicura delle credenziali](secure-storage-of-credentials.md), [Cifratura a riposo](encryption-at-rest.md) e [Gestione delle vulnerabilità](vulnerability-management.md).

Per restrizioni del deployment, requisiti mobili o politiche attuali: **compliance@fellowpro.com**.
