# Integration & SSO

<figure><img src="../../../../.gitbook/assets/integration_sso.png" alt="Integration & SSO"><figcaption><p>Strona Integration & SSO</p></figcaption></figure>

Strona Integration & SSO służy do zarządzania kluczami API dla dostępu programistycznego, identyfikatorami organizacji oraz konfiguracją jednokrotnego logowania (Single Sign-On, SSO).

## API Key

Zarządzaj kluczami API używanymi do programistycznego dostępu do DocBits.

| Kolumna | Opis |
|--------|-------------|
| **Key** | Zamaskowana wartość klucza API. Kliknij ikonę kopiowania, aby skopiować cały klucz. |
| **Name** | Opisowa nazwa klucza. |
| **Expires** | Data wygaśnięcia (lub „Never”). |
| **Last Used** | Kiedy klucz był ostatnio używany. |
| **Status** | Active lub Inactive. |
| **Actions** | Menu z trzema kropkami do unieważnienia lub usunięcia. |

Kliknij **+ Create API Key**, aby wygenerować nowy klucz.

## ID

Pokazuje identyfikatory Twojej organizacji:

| Pole | Opis |
|-------|-------------|
| **Org ID** | Unikalny identyfikator Twojej organizacji. |
| **Sub Org ID** | Identyfikator aktualnie wybranej podorganizacji. |

## SSO Service Provider Settings

Wartości konfiguracji SSO DocBits potrzebne podczas konfigurowania Twojego dostawcy tożsamości (Identity Provider):

| Pole | Opis |
|-------|-------------|
| **Entity ID** | Adres URL metadanych SAML dla DocBits. |
| **SLO URL** | Adres URL Single Logout. |
| **SSO URL** | Adres URL Assertion Consumer Service. |

Możesz także użyć **Download Certificate** i **Download Metadata** na potrzeby konfiguracji IdP.

## Identity Service Provider Settings

Skonfiguruj zewnętrznego dostawcę tożsamości (IdP):

| Pole | Opis |
|-------|-------------|
| **Tenant ID** | Identyfikator tenanta Twojego IdP. |
| **Upload file** | Prześlij plik XML z metadanymi IdP. |

Kliknij **Configure**, aby zapisać ustawienia IdP.

* **Większa efektywność:** Integracja z innymi narzędziami i usługami może usprawnić przepływy pracy i zwiększyć efektywność. Na przykład dokumenty mogą być automatycznie wymieniane między DocBits a systemem CRM, co ogranicza ręczne wprowadzanie danych i zwiększa produktywność
* **Spójność danych:** Integracja pozwala na płynną wymianę danych między różnymi systemami, poprawiając ich spójność i dokładność. Pozwala to uniknąć niespójności lub podwójnego wprowadzania danych, które mogłyby prowadzić do błędów.
* **Aktualizacje w czasie rzeczywistym**: Integracja umożliwia aktualizacje w czasie rzeczywistym między różnymi platformami, dzięki czemu użytkownicy zawsze mają najnowsze informacje. Jest to szczególnie ważne w krytycznych procesach biznesowych, które wymagają informacji w czasie rzeczywistym.
* **Automatyzacja zadań:** Integracja pozwala automatyzować rutynowe zadania, oszczędzając czas i zasoby. Na przykład powiadomienia mogą być wyzwalane automatycznie, gdy w innym systemie wystąpi określone zdarzenie, bez potrzeby ręcznej interwencji.
* **Lepsze doświadczenie użytkownika:** Dobrze skonfigurowana integracja zapewnia płynne doświadczenie użytkownika, ponieważ użytkownicy nie muszą przełączać się między różnymi systemami, aby uzyskać dostęp do istotnych informacji. Poprawia to zadowolenie użytkowników i przyczynia się do efektywności.

Aby prawidłowo skonfigurować ustawienia integracji, ważne jest zrozumienie wymagań organizacji i zapewnienie, że integracja jest płynnie włączona w istniejące przepływy pracy i procesy. Wymaga to dokładnego planowania, konfiguracji i monitorowania integracji, aby działała bez zakłóceń i dostarczała oczekiwaną wartość.
