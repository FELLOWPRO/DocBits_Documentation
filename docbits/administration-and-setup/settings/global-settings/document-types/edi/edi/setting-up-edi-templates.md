---
hidden: true
---

# Configure EDI attributes

Choose the actual message format and document type. Review the existing attributes and active versions before changing a configuration.

<figure><img src="../../../../../../.gitbook/assets/site-all-edi-list-en.png" alt="Existing EDI format with its four configured attributes."><figcaption><p>Existing EDI format with its four configured attributes.</p></figcaption></figure>

Define the segments, elements and loops in a JSON structure descriptor. Test representative messages and inspect the resulting intermediate XML.

<figure><img src="../../../../../../.gitbook/assets/site-all-edi-detail-en.png" alt="Active STRUCTUREDESCRIPTOR attribute: JSON structure descriptor in the read-only editor."><figcaption><p>Active STRUCTUREDESCRIPTOR attribute: JSON structure descriptor in the read-only editor.</p></figcaption></figure>

Use the TRANSFORMATION XSLT to map the intermediate XML to the required standard XML. Configure PREVIEW separately for its presentation; the transformation is not a direct JSON-to-XML XSLT operation.

<figure><img src="../../../../../../.gitbook/assets/site-all-edi-transformation-en.png" alt="Active TRANSFORMATION attribute: XSLT source for transforming the intermediate XML."><figcaption><p>Active TRANSFORMATION attribute: XSLT source for transforming the intermediate XML.</p></figcaption></figure>

Configure EXTRACTIONPATHS as JSON containing XPath expressions for the resulting XML. Test fields, rows and amounts against real examples. Validate a draft before activation; the screenshots show an existing active configuration.

<figure><img src="../../../../../../.gitbook/assets/site-all-edi-extraction-paths-en.png" alt="Active EXTRACTIONPATHS attribute: JSON configuration containing XPath extraction expressions."><figcaption><p>Active EXTRACTIONPATHS attribute: JSON configuration containing XPath extraction expressions.</p></figcaption></figure>
