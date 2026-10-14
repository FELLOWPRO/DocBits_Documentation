# Stratégie de cycle de vie des versions DocBits

DocBits utilise deux canaux de version, **VESTA** et **NOVA**, pour introduire de nouvelles versions et laisser à votre organisation le temps de les évaluer avant de les adopter. Pendant la phase de production parallèle, vous choisissez si et quand passer à la nouvelle version. FELLOWPRO gère ensuite la bascule qui en fait la version de production commune à tous les clients.

Les numéros de version utilisés dans ce guide (R1.0.x, R1.1.x et R1.2) sont donnés à titre d'exemple. Le même cycle de vie se répète pour chaque version successive ; `x` désigne les mises à jour au sein d'une série de versions.

## Canaux de version

| Canal     | Rôle dans le cycle de vie                                                                                                                                                                                                          |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VESTA** | Fournit la version de production actuelle.                                                                                                                                                                                         |
| **NOVA**  | Fournit la version suivante au fil de son développement, de ses tests et de sa mise à disposition en production. Pendant la phase de production parallèle, NOVA et VESTA proposent toutes deux des versions de production actives. |

## Vue d'ensemble du cycle de vie

![Cycle de vie des versions DocBits VESTA et NOVA en trois phases](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy.png)

Chaque cycle comprend trois phases. Une bascule gérée par FELLOWPRO intègre ensuite la version de production NOVA dans VESTA et lance le cycle suivant.

| Phase                                  | VESTA                | NOVA                  | Ce que cela signifie pour votre organisation                                                              |
| -------------------------------------- | -------------------- | --------------------- | --------------------------------------------------------------------------------------------------------- |
| **1. Développement**                   | R1.0.x en production | R1.1 en développement | Continuez à utiliser VESTA pendant la préparation de la version suivante.                                 |
| **2. Tests QA et tests d'acceptation** | R1.0.x en production | R1.1 en QA et UAT     | Évaluez la future version dans la sandbox NOVA tandis que le travail en production se poursuit sur VESTA. |
| **3. Production parallèle**            | R1.0.x en production | R1.1.x en production  | Restez sur VESTA ou passez de manière autonome à NOVA lorsque vous êtes prêts.                            |

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
2. Déterminez à quel moment votre organisation est prête à l'utiliser en production.
3. Passez de VESTA à NOVA à l'aide du paramètre **Release Channel** dans l'application DocBits.

Ce changement s'effectue en libre-service. FELLOWPRO ne sélectionne pas les clients qui doivent passer à NOVA. Vous pouvez continuer à utiliser VESTA pendant toute la phase de production parallèle et adopter la nouvelle version lors de la bascule qui suit.

## Bascule de version et cycle suivant

FELLOWPRO gère la bascule lorsque la version NOVA est prête à devenir la version de production commune et que l'acceptation de la transition prévue a été obtenue de la part de tous les clients :

**NOVA R1.1.x → VESTA R1.1.x**

### Annonce préalable et acceptation des clients

FELLOWPRO annonce la bascule prévue à l'avance à tous les clients par e-mail et sollicite leur acceptation de la transition. Nous vous invitons à contacter FELLOWPRO pour toute préoccupation ou objection, afin qu'elle puisse être examinée avant la bascule. La bascule et la réaffectation de NOVA n'ont lieu que lorsque la version est prête et que tous les clients ont accepté la transition prévue.

### Ce qui change lors de la bascule

| Changement                                   | Résultat                                                                                                            |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **La version NOVA devient la version VESTA** | R1.1.x devient la version de production commune dans VESTA pour tous les clients.                                   |
| **La version précédente est retirée**        | R1.0.x est mise hors service et n'est plus disponible, ni par l'un ou l'autre des canaux, ni par aucun autre moyen. |
| **NOVA est réaffecté à la version suivante** | Le développement de R1.2 commence dans NOVA, ce qui ouvre la phase 1 du cycle suivant.                              |

Les trois mêmes phases se répètent ensuite avec les nouveaux numéros de version.

Le diagramme ci-dessous illustre plus en détail le cycle de version décrit ci-dessus.

![Cycle de version DocBits VESTA et NOVA détaillé](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy-details.png)

### Cadence des versions

FELLOWPRO prévoit actuellement un cycle de version d'environ **3 à 4 mois**. Cet intervalle correspond à notre estimation de planification actuelle ; il ne s'agit ni d'un calendrier fixe, ni d'une durée maximale de cycle, ni d'une garantie quant à la date d'une version ou d'une bascule.

Le calendrier de chaque bascule et de la réaffectation de NOVA dépend à la fois de **l'état de préparation de la version et de l'acceptation de la transition prévue par tous les clients**. Si un délai supplémentaire est nécessaire pour finaliser la version, répondre aux préoccupations des clients ou obtenir l'acceptation de chaque client, le cycle sera prolongé et pourra durer plus de quatre mois.

FELLOWPRO communique chaque bascule prévue à l'avance. Tout calendrier indicatif reste soumis à la réalisation de ces conditions.

## Responsabilités et choix du client

| Transition                                     | Qui la gère        | À quoi vous attendre                                                                                                                                                                                                                                                                      |
| ---------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Passage de VESTA à NOVA pendant la phase 3** | Votre organisation | Évaluez NOVA dans la sandbox et choisissez si et quand effectuer le passage à l'aide du paramètre Release Channel de l'application.                                                                                                                                                       |
| **Bascule de NOVA R1.1.x vers VESTA R1.1.x**   | FELLOWPRO          | Prenez connaissance de l'annonce préalable envoyée par e-mail, faites part de vos éventuelles préoccupations ou objections et confirmez votre acceptation de la transition prévue. FELLOWPRO procède à la bascule une fois la version prête et l'acceptation de tous les clients obtenue. |

## Questions fréquentes

### Pouvons-nous rester sur VESTA lorsque NOVA est disponible en production ?

Oui. Pendant la phase 3, vous pouvez rester sur VESTA ou passer à NOVA lorsque votre organisation est prête. Lors de la bascule suivante, la nouvelle version devient VESTA et la version précédente est retirée.

### Comment passer à NOVA ?

Dès que NOVA est disponible en production, utilisez le paramètre **Release Channel** dans l'application DocBits. Votre organisation fait ce choix de manière autonome, en fonction de ses besoins et de son évaluation de la version dans la sandbox NOVA.

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

### Une nouvelle version est-elle garantie tous les trois à quatre mois ?

Non. La cadence d'environ 3 à 4 mois est une estimation de planification actuelle, et non un calendrier garanti ni une durée maximale. La bascule et la réaffectation de NOVA nécessitent à la fois que la version soit prête et que tous les clients aient donné leur acceptation. Si l'une ou l'autre de ces conditions demande plus de temps, le cycle sera prolongé et pourra dépasser quatre mois. FELLOWPRO communique chaque bascule prévue à l'avance.
