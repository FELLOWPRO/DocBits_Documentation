# Anforderungen an die lokale Prefect-Einrichtung

#### Anforderungen

Stellen Sie sicher, dass auf dem Hostsystem Folgendes installiert ist:

* **Docker Engine**
* **Docker Compose v2**&#x20;

#### Kompatibilität des Host-Betriebssystems

* **Linux**: Empfohlen und vollständig unterstützt.
* **Windows**: Funktioniert mit Docker Desktop (WSL2). Volume-Mounts können Probleme verursachen.
* **macOS**: Unterstützt über Docker Desktop. Verhält sich ähnlich wie Windows.

#### Systemanforderungen

* **RAM**: 1–2 GB pro Container. Bei mehreren Flows: 2–4 GB.
* **CPU**: 1–2 Kerne pro Container. Bei parallelen Flows: 2–4 Kerne.
* **Festplatte**: 2–3 GB für Image und Logs&#x20;
