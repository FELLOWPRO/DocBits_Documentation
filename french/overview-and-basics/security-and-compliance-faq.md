# DocBits (FELLOWPRO AG) — Questionnaire de Sécurité et Conformité

**Fournisseur:** DocBits par FELLOWPRO AG | **Hébergement:** Francfort, Allemagne | **Certifiée ISO 27001** | **Date:** 2026-03-04

---

## Légende du Statut

| Symbole | Signification |
|---------|---------|
| ✅ Confirmé | Réponse vérifiée à partir de la documentation officielle de DocBits ou de sources publiques |
| ✅ Partiel | Réponse partielle ; détails supplémentaires nécessaires de la part de l'équipe DocBits |
| ❓ À Confirmer | Aucune information publique disponible — doit être confirmée directement auprès de DocBits/FELLOWPRO |
| ⚠️ Nécessite Clarification | Les informations publiques soulèvent des préoccupations ou des ambiguïtés qui nécessitent une clarification explicite du fournisseur |

---

## 🔹 Localisation et Résidence des Données

### 1. Où exactement l'environnement de production est-il hébergé?

**Réponse:** Hébergé sur l'infrastructure cloud AWS à Francfort, Allemagne. Utilise S3 pour le stockage et OpenSearch pour l'indexation des journaux. DocBits est certifiée ISO 27001. Toutes les connexions sécurisées via SSH, HTTPS et protocoles de chiffrement standards du secteur.

**Statut:** ✅ Confirmé

**Notes:** AWS Francfort confirmé (S3 + OpenSearch). Demander le code spécifique de la région AWS (eu-central-1) et si c'est une seule ou multi-AZ.

---

### 2. Où l'environnement de DR (Récupération d'Urgence) est-il hébergé?

**Réponse:** DR utilise une localisation de sauvegarde secondaire à Amsterdam, Pays-Bas (UE). Combiné avec le site principal de Francfort, cela fournit une redondance géographique au sein de l'UE.

**Statut:** ✅ Confirmé

**Notes:** Francfort (principal) + Amsterdam (secondaire). Tous les emplacements en UE. Demander les objectifs RTO/RPO et les détails du processus de basculement.

---

### 3. Où les sauvegardes sont-elles stockées?

**Réponse:** Les sauvegardes sont stockées dans deux localités de l'UE:
- **Principal:** Francfort, Allemagne
- **Secondaire:** Amsterdam, Pays-Bas

Calendrier de sauvegarde: Sauvegardes quotidiennes, hebdomadaires, trimestrielles et annuelles.

**Statut:** ✅ Confirmé

**Notes:** Calendrier complet de sauvegarde (quotidienne/hebdomadaire/trimestrielle/annuelle) sur deux localités de l'UE. Toutes les données restent au sein de l'UE. Confirmer le chiffrement des sauvegardes et la fréquence des tests de restauration.

---

### 4. Existe-t-il des options de partitionnement géographique (par exemple, uniquement UK)?

**Réponse:** Deux régions de centre de données disponibles:
- **Francfort, Allemagne** — pour tous les clients de l'UE
- **New York, USA** — pour les clients américains uniquement

Les données des clients de l'UE sont hébergées exclusivement à Francfort. Aucune option uniquement pour le UK n'est actuellement disponible.

**Statut:** ✅ Confirmé

**Notes:** Les clients de l'UE sont limités à Francfort — pas de mélange de données interrégionales. L'hébergement uniquement pour le UK n'est pas disponible ; les clients du UK seraient servis depuis Francfort. Clarifier si des régions supplémentaires sont prévues.

---

### 5. Les données sont-elles chiffrées au repos et en transit?

**Réponse:** Toutes les connexions entre les composants sont sécurisées en utilisant les protocoles de chiffrement standards du secteur (SSH, HTTPS). La certification ISO 27001 mandate les contrôles de chiffrement.

**Statut:** ✅ Confirmé

**Notes:** Confirmer les standards de chiffrement spécifiques (par exemple, AES-256 au repos, TLS 1.2+ en transit).

---

## 🔹 Gestion des Modèles IA/ML

### 6. Les contenus des factures sont-ils envoyés à un hôte de modèle tiers (par exemple, OpenAI, Azure AI)?

**Réponse:** Les modèles IA ne sont PAS envoyés à des hôtes tiers. DocBits utilise des modèles Mistral AI fonctionnant à Francfort, Allemagne — même localisation que l'environnement de production. Aucune donnée ne quitte la région de Francfort pour le traitement de l'IA.

**Statut:** ✅ Confirmé

**Notes:** Modèles Mistral hébergés à Francfort. Aucun appel d'API tiers pour le traitement des documents. Totalement autonome.

---

### 7. Les documents extraits sont-ils utilisés pour entraîner des modèles plus larges entre les clients?

**Réponse:** Oui — DocBits utilise une « intelligence collective de l'IA » qui entraîne les modèles de classification et d'extraction à travers tous les clients. Cependant, la technologie fonctionne comme une carte à travers les données — elle apprend les coordonnées/positions structurelles des champs de données sur les documents, PAS le contenu réel des documents. Les données brutes des documents ne sont pas partagées entre les locataires.

**Statut:** ✅ Confirmé

**Notes:** L'intelligence collective apprend les modèles de disposition structurale (coordonnées de champs/positions), pas le contenu des documents. Cela signifie qu'aucune donnée client (montants des factures, noms des fournisseurs, etc.) n'est partagée entre les locataires — uniquement la connaissance de la structure des documents.

---

### 8. Pouvez-vous restreindre l'entraînement du modèle à votre locataire uniquement?

**Réponse:** Aucune option d'isolement du modèle par locataire. Cependant, les modèles IA partagés apprennent uniquement les coordonnées de disposition des documents et les modèles structurels — pas le contenu réel des documents ou les données commerciales. Les clients peuvent également entraîner des types de documents personnalisés limités à leur propre locataire.

**Statut:** ✅ Confirmé

**Notes:** Risque faible: Les modèles partagés apprennent uniquement les données positionnelles/structurelles (coordonnées), pas le contenu commercial. L'entraînement du type de document personnalisé reste limité au locataire.

---

### 9. Où les modèles IA/ML sont-ils hébergés et exécutés?

**Réponse:** Les modèles IA/ML (Mistral) sont hébergés et exécutés à Francfort, Allemagne — même région que l'environnement de production.

**Statut:** ✅ Confirmé

**Notes:** Bon: Le traitement de l'IA reste à Francfort. Aucun transfert de données vers l'infrastructure IA externe.

---

### 10. Quelles technologies IA/ML sont utilisées (moteur OCR, LLM, NLP)?

**Réponse:** DocBits utilise l'IA, l'OCR, l'apprentissage automatique pour l'extraction. Supporte 120+ langues. Revendique une précision de 96%+. Utilise également l'IA générative pour la fonctionnalité « Balises IA ».

**Statut:** ✅ Partiel

**Notes:** Demander les détails spécifiques du modèle: OCR propriétaire vs. tiers, quel LLM alimente les fonctionnalités d'IA générative.

---

### 11. Existe-t-il une option pour le déploiement du modèle IA sur site?

**Réponse:** La documentation d'architecture DocBits référence à la fois les options de déploiement « Client Cloud de DocBits » et « DocBits Sur site ».

**Statut:** ✅ Partiel

**Notes:** Confirmer la portée de l'option sur site: Inclut-elle le traitement complet de l'IA ou uniquement le stockage des documents?

---

## 🔹 Accès aux Données et Journalisation

### 12. Qui (support fournisseur/ingénieurs) peut accéder aux documents bruts et aux données Infor LN?

**Réponse:** FELLOWPRO AG dispose d'un Responsable de la Protection des Données (Daniel Jordan) désigné. Des DPAs avec des sous-traitants sont en place conformément au RGPD. ISO 27001 mandate les contrôles d'accès.

**Statut:** ✅ Partiel

**Notes:** Demander à DocBits: Liste exacte des rôles du personnel ayant accès aux documents bruts. L'accès est-il basé sur le besoin / à la demande uniquement?

---

### 13. Quels contrôles d'accès et journalisations existent pour le personnel du fournisseur?

**Réponse:** La certification ISO 27001 nécessite des contrôles d'accès documentés, des pistes d'audit et des mesures de sécurité. DocBits maintient une piste d'audit pour la conformité et l'examen.

**Statut:** ✅ Partiel

**Notes:** Demander: Détails RBAC, exigences MFA, gestion des accès privilégiés (PAM), et si l'accès est enregistré avec des pistes d'audit immuables.

---

### 14. Combien de temps les journaux d'accès sont-ils conservés?

**Réponse:** Les journaux sont stockés sur AWS S3 à Francfort et OpenSearch. Les journaux accessibles aux clients sont retenus pendant 30 jours. Les journaux internes sont retenus pendant 3 mois.

**Statut:** ✅ Confirmé

**Notes:** S3 + OpenSearch à Francfort. Rétention de 30 jours client / 3 mois interne. Confirmer si les journaux sont immuables/protégés contre la falsification.

---

### 15. Combien de temps les documents téléchargés / données extraites sont-ils conservés dans DocBits?

**Réponse:** Les clients peuvent configurer la rétention des données dans les paramètres. Options: 30 jours ou 3 mois. Après la période configurée, les documents et les données extraites sont automatiquement supprimés des serveurs DocBits.

**Statut:** ✅ Confirmé

**Notes:** Rétention configurable par le client (30 jours / 3 mois). Confirmer: La suppression inclut-elle toutes les copies (S3, OpenSearch, données d'entraînement IA)?

---

### 16. Les clients peuvent-ils demander la suppression des données à la demande?

**Réponse:** FELLOWPRO AG se conforme aux droits des personnes concernées du RGPD, y compris les demandes d'effacement. Le DPO traite ces demandes conformément à l'article 17 du RGPD.

**Statut:** ✅ Confirmé

**Notes:** Confirmer: La suppression couvre-t-elle toutes les copies, y compris les sauvegardes et les données d'entraînement IA dérivées du locataire?

---

### 17. Quels sous-traitants ont accès aux données des clients?

**Réponse:** Cloudflare est utilisé pour la protection anti-bot/DDoS. Des DPAs sont en place avec tous les sous-traitants conformément aux exigences du RGPD.

**Statut:** ✅ Partiel

**Notes:** Demander la liste complète des sous-traitants. Cloudflare confirmé; demander le fournisseur d'hébergement cloud, les fournisseurs de services IA, etc.

---

### 18. Quelles certifications et cadres de conformité DocBits détient-il?

**Réponse:** Certifiée ISO 27001. Conforme au RGPD. Maintient des DPAs avec tous les sous-traitants. DPO désigné.

**Statut:** ✅ Confirmé

**Notes:** Demander: SOC 2 Type II? Rapports de test de pénétration? ISO 27701 (confidentialité)? Calendrier d'audit annuel?

---

## 🔹 Portée de l'Intégration (Infor LN)

### 19. Quelle est la liste exacte des champs de données extraits de LN pour la validation?

**Réponse:** Données principales importées via BODs Infor:
- **Fournisseurs:** Sync.SupplierPartyMaster, Sync.RemitToPartyMaster
- **Commandes d'Achat:** Sync.PurchaseOrder
- **Plan Comptable:** Sync.CodeDefinition (ChartOfAccounts)
- **Dimensions Flexibles:** Sync.CodeDefinition (FlexDimensions)
- **Codes Fiscaux:** via publication BOD

**Statut:** ✅ Confirmé

**Notes:** Demander à DocBits la liste BOD complète et la documentation de mappage au niveau des champs pour votre configuration LN spécifique.

---

### 20. Quels champs d'en-tête spécifiques sont exportés vers LN?

**Réponse:** Les champs d'export d'en-tête incluent: SupplierCode, PurchaseType, InvoiceType, InvoiceNumberSupplier, InvoiceDate, InvoiceAmount, InvoiceCurrency, RateDeterminer, RateDate, TaxCountry, TransactionEntryDate, Reference, IDMReference, TaxBaseAmount, InvoiceDocumentType, et plus.

**Statut:** ✅ Confirmé

**Notes:** Examiner le fichier de mappage des champs pour votre environnement spécifique. Confirmer que tous les champs statiques correspondent à la configuration de votre société LN.

---

### 21. Les opérations d'écriture sont-elles limitées aux objets d'interface AP/PO uniquement?

**Réponse:** L'export utilise le BOD Sync.CaptureDocument qui est transformé en BODs cibles (par exemple, BODs de facture AP) dans ION Desk. Les données sont également exportées vers Infor IDM pour l'archivage des documents.

**Statut:** ✅ Partiel

**Notes:** Confirmer: DocBits écrit-il UNIQUEMENT aux objets de facture AP et de reçu de bon de commande? D'autres modules LN touchés? Quelle est la portée d'écriture IDM?

---

### 22. Quelle méthode d'intégration est utilisée (ION API, BODs, BD directe)?

**Réponse:** Intégration via Infor ION API, ION Desk et BODs Infor standard. Aucun accès direct à la base de données. Utilise les fichiers ION API et les comptes de service pour l'authentification.

**Statut:** ✅ Confirmé

**Notes:** Bon: Aucun accès BD direct. Toute la communication via la couche d'intégration Infor standard.

---

### 23. Quelle authentification/autorisation est utilisée pour la connectivité LN?

**Réponse:** Utilise les Fichiers ION API (informations d'identification du client OAuth2) avec les ID Client ION API et les comptes de service créés dans InforOS.

**Statut:** ✅ Confirmé

**Notes:** Assurer que les comptes de service suivent le principe du moindre privilège. Examiner les permissions accordées à l'utilisateur ION API de DocBits.

---

### 24. Le transfert de données entre DocBits et LN est-il chiffré de bout en bout?

**Réponse:** Toutes les connexions entre les composants sont sécurisées en utilisant le chiffrement standards du secteur (SSH, HTTPS).

**Statut:** ✅ Confirmé

**Notes:** La communication ION API utilise HTTPS/TLS. Confirmer la version TLS minimale (1.2+).

---

### 25. Quels types de documents sont supportés au-delà des factures AP?

**Réponse:** Supporte les factures, bordereaux de livraison/factures, devis, confirmations de commande, contrats, et plus. Gère les factures liées aux bons de commande et hors bons de commande.

**Statut:** ✅ Confirmé

**Notes:** Clarifier quels types de documents sont écrits vers LN par rapport à ceux uniquement stockés dans IDM.
