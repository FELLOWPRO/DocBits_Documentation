# Obliczanie ceny jednostkowej zamówienia zakupu

## **Przegląd**

Możesz wybrać automatyczne obliczanie **ceny jednostkowej** każdej pozycji zamówienia zakupu na podstawie **kwoty** i **ilości** z tej pozycji, zamiast używać ceny jednostkowej podanej w zamówieniu zakupu. Jest to szczególnie przydatne, gdy cena jednostkowa w zamówieniu zakupu (w Infor ERP / SAP) różni się od ceny na dokumencie. Takie rozbieżności mogą wystąpić, jeśli do ceny jednostkowej w zamówieniu zakupu zastosowano rabat, podczas gdy na dokumencie rabat jest stosowany tylko do kwoty netto.

## **Kroki aktywacji**

1.  Przejdź do **Ustawienia** -> **Ustawienia globalne** -> **Typy dokumentów**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Wybierz żądany typ dokumentu i kliknij **Więcej ustawień**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  W sekcji **Zamówienie zakupu** włącz opcję **Oblicz cenę jednostkową zamówienia**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_3.png" alt=""><figcaption></figcaption></figure>

## Jak obliczana jest cena

Po aktywowaniu ustawienia cena jednostkowa pozycji zamówienia zakupu jest obliczana jako:

**`Cena jednostkowa = Kwota pozycji ÷ Ilość × Cena jednostkowa za`**

gdzie **kwota pozycji** jest wybierana w następujący sposób:

| Pozycja zamówienia zakupu zawiera                                                         | Używana kwota pozycji                 |
| ------------------------------------------------------------------------------------------ | ------------------------------------ |
| **kwotę netto** (`extended_amount`) większą niż 0 i nieprzekraczającą sumy pozycji          | kwotę netto                          |
| brak kwoty netto lub kwota netto przekracza sumę pozycji                                  | sumę pozycji (`total_amount`)         |
| brak dodatniej kwoty lub brak dodatniej ilości                                            | nic nie jest obliczane, cena PO pozostaje |

Dlaczego kwota netto jest wybierana jako pierwsza: Dane ERP (Infor BODs) przesyłają netto kwotę pozycji jako `extended_amount` i zawierają **podatek i opłaty dodatkowe** w `total_amount`. Podzielenie kwoty brutto przez ilość daje cenę jednostkową brutto, a każda faktura wyceniona netto wtedy pokazuje się jako _cena jednostkowa niedopasowana_, mimo że jest poprawna. Przykład z rzeczywistej pozycji zamówienia: ilość 9, kwota netto 879,84, suma 954,63 (podatek 8,5%) — cena oparta na kwocie netto to 97,76 i zgadza się z fakturą; cena oparta na sumie to 106,07.

Kwota netto, która jest **większa** niż suma pozycji, nie może być kwotą netto, dlatego w takim przypadku używana jest suma. `Cena jednostkowa za` równa 0 lub pusta jest traktowana jako 1.

{% hint style="info" %}
Obliczona cena jest zapisywana w migawce zamówienia zakupu przechowywanej na dokumencie i jest **przeliczana za każdym razem, gdy dokument jest dopasowywany** (Auto PO Match, dopasowanie ręczne, dopasowanie przy zapisie). Dokument, który był dopasowany przed zmianą ustawienia, przy następnym dopasowaniu pobiera nową cenę — nie jest wymagane ponowne załadowanie zamówienia zakupu.
{% endhint %}

## Przykład:

<figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_4.png" alt="" width="563"><figcaption></figcaption></figure>

W tym przypadku cena jednostkowa (bez rabatu) jest pobierana z dokumentu, podczas gdy zamówienie zakupu w ERP przechowuje cenę jednostkową z zastosowanym rabatem. Powoduje to rozbieżność w cenie jednostkowej. Po aktywowaniu ustawienia cena jednostkowa jest pobierana z kwoty pozycji i ilości, dzięki czemu obie strony się zgadzają.

## Powiązane ustawienia

* [Reguły dopasowywania zamówień zakupu](purchase-order-matching-rules.md) — reguły porównują **efektywną** cenę jednostkową, która jest tą obliczoną ceną, gdy ustawienie jest włączone.
* [Ustawienia tolerancji zamówienia zakupu](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) — o ile cena faktury może różnić się od ceny obliczonej.