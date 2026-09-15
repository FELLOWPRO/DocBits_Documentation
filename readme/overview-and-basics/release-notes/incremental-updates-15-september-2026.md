# Notes de version DocBits — 15 septembre 2026

_Ce qui change avec le correctif urgent de production DocBits du 15 septembre
2026 (version R1.0.13), couvrant tout ce qui a été livré depuis la version du
1er septembre. Chaque service indique la version déployée, suivie des
nouveautés ou corrections expliquées en langage clair. Les services non
répertoriés n'ont connu aucune modification visible par le client._

---

## Points forts

- **Un seul jeu de règles pour la recherche du tableau de bord.** `field=value`
  signifie désormais exactement cette valeur sur chaque moteur de recherche,
  `field:value` signifie « contient » (avec `value*` et `*value` pour
  « commence par » et « se termine par »), et `field!=value` renvoie aussi les
  documents qui n'ont aucune valeur. Une recherche sans puce est une recherche
  par sous-chaîne sur tous les champs, numéros de bon de commande, codes-barres
  et numéros de demande d'achat compris. Le nombre de résultats, les tuiles de
  statut et la pagination décrivent le même ensemble de documents, et une
  recherche qui a atteint la fenêtre de résultats ou s'est exécutée sans
  l'index de texte intégral le signale au lieu d'annoncer « complet ». La
  connexion de recherche propre au tableau de bord (WebSocket) n'atteignait
  jamais l'index de texte intégral auparavant ; c'est désormais le cas.
- **Les fournisseurs sont reconnus plus souvent.** Lorsqu'un champ de recherche
  (identifiant fiscal, IBAN, numéro de fournisseur) correspond à exactement un
  fournisseur, ce fournisseur est utilisé même si un champ large tel que le
  nom en fait correspondre plusieurs. Les documents XRechnung CII et Facturae
  transportent à nouveau leurs champs fournisseur. Lorsque les données de base
  ont remplacé une valeur extraite, l'écran de validation l'indique et vous
  permet de restaurer l'original.
- **La correspondance des bons de commande s'explique d'elle-même.** L'écran
  indique pourquoi il n'y a pas de correspondance, l'infobulle de
  non-concordance nomme la colonne qui a échoué, l'historique des
  correspondances liste les règles de transformation exécutées, et les prix
  unitaires des bons de commande sont dérivés du montant net. Les
  correspondances manuelles fonctionnent à nouveau pour les organisations sans
  règle de secours, les bons de commande retirés le restent, et une tâche de
  correspondance interrompue marque le document en échec au lieu de le laisser
  indéfiniment en « Queue ».
- **Documents bloqués et fausses erreurs.** Les organisations qui téléversent
  en continu voyaient leurs documents rétrogradés à une priorité de file
  d'attente jamais servie pendant les heures ouvrées (866 documents bloqués en
  « new » chez un client). Un processus de relance pouvait écraser un document
  exporté avec succès par « error » des heures plus tard et déclencher
  l'e-mail d'erreur d'export correspondant. Ce chemin est fermé.
- **Touchless Intelligence.** L'onglet Analytics qui mesure combien de
  documents traversent DocBits sans intervention humaine reçoit sa première
  version complète : groupes de problèmes avec conseils IA, analyse en masse,
  propositions de modification avec aperçu, application et annulation, une
  page fournisseur avec tendance et exemples, un diagramme de flux du pipeline
  par document, et un diagramme du jeu de règles de bons de commande qui
  indique pourquoi un document n'est pas passé.
- **Plus rapide là où les données sont volumineuses.** Les connexions à froid
  sautent la somme du grand livre de crédits qui prenait jusqu'à 33 s, la
  liste déroulante de comptabilité fonctionne pour les organisations de plus
  de 2 000 comptes, la page des règles E-Documents pagine ses 1 600 règles
  côté serveur au lieu de figer le navigateur, et Actualiser sur le tableau de
  bord des bons de commande renvoie des données fraîches au lieu d'une liste
  en cache.
- **Sécurité.** Les source maps du frontend ne sont plus livrées à chaque
  déploiement, les filtres de recherche des données de base sont liés comme
  paramètres SQL au lieu d'être interpolés, un jeton expiré est rejeté même
  lors d'un accès au cache, et le contrôle d'organisation sur le jeton de
  traitement est appliqué indépendamment de la couche qui le précède.

---

## Web App — `10.66.3`

### Connexion et comptes

- La connexion est plus rapide. Le contrôle d'abonnement à la connexion
  demandait le solde de crédits complet, ce qui additionnait des millions de
  lignes de grand livre et dépassait souvent le délai d'attente de 10 s du
  client. La connexion demande désormais seulement si un abonnement existe ;
  les soldes sont toujours calculés dans Settings → Subscription.
- Le changement de région (UE ↔ US) vous garde connecté. La région cible
  répond « invalid token » pendant quelques secondes jusqu'à ce que la session
  soit répliquée, et deux chemins de code interprétaient cela comme une
  session morte.
- La superposition « Updating DocBits v10.59.3.1 → v10.59.3.1 » qui rechargeait
  indéfiniment sur sandbox est corrigée. Un rechargement vers la même version
  n'affiche plus la superposition, la boucle est bornée par onglet, et un
  bandeau propose une récupération manuelle si cela se reproduit.
- Les administrateurs peuvent accorder l'onglet Analytics Dashboard à des rôles
  spécifiques, et les modifications de rôles s'enregistrent de manière fiable.
- La case System Admin peut être cochée sur un utilisateur existant. Créer un
  administrateur système depuis le frontend a désormais un effet ; une tâche
  de synchronisation réinitialisait l'indicateur à chaque exécution.
- Settings → Roles : la liste des membres s'affiche au lieu de rester bloquée
  derrière un indicateur de chargement lorsque le serveur répond par une
  erreur.
- La connexion au serveur MCP DocBits impose l'authentification à deux
  facteurs et un consentement à usage unique.

### Tableau de bord et recherche

- Nouvelles règles d'opérateurs, également décrites dans la fenêtre d'aide de
  la recherche : `=` signifie exactement cette valeur (sans distinction de
  casse), `:` signifie contient, `: value*` commence par, `: *value` se
  termine par, `!=` signifie tout ce qui n'est pas exactement cette valeur, y
  compris les documents sans valeur. Les guillemets servent uniquement à
  grouper une valeur contenant des espaces.
- Une expression entre guillemets telle que `"Johnson and Johnson"` est
  recherchée comme une seule expression. « and » et « or » entre guillemets ne
  sont plus interprétés comme des connecteurs.
- Lorsqu'une recherche libre ne trouve rien, le tableau de bord explique la
  règle et propose des puces en un clic (`Invoice number : <term>`,
  `Purchase order : <term>`, `Supplier ID : <term>`).
- Une recherche sans résultat réinitialise la pagination et chaque compteur de
  la page. Auparavant, la pagination conservait le nombre de la recherche
  précédente.
- Les numéros de bon de commande, numéros de commande, codes-barres, types de
  facture et numéros de demande d'achat peuvent être trouvés sans puce.

### Écran de validation

- Les valeurs remplacées par les données de base sont marquées. Un badge ambre
  affiche la valeur d'origine et la valeur actuelle, le jeu de données et la
  façon dont il a correspondu, et un bouton restaure la valeur extraite. Les
  valeurs confirmées par les données de base ou remplies depuis le bon de
  commande reçoivent leurs propres libellés. Auparavant, toutes portaient le
  badge « Extracted using saved rules ».
- Le tampon d'approbation est enregistré même lorsque la page porte déjà une
  autre annotation. Les documents annotés téléchargés ne comportaient pas le
  tampon dans ce cas.
- « Hide non mapped columns » conserve les colonnes que vous avez entraînées
  manuellement (par exemple Item Number et Purchase Order).
- L'enregistrement des règles d'extraction fonctionne après avoir saisi un
  numéro de page puis tracé un cadre pour un champ. Cette séquence faisait
  planter l'enregistrement.
- L'extraction structurée peut être activée par fournisseur, dans la fenêtre
  tfidf de l'écran de validation et sous forme de colonne en lecture seule
  dans Settings → Classification & Extraction.
- Train Model s'exécute en arrière-plan. L'écran affiche « training started »,
  interroge le résultat et signale la réussite ou l'échec. Les grandes
  organisations recevaient une erreur de passerelle alors que l'entraînement
  se poursuivait côté serveur.
- Mode sombre : le curseur ciseaux de l'écran de scission et le commutateur de
  mode de l'écran Auto Accounting sont à nouveau lisibles.

### Correspondance des bons de commande

Les changements annoncés dans [Correctifs urgents 8 septembre 2026](incremental-updates-8-september-2026.md)
arrivent en production avec cette version : la correspondance survit à
l'enregistrement, la correspondance s'exécute à nouveau lorsque le numéro de
bon de commande est corrigé, l'écran indique pourquoi il n'y a pas de
correspondance et pourquoi une correspondance n'a pas été conservée,
l'historique des correspondances affiche les règles de transformation, et le
prix unitaire du bon de commande est calculé à partir du montant net. En
complément :

- L'infobulle de non-concordance nomme la colonne qui n'a pas correspondu. Elle
  était vide auparavant parce que seules les colonnes concordantes étaient
  enregistrées, et l'écran ne pouvait dire que « Mismatched ».
- Le bouton Auto Match exporte aussi le document lorsque « PO Auto Match and
  Export » est activé. Auparavant, l'export n'avait lieu que lorsque le
  document était ouvert depuis le tableau de bord via « PO Match ».
- La fenêtre de tolérance quantité/prix unitaire reste ouverte lorsque le
  serveur rejette l'enregistrement, de sorte que les valeurs saisies ne sont
  pas perdues.
- Le bouton Actualiser du tableau de bord des bons de commande vide le cache
  côté serveur avant de recharger. Un bon de commande importé depuis l'ERP
  n'apparaissait qu'après sept à huit minutes.
- La page des règles de correspondance des bons de commande dessine le jeu de
  règles sous forme d'organigramme, et l'historique des correspondances a été
  déplacé dans la barre d'outils d'actions.

### Comptabilité automatique

- Les organisations de plus de 2 000 comptes recherchent la liste des comptes
  côté serveur. La liste déroulante était vide sur sandbox pour ces
  organisations, et le chargement des pages prenait cinq secondes.
- Les comptes référencés par un document sont résolus par lots : un document
  de 100 lignes avec deux ventilations par ligne nécessite 4 requêtes au lieu
  de 403.
- Les en-têtes des tableaux Auto Accounting et PO suivent le libellé défini
  dans le concepteur de mise en page au lieu d'un texte codé en dur.

### Paramètres

- Settings → E-Documents → Rules pagine, recherche et trie le catalogue de
  1 600 règles côté serveur. L'onglet rendait auparavant chaque règle d'un
  coup et figeait le navigateur. « Reset all » est un seul appel au lieu d'un
  par règle.
- Les paramètres avancés d'un type de document affichent l'état enregistré de
  chaque commutateur. Un `false` enregistré, une tolérance à `0` ou une liste
  vide étaient remplacés par la valeur par défaut, et changer de type de
  document laissait les valeurs du type précédent en place.
- Règles de transformation : une action « Set value » s'enregistre. L'éditeur
  l'envoyait sous un nom que le serveur rejette.
- List of Values : la barre latérale affiche une nouvelle liste et retire une
  liste supprimée sans rechargement ; les réponses tardives d'une liste
  précédente n'écrasent plus la liste actuelle.
- Le lien vers les sous-types de document s'affiche sur les types de document
  standard.
- Le mappage JPL de l'export SMB se télécharge en `.properties`, de sorte que
  le fichier peut être téléversé à nouveau. Il était nommé `.xml` et rejeté
  au retour.

### Workflows

- Renommer un workflow conserve les modifications de cartes effectuées dans la
  même session. Les nouveaux workflows sont créés en une seule requête
  d'enregistrement, et les renommages de modèles sont persistés.
- Un fichier de workflow exporté contient l'enveloppe d'export complète
  (version, nom, description). Les workflows avancés peuvent à nouveau être
  importés ; auparavant, le fichier perdait sa version, était relu comme un
  workflow standard et rejeté.
- Les filtres de colonnes de la liste des workflows se combinent avec ET. Avec
  un filtre de nom et un filtre de date actifs, des lignes ne correspondant
  qu'au nom se glissaient dans le résultat.
- Les échéances de tâches utilisent le format de date de vos paramètres
  utilisateur dans la liste, le tableau et la vue détaillée.

### Analytics : Touchless Intelligence

L'onglet Touchless (Analytics → Touchless) mesure combien de documents
traversent DocBits sans qu'une personne n'y touche, et pourquoi les autres n'y
sont pas parvenus. Cette version le complète :

- **Groupes de problèmes avec preuves.** Les documents qui ont nécessité une
  intervention sont regroupés par cause. Chaque carte de groupe nomme les
  champs, codes de validation et messages d'erreur sur lesquels il échoue,
  ainsi que son fournisseur, ou indique qu'il n'y en a pas. Les groupes que
  DocBits peut corriger (une règle, un paramètre de champ) sont séparés de
  ceux que seul le fournisseur peut corriger, et le budget d'analyse IA va
  d'abord aux groupes corrigibles.
- **Analyse IA, signalée comme telle.** Une carte de groupe indique si le
  conseil a été rédigé par un modèle de langage ou par une règle, ce que
  l'analyse a compté et quand elle a cessé d'être valable, et si un clic
  réutilisera une analyse en cache. Si le conseiller IA ne peut pas s'exécuter
  dans cet environnement, l'onglet en explique la raison.
- **Analyse en masse.** Analysez de nombreux groupes en une seule exécution,
  suivez groupe par groupe ce que fait l'exécution, et retrouvez les résultats
  ensuite. La liste des résultats survit à la navigation et au rechargement,
  et l'exécution ne reste plus figée sur « Running · 0/6 done » dans une vue
  de sous-organisation.
- **Propositions de modification.** Une recommandation devient une action
  concrète : la carte explique la modification proposée en quatre questions,
  vous permet de l'ajuster, prévisualise ce qu'elle ferait (rien n'est
  enregistré), l'applique, mesure l'effet et peut l'annuler. Les étapes de
  correction renvoient directement vers la page de paramètres qu'elles
  nomment, préfiltrée par type de document, champ ou règle.
- **Page fournisseur.** Choisissez un fournisseur depuis l'onglet ou
  recherchez la file d'opportunités par nom ou numéro. La page affiche le taux
  touchless du fournisseur dans le temps (de 30 jours à 1 an), ses documents
  à problème et les documents qui se sont bien passés, et propose un
  diagnostic IA par fournisseur. Jusqu'à cinq fournisseurs peuvent être
  comparés côte à côte. Le numéro de fournisseur est affiché au lieu d'un
  hachage interne.
- **Flux du pipeline.** Un diagramme par document et par groupe montre le
  parcours à travers la réception, la classification, le contrôle e-document,
  le fournisseur, l'OCR, l'extraction, la validation, la correspondance des
  bons de commande, l'approbation et l'export, avec l'étape qui l'a arrêté.
- **La correspondance des bons de commande, expliquée.** Le jeu de règles de
  bons de commande est dessiné sous forme d'organigramme sur la page des
  paramètres et dans Touchless, avec le chemin qu'un document a suivi et une
  raison en langage clair expliquant pourquoi il n'est pas passé. Les codes de
  raison distinguent « bon de commande non trouvé » de « lignes non
  concordantes » et « champ obligatoire manquant ».
- **Segmentation.** Les KPI, groupes et propositions peuvent être répartis
  selon un champ de document, par exemple Order Type = Direct / Indirect.
- **Des chiffres corrects.** Les tuiles KPI respectent le filtre de
  sous-organisation et ne comptent que les documents que l'exploration
  détaillée peut lister. Une session de navigateur de l'utilisateur système de
  l'organisation compte comme humaine, de sorte que les documents corrigés à
  la main ne sont plus classés comme touchless.
- La barre d'outils du rapport fait tenir ses commandes sur les écrans larges,
  et les couleurs du mode sombre proviennent du thème.

### DocNet

- Le fil Activities, le widget Recent Activity et la chronologie des missions
  sont traduits. Les résumés d'audit étaient en anglais dans les 22 langues.
- Les agents voient les champs que le type de document définit mais que
  l'extraction a laissés vides. Ils en concluaient auparavant que ces champs
  n'existaient pas et sautaient les mises à jour prescrites sans tenter
  d'écriture.

### Sécurité

- Les source maps du frontend sont retirées de chaque déploiement. Tous les
  environnements les servaient, production comprise.

---

## API Service — `12.83.156`

### Reconnaissance des fournisseurs et données de base

- Un fournisseur est identifié lorsqu'un champ de recherche est unique. Avec
  plusieurs champs interrogeables, les résultats étaient combinés en union, de
  sorte qu'une correspondance large sur le nom avec quatre fournisseurs noyait
  un identifiant fiscal qui n'en désignait qu'un seul. Les champs sans
  correspondance n'opposent plus leur veto aux champs qui en ont une. Voir
  [Réglages des données de base](../../administration-and-setup/settings/global-settings/document-types/fields/master-data-settings.md)
  pour la façon dont les champs se combinent.
- Les remplacements par les données de base sont enregistrés avec leur
  origine : jeu de données, configuration, champ source, opérateur et type de
  correspondance. L'écran de validation l'affiche et peut restaurer la valeur
  extraite.
- Le Cash Discount Term est importé depuis le BOD fournisseur ; les
  fournisseurs synchronisés depuis l'ERP l'avaient vide. Un Discount Term
  Overwrite saisi comme code complet (« 143 », « 012 », « X08 ») est
  appliqué ; seul le préfixe de pourcentage était consulté auparavant.
- Les recherches dans les données de base sont plafonnées à 1 000 lignes par
  page et pivotent en SQL. Une recherche sur 19 000 enregistrements prenait
  cinq secondes par appel et bloquait l'API.
- Les noms de propriétés de filtre et les types de données de la recherche
  dans les données de base sont liés comme paramètres SQL. Ils étaient
  interpolés dans la requête.

### Traitement des documents

- Les documents d'une organisation qui téléverse en continu étaient
  rétrogradés à la priorité 9, que la file d'attente ne sert que lorsque
  toutes les priorités supérieures sont vides. La rétrogradation est désormais
  plafonnée à 3. Le réconciliateur censé remettre en file les documents
  bloqués n'avait pas d'identifiants fonctionnels en production ; c'est
  désormais le cas.
- Un document terminé et exporté n'est jamais écrasé par « error ». Un
  indicateur de workflow jamais effacé faisait reprendre par le processus de
  relance un document exporté avec succès une fois par minute, jusqu'à ce que
  la limite de relances le marque « error » et déclenche l'e-mail d'erreur
  d'export du client, 2 h 17 min après l'export.
- La fusion et l'ajout acceptent les fichiers `.PDF` et `.Pdf`. Une sortie de
  scanner nommée `SCAN0001.PDF` était rejetée avec « Only PDF files are
  allowed ».
- L'invalidation du cache parcourt l'espace de clés une fois au lieu de deux
  et ne vide que les types de données de recherche modifiés par un BOD. Chaque
  BOD effaçait auparavant tout le cache de recherche de l'organisation,
  bloquant l'API pendant qu'il parcourait les clés de tous.
- Le réentraînement du modèle s'exécute en tâche de fond et renvoie
  immédiatement un statut que l'interface interroge.
- Un jeton de traitement d'une autre organisation est rejeté indépendamment
  du contrôle d'appartenance à la sous-organisation qui le précède.
- La synchronisation des utilisateurs ne touche plus à l'indicateur
  d'utilisateur système au lieu de le réinitialiser à chaque exécution.

### Export

- Les lignes de réception M3 associent le prix unitaire exporté à la base de
  prix propre à la ligne de facture. Le prix voyageait avec le diviseur de la
  ligne du bon de commande et l'ERP revalorisait la ligne à 1 000 fois le
  montant facturé.
- Un export de tableau survit à une ligne dont le bon de commande a été
  supprimé ; la ligne est exportée sans base de prix.
- Export IDM : un champ multivaleur mappé sur un champ numérique (par exemple
  une quantité) faisait planter la charge utile d'export. La valeur est
  d'abord convertie en texte.

### E-documents

- Les factures XRechnung CII dont le montant à payer est de 0,00 parce qu'un
  acompte compense le total affichent le total général (BT-112) comme montant
  total. Le client voyait « total amount 0,00 ».
- Les documents XRechnung CII et Facturae livrent à nouveau leurs champs
  fournisseur. Des surcharges obsolètes au niveau de l'organisation masquaient
  le mappage par défaut correct, de sorte que la reconnaissance des
  fournisseurs ne pouvait jamais aboutir.
- Le catalogue des règles de validation est paginé, recherché et trié côté
  serveur, avec des facettes pour la barre de filtres.

### Classification

- Les documents suisses sont classifiés `de_CH`, `fr_CH` ou `it_CH` d'après
  leur contenu (montants en CHF, numéros de TVA CHE, IBAN CH). Les paramètres
  régionaux étaient repris de la valeur par défaut de l'organisation et les
  documents suisses recevaient `de_DE`.

### Recherche du tableau de bord

- Une seule sémantique des opérateurs sur Postgres et ClickHouse : `=` exact,
  `:` contient avec jokers en bordure, `!=` complément incluant les valeurs
  vides. Sur Postgres, `=` était une correspondance par préfixe, de sorte que
  `invoice_id=911892112` renvoyait aussi 911892112333.
- Une recherche libre est une recherche par sous-chaîne sur tous les champs,
  identifiants métier compris. Le bon de commande, le numéro de commande, le
  code-barres, le type de facture, le sous-type de facture et le numéro de
  demande d'achat n'avaient aucune branche de recherche en texte libre.
- La puce de numéro de facture est exacte sur Postgres, comme elle l'était
  déjà sur l'index. Les zéros initiaux, les formes décimales et la casse sont
  traités de la même manière en texte libre et dans les puces.
- La recherche WebSocket du tableau de bord transmet l'identifiant de
  l'appelant au service de texte intégral. Chaque délégation était refusée
  auparavant, de sorte que le tableau de bord interrogeait silencieusement
  Postgres seul et présentait la réponse comme complète.
- Les tuiles de statut, le nombre de résultats et la liste des résultats
  s'appuient sur un même jeu de prédicats. Les tuiles décrivaient auparavant
  toute l'organisation pendant n'importe quelle recherche.
- Les autorisations de sous-organisation et de type de document sont
  appliquées avant la fenêtre de résultats, de sorte que les documents
  autorisés ne tombent plus hors du plafond de 500 / 10 000.
- La recherche vectorielle est plafonnée à la fenêtre de résultats réelle et
  signale le plafond au lieu d'afficher « (50) » comme total exact.
- Une recherche exécutée sans l'index de texte intégral (index absent, index
  en retard de plusieurs minutes, échec de la consultation des capacités,
  résolution de champs dégradée) signale l'état de sa fenêtre au lieu de
  « complet ».
- Les exports du tableau de bord d'une recherche tronquée comportent une ligne
  d'avertissement dans le CSV/XLSX et dans l'e-mail de notification.
- Les scripts de document qui appellent la recherche en texte intégral
  s'authentifient correctement et font remonter les échecs au lieu de renvoyer
  un résultat vide.

### Correspondance des bons de commande (moteur intégré)

Pour les organisations dont la correspondance s'effectue dans l'API plutôt que
dans le PO Match Service :

- Chaque comparaison de colonne est enregistrée, y compris le prix unitaire et
  la quantité, de sorte que l'infobulle de non-concordance peut nommer la
  colonne qui a échoué.
- Les bons de commande retirés par l'utilisateur le restent dans la
  correspondance automatique.
- Un numéro de bon de commande corrigé est mis en correspondance lors de
  l'enregistrement qui le corrige.

### Analytics

- Touchless : toutes les modifications côté serveur derrière la section
  Web App ci-dessus, y compris les preuves enregistrées par chaque étape du
  pipeline, la trace de correspondance des bons de commande, les propositions
  de modification avec aperçu, application et annulation, la segmentation, le
  statut en masse en un seul appel par cycle, et le point de terminaison de
  tendance qui accepte n'importe quelle fenêtre et un fournisseur.
- Trois tâches d'arrière-plan d'analytique qui échouaient à chaque exécution
  planifiée sont corrigées.

---

## PO Match Service — `1.59.34`

- Le prix unitaire d'une ligne de bon de commande est dérivé de son montant
  net, et non de son total taxé, et l'instantané du bon de commande d'un
  document recalcule ses prix unitaires au moment de la correspondance.
- Le service enregistre d'où provient chaque candidat de numéro de bon de
  commande et quels numéros une exécution a recherchés. Le numéro de facture
  propre au document n'est jamais un candidat de bon de commande. Une
  correspondance abandonnée laisse sa raison sur le document pour l'écran.
- La colonne qui n'a pas correspondu est enregistrée, et les colonnes retirées
  par une règle de secours sont mesurées.
- Les bons de commande retirés par l'utilisateur sont respectés, et les
  correspondances d'arrière-plan obsolètes sont effacées après l'exclusion
  finale.
- La correspondance manuelle fonctionne pour les organisations dont les règles
  ne portent pas d'indicateur `is_fallback`. Les utilisateurs sélectionnaient
  des lignes, lançaient la correspondance, et rien ne revenait.
- Plus de documents orphelins en « Queue » : les délais d'expiration des
  instructions de base de données, les keepalives et un gestionnaire explicite
  de limite de temps souple marquent la tâche en échec au lieu de compter sur
  un arrêt forcé qui ne laissait aucune trace.
- Deux erreurs de production (un prix unitaire `NaN`, un groupe sans
  quantités) ne font plus échouer toute la correspondance.
- Les modifications de tolérance sont lues à chaque requête de correspondance,
  de sorte qu'une tolérance enregistrée à l'instant est utilisée par la
  correspondance suivante.
- La trace de décision en cinq étapes est persistée par document pour
  Touchless.

---

## Auth Service — `1.78.27`

- `/organisation/subscriptions` peut ignorer le solde de crédits, et le calcul
  des crédits exécute toutes les fenêtres d'année contractuelle en une seule
  instruction au lieu d'une requête par fenêtre (32 requêtes d'environ 700 ms
  chacune pour la plus grande organisation). Un cumul quotidien d'utilisation
  est préparé pour un usage ultérieur.
- Les chiffres de jetons restants sur les lecteurs d'organisation sont
  calculés par année contractuelle.
- L'expiration des jetons est appliquée lors des accès au cache. Une entrée en
  cache pouvait authentifier jusqu'à neuf heures après l'expiration du jeton.
- La vérification des jetons cesse de réécrire un `org_id` inchangé dans la
  ligne utilisateur à chaque requête, ce qui produisait un UPDATE par appel.
- Les contrôles de santé évitent les E/S Redis, et le client Redis est mis en
  pool. Une fuite de mémoire qui poussait l'autoscaler au nombre maximal de
  réplicas est corrigée, et le service est revenu à deux workers.
- Un enregistrement de fournisseur répété (lien magique ouvert deux fois)
  réutilise l'adhésion existante au lieu d'échouer avec une erreur de clé en
  double.
- Le fil d'e-mail de réinitialisation de mot de passe utilise l'unique
  application Flask enregistrée ; la réinitialisation échouait avec « current
  Flask app is not registered » depuis le 25 août.
- L'indicateur d'utilisateur système peut être modifié sur un utilisateur
  existant lorsqu'aucun autre membre ne le détient.
- Connexion MCP : MFA liée à la transaction, consentement à usage unique et
  choix de compte forcé lorsque le navigateur détient deux identités de
  session.

---

## Auth Bridge Service — `0.5.7`

Réplication de l'authentification UE ↔ US :

- La réconciliation périodique maintient le flux de réplication en vie. Elle
  prenait environ 95 s alors que le délai d'attente de l'émetteur était de
  60 s, de sorte que chaque réconciliation de six heures coupait le flux à
  heure fixe.
- Lorsque le flux s'interrompt, le slot de réplication est rattaché sur place
  au lieu de reconstruire le pont et de relancer la réconciliation complète de
  démarrage.
- La réconciliation compare les clés primaires par pages au lieu de charger
  les deux côtés en mémoire, ce qui ne tient plus depuis que la table des
  jetons a rejoint la réplication.
- Une origine de réplication existante est traitée comme un succès, non comme
  une dégradation.

---

## Extraction Service — `1.55.33`

- L'extraction structurée est résolue par fournisseur : le paramètre d'une
  mise en page entraînée l'emporte sur la préférence de l'organisation, de la
  même manière que le modèle IA.
- Un mappage de colonnes appris ne peut pas interdire des colonnes que la
  facture possède.
- Extraction de tableaux par IA : les colonnes de montant sont typées comme
  nombres avec une description, et les valeurs non numériques inventées dans
  les colonnes de montant (un « St. » copié depuis la cellule voisine dans le
  prix unitaire par) sont écartées au lieu d'être enregistrées.
- Factures US : lorsque le montant net est déjà égal au total, la taxe se
  résout à 0 au lieu de conserver une taxe extraite parasite. Le bruit de
  virgule flottante inférieur au centime ne départage plus les paires
  net/taxe candidates (268.28 + 22.13 perdait face à net = total, taxe = 0).
- Un tableau dont la ligne d'en-tête n'a jamais été mappée sur des noms réels
  est extrait au lieu d'échouer entièrement.

---

## Fulltext Service — `1.42.35`

- Le cache des résultats de recherche est activé dans tous les
  environnements ; production, sandbox et stage fonctionnaient sans lui depuis
  la création des fichiers d'environnement actifs. Le téléversement et la
  suppression l'invalident, de sorte qu'une recherche après un téléversement
  voit le nouveau document.
- Le `=` exact sur un champ texte dynamique ne compare que la valeur entière.
  Un joker sur le chemin analysé faisait correspondre `note_field=53173` à
  « PO 53173 / 2024 ».
- Un identifiant avec tiret tel que `2026-003` est un seul littéral, et non un
  sac de jetons.
- Les numéros de bon de commande sont trouvés sous toutes leurs formes de
  stockage, y compris les identifiants uniquement numériques dont la clause
  exacte était silencieusement abandonnée.
- Les chemins de lecture ne créent plus l'index qu'ils lisent. Un index absent
  ou vide signalait « complet, 0 résultat » ; chaque réponse sans résultat
  porte désormais un état de fenêtre et une raison.
- Les valeurs monétaires écrites, les anciens mappages booléens, les dates et
  les indicateurs de taxe survivent à la reconstruction de l'index allégé, et
  les entrées d'index sans champs sont détectées et récupérées depuis
  l'extraction.

---

## Docflow Service — `2.10.11`

- Les imports de workflows avancés sont conditionnés au droit de
  l'organisation, et un lot est vérifié avant toute écriture. Une organisation
  sans le module avancé pouvait importer un workflow avancé qu'elle n'avait
  ensuite aucun moyen d'ouvrir.
- Le renommage d'un workflow accompagne l'enregistrement, et les renommages de
  modèles sont persistés.
- La mise à jour « pending workflow execution » est retentée en cas de
  connexion interrompue. Une seule requête échouée laissait l'indicateur
  inchangé et tenait le document hors de l'export jusqu'à ce que quelqu'un le
  redémarre.

---

## Docnet Service — `1.56.12`

- La découverte des champs renvoie chaque champ d'en-tête défini par la mise
  en page, renseigné ou non, et correspond à ce que la garde d'écriture
  vérifie. Les agents sautaient des mises à jour de champs prescrites parce
  que les champs vides semblaient absents.
- Les identités sont mises en cache sous la même clé délimitée par
  organisation que celle utilisée par l'API, de sorte que la frontière des
  clés API d'organisation tient entre les deux services.

---

## Email Service — `1.41.6`

- Les boîtes aux lettres partagées Office 365 de plus de dix sous-dossiers
  résolvent chaque dossier. Microsoft Graph pagine les dossiers dix par dix ;
  la 11e configuration et les suivantes échouaient à chaque interrogation avec
  « unable to find the selected Folder ».

---

## FTP Service — `1.32.18`

- Le planificateur SFTP démarre dans chaque processus worker au lieu d'avant
  le fork. Les imports SFTP périodiques échouaient silencieusement avec un
  état de planificateur corrompu, alors qu'un processus neuf fonctionnait
  correctement.

---

## Auto Accounting `1.21.7`, Barcode `1.18.14`, OCR `1.10.11`, Operator `1.42.12`, Ideas `0.3.6`

Modifications de build et de déploiement uniquement (mise à jour de l'image de
base, identifiants CI). Aucun changement de comportement.

<!-- Release R1.0.13. Everything in the prod->sandbox code delta is announced.
     Held back because Jira "Release No." names the later release R1.1:
     DRFS-778 (discount due dates on import), DRFS-712, MEF-165, MEF-166,
     DOCB-14389. Announce them with R1.1. -->
