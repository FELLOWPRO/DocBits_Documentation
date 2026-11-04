# Modification des Modèles d'Email

### Aperçu

La fonctionnalité des Modèles d'Email permet aux administrateurs de créer et de personnaliser des communications par email qui sont automatiquement envoyées aux fournisseurs. L'un des éléments clés utilisés dans ces modèles est le `{{magic_link}}`, qui fournit un lien dynamique adapté à chaque destinataire.

<figure><img src="../../../.gitbook/assets/docbits_email_template_magic_link.png" alt="Docbits Email Template Magic Link'Email"><figcaption></figcaption></figure>

#### Qu'est-ce que `{{magic_link}}` ?

Le `{{magic_link}}` est un espace réservé qui est remplacé dynamiquement par une URL unique lorsque l'email est envoyé. Cette URL dirige généralement le destinataire à accomplir une action, comme l'inscription, l'approbation ou l'accès à une partie spécifique du portail fournisseur.

### Modification des Modèles d'Email

<figure><img src="../../../.gitbook/assets/docbits_email_template_editor_access.png" alt="Docbits Email Template Editor Access"><figcaption></figcaption></figure>

#### Accéder à l'Éditeur de Modèle d'Email

1. **Naviguer vers les Modèles d'Email** :
   * Allez dans la section **Modèles d'Email** depuis le menu principal.
2. **Sélectionner un Modèle à Modifier** :
   * Choisissez le modèle d'email que vous souhaitez modifier en cliquant sur le nom du modèle (par exemple, "Email d'Invitation au Fournisseur").
3. **Modifier le Modèle** :
   * L'éditeur vous permet de modifier à la fois le code HTML et le design visuel de l'email.
   * Vous pouvez basculer entre l'édition visuelle et l'édition de code en utilisant les onglets fournis.

<figure><img src="../../../.gitbook/assets/docbits_email_template_visual_code_toggle.png" alt="Docbits Email Template Visual Code Toggle"><figcaption></figcaption></figure>

#### Définir `{{magic_link}}` comme un Lien

Pour définir `{{magic_link}}` comme un lien cliquable dans l'email, vous devez vous assurer qu'il est correctement formaté dans le code HTML du modèle. Suivez ces étapes :

1. **Localiser la Section de Lien dans le Code HTML** :
   * Dans l'éditeur de code, trouvez la section où vous souhaitez que le lien magique apparaisse. Cela se trouve généralement dans une balise `<a>` (ancre).
2. **Insérer l'Espace Réservé `{{magic_link}}`** :

    * Remplacez l'attribut `href` de la balise d'ancre par `{{magic_link}}`.
    * Assurez-vous que le lien est stylé de manière appropriée pour le modèle d'email. Voici un exemple :

    ```html
    <a href="{{magic_link}}" target="_blank" style="
        background-color: #B7184B;
        border-radius: 25px;
        font-family: 'Montserrat', Arial, sans-serif;
        font-size: 14px;
        font-weight: bold;
        padding: 12px 25px;
        color: #FFFFFF;
        text-decoration: none;
        display: inline-block;
        cursor: pointer;">
        Compléter l'Inscription
    </a>
    ```

### 3. Personnaliser le Texte du Lien :

• Modifiez le texte entre les balises d'ouverture \<a> et de fermeture \</a> pour refléter l'action que vous souhaitez que l'utilisateur effectue. Par exemple, “Compléter l'Inscription” ou “Accéder à Votre Compte”.

4. Enregistrer et Tester le Modèle :

• Après avoir effectué les modifications, cliquez sur le bouton Enregistrer.

• Vous pouvez utiliser le bouton Envoyer un Test pour envoyer un email test afin de vous assurer que le lien fonctionne comme prévu.

## Meilleures Pratiques pour Utiliser \{{magic\_link\}}

• Placement du Lien : Placez le \{{magic\_link\}} de manière proéminente dans l'email pour garantir qu'il est facilement accessible aux destinataires.

• Appel à l'Action Clair : Le texte à l'intérieur du lien doit être un appel à l'action clair, tel que “Compléter l'Inscription” ou “Confirmer Votre Email.”

• Style : Assurez-vous que le lien est stylé de manière cohérente avec le reste du modèle d'email et se distingue visuellement.

• Test : Envoyez toujours un email test après avoir modifié le modèle pour vérifier que le \{{magic\_link\}} se résout correctement et que le style est approprié.

## Conclusion

En définissant correctement le \{{magic\_link\}} dans vos modèles d'email, vous pouvez vous assurer que les destinataires reçoivent un email personnalisé et actionnable qui les guide vers la tâche appropriée dans votre portail fournisseur. Cela améliore l'expérience utilisateur et garantit des processus d'intégration et de communication fluides.

\

Cette documentation fournit des instructions étape par étape pour les administrateurs sur la façon de définir et d'utiliser le \{{magic\_link\}} dans les modèles d'email, garantissant que les emails sont à la fois fonctionnels et visuellement attrayants.