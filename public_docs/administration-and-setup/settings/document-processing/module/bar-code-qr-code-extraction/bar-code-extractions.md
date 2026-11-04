# Extracción de códigos de barras

## Descripción general

Esta función permite la detección automática de códigos de barras en los documentos. Cuando está activada, todos los tipos de código de barras admitidos se escanean y se extraen durante el procesamiento.

## Cómo activar la extracción de códigos de barras

Para activar la función Bar-Code Extraction, siga estos pasos:

1. **Vaya a Settings**:
   * Desde el Dashboard, vaya a **Settings**.
   * Seleccione **Document Processing** y, a continuación, elija **Module**.
2. **Active la función**:
   * Desplácese hacia abajo para localizar la opción **Bar-Code Extraction**.
   * Mueva el control deslizante para activar Bar-Code Extraction.\\

## **Ajustes adicionales**

### **Asignación de códigos de barras**

#### **Finalidad:** permite a los validadores asignar manualmente un valor de código de barras extraído a un campo concreto del documento durante la validación de campos.

#### Cómo activar **Barcode Assignment**

Para activar la función **Barcode Assignment**, siga estos pasos:

1. **Vaya a Settings**:
   * Desde el Dashboard, vaya a **Settings**.
   * Seleccione **Document Processing** y, a continuación, elija **Module**.
2. **Active la función**:
   * Desplácese hacia abajo para localizar la opción **Barcode Assignment**.
   * Mueva el control deslizante para activar **Barcode Assignment**.\\

#### **Cómo funciona:**

* Habilita una opción “Assign Barcode” en la pantalla de validación de campos.\\
* Los usuarios pueden seleccionar un valor de código de barras detectado y asignarlo a un campo del documento, como PO Number o Invoice Number.\\

### División del documento por código de barras o código QR

**Finalidad:** divide automáticamente los documentos de varias páginas en documentos independientes según la presencia de determinados códigos de barras o códigos QR.

#### Cómo activar Split of Document by Barcode / QR Code

Para activar la función **Split of Document by Barcode / QR Code**, siga estos pasos:

1. **Vaya a Settings**:
   * Desde el Dashboard, vaya a **Settings**.
   * Seleccione **Document Processing** y, a continuación, elija **Classification and Extraction**.
2. **Active la función**:
   * Localice la opción **Document Splitting**.
   * En **Split**, seleccione **Split by Barcode / QR Code**.
   * En **Barcode Type**, elija uno o varios tipos de código de barras admitidos de la lista.
   * En **Barcode Pattern**, defina el patrón que debe provocar una división. Puede utilizar una **expresión regular** (regex) para detectar valores dinámicos de códigos de barras.

**Cómo funciona:**

* Usted selecciona los tipos de código de barras que deben provocar una división.
* Usted define un patrón que debe cumplir el código de barras; puede ser una cadena fija o una expresión regular (por ejemplo, `^INV\d{6}$` para detectar códigos de barras como `INV123456`).
* Durante el procesamiento del documento, cada vez que una página contiene un código de barras coincidente, se **crea un nuevo documento** a partir de esa página.

### Tipos de código admitidos

Consulte la [página de descripción general](./) para ver la lista completa de formatos de código de barras y códigos QR admitidos.
