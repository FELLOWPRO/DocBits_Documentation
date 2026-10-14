# Company Information

<figure><img src="../../../../.gitbook/assets/company_information.png" alt="Formulaire Company Information dans l'organisation de test DocBits Sandbox en anglais"><figcaption><p>Company Information : modifiez le nom de l'organisation, l'adresse, les identifiants légaux et les coordonnées, puis sélectionnez Save.</p></figcaption></figure>

La page Company Information vous permet de gérer le profil de votre entreprise, vos préférences et les détails de votre abonnement. Elle est organisée en plusieurs sections :

## Company Information

Cette section contient les données de base de votre entreprise, regroupées en quatre zones :

### Company Identity

* **Name** *(obligatoire)* : la dénomination légale de votre entreprise.

### Address

* **Street + Number** : l'adresse postale de votre entreprise.
* **Postal Code** : le code postal.
* **City** : le nom de la ville.
* **Country** : sélectionnez votre pays dans la liste déroulante.

### Legal Information

* **Company ID** : un identifiant unique de votre entreprise, utilisé pour les intégrations et comme référence interne.
* **Tax ID** : votre numéro d'identification fiscale pour les rapports financiers.
* **Commercial Register ID** : votre numéro de registre du commerce pour la documentation légale.

### Contact

* **Official Company Phone Number** : le numéro de téléphone principal de votre entreprise.
* **E-Mail** : l'adresse e-mail principale utilisée pour les communications officielles.

Après avoir saisi ou mis à jour des champs, cliquez sur **Save** pour appliquer vos modifications. Les icônes **?** à côté des identifiants légaux affichent des indications supplémentaires sur le champ. Sélectionnez le titre de la section pour développer ou réduire le formulaire.

## E-mail domains

Les administrateurs de l'organisation peuvent ouvrir **Settings → Company Information → E-mail domains** pour gérer les domaines utilisés pour l'affectation automatique à l'organisation. Lorsqu'une personne se connecte avec Microsoft ou Google et n'est pas encore membre d'une organisation, DocBits peut l'affecter à cette organisation si son adresse e-mail utilise l'un des domaines listés. Un domaine ne peut appartenir qu'à une seule organisation.

<figure><img src="../../../../.gitbook/assets/company_email_domains_en.png" alt="Section E-mail domains développée avec une liste de domaines vide, un champ de saisie et le bouton Add domain"><figcaption><p>La section E-mail domains en anglais avant l'ajout d'un domaine. Saisissez un domaine d'entreprise, puis sélectionnez Add domain.</p></figcaption></figure>

Saisissez uniquement le domaine, par exemple `example.com`, dans le champ, puis sélectionnez **Add domain** ou appuyez sur Entrée. Le premier domaine devient le domaine principal. Si plusieurs domaines sont listés, utilisez **Make primary** sur une autre ligne pour modifier le domaine principal, ou l'icône de corbeille pour supprimer un domaine. Les erreurs, telles qu'un domaine non valide, un fournisseur de messagerie personnelle ou un domaine déjà affecté ailleurs, apparaissent sous le champ de saisie. **No domains assigned yet** signifie que cette organisation n'a aucune règle de domaine.

Avant d'ajouter un domaine, vérifiez quelle organisation doit recevoir les nouvelles connexions. Pour gérer les appartenances existantes, poursuivez avec [Users](../groups-users-and-permissions/users/README.md).

## Company Preferences

Configurez les paramètres par défaut applicables à toute l'entreprise :

* **Date Pattern** : choisissez le format d'affichage des dates dans DocBits (p. ex. `%m/%d/%Y`, `%d.%m.%Y`).
* **Amount Formatting** : sélectionnez le format numérique des montants (p. ex. Deutsch pour `1.000,00`, English pour `1,000.00`).
* **New Version Info Dialog** : active ou désactive l'affichage d'une notification aux utilisateurs lors de la publication d'une nouvelle version de DocBits.

Cliquez sur **Save** après avoir effectué des modifications.

## App-Color

Personnalisez la couleur principale de l'interface DocBits. C'est utile pour distinguer visuellement différents environnements (p. ex. dev et production).

* **Color** : saisissez un code couleur hexadécimal (p. ex. `#2388AE`) ou utilisez le sélecteur de couleur.
* Cliquez sur **Save** pour appliquer, ou sur **Reset** pour rétablir la couleur par défaut.

## Subscription Plan

Consultez vos plans d'abonnement actifs et leurs détails :

* **Plan Name** : le nom de chaque plan actif (p. ex. DocBits, DocFlow Users, DocSearch).
* **Days Left** : le nombre de jours restants avant l'expiration du plan.
* **Start Date / End Date** : la période d'abonnement.
* **Users Count** : le nombre total d'utilisateurs de votre organisation.
* **Sub Organizations Count** : le nombre de sous-organisations configurées.
* **Suppliers Count** : le nombre de fournisseurs enregistrés.

## Subscription Usage

Suivez votre consommation mensuelle de jetons et de workflows :

| Colonne | Description |
|--------|-------------|
| **Type** | Le type d'utilisation (Document ou Workflow). |
| **From / To** | Les dates de la période de facturation. |
| **Tokens Used** | Le nombre de jetons consommés pendant la période en cours. |
| **Remaining Tokens** | Les jetons encore disponibles pendant la période en cours. |

Utilisez le bouton **Select** pour filtrer par plages de dates spécifiques.
