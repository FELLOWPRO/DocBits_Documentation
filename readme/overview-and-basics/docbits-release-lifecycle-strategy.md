# Stratégie de cycle de vie des versions DocBits

Avec le déploiement de la prochaine version mineure R1.1, DocBits introduit une nouvelle stratégie de cycle de vie des versions reposant sur deux canaux de version : VESTA et NOVA.

**NOVA** est le canal d'introduction des nouvelles versions majeures et mineures, telles que **Rx** et **Rx.y**. **VESTA** continue de fournir la version de production existante.

{% hint style="success" %}
**Important : une seule URL pour VESTA et NOVA**

Continuez à utiliser l'URL habituelle de votre application DocBits. VESTA et NOVA n'ont pas d'URL d'accès distinctes : les deux canaux de version sont accessibles via la même URL standard que vous utilisez déjà pour l'environnement correspondant.

Pour changer de canal, accédez à **Settings > Company Information > Release Channel** et sélectionnez **VESTA** ou **NOVA**. Il n'est pas nécessaire de vous déconnecter puis de vous reconnecter. Votre prochain clic dans l'application vous dirige automatiquement vers la version du canal sélectionné.

Avant de changer de canal, vérifiez que les deux canaux sont prêts et disponibles dans votre environnement, comme expliqué dans [Vérifier impérativement la disponibilité des environnements avant de changer de canal](#vérifier-impérativement-la-disponibilité-des-environnements-avant-de-changer-de-canal).
{% endhint %}

## Canaux de version

| Canal | Rôle dans le cycle de vie |
| --- | --- |
| **VESTA** | Fournit la version de production actuelle. |
| **NOVA** | Fournit la version suivante au fil de son développement, de ses tests et de sa mise à disposition en production. Pendant la phase de production parallèle, NOVA et VESTA proposent toutes deux des versions de production actives. |

## Vue d'ensemble du cycle de vie

![Cycle de vie des versions DocBits VESTA et NOVA en trois phases](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy.png)

Chaque cycle comprend trois phases. Une bascule gérée par FELLOWPRO intègre ensuite la version de production NOVA dans VESTA et lance le cycle suivant.

| Phase | VESTA | NOVA | Ce que cela signifie pour votre organisation |
| --- | --- | --- | --- |
| **1. Développement** | R1.0.x en production | R1.1 en développement | Continuez à utiliser VESTA pendant la préparation de la version suivante. |
| **2. Tests QA et tests d'acceptation** | R1.0.x en production | R1.1 en QA et UAT | Évaluez la future version dans la sandbox NOVA tandis que le travail en production se poursuit sur VESTA. |
| **3. Production parallèle** | R1.0.x en production | R1.1.x en production | Restez sur VESTA ou passez de manière autonome à NOVA lorsque vous êtes prêts. |

Après la bascule, tous les clients utilisent VESTA R1.1.x, et NOVA est réaffecté au développement de R1.2. La phase 1 recommence alors avec ces versions mises à jour.

### Phase 1 — Développement

VESTA fournit la version de production actuelle, R1.0.x, tandis que la version suivante, R1.1, est développée dans NOVA. Votre organisation poursuit ses activités quotidiennes sur VESTA tout au long de cette phase.

### Phase 2 — Tests QA et tests d'acceptation

La future version NOVA passe par l'assurance qualité (QA) et les tests d'acceptation utilisateur (UAT). Vous pouvez l'évaluer dans la sandbox NOVA afin de déterminer comment les modifications s'intègrent aux processus de votre organisation et de préparer son adoption.

VESTA R1.0.x reste la version de production pendant cette phase. Vous pourrez passer à NOVA pour un usage en production dès qu'elle sera disponible en phase 3.

### Phase 3 — Production parallèle

VESTA R1.0.x et NOVA R1.1.x sont toutes deux des versions de production actives. Votre organisation décide si et quand passer à NOVA, en fonction de ses besoins et des résultats de son évaluation dans la sandbox.

Pour adopter NOVA pendant cette phase :

1. Évaluez la version dans la sandbox NOVA.
2. Consultez l'annonce de la version ou confirmez auprès du support FELLOWPRO que les deux environnements de production sont prêts et disponibles pour le changement de canal.
3. Déterminez à quel moment votre organisation est prête à utiliser la nouvelle version en production.
4. Dans DocBits, accédez à **Settings > Company Information > Release Channel** et sélectionnez **NOVA**.

Pendant la production parallèle, vous pouvez également revenir à VESTA en accédant à **Settings > Company Information > Release Channel** et en sélectionnant **VESTA**.

Le changement de canal s'effectue en libre-service. FELLOWPRO ne sélectionne pas les clients qui doivent passer à NOVA. Vous pouvez continuer à utiliser VESTA pendant toute la phase de production parallèle et adopter la nouvelle version lors de la bascule qui suit.

## Bascule de version et cycle suivant

FELLOWPRO gère la bascule lorsque la version NOVA est prête à devenir la version de production commune et que l'acceptation de la transition prévue a été obtenue de la part de tous les clients :

**NOVA R1.1.x → VESTA R1.1.x**

### Annonce préalable et acceptation des clients

FELLOWPRO annonce la bascule prévue à l'avance à tous les clients par e-mail et sollicite leur acceptation de la transition. Nous vous invitons à contacter FELLOWPRO pour toute préoccupation ou objection, afin qu'elle puisse être examinée avant la bascule. La bascule et la réaffectation de NOVA n'ont lieu que lorsque la version est prête et que tous les clients ont accepté la transition prévue.

### Ce qui change lors de la bascule

| Changement | Résultat |
| --- | --- |
| **La version NOVA devient la version VESTA** | R1.1.x devient la version de production commune dans VESTA pour tous les clients. |
| **La version précédente est retirée** | R1.0.x est mise hors service et n'est plus disponible, ni par l'un ou l'autre des canaux, ni par aucun autre moyen. |
| **NOVA est réaffecté à la version suivante** | Le développement de R1.2 commence dans NOVA, ce qui ouvre la phase 1 du cycle suivant. |

Les trois mêmes phases se répètent ensuite avec les nouveaux numéros de version.

Le diagramme ci-dessous illustre plus en détail le cycle de version décrit ci-dessus.

![Cycle de version DocBits VESTA et NOVA détaillé](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy-details.png)

### Cadence des versions

La cadence prévue diffère entre les versions majeures et mineures introduites via NOVA et les correctifs (hotfixes) appliqués aux versions de production dans VESTA et NOVA.

#### Versions majeures et mineures via NOVA

FELLOWPRO prévoit actuellement un cycle d'environ **3 à 4 mois pour les versions majeures et mineures** introduites via le canal de version NOVA, telles que **Rx** et **Rx.y**. Cette estimation s'applique au cycle de vie décrit ci-dessus, y compris la bascule ultérieure vers VESTA et la réaffectation de NOVA à la version suivante. Elle ne décrit pas la fréquence des hotfixes.

Cet intervalle correspond à notre estimation de planification actuelle ; il ne s'agit ni d'un calendrier fixe, ni d'une durée maximale de cycle, ni d'une garantie quant à la date d'une version ou d'une bascule. Le calendrier de chaque bascule et de la réaffectation de NOVA dépend à la fois de **l'état de préparation de la version et de l'acceptation de la transition prévue par tous les clients**. Si un délai supplémentaire est nécessaire pour finaliser la version, répondre aux préoccupations des clients ou obtenir l'acceptation de chaque client, le cycle sera prolongé et pourra durer plus de quatre mois.

FELLOWPRO communique chaque bascule prévue à l'avance. Tout calendrier indicatif reste soumis à la réalisation de ces conditions.

#### Hotfixes en production VESTA

Les hotfixes pour la version de production VESTA sont attendus environ **une fois par mois, ou à intervalles un peu plus longs**. Il s'agit d'une cadence indicative, et non d'un calendrier fixe ni d'une date de livraison garantie.

#### Hotfixes de stabilisation en production NOVA

Il n'est pas possible de définir une cadence générale pour les hotfixes de stabilisation en production NOVA. NOVA introduit des versions entièrement nouvelles : le calendrier et la fréquence de ces hotfixes dépendent donc des besoins de stabilisation de chaque version. Ils ne suivent par conséquent ni la cadence mensuelle indicative de VESTA, ni le cycle de 3 à 4 mois des versions majeures et mineures.

## Responsabilités et choix du client

| Transition | Qui la gère | À quoi vous attendre |
| --- | --- | --- |
| **Passage de VESTA à NOVA et inversement pendant la phase 3** | Votre organisation | Évaluez NOVA dans la sandbox et choisissez si et quand effectuer le passage. Utilisez **Settings > Company Information > Release Channel** pour sélectionner NOVA ou revenir à VESTA pendant la production parallèle. |
| **Bascule de NOVA R1.1.x vers VESTA R1.1.x** | FELLOWPRO | Prenez connaissance de l'annonce préalable envoyée par e-mail, faites part de vos éventuelles préoccupations ou objections et confirmez votre acceptation de la transition prévue. FELLOWPRO procède à la bascule une fois la version prête et l'acceptation de tous les clients obtenue. |

## Vérifier impérativement la disponibilité des environnements avant de changer de canal

Ne changez de canal entre VESTA et NOVA via **Settings > Company Information > Release Channel** que lorsque les versions sont disponibles en parallèle et prêtes à l'emploi dans **l'environnement correspondant sur les deux canaux**. La disponibilité en sandbox et en production doit être évaluée séparément :

- **Sandbox :** vous pouvez passer de VESTA Sandbox à NOVA Sandbox dès que la nouvelle version est prête et disponible dans NOVA Sandbox, tandis que VESTA Sandbox reste disponible. La même exigence de disponibilité s'applique pour revenir en arrière.
- **Production :** vous ne pouvez passer de VESTA Production à NOVA Production, et inversement, que tant que les deux versions de production sont prêtes et disponibles en parallèle. La disponibilité dans NOVA Sandbox ne signifie pas que NOVA Production est prête à l'emploi.

Changer de canal alors que l'environnement correspondant n'est pas prêt ou disponible peut perturber vos opérations. FELLOWPRO envoie des e-mails d'annonce de version quelques jours avant que les versions ne soient disponibles en sandbox ou en production. Consultez ces annonces avant de changer de canal. Si vous ne savez pas si un changement de canal est possible ou approprié pour votre organisation, contactez le support FELLOWPRO pour obtenir une confirmation.

**Contrôle de disponibilité prévu :** FELLOWPRO travaille sur un contrôle Oui/Non qui permettra au support de rendre le paramètre Release Channel en lecture seule ou d'activer le changement de canal indépendamment d'un déploiement logiciel. Une fois ce contrôle disponible, le support l'utilisera pour activer le changement de canal lorsque les environnements correspondants sont prêts et pour maintenir le paramètre en lecture seule dans le cas contraire. L'objectif est de permettre aux clients de passer en toute sécurité de VESTA à NOVA et inversement lorsque le paramètre est activé. Tant que ce contrôle n'est pas introduit, un paramètre modifiable ne doit pas, à lui seul, être considéré comme une confirmation qu'un changement de canal est approprié ; suivez les annonces de version ou confirmez auprès du support.

## Questions fréquentes

### Comment savoir s'il est sûr de passer de VESTA à NOVA et inversement ?

Consultez l'annonce de la version pour l'environnement que vous comptez utiliser, ou demandez au support FELLOWPRO de confirmer que le changement de canal est approprié. Les deux environnements correspondants doivent être prêts et disponibles en parallèle ; la disponibilité en sandbox ne confirme pas celle de la production. Consultez [Vérifier impérativement la disponibilité des environnements avant de changer de canal](#vérifier-impérativement-la-disponibilité-des-environnements-avant-de-changer-de-canal) ci-dessus pour les indications complètes, y compris le contrôle prévu pour activer ou désactiver le changement de canal.

### Pouvons-nous rester sur VESTA lorsque NOVA est disponible en production ?

Oui. Pendant la phase 3, vous pouvez rester sur VESTA ou passer à NOVA lorsque votre organisation est prête. Lors de la bascule suivante, la nouvelle version devient VESTA et la version précédente est retirée.

### Comment passer à NOVA ou revenir à VESTA ?

Commencez par vérifier que l'environnement correspondant est prêt et disponible sur les deux canaux, comme expliqué dans [Vérifier impérativement la disponibilité des environnements avant de changer de canal](#vérifier-impérativement-la-disponibilité-des-environnements-avant-de-changer-de-canal). La disponibilité en sandbox et la disponibilité en production sont distinctes.

Pendant la phase 3, accédez à **Settings > Company Information > Release Channel** dans DocBits et sélectionnez **NOVA** pour adopter la nouvelle version de production, ou **VESTA** pour revenir à la version de production VESTA actuelle. Votre organisation fait ce choix de manière autonome, en fonction de ses besoins et de son évaluation de NOVA dans la sandbox. Ce choix s'applique tant que les deux versions sont disponibles en parallèle ; la version VESTA précédente est retirée lors de la bascule.

### Quand NOVA est-il disponible pour un usage en production ?

NOVA devient une version de production active en phase 3, après le développement et les phases QA/UAT. Pendant cette phase, VESTA et NOVA fonctionnent en parallèle en production avec des versions logicielles différentes.

### Comment serons-nous informés de la bascule, et pouvons-nous émettre des objections ?

FELLOWPRO envoie un e-mail à l'avance à tous les clients et sollicite leur acceptation de la transition prévue. Nous vous invitons à faire part de toute préoccupation ou objection à FELLOWPRO. La bascule et la réaffectation de NOVA n'ont lieu que lorsque la version est prête et que l'acceptation de tous les clients a été obtenue.

### Pouvons-nous continuer à utiliser R1.0.x après la bascule ?

Non. R1.0.x est mise hors service lors de la bascule et n'est plus disponible, ni par l'un ou l'autre des canaux, ni par aucun autre moyen. R1.1.x devient la version de production VESTA commune à tous les clients.

### En quoi la bascule diffère-t-elle de notre passage à NOVA ?

Votre passage à NOVA pendant la phase 3 est un choix en libre-service quant au moment d'adopter la nouvelle version de production. La bascule est la transition ultérieure gérée par FELLOWPRO : NOVA R1.1.x devient VESTA R1.1.x, la version précédente est retirée et le cycle suivant commence.

### Qu'advient-il de NOVA après la bascule ?

NOVA est réaffecté au développement de la version suivante, R1.2 dans cet exemple. VESTA fournit R1.1.x tandis que NOVA repasse par les phases de développement, de QA/UAT et de production parallèle.

### Une version majeure ou mineure est-elle garantie tous les trois à quatre mois ?

Non. La cadence d'environ 3 à 4 mois pour les versions majeures et mineures introduites via NOVA est une estimation de planification actuelle, et non un calendrier garanti ni une durée maximale. La bascule et la réaffectation de NOVA nécessitent à la fois que la version soit prête et que tous les clients aient donné leur acceptation. Si l'une ou l'autre de ces conditions demande plus de temps, le cycle sera prolongé et pourra dépasser quatre mois. FELLOWPRO communique chaque bascule prévue à l'avance.
