# Paramètres OCR

{% embed url="https://youtu.be/5XqEP-5fq6M" %}
DocBits OCR & E-Text expliqués : paramètres, qualité et extraction d'en-tête
{% endembed %}

## Vue d’ensemble

Dans les paramètres **OCR (Reconnaissance optique de caractères)**, vous pouvez configurer la façon dont OCR est appliqué pendant le traitement du document. Cela inclut la spécification de la qualité minimale requise, le choix d'utiliser ou non du texte intégré (texte électronique), la sélection de la version OCR, etc. Cette page fournit une explication détaillée de tous les paramètres disponibles.

## Accéder aux paramètres OCR

Pour accéder aux paramètres OCR :

*   Accédez à : **Paramètres** → **Traitement des documents** → **OCR Paramètres**

    <figure><img src="../../../.gitbook/assets/settings_ocr.png" alt="Menu des paramètres de DocBits avec Document Processing ouvert et OCR Settings sélectionné parmi Import, Rule Management et Export"><figcaption></figcaption></figure>

## Qualité OCR

Dans cette section, vous pouvez définir la qualité minimale du document requise pour le traitement OCR en ajustant le curseur de qualité. Déplacez le curseur vers la gauche ou la droite pour diminuer ou augmenter le seuil de qualité, respectivement.

Si un document ne répond pas au niveau de qualité défini, DocBits propose trois options pour le traiter :

* **Run Anyway**\
  Le document sera traité quelle que soit sa qualité.
* **Exécuter à nouveau après confirmation**\
  **DocBits** fera une pause et vous demandera de confirmer si vous souhaitez poursuivre le traitement.
* **Throw Error**\
  Le traitement du document s'arrêtera complètement et un message d'erreur s'affichera, indiquant que le document n'a pas atteint le seuil de qualité requis.

<figure><img src="../../../.gitbook/assets/ocr_settings_1.png" alt="Page de paramètres OCR Quality avec le curseur de qualité et Run again after confirmation sélectionné en dessous"><figcaption></figcaption></figure>

## Paramètres OCR généraux

* **Use E-Text if Available**\
  Lorsqu'il est activé, **DocBits** utilisera le texte électronique intégré (par exemple, à partir de PDF) au lieu d'exécuter OCR. Cela améliore à la fois la vitesse et la précision, car le texte est extrait directement sans nécessiter de traitement OCR.
* **Use DESKEW if Available**\
  Cette option corrige automatiquement l'alignement des documents numérisés. Le redressement des images inclinées contribue à améliorer la précision de l’OCR.
*   **AI OCR Version**\
    Vous permet de sélectionner une version spécifique du AI-basé OCR moteur.\
    Cela peut être utile si :

    * Vous n'obtenez pas les résultats souhaités avec la version actuellement sélectionnée.
    * Vous résolvez des problèmes liés aux performances ou à la précision de l’OCR.

    <figure><img src="../../../.gitbook/assets/ocr_settings_2.png" alt="Page OCR Settings avec le menu déroulant AI OCR Version ouvert affichant les versions 1.2, 2.0 et 2.1"><figcaption></figcaption></figure>

## Paramètres OCR pour les tableaux

* **Use AI Data for Tables if Available**\
  Lorsqu'il est activé, DocBits utilisera les données OCR pour les tableaux au lieu du texte électronique intégré (texte électronique) — même si le paramètre **Utiliser le texte électronique si disponible** est activé.

## Paramètres OCR pour les champs d’en-tête

* **Use Rules Extraction**\
  DocBits appliquera vos règles d'extraction prédéfinies pour identifier les champs d'en-tête.
* **Use AI Extraction**\
  DocBits utilisera AI pour détecter et extraire automatiquement les champs d'en-tête.

**Execution Order:**\
Si les deux options sont activées, **DocBits** effectuera l'extraction dans l'ordre suivant :\
**Rules Extraction → AI Extraction**\
\
<mark style="color:red;">**Remarque**</mark> : Pour de meilleurs résultats et un comportement cohérent, activez les deux options. Cela permet à **DocBits** d'utiliser à la fois des méthodes basées sur des règles et des méthodes basées sur AI en combinaison lors de l'extraction d'en-tête.
