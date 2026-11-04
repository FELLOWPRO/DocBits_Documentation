# Potwierdzenie Zamówienia Zamówienia Zakupu

### Porównaj z Zamówieniem Zakupu:&#x20;

**Potwierdzenie Zamówienia Zamówienia Zakupu**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Karta Logiki: Dopasowanie ilości, ceny jednostkowej lub rabatu

Ta karta logiki została zaprojektowana w celu automatycznego sprawdzenia, czy ilość, cena jednostkowa lub rabat szczegółowo opisane w potwierdzeniu zamówienia zgadzają się z odpowiadającymi wartościami w zamówieniu zakupu. Weryfikacja ta zapewnia spójność i dokładność między tym, co zostało zamówione, a tym, co dostawca potwierdza dostarczenie.

#### Warunek Wywołania

Logika jest aktywowana, gdy którykolwiek z poniższych warunków zostanie spełniony w potwierdzeniu zamówienia w odniesieniu do oryginalnego zamówienia zakupu:

* **Ilość**: Ilość zamówionych przedmiotów zgadza się z ilością potwierdzoną przez dostawcę.
* **Cena jednostkowa**: Cena za sztukę uzgodniona zgadza się z potwierdzeniem dostawcy.
* **Rabat**: Wszelkie zastosowane rabaty są zgodne między zamówieniem zakupu a potwierdzeniem zamówienia.

#### Wyniki

* **Równe**: Jeśli ilość, cena jednostkowa lub rabat w potwierdzeniu zamówienia dokładnie zgadza się z zamówieniem zakupu, system uznaje potwierdzenie za ważne i przechodzi do kolejnych kroków w procesie zamówień.
* **Nierówne**: Jeśli występuje rozbieżność w ilości, cenie jednostkowej lub rabacie, system oznacza potwierdzenie zamówienia do ręcznej weryfikacji. Zapewnia to rozwiązanie wszelkich niezgodności przed kontynuacją.

#### Korzyści

* **Dokładność i Spójność**: Utrzymuje dokładność w procesie zamówień, zapewniając, że płatności i dostawy są dokonywane na podstawie poprawnych wartości.
* **Efektywność**: Automatyzuje proces weryfikacji, zmniejszając potrzebę manualnych kontroli i przyspieszając przetwarzanie zamówień.
* **Kontrola Kosztów**: Pomaga zapobiec nadpłatom lub nieprawidłowym dostawom, wyłapując niezgodności we wczesnym etapie procesu.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Zdefiniuj Parametry Porównania**: Skonfiguruj konkretne pola (ilość, cena jednostkowa, rabat), które karta logiki będzie sprawdzać pod kątem dopasowania.
2. **Automatyzuj Weryfikację**: Skonfiguruj system do automatycznego porównywania tych szczegółów po otrzymaniu potwierdzenia zamówienia.
3. **Dostosuj Alerty**: Zdecyduj o przepływie pracy w przypadku niezgodności, w tym dostosowanie alertów do ręcznej weryfikacji.

Ta karta logiki jest niezbędna do zapewnienia, że szczegóły potwierdzenia zamówienia są zgodne z oryginalnym zamówieniem zakupu, chroniąc integralność cyklu zamówień. \`\`
