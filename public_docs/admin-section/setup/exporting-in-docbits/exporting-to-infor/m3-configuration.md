# Configuración de M3

## Requisitos previos

Has creado:

* Un punto final de API de ION
* Un archivo de API de ION
* Un archivo de mapeo BOD
* Un archivo de mapeo IDM

## Importar archivos de mapeo

Antes de configurar el flujo de datos, necesitas importar los archivos de mapeo en InforOS.

En ION Desk → Conectar y abrir Mapeos

![](https://lh7-us.googleusercontent.com/EV8z6b_W9tjTgML0j3qJAYHCTYLd4N5yLrArdIECftYpMOCRTRJ_a7eADEzljFM4XHxMUJ6Nx9Z6EN3Hmzote5F0HrM5zd4p1BS0NYicUWDnkhQFX-_3MGbblEYi6x2a1K25SclYYttgW3cWQbOjvfQ)

Haz clic en el ícono de Importar

![](https://lh7-us.googleusercontent.com/agBHtjNitneogoZsSG1791QAARbvesv9eSriAkw0HL9Fy372Ty6SmQG1sKJjOYZCuE0SnGT3agHAFRJYjgGNxJrN1CMJj9L-fSPhNmXxN78iDKqrrdgEVYFHxsNwy9XLiUFpBCQ1wnWlwyeFH08DsWI)

Desde aquí, debes seleccionar los diversos archivos de mapeo que necesitarás, que incluyen: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice y LoadSupplierInvoice\_ProcessSupplierInvoice.

Una vez que hayas importado todos los archivos de mapeo, asegúrate de aprobar cada uno de ellos haciendo clic en el ícono de marca de verificación dentro de cada uno de sus cuadrados en el panel de Mapeo.

## DocBits a M3

El siguiente paso es configurar el Flujo de Datos en ION Desk, navega hasta la aplicación ION Desk y selecciona Flujo de Datos → + AGREGAR → Flujo de Documentos como se muestra a continuación

![](https://lh7-us.googleusercontent.com/Kkro7w2LPfnwf-JPMmPI2DzrSRNEi_F9aWW02KDtBvAZz_R7j9DZ71Nqw3ETPSQqDuxBzJ1TU8Uuzz5jU9rOO_tvDBf9abVF-FDSxln_pjr-HMRdYBnGMwgcM6hg-pC2B7FgdBkXibivMB4PptvZ6fk)

Luego verás esta página, aquí es donde construirás el flujo de información de DocBits a M3

![](https://lh7-us.googleusercontent.com/K0B1lC_KLO5RZqGqAltp6JnZZ1sfZG4wg-i_nxZCnLjML33yvViRUHOInK3iHYbzbV4I0uqDY8JpsZMxssD8bbJy24A1zKr9PfQEyqVxewx_L87RCIwzn5MDRjMqgx4X42vkKthbyz--5DDe1H0rvHQ)

Un flujo de datos de M3 se verá similar a lo que se muestra a continuación (hay 3 aplicaciones y APIs de DocBits debido a que se utilizan para 3 entornos separados).

![](https://lh7-us.googleusercontent.com/6Oy_UBzYNml-7_sayDEKhqYF92yDzlUNzmGLQSWZOfDT-avvfg3oNUnv_DtXNSP0XF43D-zgIizIuTrCXl6ockLU2uQLYFJna72fzL5BP-T89xjF4oWz2eAz9w0hsoVieyTpgSw_Prvj--89Kc4Kqoo)

Todas las partes de la cadena se arrastran y sueltan desde la sección superior

En la cadena, DocBits y M3 son ambas Aplicaciones mientras que entre ellos hay mapeos que convierten los datos en una forma que puede ser entendida por la siguiente sección del tren y "mapean" la información para que vaya a donde se necesita o se pretende.

![](https://lh7-us.googleusercontent.com/1kjgKNmIQ-NbM_JukcPsj7qmyiMB9b693ixg6Dh1kOlZ6NKgBXViYwn0MNUBHt0WKKWf_1gpRvxgqjIaqpqcy-SyXoYjhJLt3m_bv7wbVADzqHRsx8TYXWyIQO82X-Ixfl5b7iI7nxTRkw06sX3xsBM)

### Aplicación DocBits

Dale el nombre apropiado, como "DocBits", luego selecciona el signo más y busca el punto de conexión que creaste anteriormente, como DocBits_Export o similar y haz clic en él.

Para crear este punto de conexión, ve a ION Desk → Conectar → Puntos de Conexión

![](https://lh7-us.googleusercontent.com/8qsMIUKMrgmcYqqJPL2zF4GVeHuvSHvn8Z7dfonRuvKFPcXmN4hx2PIrXko4lvW7ayD7s2VRFOMvWkQSxfAH5tTuhg0XhzYmSzlsgnowWRw8GmQC2y5BjcS9X2MjDzLSutgoHg2VN59kCYRunMSxkIY)

Haz clic en "+ Agregar"

![](https://lh7-us.googleusercontent.com/-3-3TzgEQppYmX64-clxjp1JBjNz9fsA2FDPqirgNF0wL8DsDJACzUBuSw5wBL2k9JanqvMzAG352CWafOdtjhMfZalJnBFVSjaWA1AszhCjKtCsTvLUUqq1WwMfF-PqL-u7LRo4TPbj4fP2_j48240)

Selecciona "IMS a través de API Gateway" y completa la siguiente información

![](https://lh7-us.googleusercontent.com/wImUEi9mXiQjW5O6mp7_IrKk4CTaHFs903DJ6TXqUEcjGq45TnUWdusFTGH1jzpBPP_TC7rokyjrkYWmh3emSKBQs05qYbO80TO87De0C5OveVURykQMCLFRRYakEMoFHpoeXzxH5QIbKJdjxujeY98)

El ID de Cliente de API de ION está en el Archivo de API de ION que creaste en Cómo Crear un Archivo de API de ION, esto se puede encontrar por el valor "ci".

Cambia a la pestaña de documento y agrega el BOD de Sync.CaptureDocument al punto de conexión de DocBits como se muestra a continuación.

![](https://lh7-us.googleusercontent.com/ga1q0Uwdi2GNwuiz22NvDtCzGL0krSkBPLsEVxE-mtoMV7CtEU8TPO0PhF40oB9NB9iv7DCJi9niLnsKjpqarWJsgGRdc1W0pFl9rTDm7i2_BS_Lj3JOrzR7iclPdqOdpztgCxWZG2Teg1gWljaMUq2E)

Luego guarda el punto de conexión presionando el ícono de disco en la esquina superior izquierda.

Regresa a la sección de Flujo de Datos de ION Desk para acceder a tu flujo de datos. Tu aplicación DocBits debería verse similar a lo que se muestra a continuación.

![](https://lh7-us.googleusercontent.com/fBzKL6RU0XvGpn1cKFZIyAp2amKonBWc8ilbAq5u_r867xywWWAD7EjP-g-wjlwUsrG4Wz0lS6Ujdnu8P3vc8Q3FbtbRR4qSBmbSLoICfX-aHITMDdHp07bESefC9TuUUUQiHGb1j00HNtB_7A3iDFs)
### Mapeo 1

El primer nodo de mapeo debería lucir de la siguiente manera

![](https://lh7-us.googleusercontent.com/F9AcE4V-s9vs-0kRz8BcCtdHUUQoaooyK3GqOj8pAQWuvIguoUO-tJx7WBEW6_GmzwNsJp8VUYezGCiLPXvPhEynac3FPh_NJOvqs1SXtMIUsF5_HjWmcvY3VC-eZsjG0ZE8HmsKsFhocadr96drSbY)

### Mapeo 2

El segundo nodo de mapeo debería lucir de la siguiente manera

![](https://lh7-us.googleusercontent.com/8M_V2BtkOGyqV-828ct5c2QvSs5n5_RtLjlH717kspZwlgtfjbz6tpOJCCXDelruBenMjxsJPqncQ5hUw2bQkM3ya7_WrVyEBz3UnaU-C9oVOWB8nNtXA20RBYgO3EBMon2TfgpefY0lSPBzF9NoTeU)

### Mapeo 3

El tercer nodo de mapeo debería lucir de la siguiente manera

![](https://lh7-us.googleusercontent.com/x9QUHTgQrNaeKnTeMIUflkWjcBr2c3LgsYe2BZBjv01hXiEkvsLtU0GzYt5KppcE12ZqxWeBJ1kbLOC6qA3yKHhujCZt3sFpDNE5yERkHHMJJEjFl0jJE90nQ-iXeMLbR-Bk6G0NIL8AqG3U48Seiuc)

### Aplicación M3

Debería haber un punto de conexión M3 o similar creado en INFOR, así que al igual que la Aplicación DocBits, selecciónelo haciendo clic en el signo “+” y debería lucir de la siguiente manera

![](https://lh7-us.googleusercontent.com/JTXIN5QxidvFJyjegxSw8kA7yVfHfuypxi5yX21CsSlGtOVgykc52U2r0077-cKqNhc0B4zSSZotlipFesmLo371kho3wUSRPzmwEir-stbxyZV1PwCDXkq6qJMm4PNXt_wGarDMixGIU0tu-eAqV5Y)

### API de DocBits

Primero necesitarás crear esta API como un punto de conexión, lo cual se hace así:

ION Desk → Conectar → Puntos de Conexión

![](https://lh7-us.googleusercontent.com/VOXW6LixmcKjHW0CTOO5L8fK6r-4k3jqk0AnoR6DEVoGgJMbx65hS3yKSgMWItypdz4Ha82T-bKCN0aMv34gif-b0Aw7zpDFPBK9G-K6x9_csrM9xyKcpmWam15tKqO1_rwKtMsJ2CSoWqdpLxCD5tA)

Haz clic en “+ Agregar” y selecciona API

![](https://lh7-us.googleusercontent.com/c1RAUNoA3YBhvf6FLJ_L3ouyZwHK-3bBRU83eL3oAQXjG6SjWEO9O-gDKPItPm8AI_YhadaCZU-GxY-qUXNuQMiRiKUhBYUtJ8kOFVg_YYpzJDSoJ68NYSaEtHBSyyfnq0VbHUdWY1e8lBQ0j_G5xvI)

La información que ingreses debería lucir como la siguiente

![](https://lh7-us.googleusercontent.com/h2KU6pKeKl9wX8oyul0KmbL_kg-iPQJpBqbf29l64ED2e-Z4tNj8-m4hBN_4SSiNPf2TrE92TD4H0-0AZ0eWxMFmDV22IdPlU9NO4XlQF9k0Swg0X3Sm1HMsSPvWi7Q1HUr8uy8j3aDRheFxZqZ2Gbc)

Cambia a la pestaña de documento y agrega la siguiente configuración

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_api_docs1-1024x279.png)

**Acknowledge.SupplierInvoice**

La configuración para este BOD es la siguiente

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_ack_11.png)

Asegúrate de haber seleccionado la opción “Enviar a API” en el menú anterior.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_ack_2-1024x338.png)

Por último, asegúrate de modificar también el cuerpo de la solicitud para que luzca así.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_ack_3-1024x260.png)

Repite este proceso para el resto de los BODs, cada configuración se muestra a continuación.

**Sync.PurchaseOrder**

La configuración para este BOD es la siguiente

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_po_1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_po_2-1024x359.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_po_3-1024x297.png)

**Sync.RemitToPartyMaster**

La configuración para este BOD es la siguiente

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_remit_1-1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_remit_2-1024x351.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_remit_3-1024x299.png)

**Sync.SupplierPartyMaster**

La configuración para este BOD es la siguiente

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_sup_1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_sup_2.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_sup_3-1024x295.png)

### BODs

![](https://lh7-us.googleusercontent.com/zaDSnm844wXqyefN58Y1DvuJOnMaoOrYQ_12Z5ZSng8-TPy38Th2ZPdAD6hyIYCOvBKGPDSvGpTmtBPq4K5IwyGtsKyMvk-CKOuY-hzD-RL7UrsG39qLN7m3_IDcDS66KeIQF5e70OWlHO1cbVvQUXM)

Las siguientes configuraciones deberían lucir de la siguiente manera:
#### Primero

![](https://lh7-us.googleusercontent.com/5gLpbQEYYW90dVLkSc5V60LeToMe2wcOcHHtwTdIdT0o0Gktu8T_7i7zfNikjgETM3QmzAsJAknlEGeB0W0YFLLi56g2PKPwyr2zPcHaKdu8XJWHgaC1u4--_CHNYfd1wQ__3kZpv1_PwyZty3JEyak)

#### Segundo

![](https://lh7-us.googleusercontent.com/xbWTcP8hYA72Ijt7_IV6l-9jKeSalbRPvTn7aNVcnWYMQcD2RDjM-EzKpBKjSIKF_-r8BaxmmCo9uz6-E-vC9flKb4toU3SH24EPLgbXc-VcfJeDdJKglf5P6WV6XYZg0cZVWAoyvS8qgtuR6ZqJYlI)

#### Tercero

![](https://lh7-us.googleusercontent.com/F8wVWXuHkLLW2kuu_7Dxe9LhyYdm04tl__Sp6FjeTyk_JFUzhCIUhVlKS_cq3I3FP_h2ksV4zEJHFC_KXK6sSZ5iz5yhTFZcPnH1HS_RvZb2Nr-UXYQ1H316UMoj6eRv6wMn3wHX842B5WVfPHVnJ74)

#### Cuarto

![](https://lh7-us.googleusercontent.com/myhi9y2sCvS5ZFkIJa5ysLbu7p0X6CYqbiuJ3sQ5-O-2QWlfAseunjwhXK0kakmAofplm0zmh_H1Np7bA559w0-jdurQUsZwYF9CyKYSKSeGnQaIit0HQ5iN-3Xv8CIC-5nk6mMj3JTDS97SlzbsOFE)

#### Quinto

![](https://lh7-us.googleusercontent.com/c-5iaUhhx0swH-mQfXE5Mdwe4J0skGt7mst4kJdOpjL3Uat329TZmKM5Af-lGQWmcmBht-ib_aUj4dVG7GaUAHHULjly3jxsR8MJNnLDcu5eZB268Vy-dXPxHmkVB8dMZTRhU5SUB59AREurJlW-K6o)

El último ícono debería estar vacío ya que no lleva ningún documento o información.

Una vez que hayas agregado todos los nodos necesarios al flujo de datos, presiona este botón para activar el flujo de datos (después de guardar el flujo de datos presionando el ícono del disco).

![](https://lh7-us.googleusercontent.com/WIecHktG7e5dbVScLbR8hUcZUdCEWXBW4xWDEuq0IqTMmguA_Ih_oRymvpk6CzowWFG5TTSCPIH-68ICnPSOPxeZksc-n4bmpvuH8dvHuHFU1DlppGRno3PKjCSJiK12p9bNlo_9cN2t9Ps3nbqF3xE)
