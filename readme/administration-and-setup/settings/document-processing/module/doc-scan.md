---
description: Cree documentos en DocBits con un escáner local y Doc Scan.
---

# Doc Scan

## Descargar e instalar el software del escáner

En el panel de DocBits, haga clic en Scan Document.

<figure><img src="../../../../.gitbook/assets/image (203).png" alt="Botón Scan Document en el panel de DocBits"><figcaption></figcaption></figure>

Si el software local del escáner no está instalado, DocBits muestra una solicitud de descarga. Seleccione la descarga correspondiente a su sistema operativo.

<figure><img src="../../../../.gitbook/assets/image (204).png" alt="Solicitud de descarga del software local del escáner"><figcaption></figcaption></figure>

Abra el archivo de instalación descargado. El instalador ilustrado es para macOS; siga las instrucciones de su sistema operativo.

<figure><img src="../../../../.gitbook/assets/image (205).png" alt="Inicio del instalador del software del escáner"><figcaption></figcaption></figure>

En el instalador ilustrado, haga clic en Continue, acepte la licencia de software con Agree y continúe. Revise el destino y el espacio necesario y haga clic en Install. Los 33,6 MB mostrados corresponden a esa versión del instalador; el espacio necesario puede cambiar según la versión.

Cuando termine la instalación, cierre el instalador.

<figure><img src="../../../../.gitbook/assets/image (206).png" alt="Instalación del software del escáner completada"><figcaption></figcaption></figure>

Abra https://local.polydocs.io:12500/ en el navegador para probar el servicio local. Si no puede acceder y utiliza un FRITZ!Box, revise los ajustes de protección contra DNS rebinding descritos más abajo.

<figure><img src="../../../../.gitbook/assets/image (207).png" alt="Error del navegador al probar el servicio local del escáner"><figcaption></figcaption></figure>

Cuando aparezca la página del servicio local, haga clic en DocBits para abrir DocBits.

<figure><img src="../../../../.gitbook/assets/image (208).png" alt="Página del servicio local del escáner tras una conexión correcta"><figcaption></figcaption></figure>

Inicie sesión en la página de acceso de DocBits para entrar en su panel.

<figure><img src="../../../../.gitbook/assets/image (209).png" alt="Página de inicio de sesión de DocBits abierta desde el servicio local"><figcaption></figcaption></figure>

Active Doc Scan en los ajustes, en Módulos.

<figure><img src="../../../../.gitbook/assets/image (210).png" alt="Ajuste del módulo Doc Scan"><figcaption></figcaption></figure>

## Ajustes de red del FRITZ!Box

Si no se puede acceder a https://local.polydocs.io:12500/ porque el FRITZ!Box bloquea respuestas DNS con direcciones privadas, el navegador puede indicar que se ha agotado el tiempo de espera de DNS. El FRITZ!Box utiliza esta protección contra DNS rebinding. Añada una excepción de nombre de host para este servicio local:

1. En la interfaz alemana del FRITZ!Box, abra Heimnetz (red doméstica) y después Netzwerk (red).
2. Abra la pestaña Netzwerkeinstellungen (ajustes de red).
3. En DNS-Rebind-Schutz (protección contra DNS rebinding), añada local.polydocs.io a las excepciones de nombres de host.
4. Haga clic en Übernehmen (aplicar) y vuelva a probar el servicio local.

## Desinstalar Doc2Scan Service Manager

Para desinstalar Doc2Scan Manager en macOS, ejecute:

```bash
sudo bash /Library/doc2scan/uninstall.sh
```

## Compatibilidad de escáneres

sane-airscan es un backend de SANE para Apple AirScan/eSCL y Microsoft WSD (WS-Scan, Web Services for Devices). Son protocolos de escaneo en red.

Consulte la [información de compatibilidad mantenida por sane-airscan](https://github.com/alexpevzner/sane-airscan) para conocer los dispositivos y protocolos cuyo funcionamiento se ha comunicado. La disponibilidad de un protocolo o un informe sobre sane-airscan no garantiza que todas las funciones del dispositivo funcionen en Doc Scan. Pruebe su escáner con el flujo de trabajo de Doc Scan que necesite.
