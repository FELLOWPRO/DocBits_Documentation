# Overige beveiligingsmaatregelen

Gecontroleerd op **16 oktober 2026**. Gepubliceerd auditbewijs wordt onderscheiden van de actuele infrastructuurinventaris.

| Maatregel | Gedocumenteerd bereik |
| --- | --- |
| Netwerkfirewalls | Het SOC 2-rapport beschrijft DigitalOcean VPC/security-groupfilters en IT-beveiligingstoezicht op wijzigingen. Actuele controles met alleen leestoegang bevestigen actieve cloudfirewalls, inclusief regels voor Kubernetes-resources. |
| Web Application Firewall (WAF) | De AVG-audit vermeldt een WAF die het product beschermt. Actuele beheerde regels, uitzonderingen en dekking per hostnaam zijn niet onafhankelijk geverifieerd. Cloudflare-botcookies zijn op website en app waargenomen; dit bewijst op zichzelf niet de WAF-regels. |
| Lastverdelers | De actuele DigitalOcean-inventaris bevestigt actieve productielastverdelers in Frankfurt met ingestelde statuscontroles. Routering en sessieaffiniteit zijn infrastructuurfuncties. Zie [Cookies en browseropslag](cookies-and-browser-storage.md). |
| IP-toegestane lijsten | Infrastructuurregels ondersteunen bronfiltering. Een door klanten instelbare lijst per tenant, de dekking en uitzonderingen zijn niet bevestigd. Spreek de gewenste beperking voor uw deployment af met FELLOWPRO. |
| Lokaal testen en sandbox | De [Strategie voor de releaselevenscyclus](../overview-and-basics/docbits-release-lifecycle-strategy.md) beschrijft ontwikkeling, QA/UAT en sandboxevaluatie vóór productie. Lokale integratietests vereisen een afgebakende omgeving en geschikte testgegevens. Sandboxtoegang alleen geeft geen toestemming voor penetratietests. |
| Virtuele machines en Kubernetes | Het SOC-rapport beschrijft hardeningsnormen, toegangscontrole, beperkte poorten en OS-/netwerkpatchbeheer. De inventaris bevestigt beheerde Kubernetes-clusters. Dit garandeert geen identieke instellingen voor iedere workload. |
| Eindpunten en mobiele apparaten | Het SOC-rapport beschrijft antimalware, automatische scans, definitie-updates en patchbewaking. Het ISO-rapport noemt MDM als verbeterkans. Algemene MDM-dekking, wissen op afstand en mobiele/BYOD-regels moeten actueel worden bevestigd. Klanten beveiligen hun eigen browserapparaten. |
| Beleid en procedures | Het SOC-rapport beschrijft formeel beveiligingsbeleid, risicobeoordeling, toegang, wijzigingsbeheer, incidenten en training. Vraag actueel beleid en de reikwijdte op bij het compliancecontact. |

## Bewijs en meer informatie

[Certificeringen](../overview-and-basics/architecture/certifications.md) bevat rapporten en perioden. Historische audits onderbouwen de maatregelen voor hun onderzochte bereik; de inventaris bevestigt aanwezige resources op de controledatum en is geen volledige configuratieaudit.

Zie [Veilige opslag van inloggegevens](secure-storage-of-credentials.md), [Versleuteling van opgeslagen gegevens](encryption-at-rest.md) en [Kwetsbaarhedenbeheer](vulnerability-management.md).

Voor deploymentbeperkingen, mobiele vereisten of actueel beleid: **compliance@fellowpro.com**.
