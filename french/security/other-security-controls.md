# Autres contrôles de sécurité

Vérifié le **16 octobre 2026**. Les preuves d'audit publiées sont distinguées de l'inventaire actuel de l'infrastructure.

| Contrôle | Périmètre documenté |
| --- | --- |
| Pare-feu réseau | Le rapport SOC 2 décrit les filtres VPC/security groups de DigitalOcean et la supervision des changements par la sécurité informatique. Les vérifications actuelles en lecture seule confirment des pare-feu actifs, notamment des règles liées aux ressources Kubernetes. |
| Pare-feu applicatif web (WAF) | L'audit RGPD mentionne une WAF protégeant le produit. Les règles gérées actuelles, exclusions et couvertures par hostname n'ont pas été vérifiées indépendamment. Des cookies Cloudflare de protection contre les robots ont été observés sur le site et l'application ; ils ne suffisent pas à établir les règles WAF. |
| Répartiteurs de charge | L'inventaire DigitalOcean confirme des répartiteurs de production actifs à Francfort avec des contrôles de santé configurés. Routage et affinité de session relèvent de l'infrastructure. Voir [Cookies et stockage du navigateur](cookies-and-browser-storage.md). |
| Listes d'adresses IP autorisées | Les règles d'infrastructure permettent le filtrage par source. Une liste IP par tenant configurable par le client, sa couverture et ses exceptions n'ont pas été confirmées. Convenez de la restriction souhaitée avec FELLOWPRO pour le déploiement. |
| Tests locaux et sandbox | La [Stratégie du cycle des versions](../overview-and-basics/docbits-release-lifecycle-strategy.md) décrit développement, QA/UAT et évaluation en sandbox avant production. Les tests d'intégration locaux nécessitent un environnement défini et des données adaptées. L'accès à la sandbox n'autorise pas à lui seul les tests d'intrusion. |
| Machines virtuelles et Kubernetes | Le rapport SOC décrit durcissement, contrôle d'accès, ports restreints et gestion des correctifs système/réseau. L'inventaire confirme des clusters Kubernetes gérés. Cela ne garantit pas des paramètres identiques pour chaque charge de travail. |
| Postes et appareils mobiles | Le rapport SOC décrit antimalware, scans automatiques, mises à jour des signatures et suivi des correctifs. Le rapport ISO présente MDM comme une piste d'amélioration. MDM généralisé, effacement à distance et règles mobiles/BYOD nécessitent donc une confirmation actuelle. Les clients sécurisent leurs propres appareils de navigation. |
| Politiques et procédures | Le rapport SOC décrit des politiques formelles de sécurité, l'évaluation des risques, les accès, changements, incidents et la formation. Demandez les politiques en vigueur et leur périmètre au contact conformité. |

## Preuves et informations complémentaires

[Certifications](../overview-and-basics/architecture/certifications.md) donne accès aux rapports et à leurs périodes. Les audits historiques étayent les contrôles pour leur périmètre évalué ; l'inventaire confirme la présence de ressources à la date de vérification, sans être un audit complet de configuration.

Voir [Stockage sécurisé des identifiants](secure-storage-of-credentials.md), [Chiffrement au repos](encryption-at-rest.md) et [Gestion des vulnérabilités](vulnerability-management.md).

Pour les restrictions du déploiement, exigences mobiles ou politiques actuelles : **compliance@fellowpro.com**.
