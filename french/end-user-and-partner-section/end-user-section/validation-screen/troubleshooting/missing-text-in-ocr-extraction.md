# Texte manquant dans l'extraction OCR

## **Problème**

Dans certains cas, du texte peut sembler manquer dans la **Vue OCR**, ce qui empêche son extraction via la fonctionnalité d'extraction.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_5-fr.png" alt="Contrôle des champs extraits sur une facture fictive."><figcaption><p>Contrôle des champs extraits sur une facture fictive.</p></figcaption></figure>

Pour vérifier cela, cliquez sur le bouton **Vue OCR** dans la barre d'outils à droite. Si le texte n'apparaît pas là, cela signifie qu'il n'est pas disponible pour l'extraction.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_6-fr.png" alt="Vue OCR du texte reconnu sur la facture fictive."><figcaption><p>Vue OCR du texte reconnu sur la facture fictive.</p></figcaption></figure>

## **Cause**

La cause la plus probable est que le texte que vous essayez d'extraire fait partie d'une image (par exemple, un logo ou une section numérisée) dans le document.\
Lorsque la fonctionnalité E-Text est activée, le texte qui apparaît sur les images ou les logos n'est pas inclus dans la couche de texte extraite. En conséquence, ce texte ne peut pas être accessible ou extrait par la logique d'extraction standard.

## **Solution**

Pour résoudre ce problème, désactivez la fonctionnalité E-Text—soit pour le [fournisseur spécifique](missing-text-in-ocr-extraction.md#desactiver-e-text-pour-un-fournisseur-specifique), soit pour [l'ensemble de l'organisation](missing-text-in-ocr-extraction.md#desactiver-e-text-pour-lensemble-de-lorganisation). Une fois E-Text désactivé, DocBits s'appuiera uniquement sur l'OCR, qui est capable d'extraire du texte à partir d'images et de logos dans le document.

### **Désactiver E-Text pour un Fournisseur Spécifique**

1. Ouvrez un document du fournisseur spécifique dans la **Validation de Champ**.
2.  Cliquez sur le menu à trois points dans la barre d'outils à droite.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_2-fr.png" alt="Menu d’options supplémentaires dans la validation des champs."><figcaption><p>Menu d’options supplémentaires dans la validation des champs.</p></figcaption></figure>

3.  Décochez **Utiliser l'E-Texte s'il est disponible**.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_3-fr.png" alt="Option d’utilisation du texte électronique dans le menu du document."><figcaption><p>Option d’utilisation du texte électronique dans le menu du document.</p></figcaption></figure>

4.  Cliquez sur **Confirmer** pour redémarrer le traitement du document.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_4-fr.png" alt="Confirmation avant modification de l’utilisation du texte électronique."><figcaption><p>Confirmation avant modification de l’utilisation du texte électronique.</p></figcaption></figure>

### Désactiver E-Text pour l'Ensemble de l'Organisation

1.  Allez dans **Paramètres → Traitement des documents → Paramètres de l'OCR**.

<figure><img src="../../../../.gitbook/assets/s150-settings_ocr-fr.png" alt="Paramètres OCR de l’interface française."><figcaption><p>Paramètres OCR de l’interface française.</p></figcaption></figure>

2.  Sous **Paramètres généraux de l'OCR**, décochez l'option **Utiliser l'E-Texte s'il est disponible**.

<figure><img src="../../../../.gitbook/assets/s150-troubleshooting_ocr_1-fr.png" alt="Paramètres OCR généraux avec l’option d’utilisation du texte électronique."><figcaption><p>Paramètres OCR généraux avec l’option d’utilisation du texte électronique.</p></figcaption></figure>

Les images utilisent une facture fictive avec du texte OCR disponible. Elles illustrent des vérifications de l’interface, pas un incident reproduit de texte manquant.
