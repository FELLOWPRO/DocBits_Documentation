# Przetestuj swoje połączenie BOD za pomocą Postman

## Przegląd

Ta strona wyjaśnia, jak zweryfikować pomyślne przetwarzanie twojego BOD (Business Object Document) za pomocą Postman. Przetestujesz odpowiedni punkt końcowy API, wysyłając żądanie z plikiem mapowania BOD. Postępuj zgodnie z poniższymi krokami, aby zakończyć proces.

## Uzyskiwanie dostępu do Klucza API i Pliku mapowania BOD

### Pobieranie Klucza API

1.  Przejdź do **Ustawienia → Ustawienia globalne → Integracja i SSO**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_integration.png)
2.  Możesz ręcznie skopiować swój **Klucz API** lub kliknąć przycisk kopiowania, aby skopiować go do schowka.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_1.png)

### **Pobieranie Pliku mapowania BOD**

1.  Przejdź do **Ustawienia → Przetwarzanie dokumentów → Eksport**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
2.  W kolumnie **Akcje** odpowiedniego wpisu eksportu kliknij menu z trzema kropkami i wybierz **Redagować**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_2.png)
3.  Zlokalizuj **Plik mapowania BOD** i kliknij przycisk **Pobierać**, aby go zapisać.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_3.png)

## Przetestuj punkt końcowy w Postman

1.  **Wklej polecenie cURL w Postman**

    Otwórz Postman i wklej następujące polecenie cURL w sekcji **Import**. Postman automatycznie skonfiguruje żądanie.

    ```bash
    curl -X 'POST' \
      'https://api.docbits.com/prod-api/import/purchase_order_bod' \
      -H 'accept: application/json' \
      -H 'X-API-KEY:' \
      -H 'Content-Type: multipart/form-data' \
      -F 'org_id=' \
      -F 'sub_org_id=' \
      -F 'file=@file.xml;type=text/xml' \
      -F 'custom_fields_mapping='
    ```

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_4.png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_5.png)
2.  **Ustaw Klucz API**\
    Przejdź do zakładki **Headers**, zlokalizuj nagłówek `X-API-KEY` i wklej swój klucz API do kolumny **Value**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_6.png)
3.  **Prześlij plik BOD**\
    Przejdź do zakładki **Body**, zlokalizuj klucz `file`, a następnie kliknij **Select Files** w kolumnie **Value** i prześlij swój plik BOD XML.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_7.png)
4.  **Wyślij żądanie**\
    Kliknij **Send**, aby wykonać wywołanie API.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_8.png)
5.  **Zweryfikuj odpowiedź**\
    Sprawdź odpowiedź, aby potwierdzić, że twój BOD został pomyślnie przetworzony.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_9.png)
