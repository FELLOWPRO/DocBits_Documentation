# Prérequis de l'installation locale de Prefect

#### Prérequis

Assurez-vous que les éléments suivants sont installés sur le système hôte :

* **Docker Engine**
* **Docker Compose v2**&#x20;

#### Compatibilité du système d'exploitation hôte

* **Linux** : recommandé et entièrement pris en charge.
* **Windows** : fonctionne avec Docker Desktop (WSL2). Les montages de volumes peuvent poser des problèmes.
* **macOS** : pris en charge via Docker Desktop. Comportement similaire à Windows.

#### Configuration système requise

* **RAM** : 1 à 2 Go par conteneur. Pour plusieurs flux : 2 à 4 Go.
* **CPU** : 1 à 2 cœurs par conteneur. Pour des flux simultanés : 2 à 4 cœurs.
* **Disque** : 2 à 3 Go pour l'image et les journaux&#x20;
