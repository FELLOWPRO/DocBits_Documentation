# Orden de compra - Preguntas frecuentes

**¿Dónde compruebo si las actualizaciones de sincronización de PurchaseOrderBOD están correctamente implementadas?**

Navegue a la sesión _BOD Implementation Registration (bobod1100m000)_ en Infor ERP / SAP. Esta sesión le permite revisar, modificar y registrar tanto las implementaciones de BOD estándar como las personalizadas, incluido PurchaseOrderBOD.

\


<figure><img src="../../../../.gitbook/assets/PO.png" alt="Sesión de LN BOD Implementation Registration (bobod1100m000) que muestra implementaciones BOD con las casillas Public, Standard y Staging"><figcaption></figcaption></figure>

**¿Cómo identifico la implementación de BOD concreta que necesito verificar?**

Busque los campos BOD Implementation Identifier y BOD Name. El BOD Name suele indicar el tipo de BOD (p. ej., PurchaseOrderBOD). El BOD Implementation Identifier es un identificador único de esa configuración de BOD.

\


**¿Qué significa la casilla ‘Public’ en la sesión BOD Implementation Registration?**

La casilla Public indica si la implementación de BOD está disponible para la comunicación externa.

• Seleccionada: el BOD se puede intercambiar fuera de Infor ERP / SAP (interfaz pública y protegida).

• Desmarcada: el BOD es solo para el procesamiento interno de Infor ERP / SAP (interfaz protegida).

\


**Veo un campo ‘Parent BOD Name’. ¿Para qué sirve?**

El campo Parent BOD Name muestra el BOD padre si el BOD actual es una versión derivada o dependiente. Si la casilla Public está seleccionada, este campo estará vacío. En caso contrario, ayuda a comprender la jerarquía de las implementaciones de BOD.

\


**¿Cómo sé si la implementación de BOD es estándar o personalizada?**

Compruebe la casilla Standard.

• Seleccionada: el BOD es una implementación estándar suministrada por Infor ERP / SAP.

• Desmarcada: el BOD es una implementación personalizada definida por su equipo o por un partner.

\


**¿Cuál es la finalidad de la casilla ‘Staging’?**

Si la casilla Staging está seleccionada, los BOD se almacenan primero de forma provisional en lugar de publicarse inmediatamente. Después se pueden publicar desde la sesión _Publish Staged BODs (bobod2200m000)_.

Nota: para ProjectBudgetBOD, el staging es obligatorio y no se puede cambiar. Para los BOD estándar de datos maestros, el staging se puede activar manualmente, y para los BOD personalizados siempre se puede configurar.

\


**¿Cómo afecta la casilla ‘Synchronous Processing’ al procesamiento de los BOD entrantes?**

Synchronous Processing determina la acción que se realiza si falla un proceso posterior tras recibir un BOD.

• Seleccionada: el BOD entrante y el proceso posterior deben completarse correctamente ambos; de lo contrario, no se procesará ninguno.

• Desmarcada: el BOD entrante se procesa, pero si falla el proceso posterior, debe gestionarse manualmente.

\


**¿Dónde verifico si la función ‘Stage’ está activa o no para mi BOD?**

En la sesión _BOD Implementation Registration (bobod1100m000)_, compruebe la casilla Staging. Si no está seleccionada, el staging no está activo para ese BOD en concreto.

\


**Si PurchaseOrderBOD no se activa en todas las actualizaciones, ¿qué más debería tener en cuenta?**

• Confirme que la opción Staging esté configurada según lo previsto. Si el staging está desactivado, el BOD debería publicarse inmediatamente.

• Verifique que el ajuste Synchronous Processing sea correcto para su flujo de trabajo.

• Asegúrese de que BOD Implementation Identifier y BOD Name sean correctos y de que está trabajando en la configuración de BOD adecuada.

• Compruebe si el BOD es estándar o personalizado y verifique si algún ajuste personalizado anula el comportamiento estándar.

\


**¿Hay escenarios en los que podría no ver las actualizaciones de PurchaseOrderBOD como se espera?**

Sí. Si el BOD no está configurado correctamente (ajustes erróneos en Public, Staging o Synchronous Processing) o si se trata de una implementación de BOD personalizada que no se ajusta a los requisitos de su proceso, es posible que las actualizaciones no se activen como se espera. Revise su configuración en la sesión _bobod1100m000_ y asegúrese de que todos los parámetros coincidan con el flujo de proceso previsto.
