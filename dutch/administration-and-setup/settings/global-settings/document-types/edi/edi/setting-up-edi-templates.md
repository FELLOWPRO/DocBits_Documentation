---
hidden: true
---

# Setting Up EDI Templates

## Here are step-by-step instructions for setting up EDI templates:

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_cert_metadata.png" alt="Docbits Sso Cert Metadata"><figcaption></figcaption></figure>

**Define the structure descriptor:**

* Identify the type of EDI message you are working with, e.g. ANSI X12, EDIFACT, or a custom format.
* Determine the segments, elements, and subelements within the EDI structure.
* Create a structure descriptor that accurately reflects the hierarchy and organization of the EDI message. This can be done using a special syntax such as XML or JSON.

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_access_settings.png" alt="Docbits Sso Access Settings" width="273"><figcaption></figcaption></figure>

**Set up transformations:**

* Use an appropriate tool or software that supports EDI transformations, such as an EDI translator.
* Define the rules for converting the EDI message to your system's internal format and vice versa.
* Configure the transformations to interpret and process segments, elements, and subelements according to your system's requirements. Test the transformations thoroughly to ensure that the data is correctly interpreted and formatted.

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_idp_config.png" alt="Docbits Sso Idp Config" width="268"><figcaption></figcaption></figure>

**Configure extraction paths for optimal data extraction and formatting:**

* Identify the data fields to be extracted and transferred to your internal system.
* Define extraction paths or rules to extract the relevant data fields from the EDI messages.
* Consider the different variations and formats that may occur in the incoming EDI messages and ensure that the extraction paths are flexible enough to accommodate them.
* Validate the extraction results to ensure that the correct data fields are extracted and correctly formatted.

<figure><img src="../../../../../../.gitbook/assets/docbits_edi_validate_extraction.png" alt="Docbits Edi Validate Extraction" width="92"><figcaption></figcaption></figure>

By carefully defining the structure descriptor, setting up transformations and configuring extraction paths, you can ensure that data extraction and formatting are performed optimally in your EDI templates. This will help improve the efficiency and accuracy of your electronic business communications.
