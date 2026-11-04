---
description: "Descargar factura sintética, workflow JSON, entradas, expectativas y respuestas reales de prueba."
---

# Paquete de formación de workflows

Utilice este paquete con el [caso Advanced](advanced-workflow-case-study.md). Incluye una factura sintética, un workflow importable, siete entradas documentales completas, expectativas independientes y respuestas reales guardadas. Las claves técnicas y los nombres de ruta son idénticos en todos los idiomas.

{% file src="../../.gitbook/assets/workflow-training-kit-v2.zip" %}
Paquete de formación con ejemplos y resultados
{% endfile %}

## Contenido y formatos

| Archivo | Uso |
| --- | --- |
| `training-invoice.pdf` | Factura sintética: 1500 EUR netos, 285 EUR de impuesto y 1785 EUR en total. No debe pagarse. |
| `advanced-workflow.json` | Importar mediante **Import Workflow**, desactivado; sin variable global, limitado a Factura y al número exacto de formación. |
| `*-input.json` | Datos completos para **Advanced Test → Custom Data**. |
| `expectations.json` | Rutas, mensajes de estado y resultados esperados; especificación funcional, no archivo de carga de Test Manager. |
| `*-result.json` | Respuestas reales de Dev con resultados y mensajes; referencias privadas de organización sustituidas. |
| `prepare_inputs.py` | Sustituye la organización sintética en las dos posiciones necesarias. |
| `verify_results.py` | Compara las respuestas con expectativas independientes. Requiere Python 3, sin clave de acceso. |

## Utilización

1. Descomprima el ZIP y lea las instrucciones incluidas.
2. Importe el workflow en su organización de prueba y compruebe que está desactivado.
3. Obtenga el ID de su organización de prueba y ejecute localmente:

```bash
python3 prepare_inputs.py --org-id YOUR_TEST_ORGANIZATION_UUID --out prepared
python3 verify_results.py
```

4. Utilice los archivos de `prepared/` en el diálogo Advanced. No sustituya una ID sintética de documento por la de una factura real de cliente.
5. Compruebe los siete casos con la [tabla de resultados](advanced-workflow-case-study.md). Las variaciones de importe son deliberadas; no modifican la factura adjunta.

Los datos incluyen `id`, `org_id`, `doc_type`, `status` y `extracted_data` con `layout.groups`, `fields` y `tables`. La organización superior y la de `extracted_data` deben coincidir con la cuenta conectada. Un valor sin definición de campo en el layout puede no leerse como campo documental existente.

## Alcance

Las expectativas comprueban rutas, texto, mensajes de estado y nodos finales, además del estado documental. No equivalen a la comparación de estado de un escenario de Test Manager.

Una prueba Advanced correcta confirma el procesamiento de los datos suministrados. Una acción simulada no es una asignación, correo o entrega real. La activación necesita la entrada de evento adecuada y una ejecución real verificada aparte. Consulte [Cuándo se ejecuta mi workflow](workflow-execution-model.md).

## WF-03: Ejercicio y aceptación

Extraiga v2, adapte organización con prepare_inputs.py y ejecute verify_results.py. decision-table-setup.json es una guía y acceptance-record-template.json una plantilla de registro; ninguno importa workflows. Confirme el estado inactivo antes de importar.

[Ruta de aprendizaje](workflow-learning-path.md)
