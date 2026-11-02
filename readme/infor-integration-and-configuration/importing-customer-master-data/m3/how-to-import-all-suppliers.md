# Cómo importar todos los proveedores

* [ ] Inicia sesión en el entorno de Infor OS y ve a la aplicación M3. Recomendación: Asegúrate de tener derechos de administrador para poder ejecutar todos los programas.

![Menú de inicio de Infor M3 en Infor OS con la lista de programas, los paneles Favorites y Recent y el campo de búsqueda evs006 abierto](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png)

* [ ] Ejecuta el programa _**evs006**_. Presiona command + R y verás la pestaña abierta para buscar e iniciar.

![Menú de inicio de Infor M3 con el campo de búsqueda mostrando evs006 Initial Load listo para abrir en Recent](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png)

* [ ] Cuando _**evs006**_ esté abierto verás una tabla vacía. Por favor, rellena las columnas “BOD noun” y “Table”. Para “BOD noun” introduce “SupplierPartyMaster” y para “Table” vamos a usar la tabla de proveedores de M3 llamada “CIDMAS”.

![Pantalla de menú de Infor M3 con el campo de búsqueda abierto para iniciar un programa](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png)

![Tabla EVS006 Initial Load con las columnas BOD noun, BOD variant, Table y BOD description](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png)

* [ ] Cuando hayas rellenado estas columnas, simplemente haz clic en el botón CREATE (en la parte superior de la pantalla). Llegarás a la siguiente pantalla.

![Tabla vacía EVS006 Initial Load con los encabezados de columna BOD noun, BOD variant, Table y BOD description](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png)

![Panel EVS006 Initial Load con Table CIDMAS Supplier, BOD noun SupplierPartyMaster y las secciones Details y Table keys](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png)

* [ ] Rellena el “BOD Description” con SupplierPartyMaster.

![Panel EVS006 Initial Load con la descripción BOD SupplierPartyMaster rellenada en Details](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png)

* [ ] Haz clic en Next. (En la parte inferior izquierda de la pantalla).

![Panel EVS006 Initial Load para la tabla CIDMAS con el sustantivo BOD SupplierPartyMaster y el botón Next en la parte inferior izquierda](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png)

* [ ] Haz clic en Next en esta ventana.

![Diálogo Text en M3 con las columnas Text block y Language y el nombre InvExt](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png)

* [ ] Ahora, cuando veas esta pantalla con la tabla rellenada con el BOD SupplierPartyMaster, haz clic derecho sobre el BOD y elige Related > Run.

![Tabla EVS006 Initial Load con la fila SupplierPartyMaster y su menú contextual de clic derecho que incluye Related, Run y Change](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png)

* [ ] En esta siguiente ventana selecciona “Sync” y Next.

![Panel BOD Processor Administration en Infor M3 con el trabajo SupplierPartyMaster, el verbo Sync y el estado Pending](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/8fbed442-7deb-4c1e-9295-5038fe124331.png)

Después de finalizar todos estos pasos, habrás activado el BOD para importar todos los proveedores desde la tabla CIDMAS. Después de algunos minutos deberías ver el proveedor en DocBits.
