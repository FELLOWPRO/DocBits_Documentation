# Contabilidad Automática

## **Requisitos previos**

* Flujo de datos de M3 a DocBits funcionando
* Entorno de DocBits configurado correctamente

## **Configuración de Infor**

En Infor, abre la aplicación ION Desk. En la pestaña izquierda, ve a Conectar → Puntos de conexión

&#x20;

![](https://lh7-us.googleusercontent.com/Gl49rTfnpYQjXjpUNF3SEouZiJ4pPeHVk60d7dyHizfPLT6sn4AoKVQPPvpgg2cD4ts40hDeWQRs3BqmKW-CAco7Dt0oWKF7ukQJUVDBgSUoMNHt\_gRkqLxkF5CC\_CNGpVRzrNs7rfF1msK320\_J02g)

Aquí es donde crearás el punto de conexión necesario para importar tus datos de M3 que se requieren para la Contabilidad Automática.

Haz clic en "+AGREGAR" para crear un nuevo punto de conexión, selecciona la opción de API como se muestra a continuación

![](https://lh7-us.googleusercontent.com/ctE76pck6mGmBVxRIMhHyn0TbSKKsiGjO7rO185fjndTIo7qYyvSZS3neUdV2CWPqBSangpJ4oG\_g946\_KyOwWyJvacZe5htWiQLTZQLzfNHvsHDhmMQmjh7MrGsqKp6sm-XPcGmEwrH2ZMYCd0bUl8)

Necesitarás configurar el punto de conexión de API llamado:

* PlanDeCuentas

### **PlanDeCuentas**

La pestaña de conexión para tu punto de conexión de PlanDeCuentas debería lucir similar a lo ilustrado a continuación. Dale al punto de conexión un nombre y descripción apropiados, e importa la Cuenta de Servicio que creaste.

![](https://lh7-us.googleusercontent.com/p-jly6\_S96TsCmpFg9oOob0h7Q7NBlTxRKgNCphiy5QfbK\_lrLMAR2miVUQh-fXrCfGdZr17ongp5c9bnK6HuHCVuDArHhYcmKDlAyO52tGcxg-VXBLXZ1ka8yqZ4DWnxFFMxUKkE7jgvCgr7P-nzdU)

![](https://lh7-us.googleusercontent.com/GkX20Q23htKae7OOcGnJ5J6f0L4I69vOU9jYBpY1m9bpDPdtsD584mh\_9IaZF37Ne1OY2uOPgFxYYjwTrBOoZqahpJLlY3n3qmBn0sgzC0eVu91wE0NWBvESBFJmeVTITQoqUTEU56tHEj47-P-nzdU)

Necesitarás agregar dos BODs en esta sección para este punto de conexión. Estos son Sync.PlanDeCuentas y Sync.DefinicionDeCodigo, para agregar estos BODs haz lo siguiente:

#### **Sync.PlanDeCuentas**

* Haz clic en el icono PLUS (+)

![](https://lh7-us.googleusercontent.com/hFWg7-4Osuy9Q0uZYqT9yfAPFYsBi7yitHj7BBxQ94vbsDVg-GuCeTBakvV2eQNjqMGwDAF90nO5h-OxFR8HtYEiYcALdBq5Fdj\_Gl-wU8QePGV4Wr3\_78OK22nUY35dfCQhUPQIp\_qkdHN0wr7V-VY)

* Selecciona "Enviar a API"

![](https://lh7-us.googleusercontent.com/jA97YupOjXJlRFRxduo\_tYO4YYDZoT0mHxWaPWfJGyU4RTNSVNRAIAsR5mzRyLh1iusHl0cBKUxhYj3hQMzacGdN2QGsvPGy1vHeq\_JNhDqxc-SI5HtZh\_Z\_zmaSjyJwmr2337tzYSWfqDl3JGkjBqY)

* Busca el BOD Sync.PlanDeCuentas

![](https://lh7-us.googleusercontent.com/hzuwy-VU8xpgQ85NGHAk9u-m-\_Sw4iffT0SNtWTJw9iWHRIsIvGTEYQgJYi7CUoYC7\_Yp2KDtsohRQkNtIgr1VutFbR8mTkT\_5HmJ7ecgW8pcGuZTuwxtPDOlJpWuONq3WPIupRRBxBJPlsYQ9w-bxo)

![](https://lh7-us.googleusercontent.com/6p8nXaRAI0ucRzmyKfYYg3J8MmHXVgHs-KxcItxeZ6wbefK1YdMrYSblHwnXkSiajApB5ds\_EgpJJWYjfbKOjHdsh-H49jG45weOX9v0YBSAqdXmKgoaBcP7A4zDyINMNVt7RWgbQ51WxNTsfBllvQ4)

* Cambia a la pestaña de API de ION, copia el nombre de la API y busca la Llamada de API presionando el botón SELECCIONAR

![](https://lh7-us.googleusercontent.com/aRXjuD3nkYsFNM2eYkfmHrshU3ycmN5G4OGSFFadbSToy3pHKYWMw6apbyMhJ9o-5xB6UDA4rbdPjZWAdP-OCH8gQFWV5vWXp0rqLxP9DozP4yMS074\_nsHzirJUgBfkBkQ8Ydp\_WjImf2bx3pDnLPE)

* En producto, selecciona el Punto de conexión de API que creaste para el entorno con el que estás trabajando, que creaste en API de ION. Busca la siguiente llamada de API, selecciónala y presiona OK.

![](https://lh7-us.googleusercontent.com/LQWk7uiEPCxJcohMmIuRrg2p\_wwE\_h5GoEEP3Y2IdpKARppHoGB4Rt1KRM\_2AiXyG0-ieIV7BM51IRN5exKkhG8eLTkKCftm88j2NLc15X50VLu9t1sZZnQ7DsIIvgUsxz7oryzVIkfmifw-m3qkLDY)

* A continuación, cambia a la pestaña Cuerpo de la Solicitud

![](https://lh7-us.googleusercontent.com/0tnYxKvtW5Fw7yJfW0QBMclidw5kKJB4oi6M932hGO8ROokbMXbyFcjPQq\_LSVe8hv3ZyVVWqjDO4vMMRgPm1L2iXV3pSoiyzrxGLvBTx4kwt5uo6XtHEt25PRVdM6aIddhHDrT7HGzx3JaZ1F02-YI)

* Aquí es donde configurarás el mapeo de campos para este BOD, tu configuración debería lucir como la siguiente. Los mapeos de campos están disponibles aquí.

![](https://lh7-us.googleusercontent.com/3giuZYeQjdZZHAg7W-pcAHB\_69KP8Ukh\_0NhATYBxvrS\_Qy3yH58fQyrp6GKfOzi1xJms5KV-XVNnAWtX6VmIBwdxSVum9JA6-H9W3XIUYKiTEK3IWoKA560a5I2lwmYd0kitdfC4pRkQVULyWp9PpA)

Una vez que hayas completado los pasos anteriores, habrás configurado exitosamente el BOD Sync.PlanDeCuentas. Haz clic en el icono PLUS para agregar el siguiente y último BOD.
#### **Sync.CodeDefinition**

La pestaña de conexión para tu punto de conexión CodeDefinition debería verse similar a lo ilustrado a continuación. Dale al punto de conexión un nombre y descripción apropiados, así como importa la Cuenta de Servicio que creaste.

* Selecciona "Enviar a la API"

![](https://lh7-us.googleusercontent.com/YLaFsc0K1Lzruo84Np3EdCTF1xsaQOLRypNpgZB7L9keTh1TwPOMnjBxJYnBOj8GrNSG\_URcRGgv\_p70-pjhBed-wvURRW08YtEWjmACMc3CleRPrHia6nihWQwVOUaZ3qHD\_zLy2W\_iMQ0I77cY\_Bs)

* Busca el BOD Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/f3ikl4jh0PBhYmP3r80BrHuGGu9w9MHe-E0VmyXOCmFEkkK92cxgVimwyP8RF0kF2GruVaeDjiYRKuONX5bQ2ZBRmdKFx8Bf9cHvX5q-xYnXNH0a2xnR4eg1ynyWbRRRoY5xn28HJ\_ziRiKcTN43aHQ)

![](https://lh7-us.googleusercontent.com/nXQZ1LLZsrndggHkAmRtMlV7YzFemnjC9CnS4AdUVDits4zNfzlaqKdHnNcLyTtDkQSX3SB8R3fnZhGBPd-By8C364IIYc4vE2VXNXzoa4LfHP6irTiAg\_N\_2BHSYBLzaQyMCN1w5LdFiiqeiiwAXuk)

* Cambia a la pestaña ION API, copia el nombre de la API y busca la Llamada a la API presionando el botón SELECT

![](https://lh7-us.googleusercontent.com/LbHmVr1PimQkPu-t6VMvNVk9wVXeQBHOu-X4pW-9vGm-dON2buizVGbKekGL7tY1t4OkwQtzhl7uDhq908UxCfDCJaRDEukpk-07pJjLO-ezRUHgblp3REm0qrKF9wOtMkNWJlVVNVhmfzZ0TtUsqQQ)

![](https://lh7-us.googleusercontent.com/K-kDDTSaZiothC4o3JDihhVJFNt0PiBnLK7kF6RcBOX9EpzutfLHGstzvywBBqaEqm4WqOSQSxtvxRPtbVafPlhtf\_YMVkXjhTkvnGwLzwH\_p-YgRCGAu-DzA94MHjqQoAYTSBPgojcGlJs7tBRcpME)

* A continuación, cambia a la pestaña Cuerpo de la Solicitud

![](https://lh7-us.googleusercontent.com/DfT6FtrbW7LbK4b4I6ssYDWOaPgUxkWsuTDpvQGw549tPFxgEU\_gmh3UwXTbyKHZR8SOHXPHDdobEhA91RIMB57ZAVatrZEsad2QW6QHiUkdZoyW\_yE\_iIGDgs2IrY0I6qL1JTZxksYoaLKu0Il8smU)

* Aquí es donde configurarás el mapeo de campos para este BOD, tu configuración debería verse como la siguiente. Los mapeos de campos están disponibles aquí.

![](https://lh7-us.googleusercontent.com/nqK7x1Km4wIP9aWnvMlSHl1\_omw22GRKONfB-zc8ikn\_rSsl60Ksml0oQacs8UNmPSLFSKPD7Eo9FsH42RjDo4oragvHZJHFW\_yv62KXDrF3SKnDN2-X6vqYJ5a-3bYkkvPDlNJSxFylvtAFr-2Kt8Y)

Una vez que hayas completado los pasos anteriores, habrás configurado con éxito el BOD Sync.CodeDefinition para la tabla de datos maestros M3FlexDimensions.

## **Flujo de Datos**

Necesitarás configurar el siguiente flujo de datos para la Contabilidad Automática:

* ChartOfAccounts

### **ChartOfAccounts**

Una visión general de este flujo de datos se ve como se muestra a continuación (la cantidad de puntos de conexión de API de DocBits al final depende de la cantidad de entornos diferentes que estés configurando).

![](https://lh7-us.googleusercontent.com/RfkP8xiF2vDzQhBNa66L0NQHk7TGjj52aK3hWoisEnWbdG3l-SZKKw8mYJ3b28ShXZ9omPS6WdNiXaCpYRQzwfges0SKznwQal7K2ElILbGBJNYu3VFm6gDQJMHYRItAFX0cdRZjXgCk2FQqHJ4iSjY)

### **Compañía M3**

![](https://lh7-us.googleusercontent.com/tqYoI-gLUpe0c0x1T-WhP0\_FolVzPGHhFY8m52Fw38mJNzsDvjb7stRrBfWVjXLnFrJTTy2lyd9Dmva3\_EPG5eRWyf5ATA2cTWvCj3Ksa4Fu4pHF6rNFjfd3Cjei0UlibT0HAQYE0V22bdTStjY61zk)

La configuración de este punto de conexión depende de la compañía M3 que contiene los datos maestros que deseas importar a DocBits, la tuya debería verse similar a lo que se muestra a continuación.

![](https://lh7-us.googleusercontent.com/wpSluEs21T5wXG0egZPfUCYBP6X\_uUm6XAh-PyD8RrojTuIztzRJzhVYdzcNI5dQGGDsrhSKx\_K2-y0JDmK9w41fVUXWcW1N2lz5rizXcMnn5BuiaGRy-TEOBryGxvP9mBGJTZ16lMisoC\_YumwpS9Q)

### **Documentos**

![](https://lh7-us.googleusercontent.com/uR6XaFI7TPQ4L8Suom25PBdtXdL4i100Juz7kRBxT5rdxhejZW7nPtVIlEGjWWnZLbo9ipx7G95NBFV8dd-g4vw\_vM-uPApJ02QdxvCmX27bwAW\_qUWUXajV6BFVmIfzTQ46Zj4DybsYKKblXjuWc6w)

Los siguientes documentos deben ser añadidos al flujo de datos:

* Sync.ChartOfAccounts
* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/6Bq-yQ9Yaf2OJwjBxyFvqAMUitcovquo\_iU4hc-pgag1iDwLcstggVjLsdY3bRl9XWNc3mKOwZrY1FSlu47IzxxUQHFkjIAl1r08Iw9UbKaaMh4WiWrqFuSObdTjEvCEI5IDvD\_Pys8jAydydJgbsK8)
### **Filtro**

![](https://lh7-us.googleusercontent.com/LyKGzQUEswTD1XfpNDPSHjChgqNFfs4guXfM0KNuW2fPoiaeUo4uPrlGgwt3RepWUGQmu\_trUMiWb68cUjUAwXU9IRoWOsv9M2l5v4zFfBkEcioz5ok7Eoss7I-tBKtpD7wVUkGWi3U3ySrIQ\_fDPiY)

Para la segunda ruta del flujo de datos (según el enrutamiento en el flujo de datos), aplicamos un filtro con la siguiente configuración.

![](https://lh7-us.googleusercontent.com/7xdqGdo9bS6\_IIzTVYF\_08woBXvhIVkA-c6-ZrDpDEzmEDFzDZSuxZ5LYHKVUhJqYq4Wlq1FXPfr5myjKFUsMbnJrefc\_L7URD7AbEq\_D90jEw7o8Yrhg5XZwLdU83OwlZVXqlYla61b0LyISXeBLWk)

![](https://lh7-us.googleusercontent.com/OdI-0FaqDaPKy2g9Mr8HUx\_oGRZkDrkeI6P1rWqOounpDauMThaqzs2wOawmw3RwcMlQHgI6wj16RXQDAP\_JNMGkxvmiEnPJ\_bvse2CvMegPwinSIJRLmXaCzfjxtB1FDqnqPOMwrMYNKJyiC2sGUe8)

![](https://lh7-us.googleusercontent.com/RMPIV6ZWsUcBA6klny6Ln-\_nhMGl1zdEHfUKK56owelabcG-6gM1S\_eqWAVLTeOHdec3D5D6xVJeC5evnJC61L8daV6IbJbCmMashkWXSK4Tv4RdE\_erjR-Mk2RihPodIG4HrqSOQ8hi7SG3xctXd-E)

### **DocBits (ChartOfAccounts)**

![](https://lh7-us.googleusercontent.com/Npm92rS\_EO5roSy3tldC88hFIyiDnZjHnnVSkkKyfmNrOcbuVj4LPNrcsWvOT8IHNQKGMqIZymG9q3VMGG6RwvuRBqZgmhHxqXn1oieajDmz8giQxSr8wOFzb8TQTJJWwj912-sDRtkrDAXCr7ne-pk)

Aquí es donde agregas el punto de conexión de la API de ChartOfAccounts que creaste anteriormente, la configuración para esto debería verse similar a esto

![](https://lh7-us.googleusercontent.com/Dw4y6OMuMAYHZjH1etj\_FqdsaFxaRhQyk6\_PaxXrWLhrNirEn7xQc5uIpbDT6Wz85XvZgY02aNuWfbYKBzo6W9aavN\_Asu5ENfr2dszWYQqs9sy6zl4o0NxRe3IPXodLIGf9JkbK2\_UtYe4dVii0JbM)

## **Desencadenamiento de BOD**

Una vez completado todo lo anterior, deberás navegar a Infor M3 y desencadenar los BOD para que los diversos datos maestros que necesitas para la Contabilidad Automática lleguen a DocBits.

Comienza presionando Command + r, para abrir el menú de comandos, escribe "evs006" y presiona enter.

![](https://lh7-us.googleusercontent.com/pzAL0cnM94AUE4KmTyBV8OPU9ft\_g9o0-KB9Ib0AjrvG7Q59GHT-2biP4n7yFyXRxQ0gjy85G6MWMWUeMIWJcTQ9TKwzCEywd7I\_6\_vV-muepobkW0O-4-CZxsmjOEQ7uM1frZpTLqlLS3aSYkEuwAw)

Se te mostrará el siguiente menú

![](https://lh7-us.googleusercontent.com/Wx41TNpg1zuaf1rXIBvSCVzSRf6q74rdLs91el21iErqQnDiF4cv7X0nyDaS2Gjimj7xbfAK-7mo6sXN6fkK934mHnCnivFTz9NqHi6dBoMYiRT\_vLrkVUlFd\_T4Oan3Zkq3WKLoI-kmsElHSKO7zY0)

Para agregar los diversos BODs, deberás ingresar los sustantivos BOD y los nombres de tabla para cada BOD individualmente.

![](https://lh7-us.googleusercontent.com/5gVWRDm\_8CSyoQRkq-7LuI8MLU1BjRN6Z6YCcVZp7G3Be62nQBht-eUNZreTzV2rFWYK\_RcKiyzwTTlT5y5X8eGf-Z7qDavDyHML0zv6Yt6jGu2z9d-nL0K-m446nDZa2-aiFLnnzjAwk8pTT4RQK6Q)

Los BODs que necesitas agregar incluyen:

* ChartOfAccounts
* CodeDefinition
* CodeDefinitionAccountingDimension

Para agregar el nuevo BOD, después de ingresar el Sustantivo BOD y el Nombre de la Tabla, presiona el ícono pLUS indicado a continuación

![](https://lh7-us.googleusercontent.com/66wclj8g8RAYT9-UIgRMs0qnuA9srmWv21PdqdNm\_q5icGmabL17-DpLOSs4pm6Nj3xJN-9xt7io\_5GZGfzSQ2qt\_8Y--CJFou6FaOdufiuxOdKHrUUYELNdGy9e-gnWg\_hAMSfs\_NJa6zYBMpoyTVs)

Los sustantivos BOD y los nombres de tabla son los siguientes.

**ChartOfAccounts**

* Sustantivo BOD: ChartOfAccounts
* Nombre de la Tabla: FCHACC

**CodeDefinition**

* Sustantivo BOD: CodeDefinitionAccountingDimension
* Nombre de la Tabla: FCHACC

### **Publicar BODs**

Después de agregar cada BOD, haz clic derecho en el BOD que agregaste, selecciona Relacionado y luego Ejecutar.

![](https://lh7-us.googleusercontent.com/225-ujyGzG\_RJOXgbx8NOh\_4s-Sn\_o80b\_h0DTsJqfr6OcyPUwkWLF2lfEyzFFFKddKmlWd32bb94qeYlOdVBTI8RL0r6ZfZKloVTrAYLNp-U5gL3aJhW4d72ExkkyM4AydLczsPvdE1cRDfGNKupdA)

Se te llevará a esta pantalla.

Cambia el Verbo BOD a "sync" y presiona SIGUIENTE.

![](https://lh7-us.googleusercontent.com/3DyjXUSlAF7msQT1OAO3aCr1U9R68XZj0oE\_yJwsBrBj-FkiZR-oRYQYSClHG0iN0FXFdDdKQA1hOBlw3jc-lXQCWkiDFa0IweuQnoR8k-Mgyp1HeI5ImJqNogz-Q3b3P33ywb0B2o1pZ-TkZ7mAwZA)

Una vez que presiones SIGUIENTE, recibirás una notificación que indica que el proceso de publicación de BOD ha comenzado.
### **Elemento de Costeo**

Para importar la tabla m3costingelement en DocBits, debes seguir estos pasos.

Desde la página de inicio de M3, escribe Command + r y busca el comando "PPS280".

Selecciona cualquiera de las líneas que se te muestren. En el siguiente menú, selecciona HERRAMIENTAS y "Exportar a Excel".

![](https://lh7-us.googleusercontent.com/I8SYWm-JwpyYRHFUp2obGtXcsa7m\_blJ\_lTrnhczztRIXIN5gfxCt3eRw6ZI42fH6AwnsKyv4ux5-rhaT505PsyDFFI\_anUNvmACFyx\_ssgxaqWq25vLt\_E5s310HNoiPPLf35qJlYtstjpj5Cc4aB4)

Selecciona "Exportar todas las filas" y luego presiona EXPORTAR.

![](https://lh7-us.googleusercontent.com/wtjHI9L4YUhf-yJFjcPGu218Vis\_zELtCIfpmkIUKgasfrdfNW-dr\_J1DqXlfD-SBrnVduDrMLAIAQh6UTlzBqEP\_JPXP48elGMyGj0ByZbX7TpqlnIfRZ4ZoD0pyCo-AKigeKjlHN6cFcdpeClZ9L4)

Una vez descargado, deberás modificar el archivo de Excel antes de convertirlo en un archivo CSV.

Debes abrir el archivo de Excel, se verá similar a lo que se muestra a continuación.

![](https://lh7-us.googleusercontent.com/l4WbidK-5zSEQ6rwqhknudPBmmDji0f1WwTh-kHomSkgEOA7s4m72cLw8z-4nflqBvPp\_2AajIEZDZz4dRLs8jlAeYHp4ee2tDysxYy8YBjj4ktHxdUXpxO\_Z34c8\_f0cNMX-9lp0lT5wOZoH1QUCgE)

De este archivo de Excel solo necesitas las primeras 2 columnas, modifica el archivo de Excel para que el resultado final se vea como se muestra a continuación.

![](https://lh7-us.googleusercontent.com/QaNRlKHrU6kZWFqmwYR8C\_\_nLVOeqowAxJlvooSVBIAF5ayx2xZtUppsn0jzBcJVi90vemM3tZMZOjn549N3RzMuWuE3w911WLVS5NMuiUmnfXM\_xUXbqmzBtiQZstnpEYj1dUSbs\_IkAydlhBfdmcc)

Una vez hecho esto, guarda el archivo como un CSV.

Una vez que tengas tu archivo CSV, ve a la siguiente página web. Esto depende del entorno que estés utilizando:

* Prod: http://api.docbits.com/
* Sandbox: http://sandbox.api.docbits.com/
* Stage: http://stage.api.docbits.com/
* Demo: http://demo.api.docbits.com/
* Dev: http://dev.api.docbits.com/

Aquí deberás cargar manualmente la tabla CostingElement a través de una API. Haz clic en el botón Autorizar.

![](https://lh7-us.googleusercontent.com/tyzOq3BR2QqTguQFKicxo0dE5j5hGsP-BhfVbS81O\_mxN5bSVp40jYfgsVJcE\_rBLFMDJNvbPkPIdjPqaqoNbHBBM-9hx0i-U4VAH9ISBYhpwKgqQeUEd67VV1E4izwNyxbAwwrhCmrAo1uIKhLherY)

Aquí deberás insertar la Clave API de tu entorno de DocBits. Esta se encuentra en Configuración bajo Integración.

![](https://lh7-us.googleusercontent.com/4ADnevq6kq\_vbxUJpyPbHNcGvRvpO-l9Gwd8ZaYf\_vO4uWhSl1jmKNpddmHGc9ZHMMbXCgLOElLDYbNwB3INmBDETecPrDnpI601IUOZQlT7tc7OLSPXwkooOJFNwML2i\_gvBPuE8CvfwRpX-ZIlb\_g)

Una vez completado, busca la API llamada master\_data\_lookup/import\_data y completa la información requerida. Una vez completado, haz clic en EJECUTAR para activar la API.

![](https://lh7-us.googleusercontent.com/8UD4FhFv2dRB4cMjCDL4G9ndjH7laVMKWqdeMaJGgEo48-UVvucB1uOydzNdfFy0yPM5bb66mZB4k9uJR7TTiEREGFaV2EqW01gxJpTyuUfGNh5QmBjySkyhZ56gWV8sYs8WI5RnHcENtXgjTU0vg0Q)

Si todo se ha realizado correctamente, la tabla M3CostingElement debería estar ahora en tu entorno de DocBits. La Contabilidad Automática para M3 ha sido configurada en tu entorno.
