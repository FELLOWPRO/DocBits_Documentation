# M3

## Paso 1: Crear un punto de conexión

1. Navegue a **OS > ION > Conectar > Puntos de Conexión**
2. Haga clic en **Add** y seleccione **IMS via API Gateway** como tipo de conexión.
3. Configure los siguientes ajustes:
   * **Name**: Establezca en `DocBits_Export`.
   * **Description**: Establezca en `DocBits_Export`.
   * **Desmarque**: _La aplicación tiene IMS Punto final_.
   * **ION API Client ID**:
     * Abra el archivo ION API.
     * Busque `"ci"` dentro del archivo.
     * Copie el valor dentro de las comillas (sin las comillas).

![Diálogo Infor Application Connection Point IMS via API Gateway con las pestañas Usage, Connection y Documents, el nombre DocBits_Export, la opción Application has IMS End Point desmarcada, el campo ION API Client ID y el Logical ID inforims.docbits_export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_1.png)

4. En **Documents**, agregue `Sync.CaptureDocument`.

![Pestaña Connection del punto de aplicación con el nombre DocBits_Export, el documento sync.captureDocument como Send from Application y el Logical ID inforims.docbits_export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_2.png)

5. Haga clic en **Save** para finalizar la configuración.

## Paso 2: Cargar Mappings

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. Descargue el archivo M3 Mapping.
2. Navegue a **Infor** > **OS** > **ION** > **Connect** > **Mappings**.
3. Haga clic en **Import** y seleccione el archivo de mapping apropiado para **M3**.

![Página Mappings de ION Desk con el campo de búsqueda, los controles de filtro y el botón Add](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_3.png)

4. Una vez importados los archivos, apruebe los mappings para activarlos.

![Asignación importada con el origen Sync.CaptureDocument y el destino Process.SupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_4.png)

## Paso 3: Crear el Data Flow

1. Navegue a **OS** -> **ION** -> **Connect** -> **Data Flows**.
2. Haga clic en **Add** y seleccione **Document Flow**.
3. Complete los detalles:
   * **Name**: `DocBits_Export_to_M3`
4. Agregue nodos al flujo:

#### Nodo de aplicación

1. Agregue un **Application Node** al flujo.
   * **Name**: `DocBits` o `DocBits-Export`.
2. Haga clic en **Add** y seleccione el **Connection Point** creado en el Paso 1.

![Flujo de datos en ION Desk con la paleta de nodos arriba y el panel Application Activity Properties a la derecha con el nombre DocBits-Dev-Demo-Export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_5.png)

3. Haga clic en el **Document Icon** junto al Application Node.
   * Haga clic en **Add** y seleccione `Sync.CaptureDocument`.

![Flujo de datos en ION Desk con el nodo de aplicación seleccionado y el panel Documents abierto con la entrada Sync.CaptureDocument](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_6.png)

#### Nodo de asignación

1. Agregue un **Mapping Node** a la derecha del Application Node.
   * **Name**: `Capt2process`.
   * **Mapping**: `CaptureDocument_to_ProcessSupplierInvoice`.

![Flujo de datos en ION Desk con el nodo de asignación seleccionado y el panel Mapping Properties a la derecha con el nombre y la asignación SyncCaptDoc_SyncSuppInv](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_7.png)

#### Nodo de aplicación

1. Agregue un **Application Node** a la derecha del Mapping Node anterior.
   * **Name**: `M3`.
2. Haga clic en **Add** y seleccione la **M3 Application** del cliente.

![Flujo de datos en ION Desk con el nodo de aplicación M3 seleccionado y el panel Application Activity Properties a la derecha con la entrada M3 BODs](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_8.png)

3. Haga clic en el **Document Icon** junto al Application Node.
   * Haga clic en **Add** y seleccione `Acknowledge.SupplierInvoice`.

![Flujo de datos en ION Desk con el nodo de aplicación M3 seleccionado y el panel Documents abierto con la entrada Acknowledge.SupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_9.png)

#### Nodo de API

1. Agregue un **API Node** a la derecha del Application Node.
   * **Name**: `DocBits-Error`.
   * **ION API Connector**: `DocBits_Import`.
   * Si `DocBits_Import` no existe, consulte el **Paso 1** y el **Paso 2** de la documentación Import from M3 para crear el Connection Point.

![Flujo de datos en ION Desk con el nodo API seleccionado y el panel ION API Activity Properties a la derecha con el ION API Connector DocBits Dev Demo-Import](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_10.png)

#### Guardar y activar el Flow

* Una vez que todos los nodos estén agregados y configurados, haga clic en **Save**.
* Active el flujo para completar la configuración.

![Flujo de datos en ION Desk con los nodos DocBits_Demo_to_M3, el nodo de asignación, el nodo M3 y el nodo de error conectados en fila y el botón REMOVE CONNECTION POINTS sobre el lienzo](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_11%20\(1\).png)

## Paso 4: Configurar Export en DocBits

### Instalación local:

1. Abra **DocBits**.
2.  Navegue a **Configuración > Procesamiento de documentos > Exportar**.

    ![Página de ajustes de DocBits con el grupo de navegación Document Processing desplegado y las entradas Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values y Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Cree una nueva exportación:
   * **Seleccionar**: **Infor IDM + ION BOD**.
   * **Título**: Elija un título significativo.
   * **Tipo de documento**: Establezca en **Factura**.
   * **Suborganización**: Puede dejarse vacío o establecerse en una suborganización específica si es necesario.
4. **Cargue los archivos requeridos**:
   * **ION Mapping File**: Puede encontrarlo en **Infor OS → API Gateway → Authorized Apps**. Busque la aplicación **DocBits**, ábrala y descargue las credenciales.
   * **IDM Mapping File**: (Proporcione la ruta del archivo relevante o ubicación).
   * **BOD Mapping File**: (Proporcione la ruta del archivo relevante o ubicación).

### Nube:

1. Abra **DocBits**.
2.  Navegue a **Configuración > Procesamiento de documentos > Exportar**.

    ![Página de ajustes de DocBits con el grupo de navegación Document Processing desplegado y las entradas Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values y Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Cree una nueva exportación:
   * **Seleccionar**: **Infor IDM + M3 (API)**.
   * **Título**: Elija un título significativo.
   * **Tipo de documento**: Establezca en **Factura**.
   * **Suborganización**: Puede dejarse vacío o establecerse en una suborganización específica si es necesario.
4. **Cargue los archivos requeridos**:
   * **ION Mapping File**: Puede encontrarlo en **Infor OS → API Gateway → Authorized Apps**. Busque la aplicación **DocBits**, ábrala y descargue las credenciales.
   * **IDM Mapping File**: (Proporcione la ruta del archivo relevante o ubicación).
   * **M3 Mapping File**: (Proporcione la ruta del archivo relevante o ubicación).

### Cloud con toml:

1. Abra **DocBits**.
2.  Navegue a **Configuración > Procesamiento de documentos > Exportar**.

    ![Página de ajustes de DocBits con el grupo de navegación Document Processing desplegado y las entradas Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values y Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Cree una nueva exportación:
   * **Seleccionar**: **Infor IDM + M3 (API)**.
   * **Título**: Elija un título significativo.
   * **Tipo de documento**: Establezca en **Factura**.
   * **Suborganización**: Puede dejarse vacío o establecerse en una suborganización específica si es necesario.
4. **Cargue los archivos requeridos**:
   * **ION Mapping File**: Puede encontrarlo en **Infor OS → API Gateway → Authorized Apps**. Busque la aplicación **DocBits**, ábrala y descargue las credenciales.
   * **IDM Mapping File**: (Proporcione la ruta del archivo relevante o ubicación).
   * **M3 toml Mapping File**: (Proporcione la ruta del archivo relevante o ubicación).
