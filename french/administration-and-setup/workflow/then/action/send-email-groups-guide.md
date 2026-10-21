# Envoyer un e-mail à des groupes

***

Ajoutez cette carte au groupe **Alors** du Workflow Builder — les actions qui s'exécutent une fois que les conditions Quand/Et correspondent :

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-fr.png" alt="Exemple non enregistré avec les cartes Quand, Et et Alors. Renseignez tous les champs avant exécution."><figcaption><p>Exemple non enregistré avec les cartes Quand, Et et Alors. Renseignez tous les champs avant exécution.</p></figcaption></figure>

***

## 📌 Informations sur la version

**Statut :** ✅ Version unique (aucune modification majeure) **Dernière version :** v1 (active) **Remarque :** Cette carte utilise un modèle de version unique avec prise en charge multilingue via des clés de traduction.

📖 [Base de données complète des cartes](../../cards-overview/export-cards-guide.md)

***

## Objectif

Cette carte envoie automatiquement des notifications par e-mail à des groupes d'utilisateurs. Au lieu d'attribuer du travail à des personnes individuelles, vous envoyez le message à un groupe et tous les membres de ce groupe le reçoivent.

**Exemple concret :** Lorsqu'une facture de grande valeur arrive, envoyez automatiquement une notification par e-mail à tous les membres du groupe « Équipe financière » afin qu'ils sachent qu'elle doit être examinée.

***

## Quand utiliser cette carte

Utilisez cette carte lorsque vous devez :

* Avertir plusieurs personnes à la fois
* Envoyer des alertes aux groupes d'équipe
* Diffusez des mises à jour aux départements
* Informer les groupes des changements de statut des documents
* Envoyer des rappels aux membres du groupe

**Scénarios courants :**

* Informer l'équipe d'approvisionnement des nouveaux fournisseurs
* Alerter l'équipe financière en cas de factures de grande valeur
* Informer l'équipe de l'entrepôt des expéditions
* Modifications du statut du document de diffusion

***

## Comment ça marche

1. **Condition Check** : le workflow vérifie les conditions "Quand" et "Et"
2. **Préparer l'e-mail** : Le système prépare l'e-mail à l'aide d'un modèle
3. **Obtenir les membres du groupe** : le système trouve tous les membres du groupe spécifié
4. **Envoyer** : L'e-mail est envoyé à chaque membre du groupe
5. **Log** : L'envoi d'email est enregistré

***

## Paramètres expliqués

### Modèle d'e-mail

Le message électronique à envoyer

**Options :**

* Choisissez parmi les modèles existants
* Chaque modèle a un sujet, un corps et une mise en forme prédéfinis
* Les modèles peuvent inclure des espaces réservés tels que {document\_number}, {supplier\_name}

**Exemple de modèle :**

```
Subject: Document {document_number} requires review

Body:
Dear Team,

A new invoice has arrived and requires review:
- Document: {document_number}
- Supplier: {supplier_name}
- Amount: {amount} {currency}
- Date: {date}

Please login to DocBits to review.

Best regards,
DocBits Automation
```

### Groupe

Le groupe d'utilisateurs à qui envoyer l'e-mail

**Exemples de groupes :**

* Équipe Finances
* Équipe d'approvisionnement
* Équipe d'entrepôt
* Comité d'approbation
* Groupe de gestion

***

## Étapes de configuration

### Étape 1 : Choisissez un modèle d'e-mail

1. Cliquez sur "Sélectionner un modèle d'e-mail"
2. Choisir un modèle dans la liste
3. Vérifier le sujet et le contenu

### Étape 2 : Sélectionner un groupe

1. Cliquez sur "Sélectionner un groupe"
2. Choisissez le groupe que vous souhaitez notifier
3. Vérifier les membres du groupe (affiche généralement le nombre)

### Étape 3 : Définir les conditions

1. Ajouter une condition : "Quand \[condition] est vraie"
2. Exemple : « Lorsque le montant de la facture est supérieur à 5 000 € »

### Étape 4 : Tester

1. Test avec un exemple de document
2. Vérifier les envois d'e-mails au groupe
3. Vérifier le rendu du modèle

***

## Exemples de modèles d'e-mails

### Modèle 1 : Alerte de facture de grande valeur

```
Subject: High-Value Invoice Alert - {document_number}

Body:
Team,

An invoice exceeding €10,000 has been received:

Document Number: {document_number}
Supplier: {supplier_name}
Amount: {amount} EUR
Received Date: {date}
Status: {status}

This requires immediate review and approval.

---
Sent automatically by DocBits
```

### Modèle 2 : Changement de statut du fournisseur

```
Subject: Supplier Status Update - {supplier_name}

Body:
Procurement Team,

The following supplier's status has been updated:

Supplier: {supplier_name}
Supplier Code: {supplier_code}
New Status: {status}
Effective Date: {date}

Please update your systems accordingly.

---
Sent automatically by DocBits
```

### Modèle 3 : Document prêt à être exporté

```
Subject: Document Approved for Export - {document_number}

Body:
Export Team,

The following document has been approved and is ready for export:

Document Number: {document_number}
Invoice Number: {invoice_number}
Supplier: {supplier_name}

Please proceed with export to {destination_system}.

---
Sent automatically by DocBits
```

***

## Cas d'utilisation courants

### Cas d'utilisation 1 : alertes de contrôle qualité

**Déclencheur :** Lorsqu'un écart est constaté entre la facture et le bon de commande

**Groupe de messagerie :** Équipe qualité

**Contenu :**

```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### Cas d'utilisation 2 : notifications d'approbation

**Déclencheur :** Lorsque le document atteint un certain statut

**Groupe de messagerie :** Comité d'approbation

**Contenu :**

```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### Cas d'utilisation 3 : notifications d'exception

**Déclencheur :** Lorsque les conditions ne sont pas remplies

**Groupe de messagerie :** Gestionnaires

**Contenu :**

```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### Cas d'utilisation 4 : mises à jour de statut

**Déclencheur :** Lorsque le statut du document change

**Groupe de messagerie :** Équipe responsable de la prochaine étape

**Contenu :**

```
Document {number} status changed to: {status}
Assigned to: {assigned_user}
Next steps: {next_steps}
```

***

## Dépannage

### "E-mail non reçu"

**Causes possibles :**

* [ ] Les utilisateurs du groupe n'ont pas d'adresse e-mail
* [ ] E-mail bloqué par le filtre anti-spam
* [ ] L'adresse e-mail est incorrecte dans le groupe
* [ ] Le groupe n'a aucun membre

**Solutions :**

1. Vérifiez que tous les membres du groupe ont une adresse e-mail
2. Vérifiez le dossier spam/indésirable
3. Vérifier que l'appartenance au groupe est correcte
4. Ajouter des utilisateurs au groupe s'ils sont manquants
5. Vérifiez auprès du service informatique que le service de messagerie fonctionne

### "Le modèle ne s'affiche pas correctement"

**Cause :** Variables d'espace réservé introuvables

**Solution :**

* [ ] Vérifiez que les noms de champs correspondent exactement
* [ ] Vérifiez si le champ a une valeur dans le document
* [ ] Utilisez le format d'espace réservé correct : {field\_name}
* [ ] Testez avec un exemple de document contenant tous les champs

### "Certaines personnes reçoivent des e-mails, d'autres non"

**Cause :** Adhésion incomplète à un groupe ou e-mails invalides

**Solutions :**

* [ ] Vérifiez que tous les membres ont une adresse e-mail valide
* [ ] Vérifiez si certains utilisateurs se sont désabonnés
* [ ] Vérifier que l'appartenance au groupe est actuelle
* [ ] Contactez le service informatique pour valider les adresses e-mail

### "Vous souhaitez ajouter/supprimer des personnes du groupe"

**Solution :**

* Contactez votre administrateur
* Les groupes sont gérés dans les paramètres système
* Ne peut pas être modifié à partir de cette carte
* Demander des modifications à l'appartenance à un groupe dans l'informatique

***

## Personnalisation du modèle d'e-mail

### Espaces réservés disponibles

```
{document_number} - Document ID
{invoice_number} - Invoice ID
{supplier_name} - Supplier name
{supplier_code} - Supplier code
{amount} - Invoice amount
{currency} - Currency (EUR, USD, etc.)
{date} - Document date
{status} - Current status
{assigned_user} - Assigned person
{assigned_group} - Assigned group
{next_steps} - What needs to happen next
{reason} - Reason for exception/alert
{comment} - Comments or notes
```

### Création d'espaces réservés personnalisés

Si vous avez besoin de données supplémentaires dans les e-mails :

1. Contactez votre administrateur
2. Demander un nouvel espace réservé
3. Ajouter le champ nécessaire au document
4. Mettre à jour le modèle d'e-mail

***

## Meilleures pratiques

✅ **Faire :**

* Gardez le contenu des e-mails bref et clair
* Incluez des éléments d'action (que doivent faire les destinataires ?)
* Inclure un lien ou des instructions pour accéder au document
* Modèle de test avec des exemples de données
* Envoyer au bon groupe (ne pas trop notifier)
* Utilisez des modèles pour plus de cohérence

❌ **À ne pas faire :**

* Envoyer trop d’e-mails (fatigue des notifications)
* Inclure des données sensibles dans les e-mails
* Envoyer à des groupes qui n'ont pas besoin d'informations
* Utilisez des lignes d'objet peu claires
* Oubliez d'inclure comment agir
* Envoyez des e-mails à des individus (utilisez plutôt le groupe)

***

## Notes de performances

* L'envoi de chaque e-mail prend \~1 seconde
* Les grands groupes peuvent prendre du temps (100 personnes = \~100 secondes)
* Ne créez pas de boucles qui envoient des milliers d'e-mails
* Surveiller la capacité du service de messagerie
* Envisagez le regroupement si de nombreux documents

***

## Cartes associées

* **ACTION\_SEND\_EMAIL** - Envoyer à une personne individuelle
* **ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP** - Attribuer une tâche au lieu de simplement notifier
* **ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL** - Créer une tâche et notifier
* **STAUS\_CHANGE** - Changer le statut et notifier

***

## Exemple de flux de travail typique

```
Document Arrives
    ↓
Check Condition: "Is amount > €10,000?"
    ↓
YES: Send Email to Finance Team
     "High value invoice alert"
    ↓
Send Email to Procurement Team
     "New invoice from supplier"
    ↓
Workflow Continues
```

***

## FAQ

**Q : Puis-je envoyer à plusieurs groupes ?** A : Créer des cartes distinctes pour chaque groupe

**Q : Que se passe-t-il si l'e-mail de quelqu'un rebondit ? ** A : L'e-mail est enregistré comme ayant échoué, le service informatique peut résoudre le problème.

**Q : Puis-je modifier le modèle d'e-mail ?** A : Contactez votre administrateur pour modifier les modèles

**Q : Puis-je envoyer en fonction de conditions ?** A : Oui ! Utilisez les conditions « Où » et « Et » pour contrôler le moment où les e-mails sont envoyés

**Q : Comment savoir si un e-mail a été reçu ?** A : Vérifiez les journaux de courrier électronique dans DocBits pour connaître l'état d'envoi
