# Mappage BOD Purchase Order

Cette page documente la façon dont DocBits ingère les BODs `SyncPurchaseOrder` d'Infor M3 et mappe les champs sur les tables internes `PURCHASE_ORDER_HEADER` et Purchase Order Line.

{% file src="../../../../.gitbook/assets/Sync.PurchaseOrder.pdf" %}
Référence d'origine du mappage BOD (PDF)
{% endfile %}

## Principes clés

- **Aucune conversion de devise dans DocBits.** Les montants sont persistés exactement tels que M3 les délivre dans le BOD, avec leur `@currencyID`. Trois montants d'en-tête sont disponibles : `ExtendedAmount` (devise de transaction), `ExtendedBaseAmount` (devise de base de la société), `ExtendedReportAmount` (devise de reporting).
- **Aucune conversion d'unité de mesure dans DocBits.** Les quantités sont stockées avec leur `@unitCode`. `ReceivedBaseUOMQuantity` est la valeur UoM de base déjà calculée par M3 — DocBits la stocke telle quelle.
- **Le statut de l'en-tête est pris dans le SXE stage lorsqu'il est disponible.** DocBits lit `UserArea/Property[@name='poeh.stagecd']` (valeurs `1..8` → Ordered / Entered / Released / Allocated / Picked / Delivered / Invoiced / Cancelled) et l'utilise comme statut d'en-tête de référence. Le `Status/Code` standard est également stocké comme repli pour les BODs dans lesquels `poeh.stagecd` n'est pas renseignée — l'émission de cette propriété UserArea dépend du tenant.
- **Pas de logique automatique de statut sur quantité partielle.** DocBits ne dérive pas de statut à partir des quantités reçues vs. commandées ; le statut délivré par M3 est repris tel quel.
- **`CONO`/`AccountingEntityID` ne fait pas partie du BOD PurchaseOrder.** Le routage par numéro de société s'applique aux données de base fournisseurs (voir [Supplier BOD Mapping](supplier-bod-mapping.md)) ; les bons de commande sont rattachés via `LocationID`. Notez que `LocationID` **n'est pas globalement unique** — lorsqu'une société M3 (CONO) est copiée entre environnements (par exemple PRD → TST), le même `LocationID` peut exister sous plusieurs CONOs. Dans ces configurations, filtrez le flux BOD entrant sur l'`AccountingEntity` attendue dans votre DataFlow ION afin d'éviter les collisions entre environnements.

## Mappage de l'en-tête

→ Table de données de base DocBits : **PURCHASE\_ORDER\_HEADER**

```python
header_mappings = {
            "purchase_order_number": "//DataArea/PurchaseOrder/PurchaseOrderHeader/DocumentID/ID",
            "warehouse_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ShipToParty/Location[@type='Warehouse']/ID",
            "location_id": "//DataArea/Sync/LocationID",
            "status": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Status/Code",
            "supplier_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/SupplierParty/PartyIDs/ID",
            "supplier_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/SupplierParty/Name",
            "order_date": "//DataArea/PurchaseOrder/PurchaseOrderHeader/OrderDateTime",
            "requested_shipment_date": "//DataArea/PurchaseOrder/PurchaseOrderHeader/RequiredDeliveryDateTime",
            "total_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedAmount",
            "buyer_contact_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CustomerParty/BuyerContact/ID",
            "buyer_contact_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CustomerParty/BuyerContact/Name",
            "order_last_modified_by": "//DataArea/PurchaseOrder/PurchaseOrderHeader/LastModificationPerson/IDs/ID",
            "order_last_modified_on": "//DataArea/PurchaseOrder/PurchaseOrderHeader/LastModificationDateTime",
            "disponent_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/PlannerReference/IDs/ID",
            "disponent_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/PlannerReference/Name",
            "extended_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedAmount",
            "extended_base_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedBaseAmount",
            "extended_report_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedReportAmount",
            "canceled_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledAmount",
            "canceled_base_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledBaseAmount",
            "canceled_reporting_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledReportingAmount",
            "type_code": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Classification/Codes/Code[@listID='Purchase Order Types']",
            "type_description": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Classification[Codes/Code[@listID='Purchase Order Types']]/Description",
            "sxe_stage": "//DataArea/PurchaseOrder/PurchaseOrderHeader/UserArea/Property/NameValue[@name='poeh.stagecd']/text()",
        }
```

### Référence des champs d'en-tête

| Champ DocBits | Source M3 | Description |
|---|---|---|
| `purchase_order_number` | `MPHEAD.IAPUNO` | Numéro de bon de commande M3, clé primaire. |
| `warehouse_id` | — | Lit `ShipToParty/Location[@type='Warehouse']/ID`. L'attribut `@type='Warehouse'` est rarement défini par M3 ; le champ reste NULL dans ce cas. Utilisez `location_id` comme entrepôt natif M3. |
| `location_id` | `MPHEAD.IAFACI` | Division/site (entrepôt) M3 où le BOD a été émis. Utilisé pour le routage organisation/site dans DocBits, y compris la mise en correspondance avec les sites de facturation. |
| `status` | `MPHEAD.IAPUSL` | `Status/Code` brut du BOD. Utilisé en repli quand `sxe_stage` est vide. |
| `sxe_stage` | `MPHEAD.IAPUSL` | Statut d'en-tête de référence, lu depuis la propriété UserArea `poeh.stagecd`. Mappe les codes SXE M3 1..8 → Ordered, Entered, Released, Allocated, Picked, Delivered, Invoiced, Cancelled. Quand défini, il supplante `status` pour les décisions de workflow. Avec la préférence `UPDATE_DOCUMENT_PURCHASE_ORDER_STATUS` activée, DocBits propage ce statut sur les factures liées. |
| `supplier_id` | `MPHEAD.IASUNO` | Numéro de fournisseur sur le bon de commande. |
| `supplier_name` | `CIDMAS.IDSUNM` | Nom d'affichage du fournisseur. |
| `order_date` | `MPHEAD.IAPUDT` | Date de création du bon de commande dans M3. |
| `requested_shipment_date` | — | Lu depuis `RequiredDeliveryDateTime` au niveau en-tête s'il existe. La plupart des configurations M3 ne portent ce champ qu'au niveau ligne ; dans ce cas, utilisez `requested_ship_date` de la ligne. |
| `total_amount` | `MPHEAD.IAOURR` | Total de la commande en devise de transaction. Stocké tel quel depuis `ExtendedAmount`. |
| `extended_amount` | `MPHEAD.IAOURR` | Même source que `total_amount`. Conservé comme colonne brute distincte pour la traçabilité et les consommateurs en aval attendant le chemin BOD canonique. |
| `extended_base_amount` | `MPHEAD.IAOUVA` | Total exprimé dans la devise de base de la société. Rempli par M3 lorsque disponible — le remplissage dépend du tenant ; si vous ne parvenez pas à reproduire une valeur renseignée, merci de partager un BOD d'exemple. |
| `extended_report_amount` | `MPHEAD.IAOUVB` | Total exprimé dans la devise de reporting de la société. Le remplissage dépend du tenant (comme `extended_base_amount`). |
| `canceled_amount` / `canceled_base_amount` / `canceled_reporting_amount` | — | Montants d'annulation en devise de transaction / de base / de reporting. Renseignés par M3 uniquement après événements d'annulation. |
| `type_code` / `type_description` | — | Type de bon de commande depuis `Classification/Codes/Code[@listID='Purchase Order Types']` (et sa `Description`). Exemples : `P10` PO normale, `P20` PO de réapprovisionnement. Stocké uniquement pour affichage — aucune logique de filtrage. |
| `buyer_contact_id` / `buyer_contact_name` | `MPHEAD.IABUYE` / utilisateur lié | Acheteur affecté à la PO. |
| `order_last_modified_by` / `order_last_modified_on` | `MPHEAD.IACHID` / `MPHEAD.IALMDT` | Champs d'audit. |
| `disponent_id` / `disponent_name` | `MPHEAD.IARESP` / utilisateur lié | Référence du planificateur. |

## Mappage des lignes

→ Table de données de base DocBits : **Purchase Order**

```python
line_mappings = {
        "sub_line_number": "SubLineNumber",
        "item_id": [
            "Item/ItemID/ID[not(@schemeName)]",
            "Item/ItemID/ID[@schemeName='NonStock']",
        ],
        "supplier_item_id": [
            "Item/ItemID/ID[@schemeName='Supplier']",
            "Item/Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']",
            "Item/SupplierItemID/ID",
        ],
        "schedule_line_number ": "DocumentReference/ScheduleLineNumber",
        "description": "Item/Description",
        "note": "Note",
        "quantity": "Quantity",
        "open_quantity": "OpenQuantity",
        "confirmed_quantity": "BackOrderedQuantity",
        "received_quantity": "ReceivedQuantity",
        "received_base_mou_quantity": "ReceivedBaseUOMQuantity",
        "unit_of_measure": "Quantity/@unitCode",
        "unit_price": "UnitPrice/Amount",
        "unit_price_per": "UnitPrice/PerQuantity",
        "unit_code_price": "UnitPrice/PerQuantity/@unitCode",
        "total_amount": ["TotalAmount", "ExtendedAmount"],
        "extended_amount": "ExtendedAmount",
        "currency": ["TotalAmount/@currencyID", "ExtendedAmount/@currencyID"],
        "buyer_id": "BuyerParty/PartyIDs/ID",
        "buyer_name": "BuyerParty/Name",
        "status": "Status/Code",
        "geo_code": "UserArea/Property/NameValue[@name='GeoCode']",
        "delivery_method": "UserArea/Property/NameValue[@name='m3.DeliveryMethod']",
        "order_multiple": "Classification/Codes/Code[@listID='Order multiple']",
        "standard_quantity": "UserArea/Property/NameValue[@name='StandardQuantity']",
        "promised_delivery_date": "PromisedDeliveryDateTime",
        "requested_ship_date": "RequiredDeliveryDateTime",
    }
```

### Référence des champs de ligne

| Champ DocBits | Source M3 | Description |
|---|---|---|
| `item_id` | `MPLINE.IBITNO` | Numéro d'article M3. Repli sur `@schemeName='NonStock'` pour articles non stockés. |
| `supplier_item_id` | `MPLINE.IBSITE` / Classification | Numéro d'article côté fournisseur. Résolu via trois replis (dans l'ordre) : `ID[@schemeName='Supplier']` → `Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']` → `Item/SupplierItemID/ID`. |
| `description` | `MPLINE.IBPITT` | Description de l'article de la ligne. |
| `note` | `MSYTXL.TLTX60` | Texte de note de ligne. |
| `quantity` | `MPLINE.IBORQA` | Quantité commandée. Stockée avec `unit_of_measure` (sans conversion). |
| `open_quantity` | `CFQA - RVQA` | Quantité encore ouverte (commandée moins reçue). Même `unit_of_measure`. |
| `confirmed_quantity` | — | Quantité confirmée par le fournisseur. M3 laisse vide ; rempli par les ERPs émettant `BackOrderedQuantity`. |
| `received_quantity` | `MPLINE.IBRVQA` | Quantité reçue. |
| `received_base_mou_quantity` | `MPLINE.IBRVQA` (UoM de base) | Quantité reçue convertie en unité de mesure de base par M3 lui-même. DocBits ne calcule pas — il stocke ce que M3 envoie. Utile pour la comptabilité de stock. |
| `unit_of_measure` | `MPLINE.IBPUUN` | UoM de transaction. S'applique à `quantity`, `open_quantity`, `received_quantity`. |
| `unit_price` | `MPLINE.IBPUPR` | Prix unitaire en devise de transaction. |
| `unit_price_per` / `unit_code_price` | `MPLINE.IBCPUC` / `MPLINE.IBPPUN` | Prix-par quantité et son code unité (modificateur de prix, ex. prix par 100 PCS). |
| `total_amount` | `LNAM + EXEP` | Total de ligne. Résolu via le repli `[TotalAmount, ExtendedAmount]` — quand `TotalAmount` manque, `total_amount` est égal à `extended_amount`. Quand les deux sont présents, `TotalAmount` peut inclure taxes/remises tandis que `extended_amount` vaut `quantity × unit_price`. |
| `extended_amount` | `LNAM` / `LNA2` | `ExtendedAmount` brut (sous-total de ligne hors taxes/remises). |
| `currency` | `MPHEAD.IACUCD` | Devise de transaction. Lue depuis `TotalAmount/@currencyID`, avec `ExtendedAmount/@currencyID` en repli. |
| `status` | `MPLINE.IBPUST` | Statut de ligne. Stocké pour reporting ; aucune logique de workflow DocBits n'en dérive. |
| `buyer_id` / `buyer_name` | `MPLINE.IBBUYE` / utilisateur lié | Acheteur au niveau ligne. `buyer_name` est rarement renseigné par M3 sur la ligne ; la référence acheteur fournisseur se trouve dans [Supplier BOD Mapping](supplier-bod-mapping.md). |
| `geo_code` | — | Code géographique pour moteurs fiscaux US/CA. Rempli uniquement par les ERPs qui l'émettent. |
| `delivery_method` | `MPLINE.IBMODL` | Mode de livraison de la ligne (code `MODL` M3). |
| `promised_delivery_date` | `CODT, DWDT/TIHM` | Date de livraison confirmée par le fournisseur. |
| `requested_ship_date` | `MPLINE.IBDWDT` | Date d'expédition demandée sur la ligne — date de livraison souhaitée opérationnellement pertinente. |
| `sub_line_number` | — | Identifiant optionnel de sous-ligne. Stocké si présent ; M3 le laisse typiquement vide. |
| `schedule_line_number` | — | Référence optionnelle à une ligne d'échéancier pour les POs à livraisons planifiées. |
| `order_multiple` / `standard_quantity` | `MPLINE.IBOMUL` / UserArea | Multiple de commande de la ligne (quantité minimale) et quantité standard d'emballage. |

## Questions fréquentes

### Comment DocBits gère-t-il les bons de commande en devise étrangère ?

DocBits ne convertit pas les devises. Le montant de transaction (`total_amount`, `extended_amount`, `unit_price`) est stocké avec son `@currencyID`. Quand la société utilise une devise de base ou de reporting différente, M3 fournit des valeurs pré-converties via `extended_base_amount` et `extended_report_amount` — stockées comme colonnes additionnelles sur l'en-tête.

### Comment DocBits dérive-t-il le statut de réception partielle ?

Il ne le fait pas. Le statut d'en-tête reflète le SXE stage M3 (`poeh.stagecd`) au moment de l'émission du BOD. Si vous avez besoin d'un indicateur de réception partielle, dérivez-le de `open_quantity` vs. `quantity` sur la table des lignes.

### Quelle différence entre `total_amount` et `extended_amount` sur la ligne ?

Les deux colonnes existent pour compatibilité historique/UI. `total_amount` est résolu via `[TotalAmount, ExtendedAmount]` ; il est donc égal à `extended_amount` chaque fois que `TotalAmount` est absent. Quand M3 émet les deux, `TotalAmount` peut inclure taxes ou remises au-dessus de la valeur `quantity × unit_price` portée par `extended_amount`.

### Pourquoi l'entrepôt est-il mappé sur deux chemins différents ?

`warehouse_id` lit `ShipToParty/Location[@type='Warehouse']/ID`, que la plupart des installations M3 laissent vide (l'attribut `@type` est rarement défini). `location_id` lit `DataArea/Sync/LocationID`, toujours rempli par M3 et correspondant à la division/site auquel la PO appartient. Traitez `location_id` comme identifiant d'entrepôt natif M3.

### Certains champs sont documentés mais toujours vides (`buyer_name`, `geo_code`, `confirmed_quantity`, `sub_line_number`, …). Pourquoi sont-ils mappés ?

Ces mappages sont défensifs : le schéma BOD autorise les champs, et d'autres ERPs ou extensions M3 sur mesure peuvent les renseigner. Quand M3 les laisse vides, les colonnes sont simplement NULL dans DocBits.

### Dois-je filtrer `AccountingEntity` (CONO) dans le DataFlow ION même si le BOD PurchaseOrder n'a pas de `CONO` ?

Oui, dans les environnements où la même société M3 a été copiée (par exemple PRD → TST, ou deux tenants parallèles). `LocationID` seul n'est pas unique entre CONOs dans ces configurations, et un BOD provenant d'une société copiée peut entrer en collision avec une société active. Le motif recommandé est de filtrer le flux entrant sur la valeur `AccountingEntity` attendue dans ION avant que le BOD n'atteigne DocBits.

### Mes BODs ne contiennent jamais `UserArea/Property[@name='poeh.stagecd']` — que se passe-t-il ?

DocBits bascule sur l'élément standard `Status/Code` dans l'en-tête. L'émission de `poeh.stagecd` dépend du tenant. Si vous attendez cette propriété mais ne la trouvez pas dans vos BODs, partagez un BOD d'exemple avec l'équipe DocBits afin que nous puissions confirmer la personnalisation M3 qui la produit.

### `ExtendedBaseAmount` / `ExtendedReportAmount` sont-ils vraiment renseignés sur l'en-tête ?

Lorsque M3 les envoie sur l'en-tête, DocBits les stocke dans des colonnes dédiées (`extended_base_amount`, `extended_report_amount`). Le remplissage dépend de la configuration des devises M3 : les sociétés avec une devise de base/reporting différente de la devise de transaction les reçoivent généralement toutes deux. Si vous ne parvenez pas à reproduire une valeur renseignée dans votre propre tenant, partagez un BOD d'exemple afin que nous puissions vérifier ensemble les conditions.
