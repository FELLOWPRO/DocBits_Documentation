---
hidden: true
---

# Dostawca na fakturze

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-f5b5666e94fe-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane.</p></figcaption></figure>

## **Cel**

Ta karta DocBits umożliwia szczegółowe porównanie dostawcy z faktury z dostawcą z potwierdzenia zamówienia. Należy zapewnić, że dostawca, który wystawił fakturę, jest taki sam jak ten w potwierdzeniu zamówienia.

## **Funkcjonalność:**

* **Dostawca na fakturze Dostawca na zamówieniu:** Ta karta sprawdza, czy dostawca na fakturze jest taki sam jak w potwierdzeniu zamówienia, czy nie.
* **Operator Value:** Użytkownicy mogą ustawić konkretne warunki, takie jak: czy dostawca, który wystawił fakturę, jest taki sam jak w PO, czy nie. Dostępne operatory obejmują:
  * **Is (=):** Sprawdza, czy dostawca na fakturze odpowiada dostawcy w potwierdzeniu zamówienia.
  * **Czy nie jest (≠):** Zapewnia, że dostawca, który wystawił fakturę, jest taki sam jak w potwierdzeniu zamówienia.

## **Zastosowanie:**

Ta karta jest pomocna, aby zapewnić, że cały proces jest obsługiwany z tym samym dostawcą i wszystko do siebie pasuje. Zapewnia to, że w przypadku rozbieżności zwracana jest uwaga na sprawdzenie tych rozbieżności i niepłacenie faktury nieprawidłowemu dostawcy, który nie ma nic wspólnego z zamówieniem i potwierdzeniem zamówienia.

## **Przykładowy scenariusz:**

* Składane jest zamówienie, następnie przychodzi potwierdzenie zamówienia, a potem wystawiana jest faktura. Cały proces zamawiania jest realizowany z jednym dostawcą. Jeśli tak nie jest, karta może natychmiast stwierdzić, że istnieją rozbieżności między dostawcami, a tym samym zapewnia, że nie są dokonywane nieprawidłowe płatności i że faktura jest realizowana tylko z dostawcą, który był również zaangażowany w cały proces.

Korzystając z karty „Supplier on Invoice … Supplier on Purchase Order”, firmy mogą zautomatyzować weryfikację dostawców, którzy wystawiają faktury, oraz powiązanych potwierdzeń zamówień.
