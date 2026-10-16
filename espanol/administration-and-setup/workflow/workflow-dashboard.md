# Panel

El **Workflow Dashboard** es la página de inicio del área de flujos de trabajo. Muestra cómo se comportan sus flujos de trabajo (totales de ejecuciones, tasas de éxito y de fallo, un gráfico de ejecuciones a lo largo del tiempo y la actividad reciente) y le da acceso a la lista de flujos de trabajo, al gestor de pruebas y al Card SDK.

<figure><img src="../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard con totales de ejecuciones, tasas de éxito y de fallo, el gráfico de ejecuciones y la actividad reciente"><figcaption><p>El Workflow Dashboard: totales de ejecuciones, tasas de éxito/fallo y actividad reciente de cada flujo de trabajo.</p></figcaption></figure>

## Pestañas

- **Dashboard**: métricas de ejecución y actividad reciente (se muestra arriba).
- **Workflow List**: todos los flujos de trabajo con su tipo, orden de ejecución y disparador. Cree uno nuevo con **New Workflow**.
- **Test Manager List**: escenarios de prueba que validan sus flujos de trabajo; ejecútelos con **Run All Tests**.
- **License**: información de licencia de los flujos de trabajo.
- **Card SDK**: cree y suba tarjetas de flujo de trabajo personalizadas (consulte [Card SDK](card-sdk.md)).

La barra de herramientas también ofrece **Templates**, que abre la biblioteca de [Plantillas de flujo de trabajo](standard-workflow-builder.md#workflow-templates), e **Import Workflow**, que importa un flujo de trabajo desde un archivo JSON.

El **Test Manager** le permite guardar escenarios de prueba por flujo de trabajo y ejecutarlos juntos, de modo que pueda confirmar que sus flujos de trabajo siguen comportándose correctamente después de los cambios:

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Test Manager List de flujos de trabajo con escenarios de prueba y Run All Tests"><figcaption><p>La Test Manager List: cada escenario muestra un resultado de aprobado/fallido; use <strong>Run All Tests</strong> para volver a ejecutarlos todos.</p></figcaption></figure>

## Próximos pasos

- Cree una automatización lineal con el constructor **Standard Workflow**.
- Cree un flujo con ramificaciones con el constructor **Advanced Workflow**.
