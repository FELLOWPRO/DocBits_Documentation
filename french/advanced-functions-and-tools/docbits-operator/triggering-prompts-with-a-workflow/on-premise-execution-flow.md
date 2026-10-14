# Flux d'exécution sur site

Pour les clients exécutant l'opérateur DocBits sur site, la séquence suivante décrit comment un document traité déclenche et exécute une invite d'opérateur via l'agent local DocBits.

1. **Chargement et traitement du document** Un document est téléchargé dans DocBits et passe par le traitement standard (extraction, validation, etc.).
2. **Déclenchement du flux de travail** Une fois le traitement terminé, un flux de travail configuré dans DocBits évalue ses conditions de déclenchement. Lorsque ces conditions sont remplies, le flux de travail crée une nouvelle **Tâche de l'opérateur**.
3. **Création et envoi de tâches**
   * Le flux de travail envoie le texte du script, les variables, le nombre maximal d'étapes, le nombre maximal de réessais en tant que charge de tâche vers le pool de travail partagé.
4. **Boucle de sondage de l'agent**
   * Un agent DocBits sur site (installé dans l'environnement du client) interroge le pool de travail toutes les 5 minutes. S'il ne trouve aucune tâche, l'agent reste inactif et réessaie après l'intervalle.
5. **Exécution de la tâche**
   * Lorsqu'une tâche apparaît dans le pool de travail, l'agent la récupère et commence l'exécution.
6. **Génération de journaux**
   * Pour chaque étape - succès ou échec - l'agent enregistre des journaux détaillés (actions, statuts, horodatages). À la fin, il compile le journal complet et l'état final.
7. **Retour et affichage des résultats**
   * L'agent envoie les journaux et l'état à DocBits. L'historique d'exécution du flux de travail d'origine est mis à jour, et les utilisateurs peuvent consulter les détails dans l'onglet **Journaux du flux de travail**.
