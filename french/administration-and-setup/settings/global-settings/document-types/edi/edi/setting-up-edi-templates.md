---
hidden: true
---

# Configuration des Modèles EDI

## Voici des instructions étape par étape pour configurer des modèles EDI :

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_cert_metadata.png" alt="Docbits Sso Cert Metadata"><figcaption></figcaption></figure>

**Définir le descripteur de structure :**

* Identifiez le type de message EDI avec lequel vous travaillez, par exemple ANSI X12, EDIFACT ou un format personnalisé.
* Déterminez les segments, éléments et sous-éléments au sein de la structure EDI.
* Créez un descripteur de structure qui reflète précisément la hiérarchie et l'organisation du message EDI. Cela peut être fait en utilisant une syntaxe spéciale telle que XML ou JSON.

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_access_settings.png" alt="Docbits Sso Access Settings" width="273"><figcaption></figcaption></figure>

**Configurer les transformations :**

* Utilisez un outil ou un logiciel approprié prenant en charge les transformations EDI, tel qu'un traducteur EDI.
* Définissez les règles de conversion du message EDI au format interne de votre système et vice versa.
* Configurez les transformations pour interpréter et traiter les segments, éléments et sous-éléments selon les exigences de votre système. Testez soigneusement les transformations pour vous assurer que les données sont correctement interprétées et formatées.

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_idp_config.png" alt="Docbits Sso Idp Config" width="268"><figcaption></figcaption></figure>

**Configurer les chemins d'extraction pour une extraction et un formatage optimaux des données :**

* Identifiez les champs de données à extraire et à transférer vers votre système interne.
* Définissez des chemins d'extraction ou des règles pour extraire les champs de données pertinents des messages EDI.
* Tenez compte des différentes variations et formats pouvant survenir dans les messages EDI entrants et assurez-vous que les chemins d'extraction sont suffisamment flexibles pour les prendre en compte.
* Validez les résultats de l'extraction pour vous assurer que les bons champs de données sont extraits et correctement formatés.

<figure><img src="../../../../../../.gitbook/assets/docbits_edi_validate_extraction.png" alt="Docbits Edi Validate Extraction" width="92"><figcaption></figcaption></figure>

En définissant soigneusement le descripteur de structure, en configurant les transformations et en configurant les chemins d'extraction, vous pouvez vous assurer que l'extraction et le formatage des données sont effectués de manière optimale dans vos modèles EDI. Cela contribuera à améliorer l'efficacité et la précision de vos communications commerciales électroniques.
