# Then

## Resumen de las tarjetas de acción "Then..."

### **1. Acciones de Document Field:**

* **Invert Checkbox:** Esta acción invierte el estado de un campo de casilla de verificación en un documento.
* **Set Checkbox:** Establece el estado de un campo de casilla de verificación a verdadero (marcado) o falso (sin marcar).
* **Set Field to Text:** Esta acción establece un campo de documento determinado a un valor de texto dado.

<figure><img src="../../../.gitbook/assets/then1.png" alt=""><figcaption></figcaption></figure>

### **2. Acciones de Document:**

* **Approve the Document:** Marca un documento como aprobado en el sistema.
* **Reject the Document:** Marca un documento como rechazado.

<figure><img src="../../../.gitbook/assets/image (259).png" alt=""><figcaption></figcaption></figure>

### **3. Acciones de Export:**

* **Export document with export configuration:** Inicia el proceso de exportación con una configuración de exportación específica.
* **Start Export:** Inicia el proceso de exportación.

<figure><img src="../../../.gitbook/assets/image (260).png" alt=""><figcaption></figcaption></figure>

### **4. Acciones de Status:**

* **Change Status:** Cambia el estado de un documento o tarea a un nuevo estado especificado.

<figure><img src="../../../.gitbook/assets/then3.png" alt=""><figcaption></figcaption></figure>

### **5. Acciones de Task:**

* Asignaciones y notificaciones:
  * **Assign Task:** Crea y asigna una tarea con detalles específicos a una persona o grupo, incluyendo opciones para notificarles por correo electrónico.
  * **Create a New Task:** Similar a asignar, pero centrado en configurar una tarea completamente nueva en el sistema.

<figure><img src="../../../.gitbook/assets/then4.png" alt=""><figcaption></figcaption></figure>

### **6. Acciones de Table:**

* **Calculate in Table:** Realiza cálculos sobre los datos de la tabla según las condiciones especificadas y almacena los resultados en una columna designada.
* **Change Entries:** Actualiza las entradas de una tabla según las condiciones especificadas.

<figure><img src="../../../.gitbook/assets/then5.png" alt=""><figcaption></figcaption></figure>

### **7. Acciones de Assignee:**

* **Assign User from Field:** Asigna un usuario a una tarea o documento basándose en los datos de usuario almacenados en un campo específico, con la opción de un usuario alternativo si el principal no está disponible.
* **Assign Document to User or Group:** Asigna directamente un documento a un usuario o grupo, garantizando que la responsabilidad se designe de forma adecuada.

<figure><img src="../../../.gitbook/assets/then6.png" alt=""><figcaption></figcaption></figure>

### **8. Acciones de interacción externa:**

* **Call API:** Envía una solicitud a una API externa, que se puede personalizar con métodos, parámetros y datos específicos.
* **Send HTTPS Request:** Similar a las llamadas a la API, pero con formato específico para protocolos HTTPS.

<figure><img src="../../../.gitbook/assets/then7.png" alt=""><figcaption></figcaption></figure>

### **9. Procesamiento avanzado:**

* **Run Workflow:** Dispara otro flujo de trabajo en el sistema, lo que permite encadenar procesos complejos.

#### Aplicación práctica

Estas tarjetas de acción se utilizan para automatizar respuestas basadas en disparadores específicos identificados en las partes anteriores de la configuración del flujo de trabajo. Por ejemplo:

* Si un documento se identifica como que necesita revisión, la acción "Approve the Document" se puede disparar automáticamente una vez que cumple todas las condiciones especificadas.
* Para tareas de gestión de datos, las acciones "Set Checkbox" o "Set Field to Text" garantizan que los campos del documento se actualicen automáticamente, reduciendo la entrada manual de datos y el potencial de errores.
* Tareas complejas como interacciones con la API o cambios de estado agilizan las interacciones no solo dentro del sistema ERP, sino también con servicios y herramientas externos, mejorando la integración y la funcionalidad.

### Conclusión

La sección "Then..." de su sistema de flujos de trabajo proporciona herramientas robustas para definir acciones precisas que deben ocurrir como resultado del cumplimiento de las condiciones del flujo de trabajo. Al utilizar estas acciones de forma eficaz, las empresas pueden automatizar procesos rutinarios, garantizar la precisión de los datos y responder dinámicamente a la información y los estados del sistema cambiantes. Comprender cómo configurar y utilizar estas acciones es clave para maximizar la eficiencia y la eficacia de las capacidades de flujo de trabajo de su sistema ERP.
