# Statuts de désactivation des bons de commande

## **Aperçu**

Le paramètre **PO Désactiver Statuts** permet aux utilisateurs de spécifier les statuts de bon de commande (PO) qui empêchent les factures d'être associées à ces POs. Si un bon de commande a un statut répertorié dans ce paramètre, il **ne peut pas** être utilisé pour l'appariement des factures dans l'écran d'appariement des PO, empêchant ainsi le traitement ultérieur des factures associées jusqu'à ce que le statut du PO change pour un statut qui n'est pas désactivé.\
\
En utilisant ce paramètre, les utilisateurs peuvent s'assurer que les bons de commande avec des statuts spécifiques ne subissent pas de traitement supplémentaire des factures, réduisant ainsi les erreurs et empêchant les paiements inutiles.

## **Étapes d'activation**

1.  Allez dans **Paramètres → Paramètres globaux → Types de documents**

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_1_fr.png" alt="Navigation des paramètres DocBits en espagnol avec les groupes Global Settings et Document Processing et les entrées d'informations sur l'entreprise et d'autorisations utilisateur"><figcaption></figcaption></figure>
2.  Sélectionnez le type de document souhaité et cliquez sur **Plus de paramètres**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_2_fr.png" alt="Page Document Types listant Invoice, Credit Note, Delivery Note, Order Confirmation et Contract avec les onglets Edit layout, Document Sub Types, Table columns et Fields"><figcaption></figcaption></figure>
3.  Dans la section **Bon de commande**, accédez à l'option **PO Désactiver Statuts**.

    <figure><img src="../../../../../../.gitbook/assets/disable_po_status_3_fr.png" alt="Page More Settings pour les types de documents avec la section Purchase Order et l'option PO disable statuses mise en évidence"><figcaption></figcaption></figure>

### **Comment identifier un bon de commande désactivé**

Dans l'écran **Appariement des PO**, un bon de commande désactivé apparaît **barré**. Cela indique visuellement que le PO est actuellement restreint d'être associé en raison de son statut.

<figure><img src="../../../../../../.gitbook/assets/disable_po_status_6.png" alt="Tableau de l'écran de PO Matching avec les colonnes LINE NUMBER, ITEM ID, STATUS, QUANTITY, UNIT PRICE et MATCHED QUANTITY"><figcaption></figcaption></figure>

### **Comment le configurer**

1. Dans le paramètre **PO Désactiver Statuts**, vous verrez un champ de sélection sur le côté gauche.
2.  En cliquant sur ce champ, une liste déroulante des statuts de PO disponibles s'ouvre.

    <figure><img src="../../../../../../.gitbook/assets/disable_po_status_4_fr.png" alt="Panneau de paramétrage du statut PO avec interrupteur du statut Purchase Order désactivé et boîte de dialogue de confirmation dans l'interface espagnole" width="261"><figcaption></figcaption></figure>
3. Sélectionnez un ou plusieurs statuts en cliquant dessus. Cliquez à nouveau pour désélectionner.
4.  Cliquez sur le bouton **Appliquer** pour enregistrer vos modifications.

    <figure><img src="../../../../../../.gitbook/assets/disable_po_status_5_fr.png" alt="Paramètre des statuts désactivés du PO avec les valeurs sélectionnées Canceled, Deleted et Invoiced, et le bouton Apply"><figcaption></figcaption></figure>

**Statuts disponibles**

* Canceled
* Deleted
* Invoiced
* Open
* Partially Invoiced
* Partially Received
* Received
* Rejeté
* Unapproved
* Hold
* Closed
