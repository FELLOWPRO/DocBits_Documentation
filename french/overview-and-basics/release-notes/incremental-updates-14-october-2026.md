# Notes de version DocBits — 14 octobre 2026

_Ce qui change avec le correctif urgent de production DocBits du 14 octobre
2026 (version R1.0.15), couvrant tout ce qui a été livré depuis le
[correctif du 15 septembre](incremental-updates-15-september-2026.md).
Chaque service indique la version déployée, suivie des nouveautés ou
corrections expliquées en langage clair. Les services non répertoriés n'ont
connu aucune modification visible par le client._

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/release-notes/2026-10-14/fr.mp4" %}

---

## Points forts

- **Le Settings Assistant.** Une barre de discussion présente sur chaque page de
  paramètres répond aux questions sur la configuration de votre organisation,
  dans votre langue et à partir de la documentation DocBits. Il lit l'état
  actuel de vos paramètres et l'explique (autorisations de groupe, canaux
  d'import, options des bons de commande, comptabilité). Lorsque vous lui
  demandez d'activer ou de désactiver une option, il affiche d'abord un aperçu,
  attend votre confirmation et propose une annulation. « Ouvrir le paramètre »
  mène directement au paramètre, même dans une section repliée, et le met en
  surbrillance. Les administrateurs de l'organisation activent ou désactivent
  l'assistant dans Informations sur la société. Il ne répond qu'aux questions
  sur DocBits et ne modifie jamais rien sans confirmation.
- **Nouveaux niveaux d'IA.** Les niveaux Fast et Full reposent sur de nouveaux
  modèles. Un nouveau niveau Auto choisit Fast ou Full pour chaque document, et
  Nexus Flash rejoint Nexus. Un mode vision (hybride ou automatique) décide
  quand l'image de la page est transmise avec le texte. Les préférences de
  modèle d'IA enregistrées passent d'elles-mêmes aux nouveaux niveaux, et les
  écrans n'affichent que les noms de niveau. « Utiliser l'IA » est une liste
  déroulante (Standard, Oui, Non) avec un aperçu de ce que demandera
  l'extraction structurée.
- **Contrôle des champs d'en-tête.** L'écran de validation comporte un bouton
  « Contrôle des champs d'en-tête » à côté d'Enregistrer. Son rapport liste
  chaque champ d'en-tête avec l'origine de la valeur (IA, règle, script ou
  données de base), sous forme de tableau compact avec filtre par source,
  recherche et tri, et avec les mêmes libellés de champ que l'écran de
  validation. La fenêtre d'origine affiche la source de chaque valeur sur une
  seule bande.
- **Sécurité de la connexion et des organisations.** Un défi MFA ne peut être
  utilisé qu'une seule fois sur chaque chemin de connexion, et l'enrôlement
  d'un authentificateur exige le code reçu par e-mail. Les organisations
  possèdent une liste de domaines e-mail vérifiés ; une connexion sociale (par
  exemple Microsoft) rejoint l'organisation qui liste le domaine et ne crée
  jamais d'organisation, d'utilisateur ni d'abonnement de sa propre initiative.
  Seuls les administrateurs de l'organisation modifient les préférences de
  l'organisation et rédigent ou approuvent les règles de correspondance des
  bons de commande. Les réponses mises en cache ne peuvent plus fuiter d'une
  organisation à l'autre.
- **Correspondance des bons de commande et frais.** Les frais que le bon de
  commande prévoit à zéro reçoivent un plancher absolu, la tolérance sur les
  frais s'applique aussi aux frais que la commande ne budgétise pas, et un même
  champ peut lister plusieurs éléments de coût dont les montants sont répartis
  proportionnellement au bon de commande. Une colonne de correspondance peut
  porter un indicateur « autoriser l'écart ». Les cartes de workflow comparent
  les frais par liste, et la limite d'exécution des workflows passe de 30 à 50.
- **Moins de chiffres erronés.** Les montants s'affichent dans le format
  personnel de chaque utilisateur (Suisse et Slovénie comprises), les valeurs
  sans heure conservent leur jour calendaire dans tous les fuseaux horaires,
  l'équation du total américain tient compte des montants supplémentaires et
  des factures à plusieurs taxes, et les documents dont les montants d'en-tête
  valent 0,00 ne tombent plus dans la mauvaise passe de candidats.

---

## Également corrigé dans cette version

- Le tableau de bord ne reste plus vide lorsqu'une condition de concurrence
  fixe le filtre de sous-organisation sur l'identifiant de l'organisation et
  exclut ainsi tous les documents.
- Les valeurs de dimension peuvent de nouveau être sélectionnées par tous les
  utilisateurs.
- Une erreur de téléversement signalée par un client est corrigée.
- « Correspondance sur le total » fonctionne pour les fournisseurs dont la
  facture ne comporte qu'une seule ligne, ainsi que pour les configurations de
  fournisseurs concernées.
- E-documents SPS : les frais du 810 sont ajustés, la présentation des frais du
  855 est mise à jour, et le logo client dans l'aperçu de l'e-document est
  corrigé.

---

## Web App — `10.78.9.4`

**Settings Assistant**
- Un panneau de discussion latéral droit avec un interrupteur est présent sur
  toutes les pages de paramètres. La conversation survit aux changements de
  page, est limitée à 20 messages et affiche les modifications appliquées avec
  une option d'annulation.
- Il vous accueille avec des questions adaptées à la page de paramètres en
  cours et affiche des cartes de paramètres avec un interrupteur
  activé/désactivé. Échap ferme d'abord les menus, Stop interrompt une réponse
  en cours, et les captures d'écran dans les réponses s'ouvrent dans une
  visionneuse.
- L'application d'une modification ouvre une boîte de dialogue avec aperçu,
  confirmation et annulation.
- Chaque paramètre est recherchable depuis la barre latérale, et le paramètre
  trouvé est mis en surbrillance d'une autre couleur. « Ouvrir le paramètre »
  fait défiler jusqu'à la cible à l'intérieur d'un accordéon replié.
- Un interrupteur réservé aux administrateurs de l'organisation pour
  l'assistant se trouve dans Informations sur la société.
- Les conseils de l'IA sont attribués à Nova, et seuls les noms de niveau
  apparaissent, jamais les identifiants de modèle.

**Écran de validation et traitement des documents**
- Nouveau bouton « Contrôle des champs d'en-tête » avec rapport, origine par
  champ et page d'aide (voir Points forts). Les libellés de source et les pastilles
  d'état restent à l'intérieur de leurs cellules.
- Les badges texte « issu des données de base » à côté des libellés de champ
  ont disparu ; la fenêtre d'origine porte cette information.
- Une validation de champ unique et partagée s'exécute partout, ce qui supprime
  l'erreur générique « Un ou plusieurs champs doivent être validés » après
  Auto Accounting.
- Des infobulles sur les boutons de la fenêtre de champ (Supprimer, Effacer,
  Confirmer) indiquent ce que fait chacun avant que vous ne cliquiez.
- Une ligne optimiste affiche désormais ce qui a été enregistré, et non ce qui
  a été saisi. Un remappage de colonne ne demande confirmation que lorsqu'une
  colonne visible perd son mappage.
- Les pages au-delà de la limite de pages OCR sont en lecture seule et
  signalées, y compris dans la visionneuse Auto Accounting. L'ancien panneau de
  restriction de pages à l'import est retiré.
- Un tableau de bons de commande apparaît pour chaque numéro de bon de commande
  d'un champ d'en-tête multi-BC, et le Layout Builder nomme les onglets BC
  d'après la clé du tableau BC et ne signale plus le module comme désactivé
  lorsque le tableau BC est actif.
- La carte de proposition affiche la tolérance au lieu de `[object Object]`, et
  l'écran de comparaison d'approbation cesse d'arrondir les colonnes de
  comparaison configurées (numéros d'article).

**Comptes, paramètres et erreurs**
- Chaque message d'erreur et chaque erreur de connexion affiche l'identifiant
  de trace de la requête en échec, afin que le support puisse la retrouver. Les
  erreurs WebSocket du tableau de bord rejettent exactement la requête qu'elles
  nomment.
- Informations sur la société liste les domaines e-mail de l'organisation.
- Les administrateurs peuvent renvoyer l'e-mail « Définir votre mot de passe »
  depuis la page utilisateur.
- Les administrateurs globaux définissent le début du contrat dans le tableau
  des abonnements.
- Les administrateurs d'organisation voient l'onglet Executive Dashboard et les
  boutons d'ajout et de suppression XSLT. Les membres enregistrent leurs mises
  en page comme préférence personnelle.
- Une session sans organisation reçoit un message d'erreur clair et le sélecteur
  d'organisation au lieu d'un tableau de bord vide.
- Les montants suivent le format numérique personnel de l'utilisateur, et les
  valeurs sans heure conservent leur jour dans tous les fuseaux horaires.
- Les données de base n'envoient les identifiants de sous-organisation que
  lorsqu'ils diffèrent de l'identifiant de l'organisation, et les en-têtes de
  données de base personnalisés sont envoyés comme en-têtes.
- Le masque Tableaux ne coupe plus la liste déroulante « Utiliser l'IA », le
  texte d'aide de l'IA ne recouvre plus la ligne d'entraînement, et le tableau
  IA conserve son bouton Appliquer direct, avec un contrôle d'en-tête réduit à
  une icône et un message de licence.
- Les icônes d'extraction de tableaux s'affichent de nouveau après la
  suppression de l'ancienne police d'icônes.

**Tableau des tâches**
- Le tableau charge sa première page avec moins de requêtes en double, Entrée
  lance immédiatement la recherche, les réponses tardives sont associées à la
  bonne recherche, le pied de page affiche le nombre réel de résultats au lieu
  de la capacité de la page, et une suppression lancée dans une organisation est
  annulée avant son envoi si vous changez d'organisation.

---

## API Service — `12.83.293`

**Settings Assistant et MCP**
- Point d'accès de discussion avec garde-fous : uniquement des questions sur
  DocBits, aucune modification sans confirmation, les questions floues ou
  méta reçoivent de l'aide plutôt qu'un refus, et les réponses diffusent
  d'abord les cartes, puis le texte.
- Des briques en lecture seule pour chaque domaine de paramètres (autorisations
  de groupe, canaux d'import, correspondance des bons de commande,
  comptabilité, domaines e-mail), un catalogue de liens profonds avec un outil
  de recherche de paramètres, et une recherche dans la documentation avec les
  images de la documentation DocBits.
- Flux d'application de la vague 1 : aperçu, confirmation et annulation pour
  les paramètres pris en charge, une seule règle de périmètre pour les trois,
  protégé contre la double confirmation et l'expiration.
- Les outils MCP ne lisent jamais de fichiers du serveur en mode distant, et
  les outils de jeux de test et de laboratoire ne fonctionnent que sur dev.

**IA**
- De nouveaux modèles derrière les niveaux Fast et Full, le niveau Auto, Nexus
  Flash et la préférence du mode vision. Les préférences `AI_MODEL`
  enregistrées sont migrées vers les nouveaux niveaux.
- « Utiliser l'IA » documente ce que demande l'extraction structurée.

**Sécurité et isolation**
- Seuls les administrateurs de l'organisation modifient les préférences de
  l'organisation.
- L'appel `/accounting/rebuild` n'entraîne que l'organisation de l'appelant,
  refuse par défaut en cas d'échec de la recherche de l'organisation et répond
  400 pour un identifiant invalide.
- Le rendu XSLT, XML et PDF interdit l'accès aux fichiers et au réseau, ne
  résout aucune inclusion externe, et les octets des factures sont assainis
  avant d'atteindre le transformateur. Les aperçus PDF rendus n'autorisent que
  les hôtes d'images de confiance.
- Les clés de cache portent l'organisation et un même identifiant donne
  toujours la même clé, de sorte qu'un identifiant d'organisation étranger ne
  peut plus lire des données en cache. Les purges du cache du tableau de bord à
  l'échelle de l'organisation à chaque modification de document ont disparu.
- La liste des domaines e-mail de l'organisation est transmise à Auth.

**Correspondance des bons de commande et export**
- Un champ peut lister plusieurs éléments de coût dont les montants sont
  répartis proportionnellement au bon de commande.
- Les substituts d'approbation renvoient à la demande d'approbation active, les
  enregistrements d'approbation réparés ne bloquent plus, et un document en
  attente d'approbation est refusé à l'export.
- L'annotation PDF/A conserve le catalogue et le XML intégré, de sorte que les
  factures électroniques gardent leur XML après annotation. Les factures UBL
  avec le seul CustomizationID EN 16931 sont classifiées (réseau de factures
  électroniques).
- GRPR arrondit aux 6 décimales acceptées par M3. Les facteurs de conversion de
  l'unité de mesure de base sont ajoutés à la ligne figée.
- Les entraînements et règles de mise en forme supprimés logiquement sont
  respectés, et `update_document_fields` de MCP ne confirme plus une écriture
  perdue. `get_table_rules` répond par un échec typé, et une charge de
  traductions vide utilise sa valeur de repli.
- Les montants slovènes utilisent `sl_SI` et les préférences enregistrées sont
  migrées. Les libellés de classification personnalisés envoyés sous forme
  d'identifiants UUID sont résolus. Les tableaux de bord partagés conservent
  `created_by` et la liste de partage lors d'une mise à jour.
- Les trames d'erreur du tableau de bord portent le `request_id` de la requête,
  et chaque réponse JSON en échec porte un identifiant de trace.
- Le système ne redémarre que les workers défaillants au lieu de toute la flotte
  API et vérifie correctement la liste des tâches enregistrées. La file du
  moniteur de blocages est de nouveau consommée.

---

## Auth Service — `1.78.49`

- Un défi d'authentification multifacteur est à usage unique sur chaque chemin
  de connexion, et non plus seulement dans le flux MCP. L'enrôlement exige le
  code reçu par e-mail, aucun jeton d'enrôlement n'est émis après une connexion
  par mot de passe partagé, et les utilisateurs sont avertis lorsqu'un facteur
  est enrôlé.
- Les organisations possèdent une liste de domaines e-mail, chacun n'étant
  attribuable qu'une fois. Une connexion sociale rejoint l'organisation qui
  liste le domaine vérifié, n'invente jamais d'organisation, d'utilisateur ni
  d'abonnement, et refuse sans nommer personne tandis que les administrateurs
  sont informés. Les domaines renvoyés par Microsoft sont pris en charge.
- Chaque connexion refusée porte un identifiant de trace. Les administrateurs
  peuvent renvoyer l'e-mail « Définir votre mot de passe ». Le solde du contrat
  est signé et le début du contrat est audité.

## Auth Bridge — `0.5.7`

- La réplication des comptes UE et US garde sa connexion alimentée pendant la
  réconciliation, rattache d'elle-même un slot de réplication perdu, utilise une
  mémoire bornée et considère qu'une origine de réplication existante est un
  succès. La connexion entre régions est plus fiable.

## Docflow Service — `2.10.22`

- La carte de prix unitaire distinct lit les définitions de champ par défaut de
  l'organisation pour les frais et compare chaque élément de coût listé par un
  champ.
- La limite d'exécution des workflows passe de 30 à 50, et les recherches dans
  les journaux de workflow rejettent un identifiant qui n'est pas un UUID.

## Docnet Service — `1.56.15`

- `list_document_fields` signale chaque colonne de tableau configurée, y
  compris celles qui sont vides.

## Extraction Service — `1.56.0.1`

- Niveaux : de nouveaux modèles derrière Fast et Full, Auto, Nexus Flash et un
  mode vision. Les requêtes vision vers l'hôte d'inférence restent sous sa
  limite de taille.
- L'extraction de tableaux avec Nexus regroupe les pages par lots (deux par
  lot), exécute les lots en parallèle avec un délai d'attente mesuré, relance
  les erreurs transitoires et divise un lot qui a dépassé le délai. Les champs
  d'en-tête sont lus dans tous les lots.
- Totaux US : les montants supplémentaires font partie de l'équation du total,
  la paire 1 compte dans la protection de la paire 2, les candidats à faible
  score sont ignorés lorsque les taxes ne sont pas nulles, et « above » et
  « below » reconnaissent les libellés de plusieurs mots.
- Les champs d'identifiant corrigent les caractères qui se rencontrent
  réellement, et les caractères invisibles sont traités selon leur sens, de
  sorte qu'un « O » ne devient plus un caractère étrange.

## Fulltext Service — `1.42.41`

- Nouvel index pour la documentation DocBits, avec des points d'accès
  d'ingestion et de recherche, des images dans les réponses et un délai limite
  pour l'ensemble de la recherche. Il alimente le Settings Assistant.

## PO Match Service — `1.59.48`

- Plancher absolu pour les frais que le bon de commande prévoit à zéro, et
  tolérance sur les frais que la commande ne budgétise pas.
- Une colonne peut porter un indicateur « autoriser l'écart ». Plusieurs
  éléments de coût par champ sont répartis proportionnellement.
- Seuls les administrateurs de l'organisation rédigent ou approuvent les règles
  de correspondance, et les conditions de règle n'acceptent qu'une grammaire
  d'expressions autorisée.
- Les modifications de règles peuvent être simulées par rapport à un jeu de
  règles de substitution sans écriture, pour les propositions de modification
  Touchless. Les colonnes supplémentaires de BC à rapprocher sont lues depuis
  l'attribut du type de document, avec une migration de l'ancienne préférence.

---

_Non concernés par cette version : Auto Accounting, Barcode, E-Mail, FTP,
Ideas, OCR, Operator. FTP et Operator ne comportent que de la maintenance
interne._

<!-- Release R1.0.15 (sandbox 02-10-26, planned prod 14-10-26, deployed Wednesday 14 Oct 2026).
Versions on prod before this deploy: API 12.83.222, Auth 1.78.38, Auth Bridge 0.4.2,
Docflow 2.10.18, Docnet 1.56.13, Extraction 1.55.50.1, Fulltext 1.42.38, PO Match 1.59.39,
Web App 10.70.6.
Held back (Release No. names a later release; announce with that release):
R1.1: CORE-6145, CORE-6148 (import failure notice and card per channel), CORE-6127 and
CORE-6136 (run transformation rules after master data lookup), CORE-6117, CORE-6072, CORE-6071,
CORE-2452, CORE-2444, DRFS-779, CORE-554 (rule execution logs from the dashboard), CORE-550, CORE-6278,
CORE-6180, CORE-6168, DMB-431, OBO-160, DRFS-806 (date tolerance for PO matching and approval).
R1.0.16: CORE-6103 (assistant drafts transformation rules), DRFS-822 (charge cards use only
matched POs, trigger status filter), DPG-170 (cost invoice export gate), OBO-159 (the "x" on a
field stores "leave empty" on its own; field suppression).
R1.2 / R1.4: DRFS-535 (receipt availability flag), DOP-53 (UOM conversion).
Added from the Ready for Production Release list: DRFS-742, DU-220, MAR-67, DRFS-708, DRFS-820,
DRFS-723, DRFS-724, DRFS-726. Not on the page (no matching code in the delta, check by hand):
MEF-169 (S/MIME invoices from one supplier not arriving, Email Service version unchanged), DMB-391.
Shipped although Release No. is empty or stale: OBO-156, CORE-6102, CORE-6154, CORE-6155,
CORE-6150, CORE-6169, CORE-6181, CORE-6183, CORE-6185, CORE-6187, CORE-2606, CORE-2461,
CORE-2457, CORE-6092 (R1.0.14 labels). -->
