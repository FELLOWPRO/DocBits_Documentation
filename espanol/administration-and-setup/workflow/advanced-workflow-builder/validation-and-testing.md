# Validación y pruebas

Mientras construyes un flujo de trabajo Avanzado, dos controles de la barra de herramientas te permiten comprobarlo sin salir del editor. Son para *comprobaciones rápidas durante la construcción*; para pruebas guardadas y repetibles, usa el [Test Manager](../test-manager.md).

## Validate

Haz clic en el control **Validate** (el icono de círculo con marca de verificación, o pulsa <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). La validación revisa el grafo en busca de problemas (nodos sin conectar, configuración faltante y conexiones no válidas) y los señala para que puedas corregirlos antes de que el flujo de trabajo se ejecute con documentos reales.

## Test

Haz clic en el control **Test** (el icono de reproducción, o pulsa <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) para ejecutar el flujo actual con una muestra y observar cómo se comporta, sin afectar a los documentos en producción. Esta es la forma más rápida de comprobar un cambio que acabas de hacer en el lienzo.

## Cuándo usar cada uno

- **Validate / Test en el editor** (esta página) — retroalimentación instantánea mientras diseñas el flujo.
- **[Test Manager](../test-manager.md)** — guarda el escenario para poder volver a ejecutarlo más tarde (y junto con todos tus demás escenarios) y detectar regresiones tras cambios futuros.

## Próximos pasos

- Repasa los tipos de nodos y conexiones en [Nodos](nodes.md).
- Consulta todos los controles de la barra de herramientas y el lienzo en [Barra de herramientas y lienzo](toolbar-and-canvas.md).
