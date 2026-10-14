# Ustawienia tolerancji zamówienia zakupu / Dodatkowa tolerancja zamówienia zakupu

### **Ustawienie do konfigurowania tolerancji zamówienia zakupu**

Przejdź do **Ustawienia → Ustawienia ogólne → Typy dokumentów → Więcej ustawień → Sekcja zamówienia zakupu → Ustawienie tolerancji PO**

#### **Jak to działa**

Po włączeniu to ustawienie pozwala zdefiniować tolerancje dla **Ilości** i/lub **Ceny jednostkowej**. Tolerancje te mogą być ustawione jako procent lub jako wartość stała. Oznacza to, że faktura może odbiegać od zamówienia zakupu (PO) w określonym zakresie tolerancji, nie będąc oznaczoną jako niezgodność, co zapewnia elastyczność przy jednoczesnym zapewnieniu płynności przetwarzania.

<mark style="color:red;">**UWAGA**</mark>: Tolerancje działają w obie strony; to znaczy, że wartość faktury może być zarówno wyższa, jak i niższa niż wartość PO w dozwolonym zakresie.

#### **Jak to ustawić**

* **Włącz ustawienie:**
  * Włącz ustawienie tolerancji PO za pomocą przycisku przełącznika.
* **Skonfiguruj tolerancje:**
  * Pojawią się cztery pola:
    * Jedno pole dla **Kwoty tolerancji ilości**.
    * Jedno pole dla **Kwoty tolerancji ceny jednostkowej**.
  * Za każdym polem znajduje się menu rozwijane, w którym można wybrać typ tolerancji:
    * **Procent:** Wskazuje tolerancję procentową.
    * **Wartość:** Wskazuje stałą kwotę, o którą wartość może się różnić.

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2Fs661pgIKUsLzwhxU4kes%2Fimage.png?alt=media\&token=6d152cde-14d8-4caf-bcc8-acf1a1fe497c)

#### **Przykładowy scenariusz:**

* Załóżmy, że **Tolerancja ceny jednostkowej** jest ustawiona na **5%**.
* Zamówienie zakupu zawiera dwie pozycje:
  * **Pozycja 1:** Cena jednostkowa = **5,00 $**
  * **Pozycja 2:** Cena jednostkowa = **2,00 $**
* Na fakturze:
  * **Pozycja 1:** Cena jednostkowa została dostosowana do **4,80 $** (**w ramach** tolerancji 5%).
  * **Pozycja 2:** Cena jednostkowa została dostosowana do **2,20 $** (**poza** tolerancją 5%).
* **Wynik:**
  * Pozycja 1 **nie jest oznaczona** jako niezgodność, ponieważ 4,80 $ mieści się w 5% od 5,00 $.
  * Pozycja 2 **jest oznaczona** jako niezgodność, ponieważ 2,20 $ przekracza dozwoloną 5% odchylenie od 2,00 $. Użytkownik musi podjąć działania w celu rozwiązania niezgodności przed dalszym przetwarzaniem faktury.​

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2Fn5ki5044GfbGekHWyjhs%2Fimage.png?alt=media\&token=6e1e641b-4d6d-4236-a375-72edcfc98529)

### Ustawienie do konfigurowania dodatkowych ustawień tolerancji zamówienia zakupu

Przejdź do **Ustawienia → Ustawienia ogólne → Typy dokumentów → Więcej ustawień → Sekcja zamówienia zakupu → Dodatkowe ustawienie tolerancji PO**

#### **Jak to działa**

Po włączeniu to ustawienie pozwala zdefiniować tolerancje dla **Transportu**, **Opłat** i/lub **Podatku**. Tolerancje te mogą być ustawione jako procent lub jako wartość stała, co umożliwia niewielkie różnice faktur w stosunku do wartości PO bez oznaczania ich jako niezgodności. To zapewnia dodatkową elastyczność i gwarantuje, że drobne różnice nie przerywają przepływu pracy.

<mark style="color:red;">**UWAGA**</mark>: Podobnie jak standardowe ustawienia tolerancji, te tolerancje mają zastosowanie w obie strony — pozwalając na wzrosty lub spadki w ramach ustalonych limitów.

#### **Jak to ustawić**

* **Włącz ustawienie:**
  * Włącz dodatkowe ustawienie tolerancji PO za pomocą przycisku przełącznika.
* **Skonfiguruj tolerancje:**
  * Pojawią się sześć pól:
    * Jedno pole dla kwot tolerancji dla **Transportu**, **Opłat** i **Podatku**.
  * Każde pole ma towarzyszące menu rozwijane, w którym można wybrać typ tolerancji:
    * **Procent:** Tolerancja jest definiowana jako procent.
    * **Wartość:** Tolerancja jest definiowana jako stała kwota.

<figure><img src="../../../../../../.gitbook/assets/docbits_purchase_order_supplier.png" alt="DocBits Zakup Zamówienie Dostawca"><figcaption></figcaption></figure>
