# Routage des notifications

<figure><img src="../../../../.gitbook/assets/edoc_notification_routing.png" alt="Routes de notification"><figcaption><p>Association des résultats de validation aux agents</p></figcaption></figure>

La page **Routage des notifications** (**Documents électroniques → Actions**) associe les résultats de validation aux **agents AI Workforce**. Chaque résultat bloquant déclenche exactement un agent — celui dont le préfixe de code correspond le plus longtemps. Tout ce qui ne correspond à rien revient à l'agent de notification au fournisseur par défaut.

## Routes de notification

Choisissez qui gère chaque type de problème de facture. Tout ce qui n'est pas répertorié va à l'agent par défaut :

| Route | Résultats couverts |
|-------|--------------------|
| **Règles métier colombiennes** | Résultats des règles métier propres à la Colombie. |
| **Règles métier allemandes** | Résultats des règles métier propres à l'Allemagne. |
| **Vérifications IBAN / compte bancaire** | Résultats sur les données de paiement (somme de contrôle IBAN, longueur, pays). |
| **Vérifications du numéro de TVA** | Résultats sur le format du numéro de TVA. |
| **Tout le reste** | Le recours par défaut pour tout ce qui n'est pas associé ci-dessus. |

Pour chaque route, choisissez l'agent responsable dans le menu déroulant. **Avancé (règles de code personnalisées)** permet d'acheminer selon un code de résultat exact lorsque vous avez besoin d'un contrôle plus fin.

## Agents disponibles

<figure><img src="../../../../.gitbook/assets/edoc_notification_agents.png" alt="Registre des agents disponibles"><figcaption><p>Registre en lecture seule des agents AI Workforce</p></figcaption></figure>

La section **Agents disponibles** est un registre en lecture seule des agents AI Workforce fournis avec votre déploiement, par exemple :

| Agent | Rôle |
|-------|------|
| **Notification fournisseur par défaut** | E-mail générique de notification au fournisseur ; l'agent fourre-tout lorsqu'aucun agent plus spécifique ne correspond. |
| **Banking Bot** | Modèle spécialisé pour les résultats de données de paiement (corrections IBAN/BIC). |
| **Tax Bot** | Notification au fournisseur spécifique au numéro de TVA. |
| **Compliance Bot** | Gère les résultats de conformité. |

Chaque agent affiche sa tâche Celery et les préfixes de code de résultat qu'il gère par défaut.
