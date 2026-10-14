# Edytowanie szablonów e-maili

#### Przegląd

Funkcja szablonów e-maili pozwala administratorom na tworzenie i dostosowywanie komunikacji e-mailowej, która jest automatycznie wysyłana do dostawców. Jednym z kluczowych elementów używanych w tych szablonach jest `{{magic_link}}`, który zapewnia dynamiczny link dostosowany do każdego odbiorcy.

**Czym jest `{{magic_link}}`?**

`{{magic_link}}` to znacznik, który jest dynamicznie zastępowany unikalnym URL-em w momencie wysyłania e-maila. Ten URL zazwyczaj kieruje odbiorcę do wykonania akcji, takiej jak rejestracja, zatwierdzenie lub uzyskanie dostępu do konkretnej części portalu dostawcy.

#### Edytowanie szablonów e-maili

**Uzyskiwanie dostępu do edytora szablonów e-maili**

1. **Przejdź do szablonów e-maili**:
   * Przejdź do sekcji **Szablony e-maili** z głównego menu.
2. **Wybierz szablon do edycji**:
   * Wybierz szablon e-maila, który chcesz edytować, klikając na nazwę szablonu (np. "E-mail zaproszenia dla dostawcy").
3. **Edytuj szablon**:
   * Edytor pozwala na modyfikację zarówno kodu HTML, jak i wizualnego wyglądu e-maila.
   * Możesz przełączać się między edytowaniem wizualnym a edytowaniem kodu, korzystając z dostępnych zakładek.

**Definiowanie `{{magic_link}}` jako linku**

Aby zdefiniować `{{magic_link}}` jako klikalny link w e-mailu, musisz upewnić się, że jest on poprawnie sformatowany w kodzie HTML szablonu. Wykonaj następujące kroki:

1. **Zlokalizuj sekcję linku w kodzie HTML**:
   * W edytorze kodu znajdź sekcję, w której chcesz, aby magiczny link się pojawił. Zazwyczaj znajduje się to w tagu `<a>` (kotwicy).
2.  **Wstaw znacznik `{{magic_link}}`**:

    * Zastąp atrybut `href` tagu kotwicy `{{magic_link}}`.
    * Upewnij się, że link jest odpowiednio stylizowany dla szablonu e-maila. Oto przykład:

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
        Zakończ rejestrację
    </a>
    ```

#### 3. Dostosuj tekst linku:

• Zmień tekst pomiędzy otwierającymi \<a> a zamykającymi \</a> tagami, aby odzwierciedlał akcję, którą chcesz, aby użytkownik wykonał. Na przykład „Zakończ rejestrację” lub „Uzyskaj dostęp do swojego konta”.

4. Zapisz i przetestuj szablon:

• Po wprowadzeniu zmian kliknij przycisk Zapisz.

• Możesz użyć przycisku Wyślij test, aby wysłać testowy e-mail i upewnić się, że link działa zgodnie z oczekiwaniami.

### Najlepsze praktyki dotyczące używania \{{magic\_link\}}

• Umiejscowienie linku: Umieść \{{magic\_link\}} w widocznym miejscu w e-mailu, aby zapewnić łatwy dostęp dla odbiorców.

• Jasne wezwanie do działania: Tekst w linku powinien być jasnym wezwaniem do działania, takim jak „Zakończ rejestrację” lub „Potwierdź swój e-mail”.

• Stylizacja: Upewnij się, że link jest stylizowany w sposób spójny z resztą szablonu e-maila i wyróżnia się wizualnie.

• Testowanie: Zawsze wysyłaj testowy e-mail po edytowaniu szablonu, aby zweryfikować, że \{{magic\_link\}} działa poprawnie i stylizacja jest odpowiednia.

### Podsumowanie

Poprawne zdefiniowanie \{{magic\_link\}} w szablonach e-maili zapewnia, że odbiorcy otrzymują spersonalizowany i wykonalny e-mail, który prowadzi ich do odpowiedniego zadania w Twoim portalu dostawcy. To poprawia doświadczenie użytkownika i zapewnia płynne procesy onboardingu i komunikacji.

\\

Dokumentacja ta zawiera szczegółowe instrukcje krok po kroku dla administratorów dotyczące definiowania i używania \{{magic\_link\}} w szablonach e-maili, zapewniając, że e-maile są zarówno funkcjonalne, jak i estetycznie atrakcyjne.
