# Modelo de IA Específico del Proveedor para Extracción de Campos y Tablas

En la sección de herramientas de la **Pantalla de Validación**, puedes elegir el modelo de IA utilizado para la **Extracción de Campos** y la **Extracción de Tablas**.\
El **modelo de IA** seleccionado se aplica solo a todos los documentos del proveedor actual.

Para cambiar el modelo, abre el menú de opciones haciendo clic en el botón **Más opciones** (tres puntos) en el lado derecho de la pantalla y, a continuación, elige uno de los modelos disponibles:<br>

* **Full** – Máxima precisión; cuesta 2 tokens por documento
* **Fast** – Nivel predeterminado; cuesta 1 token por documento
* **Nexus** – Cuesta 1 token por documento
* **Nexus Flash** – Nivel más rápido de la familia Nexus; cuesta 1 token por documento
* **Auto** – DocBits decide por documento si Fast es suficiente o si hace falta Full; cuesta 1 token por documento
* **Auto Nexus** – Como Auto, pero limitado a la familia de modelos Nexus; cuesta 1 token por documento

<figure><img src="../../../.gitbook/assets/dbdc860-supplier-ai-model-menu-es-20261012.png" alt="Menú de opciones de la pantalla de validación con el desplegable Modelo de IA"><figcaption><p>Abre el menú de opciones y elige el modelo de IA para este proveedor.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/dbdc860-supplier-ai-model-options-es-20261012.png" alt="Desplegable Modelo de IA abierto con Full, Fast, Nexus, Nexus Flash, Auto y Auto Nexus"><figcaption><p>El desplegable Modelo de IA con las seis opciones disponibles.</p></figcaption></figure>

Si los resultados de la **extracción de campos** o la **extracción de tablas** no son satisfactorios, intenta cambiar a otro modelo para mejorar la precisión.

Para configurar el modelo de IA **globalmente para proveedores sin un modelo personalizado** o para **administrar qué modelo está activo para cada proveedor**, consulta la documentación correspondiente [**aquí**](../../../administration-and-setup/settings/document-processing/classification-and-extraction/ai-model.md).
