# Automatic Purchase Order Data Matching

Docbits is an advanced system designed to automate the matching of purchase order data (POs) with incoming invoice documents. This tool is specifically designed for efficient management and processing of invoice data within ERP systems. This documentation explains the basics of automatic matching through Docbits and defines the specific rules required for successful matching.

<figure><img src="../../../.gitbook/assets/Automatic Purchase Order Data Matching.svg" alt=""><figcaption></figcaption></figure>

## **Fundamental Principles of Auto Matching in Docbits**

**Data Extraction:** Docbits begins the process by extracting relevant data from digitized invoice documents. Typically, this data includes item numbers, quantities, and unit prices of each invoice line. The precision of this extraction is crucial, as it forms the basis for the subsequent matching process.

**Comparison with PO Data:** The extracted data are compared with the corresponding information in the stored purchase orders. Docbits checks whether the item numbers, quantities, and prices match those in the POs. For a successful match, the data in the invoices must correspond to the data in the purchase orders, considering defined tolerance thresholds.

**Automatic Matching:** Based on the comparison results, Docbits performs the matching. The system verifies whether the matching criteria fall within the set tolerance limits. If these criteria are met, the match is considered successful.

**Reporting:** After completing the matching process, Docbits generates reports that show the status of the matches. These reports inform about successfully matched invoices and identify those with discrepancies.

## **Definition of Matching Rules**

**Item Number:** The item number on the invoice must exactly match the item number in the purchase order. There is no tolerance for deviations in item numbers.

**Quantities:** The quantity of goods delivered on the invoice may vary within a predefined tolerance range. Typically, a tolerance of ±5% might be acceptable to account for minor differences in delivery quantities.

**Prices:** Price deviations are tolerable up to a set threshold. A common tolerance might be ±2% of the price to accept slight differences in price statements that arise from rounding differences or currency fluctuations.

## **Match Status:**

* **Full Match:** All data points (item number, quantity, and price) are within the set tolerance limits.
* **Partial Match:** One or more data points deviate outside the tolerance limits, but the deviations are minimal and require manual review.
* **No Match:** Significant deviations in one or more data points that require immediate correction or further investigation.

The precise definition of these rules and the setting of tolerance limits are crucial for the efficiency of the automatic matching and the reduction of manual interventions. Docbits allows for flexible configuration of these parameters to meet the needs of various businesses and industries.
