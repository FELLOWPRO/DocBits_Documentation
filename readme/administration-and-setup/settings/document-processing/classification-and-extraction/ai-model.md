# Modelo de IA

## Descripción general

La configuración del **Modelo de IA** te permite definir qué modelo de IA se utiliza de forma predeterminada para la **extracción de campo** y la **extracción de tabla** durante el procesamiento de documentos.\
En esta sección, puedes revisar el costo de tokens para cada modelo y ver qué modelo está actualmente asignado a cada proveedor.

## Cómo acceder

1.  Navega a **Configuración** → **Procesamiento de documentos** → **Clasificación y extracción**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)
2.  Desplázate hacia abajo hasta la sección de **Extracción de tabla**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_1.png)

## Opciones del Modelo de IA

DocBits ofrece tres opciones de modelo de IA para la extracción de campos y tablas. Se diferencian en el equilibrio entre **precisión de extracción**, **velocidad de procesamiento** y **costo de tokens por documento** — así puedes ajustar la opción al tipo de documentos que procesas. Pasa el cursor sobre el icono de información junto al ajuste para ver el costo de tokens de la opción seleccionada actualmente.

* **Full** – La opción más exhaustiva, con la mayor precisión de extracción. Ideal para diseños complejos, escaneos de baja calidad o documentos en los que la precisión es lo más importante. Al ser la opción más potente, también es la más lenta, con **2 tokens por documento**.
* **Fast** – Una opción equilibrada que combina alta precisión con un procesamiento más rápido y un costo menor. Es la opción predeterminada recomendada para la mayoría de los documentos habituales, con **1 token por documento**.
* **Turbo** – La opción más rápida y económica. Más adecuada para grandes volúmenes de documentos sencillos, limpios y bien estructurados, donde la velocidad y el bajo costo importan más que la máxima precisión, con **1 token por documento**.

| Opción | Ideal para | Precisión | Velocidad | Costo de tokens |
|--------|-----------|-----------|-----------|-----------------|
| **Full** | Diseños complejos, escaneos deficientes, alta precisión | Máxima | La más lenta | 2 / documento |
| **Fast** | Documentos habituales (predeterminado recomendado) | Alta | Rápida | 1 / documento |
| **Turbo** | Grandes volúmenes de documentos sencillos y limpios | Buena | La más rápida | 1 / documento |

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_2.png)

## Tabla de Asignación del Modelo de IA

También puedes configurar **modelos de IA** específicos por proveedor directamente en la pantalla de **Validación**, lo que te permite ajustar la precisión de extracción para proveedores individuales.\
\
Para más información, consulta la documentación correspondiente [aquí](../../../../end-user-and-partner-section/end-user-section/validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

La tabla de asignación muestra la configuración del modelo de IA para cada proveedor e incluye los siguientes detalles:

* **Supplier ID** – El identificador único del proveedor
* **AI Model** – El modelo de IA actualmente asignado al proveedor
* **E-Text**: Indica si la función E-Text está habilitada
* **Action** – Contiene la opción para eliminar la entrada

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_3.png)

### Eliminar entrada – Restablecer configuración específica del proveedor

Para restablecer la configuración del modelo de IA de un proveedor al valor predeterminado:

1.  Haz clic en el icono de la papelera en la columna **Action** junto a la entrada del proveedor.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_4.png)
2.  Aparecerá un cuadro de diálogo de confirmación—confirma que deseas eliminar la entrada.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_5.png)

Una vez eliminada, el proveedor volverá a utilizar el **modelo de IA** predeterminado para la **extracción de campo** y la **extracción de tabla**.
