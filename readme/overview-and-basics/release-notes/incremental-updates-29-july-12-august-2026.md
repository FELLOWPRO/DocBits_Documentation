# Notes de version DocBits — 29 juillet – 12 août 2026

_Ce qui a changé avec la mise à niveau de production DocBits déployée du 10 au
12 août 2026, couvrant tout ce qui a été livré depuis la version du 29 juillet.
Chaque service indique la version mise en ligne, suivie des nouveautés ou
corrections expliquées en langage clair. Les services non répertoriés
(Auto Accounting `1.21.1`, Ideas `0.3.1`, OCR `1.10.3`, Operator `1.42.1`,
PO Match `1.59.3`, FTP `1.32.4`) n'ont connu aucune modification visible par le
client._

---

## Points forts

- **Prise en charge de FacturaE.** Les e-factures espagnoles FacturaE 3.1 sont
  classifiées et extraites d'emblée, avec des mappages de champs complets.
  Dans la même vague, les mappages ebInterface (Autriche) sont devenus fidèles
  à chaque version, les mappages par défaut de Factur-X et ZUGFeRD ont gagné le
  chemin d'extraction du nom de société, et plusieurs mappages par défaut
  erronés pour les remises, la TVA et les prix unitaires ont été corrigés.
- **Recherche et tri du tableau de bord réparés.** Le tri ne dépend plus des
  colonnes qui se trouvent être visibles, un filtre OR combiné à une condition
  de plage ou d'égalité n'efface plus les termes de recherche, les noms de
  fournisseurs réapparaissent dans la recherche rapide, et les dates au format
  ISO sont lues correctement.
- **L'extraction par IA se corrige elle-même.** Une inversion avérée des
  montants net/total commise par l'IA est annulée automatiquement, les champs
  scannés par IA ne reviennent plus erronés après un redémarrage de document,
  et l'extraction de tableaux par IA traite les documents par lots de pages,
  de sorte que les longs tableaux arrivent complets.
- **Les workflows survivent à un incident d'authentification.** Un service
  d'authentification brièvement injoignable est retenté au lieu de faire
  échouer l'exécution, et un déclencheur de workflow qui ne parvient pas à
  s'authentifier signale l'erreur au lieu de laisser le document bloqué.
- **Les PDF difficiles à lire s'extraient à nouveau.** Lorsque le décodeur de
  texte PDF standard ne peut pas lire une page (fréquent avec les fichiers
  produits par Ghostscript), l'extraction bascule sur un second moteur au lieu
  de ne rien renvoyer.
- **La MFA fonctionne entre les régions.** Les données d'enrôlement à deux
  facteurs sont répliquées entre les régions UE et US, de sorte qu'un second
  facteur configuré dans une région est reconnu dans l'autre.

---

## Web App — `10.49.4`

### Connexion et comptes

- La déconnexion dans un onglet du navigateur déconnecte aussi les autres
  onglets, sans les messages d'erreur qui apparaissaient lorsque les onglets
  étaient en désaccord sur la session.
- Le changement de votre propre mot de passe dans le profil passe par le point
  de terminaison en libre-service dédié, de sorte qu'il fonctionne sans
  permissions d'administrateur.
- La connexion par clé d'accès depuis une région autre que la région d'origine
  affiche des messages d'erreur traduits, et son bouton d'envoi est visible.

### Écran de validation

- L'onglet « Extracted table » ne tourne plus indéfiniment lorsqu'un tableau
  IA existe déjà.
- Les documents dont les données de code-barres manquent ne cassent plus la
  vue d'affectation des codes-barres.
- Les lignes multi-taxes M3 proposent le code de taxe sous forme de liste
  déroulante alimentée par la liste de valeurs, au lieu d'un champ de texte
  libre.
- L'ouverture des factures fournisseurs volumineuses est nettement plus
  rapide.

### Tâches

- Les colonnes Kanban se chargent au fil du défilement, de sorte que les
  tableaux comportant de nombreuses tâches s'ouvrent rapidement.
- Le compteur de tâches ouvertes de la barre latérale compte les tâches dans
  le contexte de votre sous-organisation, et non dans celui du document
  ouvert à ce moment-là.

### Workflow Builder

- La liste des workflows conserve votre recherche, l'ordre de tri, la page et
  la taille de page lorsque vous ouvrez un workflow puis revenez, y compris
  via le fil d'Ariane, et la page s'ouvre par défaut sur l'onglet List.

### Paramètres et administration

- La page des données de base ne s'affiche plus vide à cause d'une condition
  de concurrence au tri, et le tri par badges ne fait plus planter la page.
- Un abonnement en état « cancelling » (résiliation en cours) peut être
  repris.
- La page de détail XSLT signale les erreurs de chargement au lieu de ne rien
  afficher, et les paramètres de notification par e-mail utilisent toute la
  largeur de la page, avec un panneau de journaux fonctionnel.
- Le sélecteur d'organisation pour les utilisateurs multi-organisations a une
  disposition de lignes, un dimensionnement et des couleurs de thème corrects,
  défile correctement, et propose un filtre pour les comptes comptant de
  nombreuses organisations.
- Analytics : une requête de métriques en échec affiche un état d'erreur au
  lieu d'afficher des zéros, et les widgets d'utilisation le signalent
  honnêtement lorsqu'aucune donnée de mesure n'est disponible.
- Les options de cache obsolètes ont été retirées de la page de gestion du
  cache, et les pages Utilisateurs et Groupes ont perdu leurs doubles barres
  de défilement imbriquées.
- « Use Default Template » dans le gestionnaire de mises en page ne plante
  plus et ne reste plus inerte ; la fonction cesse aussi d'affirmer qu'aucune
  mise en page par défaut n'existe.
- Les règles de sélection conservent leurs opérateurs de correspondance de
  texte, de présence et d'expression régulière lorsqu'une règle est rouverte.
- Les types de documents prennent en charge des règles de transformation par
  type, et l'interface de la liste des règles a gagné une action de valeur
  fixe.
- Les badges de statut des bons de commande se mappent correctement pour les
  valeurs de statut dans la casse de l'ERP.
- Les écrans DocNet (AI Workforce), y compris l'Agent Wizard, sont traduits,
  et la boîte de dialogue de création/modification d'idée défile
  horizontalement.
- Devis du portail fournisseurs : les unités de mesure gérées s'affichent dans
  le tableau des lignes, le style d'approbation s'applique uniquement aux
  devis de contrat, et la ligne de comparaison n'apparaît plus lorsque les
  deux valeurs sont identiques.
- Le repli JSON de la page d'erreur est lisible en mode sombre, et les
  rapports utilisent un véritable libellé « 7 derniers jours » au lieu d'un
  « 7 » isolé.

## API Service — `12.74.0`

### Tableau de bord et recherche

- Le tri fonctionne quelles que soient les colonnes visibles, et un mot-clé
  que la recherche délègue au texte intégral ne laisse plus derrière lui un
  fragment SQL cassé.
- Les noms de fournisseurs réapparaissent dans la recherche rapide pour les
  organisations sans indexation en texte intégral.
- Les dates au format ISO (2026-08-12) ne sont plus mal interprétées par le
  normaliseur de dates qui lit le jour en premier.
- Les exports du tableau de bord dirigent les valeurs de texte brutes, comme
  les numéros de facture, vers la bonne colonne.

### E-factures

- FacturaE 3.1 (Espagne) : règle de classification et mappages de champs
  complets.
- Les règles de classification XRechnung sont ancrées à leur famille de
  syntaxe, de sorte qu'un document UBL n'est plus reconnu par des règles CII,
  et inversement.
- La version acceptée « 3.0 » couvre toute sa famille de correctifs (3.0.1,
  3.0.2).
- Les factures CII reprennent la raison sociale du fournisseur, le nom
  commercial ne servant que de repli.
- Les mappages ebInterface (Autriche) sont fidèles à chaque version, avec une
  règle fourre-tout corrigée et des jeux d'essai reconstruits.
- Les mappages par défaut de Factur-X et ZUGFeRD ont gagné le chemin
  d'extraction du nom de société, et les transformations d'en-tête par défaut
  pour le taux de taxe, le type de facture et les champs de niveau 3 ont été
  corrigées, de même que la sémantique des remises, de la TVA et des prix
  unitaires pour toute la famille.
- Les codes de catégorie de taxe source ne sont plus mappés aveuglément sur
  vos codes ERP.
- Les documents qui mentionnent à la fois « facture » et « avoir » privilégient
  la classification en avoir.

### Documents et extraction

- Lorsque le décodeur PDF standard ne peut pas lire le texte incorporé d'une
  page, l'extraction bascule sur un second moteur, de sorte que les PDF
  concernés s'extraient au lieu de revenir vides.
- L'interrupteur principal des codes-barres est désormais
  `BARCODE_EXTRACTION` ; l'ancien paramètre de codes QR continue de
  fonctionner comme alias.
- Une fuite de mémoire dans le planificateur d'arrière-plan a été colmatée ;
  elle dégradait lentement le traitement au fil des jours de fonctionnement.
- Les fournisseurs importés sans pays restent vides au lieu de recevoir
  l'Allemagne par défaut.

### Export et données de base

- La fonction « Save Rules » signale un échec lorsqu'elle n'écrit rien, au
  lieu d'annoncer un succès.
- Les lignes à montant nul ne sont plus supprimées des exports de
  comptabilisation automatique, et un filtre qui correspondait à toutes les
  catégories a été corrigé.
- Les exports M3 prennent en charge des post-hooks d'informations
  additionnelles.
- Une seule sonde de jeu de données en échec ne vide plus tout l'écran des
  données de base.
- Les caches de bons de commande sont invalidés lorsque l'ERP met à jour le
  statut d'un bon de commande, de sorte que le tableau de bord cesse
  d'afficher l'état périmé.

### Administration

- Chaque préférence indique quel utilisateur l'a modifiée en dernier.
- Les règles d'extraction peuvent être supprimées par fournisseur et clonées
  via de nouveaux points de terminaison.
- Les destinataires des e-mails d'alerte de statut sont comparés de manière
  sûre vis-à-vis des valeurs NULL, ce qui corrige un plantage dans l'envoi des
  notifications.

## Auth Service — `1.75.9`

- Une clé API d'organisation utilisée contre une organisation sans rapport est
  rejetée.
- La création d'une organisation renvoyait une erreur tout en enregistrant bel
  et bien la ligne ; elle répond désormais correctement.
- La connexion par clé d'accès alors qu'aucune n'est enrôlée renvoie son
  propre code d'erreur, de sorte que l'écran de connexion peut dire ce qui ne
  va pas.

## Auth Bridge Service — `0.4.2`

- Les tables d'enrôlement à deux facteurs sont répliquées entre les régions UE
  et US, et les lignes sont identifiées par leur véritable clé primaire.

## Docflow Service — `2.8.7`

- Un déclencheur de workflow qui ne parvient pas à s'authentifier signale
  l'échec au lieu de laisser le document bloqué, et un service
  d'authentification brièvement injoignable est retenté plutôt que traité
  comme un jeton invalide.
- Cartes de comparaison de devis : les numéros d'article ne sont comparés que
  pour les lignes décrites par la matrice de prix des articles, et les lignes
  sans unité de mesure ou sans prix sont ignorées au lieu de faire échouer la
  comparaison.
- La carte de comparaison des prix contractuels a gagné une option d'opérateur
  any/all (au moins un / tous), et les caches de cartes sont invalidés
  correctement après les migrations et les mises à jour de code.
- Les connexions SSL interrompues sont traitées comme transitoires et
  retentées au lieu de faire échouer l'exécution.

## Docnet Service — `1.56.4`

- Les points de terminaison d'état et de version ne bloquent plus sur des
  vérifications en direct, ce qui faisait auparavant se figer la boîte de
  dialogue Service Versions.

## Email Service — `1.40.6`

- Lorsqu'un e-mail entrant est ignoré, le motif est affiché dans la ligne
  d'événement d'import au lieu de rester silencieux.
- Les fichiers conteneurs `.eml` joints ne sont plus importés comme documents.
- Une connexion Microsoft Office en échec produit un message d'erreur lisible,
  et une erreur de transport du service d'IA compte comme « incertain » plutôt
  que comme un rejet.

## Extraction Service — `1.53.8`

- Une inversion avérée des montants net/total commise par l'IA est annulée
  après l'extraction des champs, et les échecs du garde-fou sont journalisés
  au lieu de passer silencieusement.
- Les champs scannés par IA ne reviennent plus erronés après un redémarrage de
  document.
- L'extraction de tableaux par IA travaille par lots de pages et accumule tous
  les lots, de sorte que les longs tableaux arrivent complets.
- Les documents mentionnant à la fois « facture » et « avoir » privilégient la
  classification en avoir.
- Le nettoyage répété des en-têtes et pieds de page est mis en cache, ce qui
  accélère l'extraction sur les documents de plusieurs pages.

## Fulltext Service — `1.41.7`

- Un filtre OR combiné à une condition de plage ou d'égalité n'efface plus les
  termes de recherche.
- Le tri utilise les bons chemins d'index et fait remonter la véritable raison
  lorsque le moteur de recherche rejette une requête ; une régression de tri
  qui cassait entièrement la recherche par requête brute a été corrigée la
  semaine même de son apparition.
- Les recherches de documents fonctionnent sur les index plus anciens mappés
  en texte.
- Le cache de jetons est limité au couple jeton-organisation, de sorte qu'un
  changement d'organisation ne peut plus servir de résultats sous le contexte
  précédent.
