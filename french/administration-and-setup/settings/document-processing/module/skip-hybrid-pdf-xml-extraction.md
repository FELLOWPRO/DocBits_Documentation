# Ignorer l'extraction XML des PDF hybrides

### Aperçu

Le paramètre **Ignorer l'extraction XML des PDF hybrides** (Skip Hybrid PDF XML Extraction) contrôle la manière dont DocBits traite les **PDF hybrides** — des factures PDF contenant une facture électronique structurée intégrée (ZUGFeRD / Factur-X). Il détermine si le **XML structuré contenu dans le PDF** est le document directeur pour le traitement automatique, ou si le **PDF lui-même** est traité par OCR en tant que document principal.

Ce paramètre est particulièrement pertinent pour les **clients américains**. Contrairement à l'UE/l'Allemagne, les États-Unis n'ont pas d'obligation générale de facturation électronique B2B ; les organisations américaines souhaitent donc généralement que le PDF soit traité comme la facture principale et lisible par l'humain, même lorsqu'un partenaire envoie un fichier ZUGFeRD/Factur-X avec du XML intégré.

### Que fait ce paramètre ?

Un fichier ZUGFeRD/Factur-X est un PDF unique qui contient également une facture XML lisible par machine. Par défaut, DocBits détecte ce XML intégré et l'utilise comme source directrice pour l'extraction (chaîne électronique structurée).

* **Désactivé (par défaut)** — DocBits détecte le XML de facture électronique intégré et traite le document via la **chaîne électronique structurée**. Le XML est la facture directrice. C'est le comportement juridiquement correct pour l'UE/l'Allemagne, où la facture électronique structurée est la facture pertinente et le PDF n'est qu'une visualisation / copie de lecture.
* **Activé** — DocBits **ignore le XML intégré** et achemine le document vers le **processeur PDF (OCR)**. Le PDF devient le document de traitement principal. C'est le choix habituel pour les **organisations américaines** qui souhaitent un traitement centré sur le PDF.

{% hint style="info" %}
Ce paramètre n'affecte que les **PDF hybrides** (ZUGFeRD / Factur-X = un `.pdf` avec XML intégré). Un fichier XRechnung/EDI pur téléversé en `.xml` est toujours traité via la chaîne électronique structurée — il n'y a pas de PDF susceptible de devenir le document principal.
{% endhint %}

### Audit et conformité — l'original est toujours conservé

Activer ce paramètre **ne supprime pas** la facture électronique. L'artefact original est toujours conservé :

* Le **PDF** ZUGFeRD/Factur-X d'origine — **y compris son XML intégré — reste stocké** et téléchargeable. Rien n'est supprimé de la copie stockée du document.
* Le traitement ne modifie que **le contenu qui pilote l'extraction** (PDF/OCR ou XML intégré), et non ce qui est archivé.

Une organisation américaine peut ainsi traiter le PDF comme document principal tandis que la facture électronique structurée reste disponible pour l'audit.

{% hint style="warning" %}
Pour les organisations de l'UE/d'Allemagne, laissez ce paramètre **désactivé**. Selon les règles de facturation électronique de 2025, une facture électronique structurée (ZUGFeRD/Factur-X, XRechnung) est la facture juridiquement pertinente ; un simple PDF n'est qu'une copie de lecture. Traiter le PDF comme document principal au lieu des données structurées n'est pas approprié lorsqu'une facture électronique valide est présente.
{% endhint %}

### Utilisation

1. **Ouvrir le paramètre** :
   * Allez dans **Paramètres**.
   * Sélectionnez **Traitement des documents**.
   * Sélectionnez **Module**.
   * Ouvrez la section **Type de document**.
   * Repérez **Ignorer l'extraction XML des PDF hybrides** et activez le commutateur.
2. **Choisir le mode** :
   * **Organisations américaines / orientées PDF** → activez le commutateur pour que les PDF ZUGFeRD/Factur-X soient traités par OCR en tant que document principal.
   * **Organisations UE/Allemagne** → laissez le commutateur désactivé pour que la facture électronique structurée reste le document directeur.
3. **Vérifier** :
   * Téléversez un PDF ZUGFeRD/Factur-X et vérifiez le résultat du traitement — commutateur activé, il est traité comme un PDF classique (OCR) ; désactivé, les données de la facture électronique intégrée sont extraites.

### Quand utiliser cette fonction

* **Clients américains / sans obligation de facture électronique** : activez-la pour que le PDF habituel soit le document de traitement principal tandis que la facture électronique intégrée reste archivée.
* **Flux mixtes/orientés PDF** : activez-la lorsque les processus en aval, la validation ou la révision reposent sur la mise en page du PDF plutôt que sur le XML.
* **Conformité UE/Allemagne** : laissez-la désactivée pour que les données structurées de la facture électronique pilotent le traitement, comme l'exige la réglementation.
