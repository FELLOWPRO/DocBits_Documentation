# Notes de version DocBits — 26–30 juin 2026

_Ce que cette mise à niveau de production a apporté, en langage clair. Chaque
service indique la version désormais en ligne en production. Les services non
répertoriés n'ont connu aucune modification visible par le client durant cette
période._

---

## Points forts

- **Une seule connexion pour les assistants IA ([DocBits MCP](https://docs.docbits.com/advanced-functions-and-tools/docbits-mcp)).** Une passerelle
  unique et unifiée dessert désormais tous les outils DocBits — y compris DocFlow —
  via l'API principale, de sorte que les assistants IA (Claude, Gemini CLI, Codex)
  se connectent par un unique point de terminaison fiable au lieu de plusieurs.
- **Une recherche multilingue plus intelligente dans le tableau de bord.** Les
  connecteurs de recherche (**AND / OR**) apparaissent désormais dans votre langue
  avec une mise en évidence par couleur, les sous-types de factures proposent une
  liste déroulante de valeurs, et les messages relatifs à la syntaxe de recherche
  sont localisés — le tout avec une gestion du clavier plus fluide.
- **Des approbations et des autorisations plus fluides.** L'approbation n'est plus
  déclenchée lorsque l'unité de conditionnement d'une confirmation de commande est
  vide, les utilisateurs normaux peuvent de nouveau approuver les éléments de coût
  après la migration du contrôle d'accès, et les autorisations au niveau du
  document s'appliquent correctement même lorsqu'une colonne de table existe déjà.
- **L'application se met à jour d'elle-même.** Lorsqu'une nouvelle version est
  déployée, DocBits s'actualise désormais automatiquement au lieu de vous
  interrompre avec une fenêtre « Actualiser maintenant ».
- **Un rapprochement de bons de commande plus robuste.** Les transformations de
  valeurs de colonnes, les protections contre les plantages pour les lignes
  dépourvues de prix ou de quantité, et la nouvelle tentative automatique en cas de
  connexion à la base de données interrompue rendent le rapprochement plus stable.
- **Moins d'erreurs partout.** De nombreuses erreurs serveur rares survenant sur
  les tableaux de bord, les factures fournisseurs, les enregistrements de bons de
  commande et les tâches OCR ont été identifiées et corrigées.

---

## Web App — en ligne : `10.34.4`

- **Recherche rapide du tableau de bord :** connecteurs **AND / OR** localisés
  (de/fr) avec coloration syntaxique ; liste déroulante de valeurs pour les
  sous-types de factures ; messages d'erreur de syntaxe de recherche localisés ;
  expérience clavier plus fluide ; l'avertissement « recherche plein texte
  requise » s'affiche désormais en ligne, de sorte que la mise en page ne saute
  plus.
- **Approbations et autorisations :** correction de l'approbation déclenchée à tort
  lorsque l'unité de conditionnement d'une confirmation de commande est vide ; les
  utilisateurs normaux peuvent de nouveau approuver les éléments de coût après la
  migration du contrôle d'accès ; les autorisations au niveau du document
  s'appliquent désormais lorsqu'une colonne de table existe déjà.
- **Mise à jour automatique :** l'application s'actualise automatiquement lors
  d'une nouvelle version au lieu d'afficher une fenêtre « Actualiser maintenant » ;
  l'ancienne boîte de dialogue d'informations de version a été supprimée.
- **Paramètres d'e-mail entrant :** nouvelle option et nouveau champ pour les
  destinataires des notifications d'échec ; le journal d'import affiche désormais
  l'activité sortante et le motif de l'échec ; l'adresse entrante se copie de façon
  fiable.
- **Séparation de documents :** l'écran de séparation de documents défile
  désormais.
- **Mode sombre :** corrections pour l'extraction de tables, le compteur de tâches
  et les marqueurs de documents clôturés dans le tableau de bord.
- **Ergonomie et stabilité :** corrections de l'interface d'exportation du tableau
  de bord ; les en-têtes de tableau fixes ne transparaissent plus à travers les
  boîtes de dialogue ; le tableau de bord DocNet ne plante plus lors de l'échec
  d'une requête de statistiques ; les scripts de champ ne rétablissent plus les
  anciennes valeurs des champs vidés ; corrections des cases à cocher et de la mise
  en page des paramètres PO ; corrections de l'affichage de la liste de
  classification.
- **Fournisseurs :** les organisations fournisseurs peuvent désormais s'inscrire
  via un lien magique.

## API Service — en ligne : `12.46.8`

- **Passerelle DocBits MCP :** une passerelle unifiée relaie désormais les outils
  DocFlow via l'API principale, de sorte que les assistants IA atteignent chaque
  outil DocBits par un seul point de terminaison ; le point de terminaison MCP est
  servi sans redirection susceptible de rompre les connexions.
- **Comptabilité :** ajout de la validation du centre de coûts pour l'identifiant
  comptable.
- **Routage OCR :** les documents sont soumis à une nouvelle OCR complète lorsque
  l'e-text du fournisseur est désactivé, afin que le texte reste fiable.
- **Infor ERP / SAP :** les frais supplémentaires sont routés correctement lorsque
  l'ERP détient déjà le frais avec un montant nul.
- **Fiabilité (moins d'erreurs serveur) :** renforcement des requêtes du tableau de
  bord, des factures fournisseurs, des enregistrements de bons de commande et du
  gestionnaire de tâches afin qu'elles ne renvoient plus de rares erreurs 500 ;
  synchronisation du cache d'organisation et nettoyage des fichiers stockés plus
  résilients.
- **Filtres de tableau de bord plus clairs :** suppression du champ de filtre de
  numéro de facture redondant ; correction de la quantité rapprochée.
- **Documentation de l'API pour développeurs :** l'interface Swagger propose
  désormais une liste déroulante de spécifications (OpenAPI 3.0 ainsi que la vue
  Infor Swagger 2.0) aux couleurs de DocBits.

## Auth Service — en ligne : `1.68.0`

- **Déconnexion / révocation de jetons plus rapide :** la révocation groupée des
  jetons ne dure plus plusieurs minutes et ne coupe plus la connexion.
- **Correction des e-mails de définition de mot de passe** afin qu'ils s'affichent
  correctement.
- **Fournisseurs :** les organisations fournisseurs peuvent s'inscrire avec un lien
  magique.
- **Stabilité de la connexion :** un membre n'est plus bloqué en cas d'échec
  transitoire de recherche d'organisation, et un identifiant d'organisation
  invalide renvoie désormais un message clair au lieu d'une erreur.

## Docflow Service — en ligne : `2.4.1`

- **Passerelle IA fiable :** correction des blocages et des dépassements de délai
  sur le point de terminaison DocFlow MCP (handshake, déconnexions clients,
  réponses en double) — la partie DocFlow de la passerelle unifiée DocBits MCP.

## OCR Service — en ligne : `1.7.1`

- **Un traitement OCR plus stable :** les files d'attente de réponses en
  arrière-plan expirent automatiquement et les échecs de connexion transitoires
  font l'objet d'une nouvelle tentative, ce qui réduit le nombre de tâches OCR
  bloquées.

## PO Match Service — en ligne : `1.55.7`

- **Les transformations de valeurs** sont désormais appliquées aux colonnes
  item-id, unit-code et static-value lors du rapprochement par règles.
- **Protections contre les plantages :** une ligne dépourvue de prix ou de
  quantité, une combinaison inhabituelle de clés pondérées ou une division
  impossible ne font plus planter le rapprochement.
- **Fiabilité :** les écritures en base de données font automatiquement l'objet
  d'une nouvelle tentative en cas de connexion interrompue ou fermée côté SSL.
- **Infor ERP / SAP :** les frais supplémentaires sont routés correctement lorsque
  l'ERP détient le frais avec un montant nul.

## Fulltext Service — en ligne : `1.35.6`

- **Une réindexation plus rapide :** toutes les phases de synchronisation se
  répartissent désormais en parallèle afin que l'autoscaling s'active, corrigeant
  la réindexation séquentielle lente et un widget de progression bloqué à 0 %.
- **Des statistiques plus stables :** les requêtes de statistiques de documents
  inter-régions sont désormais bornées afin de ne plus dépasser le délai d'attente.

---

## Aucune modification visible par le client durant cette période

Stables, sans changement produit notable entre le 26 et le 30 juin :
Auto Accounting (`1.18.6`), Barcode (`1.15.6`), Docnet (`1.54.6`),
Email (`1.36.4`), Extraction (`1.48.7`), FTP (`1.30.1`), Operator (`1.39.5`).
Auto Accounting et FTP n'ont reçu qu'une maintenance interne.

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-26 → 2026-06-30. -->
