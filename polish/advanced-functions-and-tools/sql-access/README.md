# SQL Access

<figure><img src="../../.gitbook/assets/sql_direct_access_settings.png" alt="Ustawienia SQL Direct Access"><figcaption></figcaption></figure>

## Przegląd

W module ustawień DocBits administratorzy mogą uzyskać bezpośredni dostęp do bazy danych BI za pomocą SQL. Ta funkcja jest przeznaczona do zaawansowanego zarządzania danymi i niestandardowych potrzeb raportowych.

### Dostęp do SQL Direct Access

Przejdź do sekcji SQL Direct Access w module ustawień. Znajdziesz tam dane uwierzytelniające i szczegóły dostępu, w tym nazwę użytkownika, hasło, nazwę bazy danych i informacje o hoście.

* **Nazwa użytkownika:** user\_23f3d6
* **Hasło:** _Zaszyfrowane_
* **Baza danych:** demo
* **Host:** zobacz na zrzucie ekranu

## **Przykładowe dane dostępu:**

```sql
SELECT
    COUNT(*),
    status,
    invoice_type
FROM dashboard
GROUP BY
    status,
    invoice_type

```

#### Wyniki przykładowego zapytania

Poniższe wyniki przedstawiają liczbę dokumentów według statusu i typu faktury:

* **Ready for Validation:** 71 faktur, 6 nieokreślonych
* **Pending Confirmation:** 1 nieokreślony
* **Finished:** 3 nieokreślone, 1 faktura
* **Error:** 2 nieokreślone

#### Użycie clickhouse-client do dostępu z terminala

Programiści, którzy wolą pracować w terminalu, mogą nawiązać połączenie za pomocą `clickhouse-client`:

```bash
clickhouse-client --host <hostname_or_ip> --port <port> --user <username> --password <your_password> --database <database_name>

```

### Tworzenie widoków zmaterializowanych

Zalecamy tworzenie widoków zmaterializowanych do wstępnego obliczania danych, aby zwiększyć wydajność w narzędziach analitycznych, takich jak PowerBI:

```sql
SELECT toStartOfWeek(created_on) as week_start, sum(toFloat64OrZero(field_value)) as total_sum
FROM document_extracted_data
WHERE field_name = 'total_amount'
GROUP BY week_start

```

Ten przykład pokazuje, jak zgrupować łączne kwoty według tygodnia ich utworzenia, co jest przydatne w tygodniowych zestawieniach finansowych lub ścieżkach audytu.

## Dodatkowe zasoby

Aby uzyskać dalszą pomoc lub zaawansowaną konfigurację, skontaktuj się z naszym zespołem wsparcia lub skorzystaj z naszych obszernych szkoleń wideo dostępnych w sekcji pomocy.
