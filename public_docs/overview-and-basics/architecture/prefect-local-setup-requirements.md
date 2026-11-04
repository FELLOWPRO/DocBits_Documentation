# Wymagania lokalnej instalacji Prefect

#### Wymagania

Upewnij się, że w systemie hosta zainstalowano następujące komponenty:

* **Docker Engine**
* **Docker Compose v2**&#x20;

#### Zgodność z systemem operacyjnym hosta

* **Linux**: Zalecany i w pełni obsługiwany.
* **Windows**: Działa z Docker Desktop (WSL2). Montowanie woluminów może powodować problemy.
* **macOS**: Obsługiwany przez Docker Desktop. Zachowanie podobne jak w systemie Windows.

#### Wymagania systemowe

* **RAM**: 1–2 GB na kontener. Dla wielu przepływów: 2–4 GB.
* **CPU**: 1–2 rdzenie na kontener. Dla przepływów równoległych: 2–4 rdzenie.
* **Dysk**: 2–3 GB na obraz i logi&#x20;
