# Konfiguracja WatchDog

Ten przewodnik wyjaśnia, jak skonfigurować usługę WatchDog w aplikacji DocBits. Wszystkie konfiguracje są zarządzane bezpośrednio w **Settings → Document Processing → WatchDog**.

<figure><img src="../../../.gitbook/assets/watchdog-v2-config-infographic.svg" alt="Przegląd konfiguracji WatchDog"><figcaption></figcaption></figure>

---

## 1. Karta General

Karta General zawiera instrukcje konfiguracji, linki do pobrania i ustawienia aktualizacji.

<figure><img src="../../../.gitbook/assets/watchdog_v2_01.png" alt="Karta General WatchDog"><figcaption></figcaption></figure>

### 1.1 Pobieranie i konfiguracja

* Pobierz najnowszy plik `WatchDog.exe` bezpośrednio z karty General
* Skopiuj wyświetlony klucz API
* Uruchom polecenie konfiguracyjne w Wierszu polecenia z uprawnieniami administratora:

```powershell
WatchDog.exe -api YOUR_API_KEY
```

### 1.2 Harmonogram automatycznej aktualizacji

| Opcja | Interwał |
| :--- | :--- |
| On Startup Only | Sprawdzanie jednorazowo przy uruchomieniu |
| Hourly | Co 3600 sekund |
| Daily | Co 86400 sekund |
| Weekly | Co 604800 sekund |

---

## 2. Karta Configurations

Twórz konfiguracje importu i eksportu oraz zarządzaj nimi. Wszystkie konfiguracje są tworzone bezpośrednio w DocBits — lokalne pliki konfiguracyjne nie są potrzebne.

<figure><img src="../../../.gitbook/assets/watchdog_v2_03.png" alt="Przegląd konfiguracji WatchDog"><figcaption></figcaption></figure>

### 2.1 Konfiguracje importu

Zdefiniuj, gdzie WatchDog monitoruje nowe dokumenty.

<figure><img src="../../../.gitbook/assets/watchdog_v2_02.png" alt="Konfiguracja importu WatchDog"><figcaption></figcaption></figure>

| Pole | Opis |
| :--- | :--- |
| **Name** | Wyświetlana nazwa tej konfiguracji |
| **Watch Folder** | Katalog monitorowany pod kątem nowych dokumentów (wymagane) |
| **Success Folder** | Miejsce, do którego pliki są przenoszone po udanym imporcie |
| **Document Type** | INVOICE, CREDIT\_NOTE, PURCHASE\_ORDER itd. |
| **Sub-Organisation** | Opcjonalne — kieruje dokumenty do określonej podorganizacji |

### 2.2 Konfiguracje eksportu

Zdefiniuj, jak i dokąd eksportowane są przetworzone dokumenty.

> **Ważne:** Konfiguracje eksportu **wymagają teraz typu dokumentu** (`doc_type`). Konfiguracje bez typu dokumentu zostaną odrzucone przez system.

| Pole | Opis |
| :--- | :--- |
| **Name** | Wyświetlana nazwa tej konfiguracji |
| **Document Type** | Wymagane — INVOICE, CREDIT\_NOTE itd. |
| **Export Method** | Sposób eksportu dokumentów (patrz poniżej) |
| **Export Folder** | Katalog docelowy dla eksportów do folderu |
| **Execution Order** | Priorytet, gdy pasuje wiele konfiguracji (domyślnie: 1) |
| **XSLT Template** | Opcjonalne — szablon transformacji XML |

### 2.3 Metody eksportu

| Metoda | Opis |
| :--- | :--- |
| **Folder (watcher)** | Eksport PDF + XML do lokalnego folderu |
| **Infor IDM** | Przesyłanie do Infor Document Management |
| **Infor BOD** | Wysyłanie BOD XML do Infor ERP / SAP lub M3 |
| **ION API** | Wywoływanie punktów końcowych Infor ION API |
| **GLS840MI** | Przetwarzanie wsadowe M3 (przez REST API) |
| **REST API** | Wysyłanie do zewnętrznego API z uwierzytelnianiem ION OAuth |

<figure><img src="../../../.gitbook/assets/watchdog_v2_04.png" alt="Konfiguracja eksportu WatchDog"><figcaption></figcaption></figure>

### 2.4 Opcje przetwarzania

* **Barcode Divider:** Automatyczny podział wielostronicowych dokumentów na podstawie kodów kreskowych
* **DocBits Operator:** Włącza zadania automatyzacji przeglądarki

---

## 3. Karta Status

Monitoruj kondycję i aktywność usługi WatchDog.

<figure><img src="../../../.gitbook/assets/watchdog_v2_status.png" alt="Status usługi WatchDog"><figcaption></figcaption></figure>

### Informacje o statusie

| Pole | Opis |
| :--- | :--- |
| **Online/Offline** | Bieżący stan połączenia (próg heartbeat: 30 s) |
| **Version** | Zainstalowana wersja WatchDog |
| **Version First Seen** | Kiedy po raz pierwszy zgłoszono tę wersję |
| **Last Restart** | Znacznik czasu ostatniego ponownego uruchomienia usługi |
| **Auto-Update Enabled** | Czy automatyczne aktualizacje są aktywne |
| **Latest Version** | Najnowsza dostępna wersja |
| **Latest Version Checked At** | Kiedy ostatnio sprawdzono najnowszą wersję |
| **System Info** | Ścieżka instalacji, wolna pamięć RAM, wolne miejsce na dysku |

### Wskaźnik kondycji

| Status | Znaczenie |
| :--- | :--- |
| ✅ **Online** | WatchDog jest połączony i aktywny |
| ⚠️ **Offline** | Brak heartbeat od ponad 30 sekund |
| ❌ **Not Installed** | WatchDog nigdy nie połączył się z tą organizacją |

---

## 4. Karta Logs

Przeglądaj wszystkie zdarzenia WatchDog zapisane w OpenSearch.

<figure><img src="../../../.gitbook/assets/watchdog_v2_05.png" alt="Logi WatchDog"><figcaption></figcaption></figure>

* Filtruj według daty, typu zdarzenia lub słów kluczowych
* Typy zdarzeń: `FILE_IMPORT_STARTED`, `FILE_IMPORT_COMPLETED`, `FILE_IMPORT_FAILED`, `EXPORT_STARTED`, `EXPORT_COMPLETED`, `EXPORT_FAILED`, `FOLDER_VALIDATION_FAILED`, `CONFIG_LOADED`, `SERVICE_RESTART_INITIATED`, `SERVICE_RESTART_COMPLETED`

---

## 5. Karta XSLT Templates

Zarządzaj szablonami transformacji XSLT używanymi do eksportów XML.

<figure><img src="../../../.gitbook/assets/watchdog_v2_06.png" alt="Lista szablonów XSLT"><figcaption></figcaption></figure>

* Przesyłaj i edytuj szablony XSLT
* **Walidacja na żywo** — testuj szablony na przykładowym XML z analizą pól
* Łącz szablony z konfiguracjami eksportu
* Zobacz liczbę użyć (które konfiguracje używają danego szablonu)

<figure><img src="../../../.gitbook/assets/watchdog_v2_07.png" alt="Edytor szablonów XSLT"><figcaption></figcaption></figure>

---

## 6. Karta Export Configurations

Przegląd wszystkich aktywnych konfiguracji eksportu ze stanem połączenia.

* Monitoruj znacznik czasu ostatniego udanego połączenia
* Zarządzaj konfiguracjami bezpośrednio na liście (edycja, kopiowanie, usuwanie)
* Kopiuj zbiorczo konfiguracje między podorganizacjami
