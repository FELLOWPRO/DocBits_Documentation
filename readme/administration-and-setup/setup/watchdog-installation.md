# Instalacja WatchDog

<figure><img src="../../.gitbook/assets/watchdog-infographic-pl.png" alt="WatchDog Infographic"><figcaption></figcaption></figure>

### Konfigurowanie WatchDog w DocBits

1. **Dostęp do ustawień WatchDog**
   * Przejdź do **Ustawienia → Przetwarzanie dokumentów → WatchDog**.
2. **Ustawienia folderów**
   * Zdefiniuj ścieżki, w których WatchDog znajduje i przetwarza dokumenty.
   *   Ścieżki folderów powinny odpowiadać tym utworzonym podczas instalacji:

       * `C:/WatchDog/Read`
       * `C:/WatchDog/Processed`

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzG1EFmtSO4AxZjWir401%252Fimage.png%3Falt%3Dmedia%26token%3Dc356e023-8cfb-4f45-b863-b27c5af1d9df\&width=768\&dpr=4\&quality=100\&sign=1b1ae0c4\&sv=2)
   * <mark style="color:red;">**Uwaga**</mark><mark style="color:red;">:</mark> **Zaleca się używanie lokalnych ścieżek. Powinny one odpowiadać folderom w instalacji DocBits**
3. **Ustawienia ogólne**
   *   Wybierz typy dokumentów do przetworzenia, zaznaczając odpowiednie pola wyboru.\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZbCt5UHd37PdNZsVItdt%252Fimage.png%3Falt%3Dmedia%26token%3Db3c3f203-0f60-42a0-bd56-ee70c204f5e8\&width=768\&dpr=4\&quality=100\&sign=becd5e31\&sv=2)
   * **Podział kodów kreskowych:** Włączony umożliwia podział kodów kreskowych.
   * **Operator DocBits:** Po włączeniu otwiera przeglądarkę Chrome w tle dla Operatora DocBits.
   * **Miejsce eksportu:** Ustawia miejsce eksportu.
     * **Infor:** Dokumenty są eksportowane do Infor.
     * **Folder eksportu:** Dokumenty są eksportowane do zdefiniowanego folderu, który można skonfigurować poniżej.
4. **Konfiguracje eksportu**
   * Wyświetla wszystkie skonfigurowane eksporty dla **przetwarzania lokalnego**.
   *   Pokazuje znacznik czasu **ostatniego udanego połączenia** dla każdej konfiguracji.\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FRvK5qn6EggWJxcSYNP5J%252Fimage.png%3Falt%3Dmedia%26token%3D195b9cc6-c5ac-4ee6-90da-b3ee9696ee30\&width=768\&dpr=4\&quality=100\&sign=3bc11ec5\&sv=2)
5. **Konfiguracja bod\_mapping (Opcjonalnie)**
   * <mark style="color:red;">**Wymagane pola:**</mark> Zanim dodasz niestandardowe mapowania metadanych, musisz zdefiniować następujące dwa wartości
     * **`file_name`**
     * **`pdf_path`**
   *   Kliknij **Dodaj wiersz**, aby zdefiniować mapowania metadanych.\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlzUqcr51kq18OrmYAR8X%252Fimage.png%3Falt%3Dmedia%26token%3D3035122b-f1d3-44cc-bfe6-5230943bd77d\&width=768\&dpr=4\&quality=100\&sign=e98d5a1b\&sv=2)
   * **Wartość:** Określa nazwę pola dla metadanych.
   * **Ścieżka:** Wyrażenie XPath wskazujące na dane XML, które powinny być przypisane do pola.
   * **Ikona kosza:** Używana do usunięcia konkretnego wiersza.
6. **Pobierz konfigurację**
   * Zapisz konfigurację
   *   Pobierz konfigurację\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZXiz4KB7QpnaqD9XwX3o%252Fimage.png%3Falt%3Dmedia%26token%3D04c9f8dc-7d79-443f-9ce4-6d4214edc98b\&width=768\&dpr=4\&quality=100\&sign=574a4218\&sv=2)

### Przewodnik instalacji WatchDog

1. **Utwórz wymagane foldery**
   * Utwórz główny katalog: `C:/WatchDog`
   * Wewnątrz `C:/WatchDog` utwórz następujące podfoldery: **Uwaga:** powinny one odpowiadać folderom w DocBits.
     * `C:/WatchDog/Read`
     * `C:/WatchDog/Processed`
   * <mark style="color:red;">**Uwaga:**</mark>**&#x20;Zaleca się używanie lokalnych ścieżek. Powinny one odpowiadać folderom w konfiguracji DocBits**
2. **Pobierz WatchDog**
   * Pobierz najnowszą wersję `WatchDog.exe` z: [https://github.com/Fellow-Consulting-AG/WatchDog](https://github.com/Fellow-Consulting-AG/WatchDog)
   * Umieść pobrany plik `WatchDog.exe` w `C:/WatchDog`.
   * Umieść pobrany plik `watchdog-config.json` w `C:/WatchDog`.
   * Otwórz `watchdog-config.json` i zmień **config\_path.**
   * W tym przykładzie:
     * `"config_path": "C:/WatchDog/watchdog-config.json"`
3. **Zainstaluj WatchDog**
   * Otwórz **Wiersz polecenia (CMD)** z **uprawnieniami administratora**.
   * Przejdź do folderu WatchDog.
   *   Uruchom następujące polecenie, aby zainstalować WatchDog:

       `WatchDog.exe install`
4. **Uruchom usługę WatchDog**
   *   Uruchom następujące polecenie w CMD:

       `WatchDog.exe start`
5. **Ustaw typ uruchamiania**
   * Otwórz **Usługi** (Naciśnij `Win + R`, wpisz `services.msc` i naciśnij **Enter**).
   * Zlokalizuj **WatchDog** na liście usług.
   * Kliknij dwukrotnie, aby otworzyć jego właściwości.
   * Ustaw **Typ uruchamiania** na **Automatyczny (opóźniony start)**.
   * Kliknij **OK**.
