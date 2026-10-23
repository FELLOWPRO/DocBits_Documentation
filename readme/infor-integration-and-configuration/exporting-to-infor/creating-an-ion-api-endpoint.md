# Crear un punto de conexión de ION API

## Configuración de Infor

Una vez en la pantalla de inicio, haga clic en el menú de hamburguesas y seleccione ION API

![Pantalla Available APIs de Infor ION API a la que se llega desde el menú de hamburguesa](https://lh7-us.googleusercontent.com/hSxKZMRZUv5SJc2tMxgD2aMcaAVPkmTJMEdIjPY4JoM3BWiN9BUCQSywdCNJUs54R4Df8Z6Im3Zy2TRfRQE\_bK-FU5R9DbRDF3\_drGNPPbHEYCXJzD3Go5pAbIX6mohTMDchY3q7jK6hRheoreVuT-g)

Después de abrir ION API, haga clic en API disponibles en el menú de la izquierda

![Pantalla de inicio de Infor ION API con las entradas de menú Authorized Apps, Configuration, API Metadata, Monitoring y Authorizations](https://lh7-us.googleusercontent.com/Ed2FRY1deP-21i-45Q3dUBdDrPOsnKnl6BzMq65FbUDk4kIW9jQClwWVFbuvPvR\_HGpNDOFHvXsy0RnJ\_KE1cLfgrDSoMg1\_\_Q1W0\_3bZs5sg35cCN2w4Fbc9oAy\_uH9VHwkg\_irA6AQ\_wU0q\_G4QRQ)

Click on “+ADD” block

![Pantalla Available APIs de ION API con mosaicos de suite como Push Notification y Auditing and Monitoring además del bloque Add](https://lh7-us.googleusercontent.com/GdMApy9dnygxJwFTfYJ\_LDWOE9sOgeDdNkzhzHsxqpv-JUBYnPtB18U7nwLfnGXzyJs448gpztGdLNAKIC4jYmtc56wCbKRNqXsw5e-4ITNS5aeBJ30kAOVJzvPmu-idiSu-aEKKYvr4KblwBqs55nE)

Then “+ Create New”

![Pantalla Available APIs con el botón Create New y una lista de plantillas de suite de API como Automotive Exchange y Infor CPQ](https://lh7-us.googleusercontent.com/\_MPsEXD4q7PsiAVXXbyfadZmwndAs8l3tEfPq97IqoRgk0QWdOeDV-rZwtWyhY3tUQ0uqhj1Wrr4xqDIHetzyOAnC0zAEy9j3D2uT3VJ8fJaik4HXII7Q70SdAJAVeHatuKYSlEttHCCmfa60VOgdWU)

La información que insertes debería verse así

![Formulario Add New API Suite con DocBits como Application Name además de los campos API Context, Suite Name, Suite Icon y Description](https://lh7-us.googleusercontent.com/gwvBDFrrA-vOihzWxa\_Ns1wMbXJKzz0Qds1vyJwc3cc1QrUAd3udV5oF7iW1riwS4fYgv7-fOAdxQvATtkPZ-HHbjOnmRv4QiUpAMUyXU0XlUBisMlOQPDiKH5guSw7T\_PxSmQTghiusyrv2-btGKDU)

FYI: La descripción tiene múltiples entornos ya que esta se usará para múltiples entornos y el ícono y su color siempre permanecen iguales.

A continuación, seleccione el + en la parte inferior de la pantalla.

![Formulario de endpoint de ION API con los campos Target Endpoint, Proxy Endpoint y Description rellenados](https://lh7-us.googleusercontent.com/dtYP0O6Abzd-9yDgqtLMJh\_4p1GNGqqtJMCySJEzw-3-hcvySwdXoznQBQ-6fkCGCHVrKXRFSint8\_HuL6BpjRizZ-zIpornm7F-JH\_jU48OQ1s1kPCQyV-9mKkQkPh1ge8xbINKuV0ps7gvKuddqDs)

Este punto final de destino URL se puede encontrar en doc2api.cloudintegration.eu

![Formulario de ION API que muestra el campo obligatorio Target Endpoint URL con un marcador de posición de dominio de ejemplo](https://lh7-us.googleusercontent.com/-olPQPbkiOSYtKh6JeDtVGDypj5xfS1vsb78vLAFDE3hETqHvzDC4VjiAwR0F3Le0seqxicUDNhXjOoOGrXgCe-cByPrp\_q-bg-nKG2Y1JngREWyekzdQ5Cbnxi0aWv\_VySw0LdcwpAElcXG\_b5Vmlo)

La información debajo de este campo debería verse de la siguiente manera.

![Configuración del endpoint de ION API con URL de doc2api de sandbox, Enterprise Connector, Proxy Context y Proxy Security anónima](https://lh7-us.googleusercontent.com/DKI7Ewpn6\_3euuarVLThq6Hdatfje8i44dhUCjWUtWcA0Dq38s8Idm3DbjE0HkAv3hGmYrdgUtuRF-skv6-d\_QghuHsFR8C3Vcf72IR8diP30ixrgd0YU7oEb6DWInIqK9ccH\_X-7VotPo5sCO379NA)

Una vez que hayas completado esta información, a la derecha de estos campos hay un campo “Target Endpoint Security” con un menú desplegable. Seleccione la clave de API en este menú desplegable.

![Desplegable Target Endpoint Security con opciones de Authentication Type como Anonymous, API Key, AWS Signature, Basic y JWT](https://lh7-us.googleusercontent.com/57rltIU4KnHAZ6wskQQHmn094UpRblxP\_-3Q14tVhKRT2M5uUdC4CuNINZqvy2NLjnwqDeWLIN6yr1ByNYHbV3SG1nH\_cf6zB-53I5k\_2zBeIjjQAR6BfGJBmDbh6uit5vYm0M8pGuLg0KFLXru\_N84)

Luego aparecerá una tabla debajo de este menú desplegable, complete la siguiente información. El valor clave es específico del cliente y del entorno y se puede encontrar en DocBits.

Desde el Panel → Configuración → Integración → Clave API

![Menú de configuración de DocBits con entradas de Global Settings como Company information, Groups Users and Permissions, Integration y Document Types](https://lh7-us.googleusercontent.com/SPs6Mw9-MeDAyXBgv5CK-CbKY-rEngzHVX9ruq3CcJnSuaqq76ibxuF-gbYS8VC2mv5TjsF48DLP8q2X2seN3J5voo7FP4dWipKVglWRHnWWQ3gtoBkCY6jrpUkQ1iLQ8huoWqku70LVZkcjUykp-w8)

![Configuración de DocBits en Integration que muestra la página de API key donde se encuentra el valor de la clave](https://lh7-us.googleusercontent.com/W4-UD6i9ux7l2k8lG77daDMikVm-77npHw4EOQkrwagAjOBXqrJYeJ-5mn3UQzddPCWUDTcmoihVvLqK4uf8bKT-kQ4gWAAV7HdwxllwiqqbIi0fReynpvkhK78mlfJQLQxI\_csynJx0-rWI22G8Lgk)

Copie y pegue esto en el campo Valor clave en InforOS

![Vista de API key de DocBits con parámetros personalizados que muestra el encabezado X-APL-KEY y su valor](https://lh7-us.googleusercontent.com/h\_wrZaNW70Vs3MkPOZMZk3lbfccMoJmcc6Q6ig8GeQcXY9owjyoydn4nSm-MZssXvPhDvE\_-TXr-mH73NNME28teQ1g0GsQMrWJvNFjBxJfRLWnl\_MET\_uHhFVL4ZRVdZiIaGbVsvx6esNjW8ot15n4)

Una vez completado esto, presione el siguiente icono para guardar la configuración

![Pantalla Add New API Suite de InforOS donde el valor de la clave copiado se pega en el campo de valor](https://lh7-us.googleusercontent.com/LxVzlEIhwd\_jf8VZlzOGuryjln03ZrojS2JSqdkMb-VYhp95NrRKUnNmTnm-n\_bY55W2cf4qH5Rdx2EsEKy\_NxjT8OpxISa2mXXVj1CQ22lSE0Tqt5iTWkiWXtda7TozXa3opnM5VT0i5VpN8rWaEcw)

Aún no has terminado completamente con la configuración.

Vuelva al API que acaba de configurar e ingrese los detalles como se muestra a continuación

![Icono Save utilizado para guardar la configuración del endpoint de ION API tras completar el formulario](https://lh7-us.googleusercontent.com/Tdqv5O2A-bKF7yD3JQCZkk64y1G7HEjesdUgndHv9seGDY8CCnG36T2kPy-hJqR758\_u1JSI\_LTXTkNI82H0Zlik7sKf3gByElMQGbk4bVgM2oM6lnNzJ\_gcj-57chiavEC4wHo58vorxmOHOl2sBBI)

Vaya a la pestaña Documentación en la parte inferior y haga clic en +

![Vista detallada del endpoint de ION API configurado con la pestaña Documentation en la parte inferior](https://lh7-us.googleusercontent.com/37S1zWf-RyHvhvyI-Gi9ud2FkLwASyGD\_IzskDjsKjyEQdIBc97Bfgqptg6-TLV3-mtM9yAzjmIRV5m9rAC2EW4WqVia\_lfTsvBIGo8uXx1EvgCp0m8DeYQQfPh2zSA8I6cRySfEircpl6IZG9h6xiY)

Enter the following details:

* Name = DocBits-”environment”
* Type = Swagger
* URL = vaya a doc2api.cloudintegration.eu, una vez en esta página, abra el siguiente enlace

![Pestaña Documentation de la ION API configurada que muestra la entrada DOC2 API después de hacer clic en el signo más](https://lh7-us.googleusercontent.com/tazrpqtgWhLRr5O08CVo\_gUjK1EuN\_vvRGTWnw89euSYQrQWd4Jnxx-1mdaydY56\_I2otnGdg6\_3dOJhBFp3OU8i9rIlXV5-1ApKYRRPqxVhBviUQ\_VhlQAWfAKe18NMtYBFXd3QVo5i6Za7315dqqQ)

Copie el URL y úselo para el campo URL en InforOS

Guárdelo una vez que haya ingresado la información de todos los campos. Debería haber un ícono de carga por un tiempo, pero el resultado final debería verse así

![Página de documentación de doc2api con las pestañas Resources, Documentation y Endpoint Policies que enumera los endpoints correspondientes de doc2light](https://lh7-us.googleusercontent.com/odK5Oc3n8iLl45pG6Dgb1CmWFE30suuqVq5KfWP7FoqthPT93WApITIpMU6m4nndaQgnQbz3afneBYBzUrZc\_aTfyk-HUKKv6F3v5wmEvqYZ0TWYnE8\_3K-P7Gf7u5Fk7JPzbT-HUduMoecSsuoceKM)

El mismo proceso se utilizaría para crear los puntos finales para otros entornos.

FYI: Si en el futuro tiene dificultades para encontrar estos puntos finales, en ION API vaya a Metadatos de API y haga clic en este icono para actualizar los metadatos API.

![Página ION API Metadata que describe información sobre suites, productos y las operaciones dentro de ellos](https://lh7-us.googleusercontent.com/XCcuAbf4igf7O6oXECgt-\_veEcrrC065xeHHzNWKUjFZfEi-hUJLqYkRIn2PhmBtmS3UA1\_Wpf0YdCNWBPKlyDrtWgOHRKM03Xbtlucfpmg9ulB3guwj-kgzbZFnKN5i1AMq1Kd5m-ak-ljaz1e9V5g)

## Configuración de exportación de DocBits

Desde el Panel DocBits del cliente requerido, vaya a Configuración → Exportar, para agregar un nuevo tipo de documento para exportar, haga lo siguiente:

Haga clic en el botón “+ New”

![Icono de actualización de ION API Metadata utilizado para actualizar los metadatos de la API](https://lh7-us.googleusercontent.com/zT9L2Re22S5SdupyS-VVagJhk8sp38tVs-euioezvF-QzKxkr6R0wXz3sH3MK3dFvH1ZkdqmTlQg3z81P5duItUW8tnd\_Pdt3J4VezzMT6Rgk\_KEjvK4gzp1vjj6xzEaDiB5VvnFhUHW6bxNJg478\_8)

Select “Infor IDM + ION BOD”

![Cuadro de diálogo Select Integration que ofrece Webhook, Infor ION, Infor IDM + ION BOD, Flow y ZUGFeRD](https://lh7-us.googleusercontent.com/6d04sh2VraR1919XKZSFnFr9QHf8YfpxTwLE-yXVEPtmejYPLcKO2CMekMXnzXDyOwh6Ml25BLCbVF9g7cv1I-jGrv3vUGugHEoxrl-BbBPnTL3nuCcN3ZNlYDuy0mXSNbH0AP-w-zTfKgcUCgQeIpE)

Luego será llevado a este menú donde deberá asignar un título al nuevo tipo de documento exportable, seleccionar el tipo de documento en el menú desplegable y agregar todos los archivos de mapeo necesarios (ION, IDM y BOD).

![Formulario para exportar un tipo de documento con Title, Sub-Organizations, Document Type además de los archivos de mapeo ION, IDM y BOD](https://lh7-us.googleusercontent.com/jlFJZHMeLSFSG3I-lN5tuThqieT1uCcfe\_Rj7rEQ2t9bnkbdUuyOhb9JhMBl50dn6seDmoFohtSHLU1TM9jkpPM8U7ZWpeGbD4SUFv7a0m7snpsPy33rVwus0Aub\_qXnNW3EG0IvARSzYhw7Hj6sLqY)
