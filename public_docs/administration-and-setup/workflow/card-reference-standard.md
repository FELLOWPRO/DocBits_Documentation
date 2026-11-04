---
description: "Configurar tarjetas mediante nombre, versión, entradas, alcance, resultados y efectos."
---

# Comprender y configurar tarjetas de workflow

Seleccione una tarjeta por su operación y alcance. **Field is** comprueba existencia o vacío; **Docfield is** compara valores. Asignación documental, tarea y notificación tienen efectos diferentes. Una categoría no sustituye la referencia de la versión concreta.

## Contenido de una referencia completa

| Componente | Pregunta necesaria |
| --- | --- |
| Identidad | ¿Nombre visible, tipo técnico, versión y función When/And/Then? |
| Requisitos | ¿Licencia, permisos y datos necesarios? |
| Entradas | ¿Tipo, valor, valor predeterminado y opciones permitidas por parámetro? |
| Alcance | ¿Campo, fila, todas las posiciones o variable de organización? |
| Resultados | ¿Éxito, falso o error? ¿Qué consume la siguiente tarjeta? |
| Efectos | ¿Se modifican documentos, tareas o sistemas externos? ¿Qué se simula? |
| Ejemplos | ¿Qué configuración y entrada completas producen cada resultado? |
| Límites y versiones | ¿Qué ocurre sin datos, en el límite exacto o con versiones antiguas? |

## Ejemplo completo: Docfield is

**Tipo técnico:** `condition_docfield_operator_value` · **Versión:** 2 · **Función:** And. Requiere documento con layout definido y el campo que se comprobará.

| Entrada | Configuración |
| --- | --- |
| Field Name | `total_amount`, clave técnica, no etiqueta traducida |
| Operator | `gt` / Mayor que |
| Field Value | `1000`, sin símbolo monetario |

La tarjeta compara el campo del documento actual con el valor configurado. No cambia estados, crea tareas ni exporta. En Advanced, verdadero sigue Success, falso sigue Failed Condition y un fallo de evaluación sigue Error. En Standard, una condición incumplida detiene la secuencia lineal.

Casos realmente comprobados: **1785** → Success; **999** y **1000** → Failed Condition; **1000,01** → Success; número ausente o inválido → Error. JSON utiliza punto decimal. Son resultados de esta configuración numérica, no de todos los tipos y operadores.

Distinga esta tarjeta de las tarjetas explícitas de tolerancia. No deduzca igualdad ni operadores inclusivos solo de `gt`; pruebe cada combinación necesaria con sus propios límites.

## Pasos siguientes

Conecte éxito a revisión, falso a ruta estándar y error a corrección de datos. El [caso completo](advanced-workflow-case-study.md) incluye configuración, tarjetas posteriores y resultados reales. El [modelo de ejecución](workflow-execution-model.md) explica guardado y activación; el [diagnóstico](workflow-troubleshooting.md) ayuda a investigar resultados diferentes.

## WF-05: Ejercicio y aceptación

Describa Run Workflow y una tarjeta PO con la misma estructura: parámetros, valores predeterminados revisados, rutas, efectos y versiones. Compruebe destino inactivo, datos ausentes y base porcentual.

[Ruta de aprendizaje](workflow-learning-path.md)
