# Edytowanie szablonów e-maili

<figure><img src="../../../.gitbook/assets/supplier_email_templates.png" alt="Szablony e-maili dostawców"><figcaption><p>Strona szablonów e-maili dostawców</p></figcaption></figure>

### Przegląd

Funkcja Email Templates pozwala administratorom tworzyć i dostosowywać komunikację e-mailową, która jest automatycznie wysyłana do dostawców. Jednym z kluczowych elementów używanych w tych szablonach jest `{{magic_link}}`, który zapewnia dynamiczny link dostosowany do każdego odbiorcy.

#### Czym jest `{{magic_link}}`?

`{{magic_link}}` to znacznik zastępczy, który jest dynamicznie zastępowany unikalnym adresem URL w momencie wysyłania e-maila. Ten adres zazwyczaj kieruje odbiorcę do wykonania akcji, takiej jak rejestracja, zatwierdzenie lub uzyskanie dostępu do konkretnej części portalu dostawcy.

### Edytowanie szablonów e-maili

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-08-25 um 12.35.53.png" alt=""><figcaption></figcaption></figure>

#### Dostęp do edytora szablonów e-maili

1. **Przejdź do Email Templates**:
   * Przejdź z menu głównego do sekcji **Email Templates**.
2. **Wybierz szablon do edycji**:
   * Wybierz szablon e-maila, który chcesz edytować, klikając jego nazwę (np. „Supplier Invitation Email”).
3. **Edytuj szablon**:
   * Edytor pozwala modyfikować zarówno kod HTML, jak i wizualny wygląd e-maila.
   * Możesz przełączać się między edycją wizualną a edycją kodu za pomocą dostępnych zakładek.

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-08-25 um 12.36.41.png" alt=""><figcaption></figcaption></figure>

#### Definiowanie `{{magic_link}}` jako linku

Aby zdefiniować `{{magic_link}}` jako klikalny link w e-mailu, musisz upewnić się, że jest on poprawnie sformatowany w kodzie HTML szablonu. Wykonaj następujące kroki:

1. **Znajdź sekcję linku w kodzie HTML**:
   * W edytorze kodu znajdź miejsce, w którym ma się pojawić magic link. Zazwyczaj znajduje się ono wewnątrz tagu `<a>` (kotwicy).
2.  **Wstaw znacznik zastępczy `{{magic_link}}`**:

    * Zastąp atrybut `href` tagu kotwicy wartością `{{magic_link}}`.
    * Upewnij się, że link jest odpowiednio ostylowany dla szablonu e-maila. Oto przykład:

    ```html
    <a href="{{magic_link}}" target="_blank" style="
        background-color: #B7184B;
        border-radius: 25px;
        font-family: 'Montserrat', Arial, sans-serif;
        font-size: 14px;
        font-weight: bold;
        padding: 12px 25px;
        color: #FFFFFF;
        text-decoration: none;
        display: inline-block;
        cursor: pointer;">
        Complete Registration
    </a>
    ```

### 3. Dostosuj tekst linku:

• Zmień tekst między otwierającym \<a> a zamykającym \</a> tak, aby odzwierciedlał akcję, którą użytkownik ma wykonać. Na przykład „Complete Registration” lub „Access Your Account”.

4\. Zapisz i przetestuj szablon:

• Po wprowadzeniu zmian kliknij przycisk Save.

• Możesz użyć przycisku Send Test, aby wysłać testowy e-mail i upewnić się, że link działa zgodnie z oczekiwaniami.

## Najlepsze praktyki używania \{{magic\_link\}}

• Umiejscowienie linku: Umieść \{{magic\_link\}} w widocznym miejscu e-maila, aby odbiorcy mieli do niego łatwy dostęp.

• Jasne wezwanie do działania: Tekst w linku powinien być jasnym wezwaniem do działania, takim jak „Complete Registration” lub „Confirm Your Email”.

• Stylizacja: Upewnij się, że link jest ostylowany spójnie z resztą szablonu e-maila i wyróżnia się wizualnie.

• Testowanie: Zawsze wysyłaj testowy e-mail po edycji szablonu, aby sprawdzić, czy \{{magic\_link\}} jest poprawnie rozwiązywany, a stylizacja odpowiednia.

## Podsumowanie

Prawidłowe zdefiniowanie \{{magic\_link\}} w szablonach e-maili zapewnia, że odbiorcy otrzymują spersonalizowany e-mail z jasnym wezwaniem do działania, który prowadzi ich do odpowiedniego zadania w Twoim portalu dostawcy. Poprawia to doświadczenie użytkownika i zapewnia płynny onboarding oraz komunikację.

\


Ta dokumentacja zawiera administratorom instrukcje krok po kroku dotyczące definiowania i używania \{{magic\_link\}} w szablonach e-maili, dzięki czemu e-maile są zarówno funkcjonalne, jak i atrakcyjne wizualnie.
