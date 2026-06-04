# Validación y pruebas

Antes de confiar en un Advanced Workflow, usa los controles de la barra de herramientas para confirmar que es correcto y que se comporta como esperas.

## Validate

Haz clic en el control **Validate** (el icono de círculo con marca, o pulsa <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). La validación revisa el grafo en busca de problemas — nodos sin conectar, configuración faltante y conexiones no válidas — para que puedas corregirlos antes de que el flujo de trabajo se ejecute sobre documentos reales.

## Test

Haz clic en el control **Test** (el icono de reproducción, o pulsa <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) para ejecutar el flujo de trabajo sobre una muestra y ver cómo se comporta, sin afectar a los documentos en producción.

## Escenarios de prueba

Para comprobaciones repetibles, guarda **escenarios de prueba** en el **Test Manager** (consulta el [Panel](../workflow-dashboard.md)). Cada escenario registra un resultado esperado y muestra un resultado de aprobado/fallido, y **Run All Tests** los vuelve a ejecutar todos juntos — de modo que puedas confirmar que tus flujos de trabajo siguen comportándose correctamente tras un cambio.

<figure><img src="../../../.gitbook/assets/workflow_test_manager.png" alt="Lista del Workflow Test Manager con escenarios de prueba y Run All Tests"><figcaption><p>El Test Manager — escenarios guardados con resultados de aprobado/fallido y <strong>Run All Tests</strong>.</p></figcaption></figure>

## Próximos pasos

- Revisa los tipos de nodo y las conexiones en [Nodos](nodes.md).
- Consulta todos los controles de la barra de herramientas y el lienzo en [Barra de herramientas y lienzo](toolbar-and-canvas.md).
