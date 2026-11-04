# Entonces

## Resumen de las Tarjetas de Acción "Entonces..."

### **1. Acciones de Campo de Documento:**

* **Invertir Casilla de Verificación:** Esta acción cambia el estado de una casilla de verificación en un documento.
* **Establecer Casilla de Verificación:** Establece el estado de una casilla de verificación como verdadero (marcado) o falso (desmarcado).
* **Establecer Campo a Texto:** Esta acción establece un campo de documento especificado con un valor de texto dado.

<figure><img src="../../.gitbook/assets/then1.png" alt=""><figcaption></figcaption></figure>

### **2. Acciones de Documento:**

* **Aprobar el Documento:** Marca un documento como aprobado dentro del sistema.
* **Iniciar Exportación:** Inicia el proceso de exportación de un documento.
* **Rechazar el Documento:** Marca un documento como rechazado.

<figure><img src="../../.gitbook/assets/then2.png" alt=""><figcaption></figcaption></figure>

### **3. Acciones de Estado:**

* **Cambiar Estado:** Cambia el estado de un documento o tarea a un nuevo estado especificado.

<figure><img src="../../.gitbook/assets/then3.png" alt=""><figcaption></figcaption></figure>

### **4. Acciones de Tarea:**

* Asignaciones y notificaciones:
* **Asignar Tarea:** Crea y asigna una tarea con detalles específicos a un individuo o grupo, incluyendo opciones para notificarles por correo electrónico.
* **Crear una Nueva Tarea:** Similar a asignar pero enfocado en configurar una tarea completamente nueva dentro del sistema.

<figure><img src="../../.gitbook/assets/then4.png" alt=""><figcaption></figcaption></figure>

### **5. Acciones de Tabla:**

* **Calcular en Tabla:** Realiza cálculos en datos de tabla basados en condiciones especificadas y almacena los resultados en una columna designada.
* **Cambiar Entradas:** Actualiza entradas en una tabla basadas en condiciones especificadas.

<figure><img src="../../.gitbook/assets/then5.png" alt=""><figcaption></figcaption></figure>

### **6. Acciones de Asignatario:**

* **Asignar Usuario desde Campo:** Asigna un usuario a una tarea o documento basado en datos de usuario almacenados en un campo específico, con una opción para un usuario de respaldo si el principal no está disponible.
* **Asignar Documento a Usuario o Grupo:** Asigna directamente un documento a un usuario o grupo, asegurando que la responsabilidad esté designada adecuadamente.

<figure><img src="../../.gitbook/assets/then6.png" alt=""><figcaption></figcaption></figure>

### **7. Acciones de Interacción Externa:**

* **Llamar API:** Envía una solicitud a una API externa, que puede ser personalizada con métodos específicos, parámetros y datos.
* **Enviar Solicitud HTTPS:** Similar a las llamadas de API pero específicamente formateadas para protocolos HTTPS.

<figure><img src="../../.gitbook/assets/then7.png" alt=""><figcaption></figcaption></figure>

### **8. Procesamiento Avanzado:**

* **Ejecutar Flujo de Trabajo:** Activa otro flujo de trabajo dentro del sistema, permitiendo encadenamiento de procesos complejos.

#### Aplicación Práctica

Estas tarjetas de acción se utilizan para automatizar respuestas basadas en desencadenantes específicos identificados en las partes anteriores de la configuración del flujo de trabajo. Por ejemplo:

* Si se identifica que un documento necesita revisión, la acción "Aprobar el Documento" puede ser activada automáticamente una vez que cumple todas las condiciones especificadas.
* Para tareas de gestión de datos, las acciones "Establecer Casilla de Verificación" o "Establecer Campo a Texto" aseguran que los campos de documento se actualicen automáticamente, reduciendo la entrada manual de datos y el potencial de errores.
* Tareas complejas como interacciones con API o cambios de estado agilizan las interacciones no solo dentro del sistema ERP, sino también con servicios y herramientas externas, mejorando la integración y funcionalidad.

### Conclusión

La sección "Entonces..." en su sistema de flujo de trabajo proporciona herramientas sólidas para definir acciones precisas que deben ocurrir como resultado de que se cumplan condiciones en el flujo de trabajo. Al utilizar eficazmente estas acciones, las empresas pueden automatizar procesos rutinarios, garantizar la precisión de los datos y responder dinámicamente a cambios en la información y estados del sistema. Comprender cómo configurar y utilizar estas acciones es clave para maximizar la eficiencia y efectividad de las capacidades de flujo de trabajo de su sistema ERP.
