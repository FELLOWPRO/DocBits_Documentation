# In Order Confirmation Purchase Order

### Compare with Purchase Order:&#x20;

**In Order Confirmation Purchase Order**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Logic Card: Quantity or Unit Price or Discount Match

Ta karta logiczna służy do automatycznej weryfikacji, czy ilość, cena jednostkowa lub rabat wyszczególnione w potwierdzeniu zamówienia są zgodne z odpowiadającymi im wartościami w zamówieniu zakupu. Weryfikacja ta zapewnia spójność i dokładność między tym, co zostało zamówione, a tym, co dostawca potwierdza dostarczyć.

#### Trigger Condition

Logika jest aktywowana, gdy którykolwiek z następujących warunków jest spełniony w potwierdzeniu zamówienia w odniesieniu do oryginalnego zamówienia zakupu:

* **Quantity**: Ilość zamówionych pozycji odpowiada ilości potwierdzonej przez dostawcę.
* **Unit Price**: Uzgodniona cena za pozycję odpowiada potwierdzeniu dostawcy.
* **Discount**: Wszelkie zastosowane rabaty są spójne między zamówieniem zakupu a potwierdzeniem zamówienia.

#### Outcomes

* **Equals**: Jeśli ilość, cena jednostkowa lub rabat w potwierdzeniu zamówienia dokładnie odpowiadają zamówieniu zakupu, system uznaje potwierdzenie za prawidłowe i kontynuuje kolejne kroki w procesie zakupowym.
* **Not Equal**: Jeśli istnieje rozbieżność w ilości, cenie jednostkowej lub rabacie, system oznacza potwierdzenie zamówienia do ręcznego przeglądu. Zapewnia to rozwiązanie wszelkich niezgodności przed kontynuowaniem.

#### Benefits

* **Accuracy and Consistency**: Utrzymuje dokładność w procesie zakupowym, zapewniając, że płatności i dostawy są realizowane na podstawie poprawnych wartości.
* **Efficiency**: Automatyzuje proces weryfikacji, redukując potrzebę ręcznych kontroli i przyspieszając przetwarzanie zamówień.
* **Cost Control**: Pomaga zapobiegać nadpłatom lub nieprawidłowym dostawom, wcześnie wychwytując rozbieżności w procesie.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Define Comparison Parameters**: Skonfiguruj konkretne pola (ilość, cena jednostkowa, rabat), które karta logiczna będzie sprawdzać pod kątem zgodności.
2. **Automate Verification**: Skonfiguruj system tak, aby automatycznie porównywał te szczegóły po otrzymaniu potwierdzenia zamówienia.
3. **Customize Alerts**: Zdecyduj o przepływie pracy do obsługi rozbieżności, w tym dostosowaniu alertów do ręcznego przeglądu.

Ta karta logiczna jest kluczowa dla zapewnienia, że szczegóły potwierdzenia zamówienia są zgodne z oryginalnym zamówieniem zakupu, chroniąc integralność cyklu zakupowego. \`\`
