# Edición de Plantillas de Correo Electrónico

#### Descripción General

La función de Plantillas de Correo Electrónico permite a los administradores crear y personalizar comunicaciones por correo electrónico que se envían automáticamente a los proveedores. Uno de los elementos clave utilizados en estas plantillas es el `{{magic_link}}`, que proporciona un enlace dinámico adaptado a cada destinatario.

**¿Qué es `{{magic_link}}`?**

El `{{magic_link}}` es un marcador de posición que se reemplaza dinámicamente con una URL única cuando se envía el correo electrónico. Esta URL generalmente dirige al destinatario a completar una acción, como registro, aprobación o acceso a una parte específica del portal del proveedor.

#### Edición de Plantillas de Correo Electrónico

**Accediendo al Editor de Plantillas de Correo Electrónico**

1. **Navegar a Plantillas de Correo Electrónico**:
   * Ve a la sección de **Plantillas de Correo Electrónico** desde el menú principal.
2. **Seleccionar una Plantilla para Editar**:
   * Elige la plantilla de correo electrónico que deseas editar haciendo clic en el nombre de la plantilla (por ejemplo, "Correo Electrónico de Invitación al Proveedor").
3. **Editar la Plantilla**:
   * El editor te permite modificar tanto el código HTML como el diseño visual del correo electrónico.
   * Puedes alternar entre la edición visual y la edición de código utilizando las pestañas proporcionadas.

**Definiendo `{{magic_link}}` como un Enlace**

Para definir `{{magic_link}}` como un enlace clicable en el correo electrónico, necesitas asegurarte de que esté correctamente formateado en el código HTML de la plantilla. Sigue estos pasos:

1. **Localiza la Sección del Enlace en el Código HTML**:
   * En el editor de código, encuentra la sección donde deseas que aparezca el enlace mágico. Esto suele estar dentro de una etiqueta `<a>` (ancla).
2.  **Inserta el Marcador de Posición `{{magic_link}}`**:

    * Reemplaza el atributo `href` de la etiqueta ancla con `{{magic_link}}`.
    * Asegúrate de que el enlace esté estilizado adecuadamente para la plantilla de correo electrónico. Aquí tienes un ejemplo:

    ```html
    <a href="{{magic_link}}" target="_blank" style="
        background-color: #B7184B;
        border-radius: 25px;
        font-family: 'Montserrat', Arial, sans-serif;
        font-size: 14px;
        font-weight: bold;
        padding: 12px 25px;
        color: #FFFFFF;
        text-decoration: none;
        display: inline-block;
        cursor: pointer;">
        Completar Registro
    </a>
    ```

#### 3. Personaliza el Texto del Enlace:

• Modifica el texto entre las etiquetas de apertura \<a> y cierre \</a> para reflejar la acción que deseas que el usuario realice. Por ejemplo, “Completar Registro” o “Acceder a Tu Cuenta”.

4. Guarda y Prueba la Plantilla:

• Después de realizar los cambios, haz clic en el botón Guardar.

• Puedes usar el botón Enviar Prueba para enviar un correo electrónico de prueba y asegurarte de que el enlace funcione como se espera.

### Mejores Prácticas para Usar \{{magic\_link\}}

• Ubicación del Enlace: Coloca el \{{magic\_link\}} de manera prominente en el correo electrónico para asegurarte de que sea fácilmente accesible para los destinatarios.

• Llamado a la Acción Claro: El texto dentro del enlace debe ser un llamado a la acción claro, como “Completar Registro” o “Confirmar Tu Correo Electrónico”.

• Estilo: Asegúrate de que el enlace esté estilizado de manera consistente con el resto de la plantilla de correo electrónico y se destaque visualmente.

• Pruebas: Siempre envía un correo electrónico de prueba después de editar la plantilla para verificar que el \{{magic\_link\}} se resuelva correctamente y que el estilo sea apropiado.

### Conclusión

Al definir correctamente el \{{magic\_link\}} en tus plantillas de correo electrónico, puedes asegurarte de que los destinatarios reciban un correo electrónico personalizado y accionable que los guíe a la tarea apropiada dentro de tu portal de proveedores. Esto mejora la experiencia del usuario y asegura procesos de incorporación y comunicación fluidos.

Esta documentación proporciona instrucciones paso a paso para los administradores sobre cómo definir y usar el \{{magic\_link\}} en las plantillas de correo electrónico, asegurando que los correos sean tanto funcionales como visualmente atractivos.
