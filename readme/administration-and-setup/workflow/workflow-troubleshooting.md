---
description: "Diagnosticar workflows mediante eventos, datos de entrada, rutas elegidas y resultados reales."
---

# Diagnosticar problemas de workflow sistemáticamente

Empiece con una ejecución afectada. Anote organización y entorno, nombre y revisión guardada del workflow, documento, fecha y zona horaria y mensaje exacto del nodo. En respuestas de prueba utilice también `execution_id`. No incluya claves de acceso ni datos de clientes sin protección en pruebas compartidas.

## Del síntoma a la comprobación

| Síntoma | Evidencia | Corrección y nueva prueba |
| --- | --- | --- |
| No existe ejecución | Licencia, módulo, activación, filtros temporales y evento | Corrija entrada y filtros; repita el evento real. Start manual no lo demuestra. |
| Acción gris | Resultado del predecesor y salida conectada | Siga la ruta tomada. Un nodo omitido no ha fallado por sí mismo. |
| Condición naranja | Clave, tipo, valor y operador leídos | Distinga resultado negativo y error de evaluación. Pruebe por debajo, en y por encima del límite. |
| Nodo rojo | Primer error y datos requeridos | Corrija datos o configuración; repita el caso fallido y el positivo. |
| Wait ALL no continúa | Todas las fuentes y salidas conectadas | No exija simultáneamente rutas excluyentes. Demuestre una ruta posible por fuente necesaria. |
| Tareas o exportaciones duplicadas | Ejecuciones repetidas, eventos, cambios de estado y Run Workflow | Limite condiciones y transiciones; ejecute dos veces el mismo caso. Compruebe protección adecuada frente a concurrencia en el proceso receptor. |
| Variable afecta a otros workflows | Variable compartida de organización | Revise dependencias. Los cambios se guardan fuera del canvas; repita las pruebas afectadas. |
| Prueba correcta sin efecto visible | Qué se comparó o simuló | Verifique asignación en el documento, tarea en su área y recepción en destino. El estado solo no basta. |
| Exportación iniciada sin recepción | Historial, respuesta y datos del receptor | Diagnostique antes de repetir; compruebe si el receptor ya procesó la primera solicitud. |

## Interpretar los mensajes

En el [ejemplo Advanced](advanced-workflow-case-study.md), un importe ausente toma la salida roja. El tratamiento y la unión OR pueden tener éxito mientras el resultado global conserva el error original. Un importe normalmente falso toma naranja y puede terminar correctamente por la ruta estándar.

Dos conexiones de una fuente no son dos aprobaciones independientes. Las uniones evalúan resultados conectados de sus fuentes. Revise el flujo completo: una prueba parcial desde un nodo intermedio puede omitir predecesores necesarios.

## Demostrar la corrección

1. Conserve el hallazgo original y la expectativa funcional.
2. Cambie datos o configuración de forma concreta. Modifique expectativas solo si cambia el requisito.
3. Repita fallo, caso positivo y límites afectados con el [paquete](workflow-training-kit.md).
4. Guarde la regla y compruebe su activación por separado.
5. Compare una ejecución real nueva con la anterior. Los registros antiguos describen su revisión original.

Registre causa, corrección, resultado demostrado y limitaciones. Separe tiempo de espera y tiempo de ejecución: una duración total larga no identifica por sí sola un nodo lento.

## WF-04: Ejercicio y aceptación

Empiece con invalid-number. Guarde el primer error de amount y resultado error. Repita con above y compare nuevas pruebas. Conserve el registro antiguo; tratar correctamente el error no basta.

[Ruta de aprendizaje](workflow-learning-path.md)

## Repetir pruebas de tarjeta con alcance explícito

En el diseñador Dev revisado, repetir una prueba iniciada desde un nodo seleccionado cambió al grafo completo. Abra de nuevo la prueba del menú contextual de la tarjeta y compruebe los nodos realmente visitados. Un resultado de seis nodos no demuestra una prueba aislada de vacío. El contador de acciones fallidas puede incluir una condición incumplida: consulte también la salida elegida, el registro y el resultado global.
