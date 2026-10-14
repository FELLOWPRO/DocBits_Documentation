# Send Email to Groups

Ces cartes se placent dans le groupe **Then** du Concepteur de workflow — les actions exécutées une fois les conditions When/And remplies :

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Les cartes sont ajoutées au groupe <strong>Then</strong> via <strong>Add Card</strong>.</p></figcaption></figure>

## Objectif
Cette carte envoie automatiquement des notifications par e-mail à des groupes d'utilisateurs. Au lieu d'assigner le travail à des personnes individuelles, vous envoyez le message à un groupe, et tous les membres de ce groupe le reçoivent.

**Exemple concret :** Lorsqu'une facture de valeur élevée arrive, envoyez automatiquement une notification par e-mail à tous les membres du groupe « Finance Team » afin qu'ils sachent qu'elle nécessite un examen.

---

## Quand utiliser cette carte

Utilisez cette carte lorsque vous devez :
- Notifier plusieurs personnes en même temps
- Envoyer des alertes à des groupes d'équipe
- Diffuser des mises à jour à des départements
- Notifier des groupes des changements de statut de documents
- Envoyer des rappels aux membres d'un groupe

**Scénarios courants :**
- Notifier l'équipe d'approvisionnement des nouveaux fournisseurs
- Alerter l'équipe financière des factures de valeur élevée
- Notifier l'équipe d'entrepôt des expéditions
- Diffuser les changements de statut de documents

---

## Comment ça fonctionne

1. **Vérification de la condition** : Le flux de travail vérifie les conditions « Where » et « And »
2. **Préparation de l'e-mail** : Le système prépare l'e-mail à l'aide du modèle
3. **Récupération des membres du groupe** : Le système trouve tous les membres du groupe spécifié
4. **Envoi** : L'e-mail est envoyé à chaque membre du groupe
5. **Journalisation** : L'envoi de l'e-mail est enregistré

---

## Explication des paramètres

### Email Template
Le message e-mail à envoyer

**Options :**
- Choisir parmi les modèles existants
- Chaque modèle a un objet, un corps et une mise en forme prédéfinis
- Les modèles peuvent inclure des espaces réservés comme {document_number}, {supplier_name}

**Exemple de modèle :**
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

### Group
Le groupe d'utilisateurs auquel envoyer l'e-mail

**Exemples de groupes :**
- Finance Team
- Procurement Team
- Warehouse Team
- Approval Committee
- Management Group

---

## Étapes de configuration

### Étape 1 : Choisir le modèle d'e-mail
1. Cliquez sur « Select Email Template »
2. Choisissez le modèle dans la liste
3. Vérifiez l'objet et le contenu

### Étape 2 : Sélectionner le groupe
1. Cliquez sur « Select Group »
2. Choisissez le groupe que vous souhaitez notifier
3. Vérifiez les membres du groupe (affiche généralement le nombre)

### Étape 3 : Définir les conditions
1. Ajoutez une condition : « When [condition] is true »
2. Exemple : « When invoice amount is greater than €5000 »

### Étape 4 : Tester
1. Testez avec un document d'exemple
2. Vérifiez que l'e-mail est envoyé au groupe
3. Vérifiez le rendu du modèle

---

## Exemples de modèles d'e-mail

### Modèle 1 : Alerte de facture de valeur élevée
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

### Modèle 2 : Changement de statut de fournisseur
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

### Modèle 3 : Document prêt pour l'exportation
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

---

## Cas d'usage courants

### Cas d'usage 1 : Alertes de contrôle qualité
**Déclencheur :** Lorsqu'une divergence est constatée entre la facture et le PO

**Groupe d'e-mail :** Quality Team

**Contenu :**
```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### Cas d'usage 2 : Notifications d'approbation
**Déclencheur :** Lorsqu'un document atteint un certain statut

**Groupe d'e-mail :** Approval Committee

**Contenu :**
```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### Cas d'usage 3 : Notifications d'exception
**Déclencheur :** Lorsque les conditions ne sont pas remplies

**Groupe d'e-mail :** Managers

**Contenu :**
```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### Cas d'usage 4 : Mises à jour de statut
**Déclencheur :** Lorsque le statut d'un document change

**Groupe d'e-mail :** Équipe responsable de l'étape suivante

**Contenu :**
```
Document {number} status changed to: {status}
Assigned to: {assigned_user}
Next steps: {next_steps}
```

---

## Dépannage

### « E-mail non reçu »

**Causes possibles :**
- [ ] Les utilisateurs du groupe n'ont pas d'adresses e-mail
- [ ] E-mail bloqué par le filtre anti-spam
- [ ] L'adresse e-mail est incorrecte dans le groupe
- [ ] Le groupe n'a aucun membre

**Solutions :**
1. Vérifiez que tous les membres du groupe ont des adresses e-mail
2. Vérifiez le dossier spam/courrier indésirable
3. Vérifiez que l'appartenance au groupe est correcte
4. Ajoutez des utilisateurs au groupe s'ils manquent
5. Vérifiez auprès de l'informatique que le service de messagerie fonctionne

### « Le modèle ne s'affiche pas correctement »

**Cause :** Variables d'espace réservé introuvables

**Solution :**
- [ ] Vérifiez que les noms des champs correspondent exactement
- [ ] Vérifiez si le champ a une valeur dans le document
- [ ] Utilisez le format d'espace réservé correct : {field_name}
- [ ] Testez avec un document d'exemple contenant tous les champs

### « Certaines personnes reçoivent l'e-mail, d'autres non »

**Cause :** Appartenance au groupe incomplète ou e-mails non valides

**Solutions :**
- [ ] Vérifiez que tous les membres ont un e-mail valide
- [ ] Vérifiez si certains utilisateurs se sont désinscrits
- [ ] Vérifiez que l'appartenance au groupe est à jour
- [ ] Contactez l'informatique pour valider les adresses e-mail

### « Vous souhaitez ajouter/retirer des personnes du groupe »

**Solution :**
- Contactez votre administrateur
- Les groupes sont gérés dans les paramètres système
- Ne peut pas être modifié depuis cette carte
- Demandez les modifications d'appartenance au groupe au service informatique

---

## Personnalisation des modèles d'e-mail

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

### Créer des espaces réservés personnalisés
Si vous avez besoin de données supplémentaires dans les e-mails :
1. Contactez votre administrateur
2. Demandez un nouvel espace réservé
3. Ajoutez le champ nécessaire au document
4. Mettez à jour le modèle d'e-mail

---

## Bonnes pratiques

✅ **À faire :**
- Garder le contenu de l'e-mail bref et clair
- Inclure des éléments d'action (que doivent faire les destinataires ?)
- Inclure un lien ou des instructions pour accéder au document
- Tester le modèle avec des données d'exemple
- Envoyer au bon groupe (ne pas sur-notifier)
- Utiliser des modèles pour la cohérence

❌ **À ne pas faire :**
- Envoyer trop d'e-mails (fatigue liée aux notifications)
- Inclure des données sensibles dans les e-mails
- Envoyer à des groupes qui n'ont pas besoin de l'information
- Utiliser des objets peu clairs
- Oublier d'indiquer comment agir
- Envoyer des e-mails à des individus (utilisez plutôt un groupe)

---

## Notes de performance

- Chaque e-mail prend environ 1 seconde à envoyer
- Les grands groupes peuvent prendre du temps (100 personnes = ~100 secondes)
- Ne créez pas de boucles qui envoient des milliers d'e-mails
- Surveillez la capacité du service de messagerie
- Envisagez le traitement par lots si vous avez de nombreux documents

---

## Cartes associées

- **ACTION_SEND_EMAIL** - Envoyer à une personne individuelle
- **ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP** - Assigner une tâche au lieu de simplement notifier
- **ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL** - Créer une tâche et notifier
- **STAUS_CHANGE** - Changer le statut et notifier

---

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

---

## FAQ

**Q : Puis-je envoyer à plusieurs groupes ?**
R : Créez des cartes distinctes pour chaque groupe

**Q : Que se passe-t-il si l'e-mail de quelqu'un rebondit ?**
R : L'e-mail est journalisé comme ayant échoué, l'informatique peut effectuer un dépannage

**Q : Puis-je modifier le modèle d'e-mail ?**
R : Contactez votre administrateur pour modifier les modèles

**Q : Puis-je envoyer en fonction de conditions ?**
R : Oui ! Utilisez les conditions « Where » et « And » pour contrôler quand les e-mails sont envoyés

**Q : Comment savoir si l'e-mail a été reçu ?**
R : Vérifiez les journaux d'e-mails dans DocBits pour connaître le statut d'envoi
