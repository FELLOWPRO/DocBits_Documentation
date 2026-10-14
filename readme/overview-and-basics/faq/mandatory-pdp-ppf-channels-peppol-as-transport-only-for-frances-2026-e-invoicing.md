# Canaux PDP/PPF obligatoires – PEPPOL uniquement comme transport pour la facturation électronique 2026 en France

## PDP ou PPF requis pour les factures électroniques B2B nationales

Dans le cadre de l'obligation de facturation électronique de 2026 en France, les entreprises ne peuvent pas se reposer uniquement sur le réseau PEPPOL pour échanger leurs factures B2B nationales. La loi exige que toutes les factures entre entreprises françaises assujetties à la TVA transitent soit par une plateforme privée certifiée (PDP), soit par le portail public de facturation de l'État (PPF), afin de satisfaire aux [exigences](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform) légales ￼. Autrement dit, les entreprises n'enverront plus leurs factures directement à leurs clients : elles devront les transmettre via une plateforme de facturation électronique agréée (une PDP) ou via le [portail](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html) gouvernemental ￼. Cela garantit que l'administration fiscale reçoit les données requises en temps réel. Un simple échange de factures via PEPPOL, sans l'intervention d'une PDP/PPF accréditée, ne satisferait pas aux obligations de déclaration et de transmission imposées.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt=""><figcaption></figcaption></figure>

### Présentation de l'offre de service

Le mode API permet aux utilisateurs d'accéder à toutes les fonctionnalités mises à leur disposition depuis les outils informatiques déjà déployés au sein des structures partenaires. Il existe deux modes d'intégration :

### ·       Intégration dans les systèmes d'information (SI) :

Les API sont intégrées directement dans les systèmes d'information ou les logiciels de gestion des parties émettrices et réceptrices de factures, ou de leurs opérateurs de dématérialisation (OD). Les utilisateurs accèdent ainsi directement aux fonctionnalités de la solution et à leurs évolutions depuis leurs outils informatiques habituels, internes ou proposés par leur OD.

Les API peuvent également être intégrées dans le SI des PDP afin de leur offrir davantage de souplesse (par rapport au mode EDI), certaines API étant dédiées à leur usage.

### ·       Intégration dans des logiciels tiers :

Les éditeurs pourront proposer des logiciels reposant sur les API. Selon le mode choisi par l'éditeur, la connexion pourra alors être effectuée par l'éditeur, ou par le client lui-même lors de l'installation ou du déploiement dans son SI. Ce logiciel tiers complétera le système d'information du client en ajoutant une couche de communication vers le PPF.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt=""><figcaption></figcaption></figure>

## PEPPOL utilisé uniquement comme couche d'interopérabilité

La France adopte PEPPOL dans le cadre de son infrastructure, mais uniquement comme couche de transport au sein du dispositif des PDP, et non comme voie de conformité indépendante.  L'administration fiscale française (DGFiP) devient l'autorité Peppol (Peppol Authority) afin de standardiser la manière dont les PDP [s'interconnectent](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html) . Toutes les PDP certifiées sont tenues de s'interconnecter via le réseau PEPPOL pour échanger des [factures](https://nymus.be/fr/facturation-electronique-en-france/) .  Cela signifie que PEPPOL facilitera l'interopérabilité entre les plateformes autorisées, sans remplacer le besoin de ces plateformes.  En pratique, une entreprise ne peut utiliser PEPPOL qu'en passant par une PDP (ou le PPF agissant dans son rôle limité) qui utilise PEPPOL pour envoyer ou recevoir des factures. Les directives officielles l'ont confirmé : le portail public se concentre sur la collecte des données, tandis que la distribution des factures se fera exclusivement par les PDP, celles-ci s'appuyant sur des réseaux tels que [PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) pour l'[échange](https://nymus.be/fr/facturation-electronique-en-france/) .

\


<figure><img src="../../.gitbook/assets/Picture 2.png" alt=""><figcaption></figcaption></figure>

## Connexion d'un hub :

Le hub fournit à ses clients une solution web ou applicative leur permettant d'effectuer les différents appels d'API. **C'est donc le hub qui effectue les appels d'API pour le compte de tous ses clients**. Dans ce cas, chaque partenaire doit disposer d'un compte technique, mais seul le hub a besoin d'une application sous PISTE et d'une connexion au PPF.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt=""><figcaption></figcaption></figure>



Source : l'article 91 de la loi de finances 2024 de la France (résumé par EY) impose que les factures électroniques soient envoyées via une PDP certifiée ou le portail de l'État .  Les mises à jour de l'administration fiscale française précisent en outre qu'après les réformes de 2024, les entreprises doivent recourir à une PDP immatriculée pour la facturation électronique B2B (le PPF ne servira plus de plateforme d'échange gratuite) .  PEPPOL est mis en œuvre pour interconnecter ces PDP, et non comme un canal alternatif en dehors du système .  Cela confirme que l'utilisation du seul réseau PEPPOL est insuffisante : la conformité au régime de facturation électronique 2026 en France exige une intégration avec le PPF ou une PDP certifiée, PEPPOL n'étant que le réseau de livraison sous-jacent entre ces plateformes.

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt=""><figcaption></figcaption></figure></div>
