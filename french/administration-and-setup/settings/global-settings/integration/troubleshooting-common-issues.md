# Dépannage des problèmes courants

Voici des étapes de dépannage pour les problèmes courants lors de l'intégration de DocBits avec un fournisseur de services d'identité (IdP) ou d'autres services :

* **Vérifier la configuration :** Assurez-vous que les paramètres d'intégration dans DocBits sont correctement configurés et correspondent aux exigences de votre fournisseur de services d'identité. Vérifiez en particulier l'URL SSO, l'Entity ID et les certificats.
* **Surveiller les journaux :** Surveillez les journaux dans DocBits et du côté du fournisseur de services d'identité afin d'identifier d'éventuels messages d'erreur ou avertissements. Ces journaux peuvent indiquer où se situe le problème.
* **Vérifier les connexions réseau :** Assurez-vous qu'aucun problème réseau ne perturbe la communication entre DocBits et votre fournisseur de services d'identité. Contrôlez les paramètres du pare-feu, les configurations DNS et les règles d'accès réseau.
* **Tester les processus SSO :** Effectuez des connexions de test via l'authentification unique (SSO) pour vous assurer que les utilisateurs sont correctement authentifiés et redirigés vers DocBits. Notez tout message d'erreur ou problème de redirection.
* **Vérifier les autorisations :** Assurez-vous que les utilisateurs de DocBits disposent des autorisations requises pour accéder aux fonctionnalités ou ressources concernées. Contrôlez l'affectation des groupes et des rôles.
* **Mettre à jour les certificats :** Assurez-vous que les certificats SAML et les métadonnées sont à jour des deux côtés. Si un certificat a expiré, vous devez le mettre à jour et tester de nouveau l'intégration.
* **Contacter le support :** Si vous ne parvenez pas à identifier la cause du problème, contactez le support DocBits ou votre fournisseur de services d'identité. Ils peuvent vous aider à résoudre le problème et vous fournir des conseils spécifiques à votre configuration.

En suivant ces étapes de dépannage, vous pouvez rapidement identifier et résoudre les problèmes les plus courants lors de l'intégration entre DocBits et votre fournisseur de services d'identité.
