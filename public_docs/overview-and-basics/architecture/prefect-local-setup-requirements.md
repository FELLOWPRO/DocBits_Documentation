# Requisiti per l'installazione locale di Prefect

#### Requisiti

Assicurati che sul sistema host siano installati i seguenti componenti:

* **Docker Engine**
* **Docker Compose v2**&#x20;

#### Compatibilità del sistema operativo host

* **Linux**: consigliato e pienamente supportato.
* **Windows**: funziona con Docker Desktop (WSL2). I montaggi dei volumi possono causare problemi.
* **macOS**: supportato tramite Docker Desktop. Comportamento simile a Windows.

#### Requisiti di sistema

* **RAM**: 1–2 GB per container. Per più flussi: 2–4 GB.
* **CPU**: 1–2 core per container. Per flussi concorrenti: 2–4 core.
* **Disco**: 2–3 GB per immagine e log&#x20;
