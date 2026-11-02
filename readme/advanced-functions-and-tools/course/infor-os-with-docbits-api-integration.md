# Infor OS avec l'intégration de l'API DocBits



{% embed url="https://youtu.be/0aeSDWi9cV8" %}



## Importer l'API DocBits dans Infor OS — utilisez la spécification Swagger 2.0

Lorsque vous connectez Infor OS à l'API DocBits (par exemple lors de la création d'une application personnalisée ou d'un flux d'API dans Infor OS), Infor importe la spécification de l'API de DocBits. **Pour Infor OS, utilisez la spécification Swagger 2.0 — et non celle d'OpenAPI 3.0.**

DocBits publie sa spécification d'API dans deux dialectes :

| Spécification | Chemin | À utiliser pour |
| --- | --- | --- |
| OpenAPI 3.0 / 3.1 | `/openapi.json` | Clients d'API standard, génération de SDK, documentation d'API habituelle |
| **Swagger 2.0** | `/openapi-swagger2.json` | **Infor OS** (et tout autre outil qui utilise un ancien swagger-ui) |

{% hint style="warning" %}
**Pourquoi Swagger 2.0 pour Infor ?** Infor OS utilise une ancienne version de swagger-ui qui ne peut pas construire une requête d'envoi de fichier à partir de la représentation moderne d'OpenAPI 3.0 (un `requestBody` avec `format: binary`). Il envoie le fichier **sans délimiteur multipart (boundary)**, et l'API le rejette avec :

`400 — Missing boundary in multipart`

La spécification Swagger 2.0 déclare les envois de fichiers sous la forme `in: formData, type: file`, que le swagger-ui d'Infor construit correctement (avec un délimiteur). Mêmes points de terminaison, mêmes données — seul le dialecte de la spécification diffère.
{% endhint %}

### Comment obtenir l'URL Swagger 2.0

1. Ouvrez la documentation de l'API DocBits dans votre navigateur (par ex. `https://api.docbits.com/docs`).
2. En haut de la page, ouvrez la **liste déroulante des spécifications** et sélectionnez **Swagger 2.0 (Infor OS)**.
3. Copiez l'URL affichée pour cette spécification — c'est l'URL de base de votre API DocBits suivie de `/openapi-swagger2.json`.

Utilisez cette URL partout où Infor OS demande la spécification de l'API / Swagger. La copier depuis la liste déroulante garantit l'hôte correct pour votre région et votre environnement.

{% hint style="info" %}
Tout le reste de l'intégration — authentification (clé d'API / jeton), points de terminaison et charges utiles — reste inchangé. Seul le dialecte de la spécification que vous importez dans Infor diffère.
{% endhint %}
