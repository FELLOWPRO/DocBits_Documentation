# Asystent AI w edytorze skryptów

Edytor skryptów ma wbudowanego **Asystenta AI**, który pisze i wyjaśnia skrypty DocBits. Opisujesz zwykłym językiem, co skrypt ma robić, a asystent odpowiada kodem Python, który możesz skopiować do edytora.

{% hint style="info" %}
Asystent AI jest częścią **DocNet**. Do jego używania Twoja organizacja potrzebuje aktywnej subskrypcji DocNet. Zobacz [Plan subskrypcji](../../subscription-plan/README.md) i [Moduł](../../../document-processing/module/README.md).
{% endhint %}

## Otwieranie asystenta

1. Przejdź do **Ustawienia → Typy dokumentów**, otwórz typ dokumentu i kliknij **Skrypty**.
2. Kliknij **Nowy** albo otwórz istniejącą wersję skryptu jako wersję roboczą.
3. Kliknij ikonę robota obok nazwy skryptu. Po prawej stronie edytora otworzy się panel **Asystent AI**.

## Co wie asystent

Przy każdym pytaniu DocBits przekazuje asystentowi:

* **dokumentację skryptów** (funkcje opisane w [Skrypty w DocBits](scripting-in-docbits/README.md)),
* **typ dokumentu** skryptu,
* **bieżący skrypt** z edytora,
* **nazwy pól i kolumny tabel** używane przez Twoją organizację dla tego typu dokumentu.

Dzięki nazwom pól asystent używa Twoich prawdziwych pól, na przykład `invoice_date` lub `purchase_order`, w `get_field_value()` i `set_field_value()`.

## Pisanie skryptu z asystentem

1. Wpisz swoją prośbę w polu na dole panelu, na przykład: *Ustaw walutę na EUR, jeśli jest pusta.*
2. Naciśnij **Enter** albo kliknij ikonę wysyłania. Odpowiedź pojawia się stopniowo.
3. Kliknij ikonę kopiowania (podpowiedź **Kopiuj do redaktora**) obok bloku kodu, aby wstawić kod do edytora skryptów.
4. Sprawdź kod, nadaj skryptowi nazwę i zapisz go jako wersję roboczą.

Pytania uzupełniające działają w tym samym panelu. Wklej komunikat o błędzie albo zapytaj *Dlaczego ten skrypt nie ustawia terminu płatności?*, a asystent przeanalizuje bieżący skrypt w edytorze.

## Zawsze sprawdzaj wynik

{% hint style="warning" %}
Asystent może popełniać błędy. Przeczytaj wygenerowany kod, sprawdź, czy nazwy pól odpowiadają Twojemu typowi dokumentu, i przetestuj skrypt na dokumencie testowym przed jego aktywacją. Zobacz [Testowanie skryptów](testing-scripts.md).
{% endhint %}

Skrypty działają tylko z zatwierdzonymi funkcjami skryptowymi. Jeśli skrypt wywołuje nieistniejącą funkcję, DocBits odrzuca go z komunikatem *Unknown function*.

## Użycie i limity

* Każda odpowiedź pokazuje pod treścią liczbę zużytych tokenów (wejściowych, wyjściowych i łącznie).
* Zużycie jest rejestrowane jako zużycie DocNet Twojej organizacji.
* DocBits odrzuca żądanie, gdy brakuje subskrypcji DocNet (*DocNet subscription required*), wygasła ona (*DocNet subscription expired*) albo limit został wyczerpany (*DocNet quota exhausted*).

## Powiązane strony

* [Tworzenie i edytowanie skryptów](creating-and-editing-scripts.md)
* [Funkcje Pol](scripting-in-docbits/field-functions.md)
* [Przykładowe Skrypty](scripting-in-docbits/sample-scripts/README.md)
* [Aktywowanie skryptów i zarządzanie nimi](script-activation-and-management.md)
