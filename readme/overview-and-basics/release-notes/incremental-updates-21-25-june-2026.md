# Notes de version DocBits — 21–25 juin 2026

_Ce que cette mise à niveau de production a apporté, en langage clair. Chaque
service indique la version désormais en ligne en production. Les services non
répertoriés n'ont connu aucune modification visible par le client durant cette
période._

---

## Points forts

- **Une recherche plus intelligente dans le tableau de bord.** Recherchez des
  documents de façon fiable par montants et par numéros — trouvez les factures
  supérieures à une valeur, ou effectuez une recherche par **numéro de
  réquisition** — avec des plages de montants qui comparent de vrais nombres et
  non du texte. Les sous-types de factures sont consultables par leurs noms
  traduits.
- **Des notifications par e-mail fiables.** Les alertes de changement de statut
  sont désormais envoyées pour chaque statut (plus aucun e-mail abandonné en
  silence), et les accusés de réception d'import entrant ainsi que les avis
  d'échec arborent désormais correctement la marque DocBits, avec des contrôles
  par destinataire.
- **Une connexion plus fluide entre régions (EU/US).** Le changement de région
  prend désormais la forme d'une petite bannière plutôt que d'une interruption en
  plein écran, le single sign-on aboutit dans la bonne région, et le maintien de
  la session ouverte sur plusieurs onglets de navigateur est plus fiable.
- **Corrections des autorisations.** Les utilisateurs disposent de l'accès que
  leur groupe leur accorde — l'ouverture, la modification, l'approbation et le
  redémarrage des documents fonctionnent désormais correctement, même lorsque les
  groupes et les autorisations sont configurés de manières moins courantes.
- **Un traitement des documents plus stable.** Les documents qui restaient
  auparavant bloqués après l'envoi sont automatiquement repris, et une rafale
  provenant d'un seul client ne ralentit plus les autres.

---

## Web App — en ligne : `10.32.4`

- **Saut de recherche rapide (Cmd/Ctrl + K)** directement vers le paramètre
  **Validation des factures électroniques**.
- **Région & connexion :** le changement de région s'affiche désormais sous forme
  de bannière persistante au lieu d'un écran bloquant ; le single sign-on
  redirige désormais vers la bonne région (EU/US) ; le maintien de la session sur
  plusieurs onglets est plus fiable.
- **Autorisations :** correction des cas où des utilisateurs ne pouvaient pas
  **approuver**, **modifier**, **ouvrir** ou **redémarrer** des documents malgré
  des autorisations de groupe correctes.
- **Paramètres d'e-mail entrant :** nouvelles options « Notifier l'expéditeur » et
  « Répondre à l'expéditeur à la réception ».
- **Ergonomie :** l'avertissement de document en double doit désormais être
  écarté avant de poursuivre ; la bannière « backend indisponible » n'apparaît que
  lors de réelles interruptions de service ; les compteurs de tâches se mettent à
  jour immédiatement à l'achèvement des tâches ; correction du mode sombre sur
  l'écran de validation des tables IA.
- **Performances :** correction d'un blocage de l'écran des e-documents pendant la
  validation des champs et le rapprochement de bon de commande.
- **Recherche des sous-types de factures par leurs noms traduits.**

## API Service — en ligne : `12.41.9`

- **Refonte de la recherche du tableau de bord :** le numéro de réquisition et le
  demandeur sont désormais consultables ; les recherches par montant et par numéro
  renvoient des résultats corrects (véritable comparaison numérique) ; le montant
  net total et les colonnes calculées s'affichent correctement.
- **Des e-mails d'alerte de statut fiables** pour tout statut de document, les
  échecs d'envoi n'étant plus masqués.
- **Autorisations :** les utilisateurs sans groupe peuvent ouvrir et approuver
  leurs propres documents ; la visibilité des documents pour les utilisateurs sans
  groupe est rétablie.
- **Fiabilité du traitement des documents :** les documents bloqués au statut
  « new » sont automatiquement remis en file d'attente ; un traitement équitable
  garantit qu'une grosse rafale provenant d'une organisation n'affame pas les
  autres ; auto-réparation pour de rares problèmes de séquence de base de données.
- **Les PDF numérisés dont la couche de texte est défectueuse sont dirigés vers
  l'OCR** au lieu de produire du texte peu fiable.
- **Précision de l'extraction et du PO :** le nom du fournisseur est renseigné à
  partir du bon de commande associé ; les colonnes de numéro d'article en double
  sont supprimées ; meilleure gestion des espaces spéciaux (insécables).
- **Export Infor ERP / SAP :** correction de l'authentification de l'export SFTP.
- **Facturation électronique :** améliorations du chemin d'extraction
  ZUGFeRD / e-document.

## Auth Service — en ligne : `1.66.0`

- **Correction de l'attribution d'organisation manquante** pour certains
  utilisateurs (identifiant d'organisation vide).

## Docflow Service — en ligne : `2.3.4`

- **Le délai d'attente du déclencheur de workflow** est désormais configurable par
  environnement.

## Email Service — en ligne : `1.35.9`

- **E-mails à la marque :** les accusés de réception d'import entrant et les avis
  d'échec utilisent désormais le véritable logo et les véritables couleurs
  DocBits.
- **Contrôles par organisation :** e-mail de confirmation à la réception,
  « notifier l'expéditeur » en cas d'échec, et options de réponse à l'expéditeur.
- **Un import entrant plus fiable :** les résultats d'import sont correctement
  enregistrés, les échecs partiels sont signalés comme des échecs (et non comme des
  réussites silencieuses), et les caractères problématiques dans le corps des
  e-mails ne cassent plus l'import.
- **Routage EU/US :** routage par organisation vers la bonne API régionale.

## Fulltext Service — en ligne : `1.34.5`

- **La recherche par montants et par numéros** fonctionne désormais de façon
  fiable, y compris les séparateurs de milliers et les plages de montants (le
  moteur derrière la refonte de la recherche du tableau de bord).
- **Une infrastructure de recherche plus stable :** les files d'attente en
  arrière-plan orphelines sont nettoyées afin qu'elles n'immobilisent plus de
  ressources partagées.

## PO Match Service — en ligne : `1.54.7`

- **Un rapprochement de bons de commande plus robuste :** les codes d'unité de
  conditionnement/d'emballage sous forme de texte ne bloquent plus un
  rapprochement, et le rapprochement manuel des lignes gère les résultats vides
  sans risque.

---

## Aucune modification visible par le client durant cette période

Stables, sans changement produit notable entre le 21 et le 25 juin :
Auto Accounting (`1.18.5`), Barcode (`1.15.6`), Docnet (`1.54.6`),
Extraction (`1.48.6`), FTP (`1.30.0`), OCR (`1.6.8`), Operator (`1.39.5`).

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-21 → 2026-06-25. -->
