# Edición y guardado de patrones Regex

## Guía para modificar patrones existentes y la importancia de probar esos cambios para garantizar que funcionen como se espera sin romper la funcionalidad existente.

**Para editar patrones Regex existentes y asegurarse de que los cambios funcionen como se espera sin romper la funcionalidad existente, puede seguir la guía a continuación:**

<figure><img src="../../../../../.gitbook/assets/image (99).png" alt=""><figcaption><p>Configuración: Tipo de documento</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto 2024-05-22 um 14.18.25.png" alt=""><figcaption></figcaption></figure>

**Analice el patrón existente:**

* Examine el patrón Regex existente para entender qué datos captura y cómo funciona.
* Identifique las partes del patrón que deben cambiarse y el impacto de esos cambios en los datos capturados.

**Por ejemplo: se debe leer el importe de la factura:**

*   (?<=Rechnungsbetrag:)\[\s]\*((((\d+)\[,.]{1,10})+\d{0,2})|(\d+(?!,)))

    Rechnungsbetrag: 100.00
*   Leer el importe con punto de millares pero NO aceptar el punto

    \[\d.]_\[,\d]_

    Caracteres permitidos: 0123456789,
*   Se debe leer el valor "P32180". La palabra ancla aquí es "Invoice Date".

    (?<=InvoiceDate )\[\s]\*P\d{5}

    Customer number Invoice number Invoice date P32180 613976 05/13/2019

<figure><img src="../../../../../.gitbook/assets/image (108).png" alt=""><figcaption></figcaption></figure>

**Documente los cambios:**

* Tome notas sobre los cambios que planea realizar en el patrón Regex.
* Anote qué patrones nuevos planea añadir y qué partes del patrón existente podrían necesitar modificarse o eliminarse.

**Prepare los datos de prueba:**

* Reúna datos de prueba representativos de los distintos tipos de datos que el patrón Regex suele capturar.
* Asegúrese de que sus datos de prueba cubran tanto los casos típicos como los casos límite para verificar la solidez de sus cambios.

**Realice cambios en el patrón Regex:**

* Realice los cambios planificados en el patrón Regex.
* Esto puede incluir añadir nuevos patrones, eliminar o ajustar partes existentes u optimizar el patrón para un mejor rendimiento.

**Pruebe los cambios:**

* Aplique el patrón Regex actualizado a sus datos de prueba y revise cuidadosamente los resultados.
* Verifique que el patrón siga capturando correctamente los datos deseados y que no haya efectos inesperados en otras partes de los datos o del sistema.

**Depuración y adaptación:**

* Si los resultados de las pruebas no son los esperados o surgen problemas inesperados, revise cuidadosamente sus cambios y realice más ajustes según sea necesario.
* Esto puede incluir revertir ciertos cambios o añadir ajustes adicionales para solucionar el problema.

**Documente los cambios:**

* Actualice la documentación de su patrón Regex para reflejar los cambios realizados.
* Describa los patrones actualizados y los motivos de los cambios realizados para ayudar a otros desarrolladores a entender y utilizar el patrón.

**Guardado de los cambios:**

* Cuando esté seguro de que los cambios se han realizado con éxito y funcionan como se espera, guarde el patrón Regex actualizado en su base de código o en sus archivos de configuración para garantizar que esté disponible para su uso futuro.

<figure><img src="../../../../../.gitbook/assets/image (109).png" alt=""><figcaption><p>Guardar cambios</p></figcaption></figure>

Siguiendo estos pasos y probando cuidadosamente los cambios en los patrones Regex, podrá asegurarse de que su patrón Regex siga funcionando correctamente y cumpla al mismo tiempo los nuevos requisitos.
