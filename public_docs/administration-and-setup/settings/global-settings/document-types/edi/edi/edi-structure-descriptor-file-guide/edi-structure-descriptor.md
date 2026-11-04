# EDI Structure descriptor

The primary goal of the structure descriptor is to outline the elements of an EDI message in a logical and organized manner, making it easier to manage and parse the data. By accurately reflecting the hierarchy of the message.

### Elements of the structure descriptor

**N1** – Contains the following fields:

* **N1** – Name or Identifier of the entity (e.g., party, organization).
* **N2** – Additional name information (usually a secondary name for the entity).
* **N3** – Address information (typically the street address).
* **N4** – Geographic location (city, state, ZIP code, country).\


**N9** – Contains the following field:

* **N9** – Reference identifier (e.g., purchase order number or control number).
* **Loops:**
  * **MSG01** – Contains the following field:
    * **MSG01** – Free-form message text (usually a note or special instruction related to the transaction).

**IT1** – Contains the following fields:

* **IT1** – Line item identifier (e.g., item number or product code).
* **QTY** – Quantity of the item in the transaction (e.g., units ordered or shipped).
* **TXI** – Tax information (e.g., tax rates, amounts, or classifications for the item).
* **REF** – Reference information (e.g., lot number, serial number, or other identifiers related to the item).
* **Loops:**
  * **SAC** – Can repeat and contains the following fields:
    * **SAC** – Service, promotion, allowance, or charge information (e.g., additional costs or discounts related to the item).
    * **TXI** – Tax information related to SAC (e.g., taxes on charges or allowances).

**SAC** – Contains the following fields:

* **SAC** – Service, promotion, allowance, or charge information (can be used independently or within the IT1 loop to represent additional charges/discounts).
* **TXI** – Tax information related to SAC (e.g., taxes on charges or allowances).

### Here is the full example of a structure descriptor in a JSON format:

```
{
    "N1": {
        "fields": [
            "N1",  
            "N2",   
            "N3",   
            "N4"    
        ]
    },
    "N9": {
        "fields": [
            "N9"    
        ],
        "loops": {
            "MSG01": {
                "fields": [
                    "MSG01"   
            }
        }
    },
    "IT1": {
        "fields": [
            "IT1",   
            "QTY",   
            "TXI",   
            "REF"    
        "loops": {
            "SAC": {
                "fields": [
                    "SAC",   
                    "TXI"    
        }
    },
    "SAC": {
        "fields": [
            "SAC",   
            "TXI"    
        ]
    }
}
```

