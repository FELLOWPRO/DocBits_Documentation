# Faktura

## Mostrar atributo en cada partida

Si desea mostrar un atributo específico (como el número de Orden de Compra) en cada partida, siga los pasos a continuación. El enfoque variará dependiendo de si necesita el atributo en la extracción JSON o en la salida XSL.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.33.16.png" alt="Tabla de factura con las columnas Position, Description, Quantity y Unit Price que enumera líneas del pedido de compra con totales"><figcaption></figcaption></figure>

### Método 1: Mostrar Atributo en la Extracción JSON (configuración de DocBits)

1. Vaya a **Configuración**
2. Vaya a **Tipos de Documento**
3. Seleccione **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt="Página de configuración del tipo de documento Invoice con las pestañas Extraction type, Edit layout, Document Sub Types, Table columns, Fields y Model Training"><figcaption></figcaption></figure>

4. Abra la pestaña **"FATTURAPA"**
5. Haga clic en **JSON**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.01.13.png" alt="Lista de formatos FATTURAPA con las entradas Preview, Extraction Paths, variantes FacturX ZUGFERD, Peppol y XRECHNUNG con XSLT"><figcaption></figcaption></figure>

6. Para crear un borrador, haga clic en el icono del **lápiz**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt="Configuración del tipo de documento Invoice con la entrada del tipo de documento electrónico FATTURAPA y una marca de tiempo"><figcaption></figcaption></figure>

7. Dentro de la matriz `"tables"`, agregue la columna específica que desea mostrar proporcionando un nombre y una ruta:

```
{ 
"name": "PURCHASE_ORDER",    
"path":"path_to_source" 
}
```

**NOTA:** Los documentos electrónicos siempre tendrán el origen establecido en **Gran Bretaña**, por lo que los importes se guardarán en formato internacional, utilizando un **punto (.)** como separador decimal.

8. Guarde el borrador

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt="Entrada de versión Draft con la marca de tiempo 28.01.2025 15:10:12 en la vista de pruebas de DocBits"><figcaption></figcaption></figure>

9. Asegúrese de que su borrador sea el **activo**.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt="Entrada de la lista de versiones Draft con la versión 91.20 y una marca de tiempo que confirma el borrador activo"><figcaption></figcaption></figure>

### Método 2: Mostrar Atributo en la Salida XSL (vista previa HTML/PDF)

1. Vaya a **Configuración**
2. Vaya a **Tipos de Documento**
3. Seleccione **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt="Página de configuración del tipo de documento Invoice con las pestañas Extraction type, Edit layout, Document Sub Types, Table columns, Fields y Model Training"><figcaption></figcaption></figure>

4. Abra la pestaña **"FATTURAPA"**
5. **Haga clic en XLST**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.23.06.png" alt="Pestaña FATTURAPA que enumera formatos de documentos electrónicos, incluidos EDI, variantes FacturX ZUGFERD, Peppol y versiones XRECHNUNG"><figcaption></figcaption></figure>

6. Para crear un borrador, haga clic en el icono del **lápiz**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt="Configuración del tipo de documento Invoice con la entrada del tipo de documento electrónico FATTURAPA y una marca de tiempo"><figcaption></figcaption></figure>

7. En el bloque `<xsl:for-each select="path">` que genera las filas de la tabla, agregue un fragmento como este donde desee que aparezca el atributo (por ejemplo, en su propia columna):

```
<tr>
    <!-- Otras columnas ... -->

    <td>
        <!-- PO number -->
        <xsl:variable name="variable_name" select="value" />
        <xsl:value-of 
            select="path_to_attribute" 
        />
    </td>
</tr>
```

**NOTA:** Los documentos electrónicos siempre tendrán el origen establecido en **Gran Bretaña**, por lo que los importes se guardarán en formato internacional, utilizando un **punto (.)** como separador decimal.

8. Guarde el borrador

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt="Entrada de versión Draft con la marca de tiempo 28.01.2025 15:10:12 en la vista de pruebas de DocBits"><figcaption></figcaption></figure>

9. Asegúrese de que su borrador sea el **activo**.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt="Entrada de la lista de versiones Draft con la versión 91.20 y una marca de tiempo que confirma el borrador activo"><figcaption></figcaption></figure>
