# Regex Manager

This feature by DocBits gives you an alternative to model classification as it allows you to write searchable regular expressions for a document type for classification and other purposes.

Document Type: The Regex Manager allows you to write regular expressions and this regex will then be searched for in the document. If it finds a match to the regex of a defined document, it then classifies that document to the corresponding document type. For example, if you wrote a regular expression to find “Gutschrift”. If DocBits found this term in a document it would classify that document as a credit note.

Document Origin: This lets DocBits know the country of origin of a document through regular expressions. For example, if a regular expression for a Spanish document contains the term “Factura”. If DocBits searches a document and finds this term then it would know that the document is of Spanish origin and classify it as such.

## **Accessing the Regex Manager**

To find this feature in DocBits, navigate to Settings → Document Types. Under Custom Document Types, click New. Enter a name for the document type, add an optional description and tick “Table available” if the document contains a table. Then choose “Regex” instead of “Auto” and click “Next”.

<figure><img src="../../../.gitbook/assets/regex-manager-create-en-20261006.png" alt="Create new document type page with name field, Table available checkbox, description field and the Auto and Regex buttons"><figcaption><p>Choose “Regex” to classify the new document type with regular expressions.</p></figcaption></figure>

## **Adding and Removing Regex**

The “Regex” step shows the regex models that already exist, each with its origin and pattern, and an “Add” button for creating a new regex model. Use the actions menu at the end of a row to manage that entry. Click “Next” to continue with “Fields & groups”.

<figure><img src="../../../.gitbook/assets/regex-manager-list-en-20261006.png" alt="Regex step with the Add button and a table of three regex models with origin, pattern and actions"><figcaption><p>Existing regex models with origin and pattern. “Add” creates a new one.</p></figcaption></figure>
