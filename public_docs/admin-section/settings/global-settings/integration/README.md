# Integracja

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.39.14.png" alt=""><figcaption></figcaption></figure>

## Klucz API

* **Klucz**: Jest to unikalny identyfikator używany przez zewnętrzne aplikacje do uzyskiwania dostępu do interfejsu API DocBits. Jest kluczowy do uwierzytelniania żądań wysyłanych do DocBits z innych oprogramowań.
* Tutaj można wykonać czynności takie jak wyświetlanie, odtwarzanie lub kopiowanie klucza API, w zależności od konkretnych potrzeb i protokołów bezpieczeństwa.

## Ustawienia dostawcy usługi SSO (Single Sign-On)

* **ID jednostki**: Jest to identyfikator DocBits jako dostawcy usługi w konfiguracji SSO. Unikalnie identyfikuje DocBits w ramach struktury SSO.
* **URL SLO (Single Logout)**: Adres URL, pod który wysyłane są sesje SSO w celu jednoczesnego wylogowania ze wszystkich aplikacji połączonych za pomocą SSO.
* **URL SSO**: Adres URL używany do rozpoczęcia procesu logowania jednokrotnego.
* Dostępne są czynności takie jak "Pobierz certyfikat" i "Pobierz metadane" w celu uzyskania niezbędnych certyfikatów bezpieczeństwa i informacji metadanych używanych do konfigurowania i utrzymywania integracji SSO.

{% hint style="info" %}
Zobacz [Konfiguracja SSO](../../../setup/sso-configuration/)
{% endhint %}

## Ustawienia dostawcy usługi Identyfikacji

* **ID najemcy**: Może być używane, gdy DocBits integruje się z usługami chmurowymi, które wymagają identyfikatora najemcy do zarządzania danymi i konfiguracjami dostępu specyficznymi dla firmy korzystającej z DocBits.
* **Prześlij plik**: Pozwala administratorowi przesłać pliki konfiguracyjne lub inne niezbędne pliki ułatwiające integrację z dostawcą tożsamości.
* **Skonfiguruj**: Przycisk do zastosowania lub aktualizacji ustawień po dokonaniu zmian lub przesłaniu nowych konfiguracji.
