---
description: Créez des documents dans DocBits avec un scanner local et Doc Scan.
---

# Doc Scan

## Télécharger et installer le logiciel du scanner

Dans le tableau de bord DocBits, cliquez sur Scan Document.

<figure><img src="../../../../.gitbook/assets/image (203).png" alt="Bouton Scan Document dans le tableau de bord DocBits"><figcaption></figcaption></figure>

Si le logiciel local du scanner n’est pas installé, DocBits affiche une invitation à le télécharger. Choisissez le téléchargement correspondant à votre système d’exploitation.

<figure><img src="../../../../.gitbook/assets/image (204).png" alt="Invitation à télécharger le logiciel local du scanner"><figcaption></figcaption></figure>

Ouvrez le fichier d’installation téléchargé. Le programme d’installation illustré est destiné à macOS ; suivez les instructions de votre système d’exploitation.

<figure><img src="../../../../.gitbook/assets/image (205).png" alt="Démarrage du programme d’installation du logiciel du scanner"><figcaption></figcaption></figure>

Dans le programme d’installation illustré, cliquez sur Continue, acceptez la licence du logiciel avec Agree et poursuivez. Vérifiez la destination et l’espace requis, puis cliquez sur Install. Les 33,6 Mo affichés correspondent à cette version du programme d’installation ; l’espace requis peut varier selon la version.

Une fois l’installation terminée, fermez le programme d’installation.

<figure><img src="../../../../.gitbook/assets/image (206).png" alt="Installation du logiciel du scanner terminée"><figcaption></figcaption></figure>

Ouvrez https://local.polydocs.io:12500/ dans votre navigateur pour tester le service local. Si le navigateur ne parvient pas à le joindre et que vous utilisez une FRITZ!Box, vérifiez les paramètres de protection contre le DNS rebinding décrits ci-dessous.

<figure><img src="../../../../.gitbook/assets/image (207).png" alt="Erreur du navigateur lors du test du service local du scanner"><figcaption></figcaption></figure>

Lorsque la page du service local apparaît, cliquez sur DocBits pour ouvrir DocBits.

<figure><img src="../../../../.gitbook/assets/image (208).png" alt="Page du service local du scanner après une connexion réussie"><figcaption></figcaption></figure>

Connectez-vous sur la page de connexion DocBits pour accéder à votre tableau de bord.

<figure><img src="../../../../.gitbook/assets/image (209).png" alt="Page de connexion DocBits ouverte depuis le service local"><figcaption></figcaption></figure>

Activez Doc Scan dans les paramètres, sous Modules.

<figure><img src="../../../../.gitbook/assets/image (210).png" alt="Paramètre du module Doc Scan"><figcaption></figcaption></figure>

## Paramètres réseau de la FRITZ!Box

Si https://local.polydocs.io:12500/ est inaccessible parce qu’une FRITZ!Box bloque les réponses DNS contenant des adresses privées, le navigateur peut signaler un délai DNS dépassé. La FRITZ!Box utilise cette protection contre le DNS rebinding. Ajoutez une exception de nom d’hôte pour ce service local :

1. Dans l’interface allemande de la FRITZ!Box, ouvrez Heimnetz (réseau domestique), puis Netzwerk (réseau).
2. Ouvrez l’onglet Netzwerkeinstellungen (paramètres réseau).
3. Sous DNS-Rebind-Schutz (protection contre le DNS rebinding), ajoutez local.polydocs.io aux exceptions de noms d’hôtes.
4. Cliquez sur Übernehmen (appliquer) et testez à nouveau le service local.

## Désinstaller Doc2Scan Service Manager

Pour désinstaller Doc2Scan Manager sous macOS, exécutez :

```bash
sudo bash /Library/doc2scan/uninstall.sh
```

## Compatibilité des scanners

sane-airscan est un backend SANE pour Apple AirScan/eSCL et Microsoft WSD (WS-Scan, Web Services for Devices). Il s’agit de protocoles de numérisation en réseau.

Consultez les [informations de compatibilité maintenues par sane-airscan](https://github.com/alexpevzner/sane-airscan) pour connaître les appareils et protocoles dont la prise en charge a été signalée. La disponibilité d’un protocole ou un retour concernant sane-airscan ne garantit pas que toutes les fonctions de l’appareil fonctionnent dans Doc Scan. Testez votre scanner avec le parcours Doc Scan dont vous avez besoin.
