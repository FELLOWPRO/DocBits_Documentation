# Flujo de Ejecución en las Instalaciones

Para los clientes que ejecutan el Operador de DocBits en las instalaciones, la siguiente secuencia describe cómo un documento procesado desencadena y ejecuta un aviso del Operador a través del Agente local de DocBits.

1. **Carga y Procesamiento del Documento** Un documento se carga en DocBits y pasa por el procesamiento estándar (Extracción, validación, etc.).
2. **Desencadenador del Flujo de Trabajo** Una vez que se completa el procesamiento, un Flujo de Trabajo configurado en DocBits evalúa sus condiciones de desencadenador. Cuando se cumplen esas condiciones, el Flujo de Trabajo crea una nueva **Tarea del Operador**.
3. **Creación y Envío de Tareas**
   * El flujo de trabajo envía el texto del script, variables, pasos máximos, reintentos máximos como carga de tarea al Pool de Trabajo compartido.
4. **Bucle de Sondeo del Agente**
   * Un Agente de DocBits en las instalaciones (instalado en el entorno del cliente) sondea el Pool de Trabajo cada 5 minutos. Si no se encuentran tareas, el agente permanece inactivo y reintenta después del intervalo.
5. **Ejecución de Tareas**
   * Cuando una tarea aparece en el Pool de Trabajo, el Agente la recupera y comienza la ejecución.
6. **Generación de Registros**
   * Para cada paso—éxito o fallo—el agente registra registros detallados (acciones, estados, marcas de tiempo). Al completarse, compila el registro completo y el estado final.
7. **Retorno y Visualización de Resultados**
   * El agente envía los registros y el estado de vuelta a DocBits. El historial de ejecución del flujo de trabajo de origen se actualiza, y los usuarios pueden revisar detalles en la pestaña de **Registros de Flujo de Trabajo**.
