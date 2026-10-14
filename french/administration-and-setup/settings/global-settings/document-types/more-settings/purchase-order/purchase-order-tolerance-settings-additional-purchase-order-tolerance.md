# Paramètres de tolérance de commande d'achat / Tolérance de commande d'achat supplémentaire

### **Paramètre pour configurer les tolérances de commande d'achat**

Allez à **Paramètres → Paramètres généraux → Types de documents → Plus de paramètres → commande d'achat →Réglage de la tolérance PO**

#### **Comment ça fonctionne**

Lorsqu'il est activé, ce paramètre vous permet de définir des tolérances pour la **Quantité** et/ou le **Prix unitaire**. Ces tolérances peuvent être définies soit en pourcentage, soit en valeur fixe. Cela signifie qu'une facture peut s'écarter de la commande d'achat (CA) dans la plage de tolérance spécifiée sans être signalée comme un désaccord, offrant ainsi de la flexibilité tout en garantissant un traitement fluide.

<mark style="color:red;">**REMARQUE**</mark>: Les tolérances fonctionnent dans les deux sens ; c'est-à-dire que la valeur de la facture peut être soit supérieure, soit inférieure à la valeur de la CA dans la plage autorisée.

#### **Configuration**

* **Activer le paramètre :**
  * Activez le paramètre de tolérance de CA à l'aide du bouton bascule.
* **Configurer les tolérances :**
  * Quatre champs apparaîtront :
    * Un champ pour le **Montant de tolérance de quantité**.
    * Un champ pour le **Montant de tolérance de prix unitaire**.
  * Derrière chaque champ, il y a un menu déroulant où vous pouvez sélectionner le type de tolérance :
    * **Pourcentage :** Indique une tolérance en pourcentage.
    * **Valeur :** Indique un montant fixe par lequel la valeur peut différer.

<figure><img src="../../../../../../.gitbook/assets/docbits_po_tolerance_value_fixed_fr.jpg" alt="Docbits Po Tolerance Value Fixed Fr"><figcaption></figcaption></figure>

**Scénario d'exemple :**

* Supposons que la **Tolérance de prix unitaire** soit fixée à **5 %**.
* La commande d'achat comprend deux lignes :
  * **Ligne 1 :** Prix unitaire = **5,00 $**
  * **Ligne 2 :** Prix unitaire = **2,00 $**
* Sur la facture :
  * **Ligne 1 :** Le prix unitaire est ajusté à **4,80 $** (**dans** la tolérance de 5 %).
  * **Ligne 2 :** Le prix unitaire est ajusté à **2,20 $** (**hors** de la tolérance de 5 %).
* **Résultat :**
  * La ligne 1 **n'est pas signalée** comme un désaccord car 4,80 $ est dans les 5 % de 5,00 $.
  * La ligne 2 **est signalée** comme un désaccord car 2,20 $ dépasse la déviation autorisée de 5 % par rapport à 2,00 $. L'utilisateur doit maintenant prendre des mesures pour résoudre le désaccord avant que la facture puisse être traitée davantage.

<div align="center"><figure><img src="../../../../../../.gitbook/assets/docbits_po_tolerance_mismatch_example_fr.jpg" alt="Docbits Po Tolerance Mismatch Example Fr"><figcaption></figcaption></figure></div>

### Paramètre pour configurer les paramètres de tolérance de commande d'achat supplémentaires

Allez à **Paramètres → Paramètres généraux → Types de documents → Plus de paramètres → commande d'achat → Réglage de la tolérance additionnelle de la commande**

#### **Comment ça fonctionne**

Lorsqu'il est activé, ce paramètre vous permet de définir des tolérances pour le **Fret**, les **Frais**, et/ou la **Taxe**. Ces tolérances peuvent être définies soit en pourcentage, soit en valeur fixe, permettant aux factures de varier légèrement par rapport aux valeurs de la CA sans être signalées comme des désaccords. Cela offre une flexibilité supplémentaire et garantit que les différences mineures n'interrompent pas le flux de travail.

<mark style="color:red;">**REMARQUE**</mark>: Tout comme les paramètres de tolérance standard, ces tolérances s'appliquent dans les deux sens, permettant des augmentations ou des diminutions dans les limites fixées.

#### **Configuration**

* **Activer le paramètre :**
  * Activez le paramètre de tolérance de CA supplémentaire à l'aide du bouton bascule.
* **Configurer les tolérances :**
  * Six champs deviendront visibles :
    * Un champ pour chaque montant de tolérance pour le **Fret**, les **Frais**, et la **Taxe**.
  * Chaque champ a un menu déroulant associé où vous pouvez choisir le type de tolérance :
    * **Pourcentage :** La tolérance est définie comme un pourcentage.
    * **Valeur :** La tolérance est définie comme un montant fixe.

<figure><img src="../../../../../../.gitbook/assets/docbits_purchase_order_table.png" alt="DocBits Achat Commande Tableau"><figcaption></figcaption></figure>
