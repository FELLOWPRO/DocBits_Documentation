# Debug Collector

Le Debug Collector capture un instantané complet de votre session DocBits — activité réseau, erreurs, environnement du navigateur et indicateurs de performance — l'emballe en rapport JSON et peut, sur demande, ouvrir un ticket de support directement depuis la même boîte de dialogue.

## Comment y accéder

Appuyez sur <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> sous Windows et Linux, ou <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> sous macOS. La boîte de dialogue Performance Report s'ouvre immédiatement.

<figure><img src="../../.gitbook/assets/debug-collector-dialog.png" alt="Boîte de dialogue Debug Collector"><figcaption><p>La boîte de dialogue Performance Report affiche l'instantané capturé et un formulaire intégré de création de ticket.</p></figcaption></figure>

## Ce qui est capturé

* **Appels API** — les 60 derniers appels REST et WebSocket, avec durées, codes de statut et URLs sollicitées. Les appels de plus de deux secondes sont signalés séparément.
* **Erreurs** — les erreurs JavaScript récentes et les promesses rejetées non interceptées depuis la console du navigateur.
* **Journaux de console** — les derniers messages de log écrits par l'application.
* **Environnement** — version du navigateur, système d'exploitation, taille d'écran et flags de fonctionnalités actifs.
* **Contexte utilisateur** — votre rôle, organisation et la page sur laquelle vous étiez au moment de la capture.
* **Indicateurs de performance** — temps de chargement de la page (LCP, FCP), utilisation mémoire et taille du DOM.
* **Trace IDs** — identifiants de corrélation qui relient l'instantané aux journaux backend.

## Créer un ticket de support depuis la boîte de dialogue

Vous n'avez rien à télécharger ni à attacher manuellement — la boîte de dialogue contient un formulaire **Create Support Ticket**.

1. Renseignez votre adresse e-mail, conservez ou modifiez le sujet suggéré, choisissez une priorité et ajoutez quelques notes décrivant ce que vous faisiez quand le problème s'est produit.
2. Cliquez sur **Send Report**. L'instantané JSON est joint et le ticket est créé en une seule étape.

C'est terminé — le support reçoit le ticket avec toutes les données nécessaires pour reproduire le cas.

Si vous voulez une copie locale de l'instantané, utilisez **Copy Debug Data** pour copier le JSON dans le presse-papiers, ou « Enregistrer sous » de votre navigateur pour conserver le rapport comme un fichier `.json`.

## Confidentialité et traitement des données

* Les jetons d'authentification et les en-têtes sensibles sont masqués des appels API capturés avant la construction de l'instantané.
* Rien ne quitte votre navigateur tant que vous n'appuyez pas sur **Send Report** — le raccourci ouvre simplement la boîte de dialogue.

<mark>Relisez l'instantané avant de l'envoyer si vous traitiez des documents contenant des données clients. Les identifiants de documents visibles dans les URLs apparaîtront dans le rapport.</mark>
