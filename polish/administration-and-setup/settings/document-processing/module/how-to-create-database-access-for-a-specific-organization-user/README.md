# Jak utworzyć dostęp do bazy danych dla konkretnego użytkownika organizacji

### **1. Zaloguj się do DocBits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Przejdź do strony logowania swojej aplikacji.
2. Wprowadź swoje dane uwierzytelniające (nazwę użytkownika i hasło), aby się zalogować.

### **2. Otwórz ustawienia** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Po zalogowaniu znajdź ikonę **Settings** (koło zębate ⚙️) na lewym pasku bocznym.
2. Kliknij **Settings**, aby otworzyć panel konfiguracji systemu.

### **3. Otwórz moduł Document Processing** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. W **Settings** znajdź sekcję **Document Processing**.
2. W sekcji **Document Processing** znajdź i kliknij opcję **Module**.
   * Otworzy to odpowiednią stronę konfiguracji modułu, na której możesz przejść do tworzenia użytkownika bazy danych.

### 4. Kroki umożliwiające włączenie i uzyskanie dostępu do AI Document oraz użytkownika bazy danych: <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Przełącz funkcje**:
   * Użyj przełączników po prawej stronie, aby włączyć lub wyłączyć wybrane funkcje:
     * **AI Document Warehouse**: Włącz, aby uzyskać dostęp do funkcji związanych z AI.
     * **DB Access**: Włącz, aby przyznać użytkownikowi dostęp do bazy danych.
2. **Dane uwierzytelniające bazy danych**:
   * Dashboard udostępnia następujące szczegóły połączenia z bazą danych:
     * **Username**: Wyświetlana jest unikalna nazwa użytkownika
     * **Password**: Upewnij się, że hasło jest bezpiecznie przechowywane lub skopiowane.
     * **Database**: Nazwa bazy danych
     * **Host**: Nazwa hosta
     * **Port**: Port
     * **SSL Mode:** Połączenie wymaga `sslmode=require` dla bezpiecznej komunikacji.
3. **Kopiowanie danych uwierzytelniających**:
   * Użyj ikon kopiowania obok każdego pola, aby szybko skopiować dane uwierzytelniające do klienta bazy danych lub aplikacji.
4. **Połączenie przez DBeaver**:
   * Połącz przez Host
     * wybierz PostgreSQL
     * Wypełnij wymagane informacje
     * przejdź na zakładkę SSL i zaznacz Use SSL. Przewiń w dół do SSL mode i wybierz require
   * Połącz przez URL
     * Wypełnij wymagane informacje:\n - zamień Host na podane informacje o hoście\n - zamień Port na podane informacje o porcie\n - zamień Database na podane informacje o bazie danych\n - dla Username wybierz podane informacje o nazwie użytkownika\n - dla Password wybierz podane informacje o haśle
5. **Przetestuj połączenie**:
   * Kliknij przycisk **"Test Connection"**, aby upewnić się, że dane uwierzytelniające i szczegóły połączenia są poprawne.
   * Jeśli test się powiedzie, przejdź do połączenia.
6. **Przeglądaj bazę danych**:
   * Po połączeniu przejdź w kliencie bazy danych do sekcji **schema** lub **tables**.
   * Sprawdź dostępne tabele.
