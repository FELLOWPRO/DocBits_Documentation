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

![Página Infor Application Connection Point para IMS vía API Gateway con nombre DocBits_Export, descripción y campos de ION API Client ID](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_1.png)

4. En **Documents**, agregue `Sync.CaptureDocument`.

![Página Connection Point DocBits_Export con la sección Documents que enumera Sync.CaptureDocument establecido en Send from Application](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_2.png)

5. Haga clic en **Save** para finalizar la configuración.

## Paso 2: Cargar Mappings

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. Descargue el archivo M3 Mapping.
2. Navegue a **Infor** > **OS** > **ION** > **Connect** > **Mappings**.
3. Haga clic en **Import** y seleccione el archivo de mapping apropiado para **M3**.

![Botón de añadir en la barra de herramientas de la página Mappings de Infor ION Connect](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_3.png)

4. Una vez importados los archivos, apruebe los mappings para activarlos.

![Vista general de mapeos en ION Connect que muestra el mapeo aprobado de Sync.CaptureDocument a ProcessSupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_4.png)

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

![Editor de Data Flow con la paleta de nodos abierta y el panel Application Activity Properties que nombra el nodo DocBits-Dev-Demo-Export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_5.png)

3. Haga clic en el **Document Icon** junto al Application Node.
   * Haga clic en **Add** y seleccione `Sync.CaptureDocument`.

![Editor de Data Flow que muestra la lista Documents del nodo de aplicación con Sync.CaptureDocument añadido](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_6.png)

#### Nodo de asignación

1. Agregue un **Mapping Node** a la derecha del Application Node.
   * **Name**: `Capt2process`.
   * **Mapping**: `CaptureDocument_to_ProcessSupplierInvoice`.

![Editor de Data Flow con el panel Mapping Properties que muestra el nombre y el mapeo seleccionado para el nodo](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_7.png)

#### Nodo de aplicación

1. Agregue un **Application Node** a la derecha del Mapping Node anterior.
   * **Name**: `M3`.
2. Haga clic en **Add** y seleccione la **M3 Application** del cliente.

![Editor de Data Flow con el panel Application Activity Properties que muestra el nodo de aplicación M3 llamado M3 BODs](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_8.png)

3. Haga clic en el **Document Icon** junto al Application Node.
   * Haga clic en **Add** y seleccione `Acknowledge.SupplierInvoice`.

![Editor de Data Flow que muestra la lista Documents del nodo de aplicación M3 con Acknowledge.SupplierInvoice añadido](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_9.png)

#### Nodo de API

1. Agregue un **API Node** a la derecha del Application Node.
   * **Name**: `DocBits-Error`.
   * **ION API Connector**: `DocBits_Import`.
   * Si `DocBits_Import` no existe, consulte el **Paso 1** y el **Paso 2** de la documentación Import from M3 para crear el Connection Point.

![Editor de Data Flow con el panel ION API Activity Properties que nombra el conector DocBits-Dev-Demo-Import para el nodo de API](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_10.png)

#### Guardar y activar el Flow

* Una vez que todos los nodos estén agregados y configurados, haga clic en **Save**.
* Active el flujo para completar la configuración.

<figure><img src="../../../.gitbook/assets/m3-historical-ion-activation-example.png" alt="Ejemplo histórico de Infor ION en inglés: la flecha señala el icono de activación de un flujo de demostración. La imagen no acredita una exportación realizada."><figcaption><p>Ejemplo histórico de Infor ION en inglés: la flecha señala el icono de activación de un flujo de demostración. La imagen no acredita una exportación realizada.</p></figcaption></figure>

## Paso 4: Configurar Export en DocBits

### Instalación local:

1. Abra **DocBits**.
2.  Navegue a **Configuración > Procesamiento de documentos > Exportar**.

    ![Página de ajustes en DocBits con la navegación Document Processing abierta, que muestra Import, OCR Settings, Classification and Extraction y Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
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

    ![Página de ajustes en DocBits con la navegación Document Processing abierta, que muestra Import, OCR Settings, Classification and Extraction y Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
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

    ![Página de ajustes en DocBits con la navegación Document Processing abierta, que muestra Import, OCR Settings, Classification and Extraction y Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Cree una nueva exportación:
   * **Seleccionar**: **Infor IDM + M3 (API)**.
   * **Título**: Elija un título significativo.
   * **Tipo de documento**: Establezca en **Factura**.
   * **Suborganización**: Puede dejarse vacío o establecerse en una suborganización específica si es necesario.
4. **Cargue los archivos requeridos**:
   * **ION Mapping File**: Puede encontrarlo en **Infor OS → API Gateway → Authorized Apps**. Busque la aplicación **DocBits**, ábrala y descargue las credenciales.
   * **IDM Mapping File**: (Proporcione la ruta del archivo relevante o ubicación).
   * **M3 toml Mapping File**: (Proporcione la ruta del archivo relevante o ubicación).
