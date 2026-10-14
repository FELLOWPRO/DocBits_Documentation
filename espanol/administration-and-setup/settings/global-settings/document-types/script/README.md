# Script

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2009.43.25.png" alt=""><figcaption></figcaption></figure>

{% embed url="https://youtu.be/n8NpWWIjmlA" %}
DocBits Document Scripts Explained: Automate Custom Logic in Your Document Workflow
{% endembed %}

#### Visión general

Los scripts en DocBits suelen estar escritos en un lenguaje de script compatible con el sistema Python. Se activan durante el flujo de procesamiento de documentos para aplicar lógica empresarial compleja o garantizar la integridad y precisión de los datos antes de que se procesen o almacenen más.

#### Funciones clave y opciones

1. **Gestión de scripts**:
   * **Nombre**: A cada script se le asigna un nombre único para su identificación.
   * **Tipo de documento**: Asocia el script con un tipo de documento específico, determinando en qué documentos se aplicará el script.
   * **Disparador en**: Define cuándo se activa el script (por ejemplo, al cargar un documento, antes de exportar datos, después de la validación de datos).
   * **Estado activo/inactivo**: Permite a los administradores activar o desactivar scripts sin eliminarlos, lo que proporciona flexibilidad en pruebas e implementación.
2. **Editor de scripts**:
   * Proporciona una interfaz donde se pueden escribir y editar scripts. El editor suele admitir resaltado de sintaxis, resaltado de errores y otras funciones para ayudar en el desarrollo de scripts.
   * **Ejemplo de script**: Los scripts pueden incluir operaciones como recorrer líneas de factura para validar totales o eliminar entradas que no cumplan ciertos criterios.

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2009.43.37.png" alt=""><figcaption></figcaption></figure>

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2498" %}
