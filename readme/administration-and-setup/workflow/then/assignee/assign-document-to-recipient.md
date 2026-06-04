# Assign document to recipient

<figure><img src="../../../../.gitbook/assets/image (301).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Assign Document to Disponent / Purchaser"** przypisuje dokument do **Disponenta** lub **Purchasera**. Jeśli nie zostanie znaleziony prawidłowy użytkownik, wybierany jest użytkownik zapasowy, aby zapewnić, że dokument jest zawsze do kogoś przypisany.

## **Komponenty karty:**

1. **Disponent / Purchaser**
   * **Opis:** Określa, czy dokument zostanie przypisany do Disponenta, czy Purchasera.
   * **Opcje:**
     * **Disponent:** Przypisz dokument do Disponenta.
     * **Purchaser:** Przypisz dokument do Purchasera.
2. **Fallback User**
   * **Opis:** Określa użytkownika zapasowego na wypadek, gdyby dokumentu nie można było przypisać do wybranego Disponenta lub Purchasera.
   * **Szczegóły:** Lista rozwijana dostępnych użytkowników umożliwia wybór użytkownika zapasowego, aby zapewnić, że dokument zostanie przypisany, nawet jeśli podstawowego użytkownika nie można ustalić.

## **Funkcjonalność:**

* **Ocena warunku:**\
  Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **"Where"**, jak i **"And Sections"** są prawdziwe.
* **Przypisanie dokumentu:**\
  Karta przypisuje dokument do **Disponenta** lub **Purchasera** zgodnie z wyborem. Jeśli wybrana osoba jest niedostępna lub nieprawidłowa, dokument jest przypisywany do użytkownika zapasowego.

## **Konfiguracja:**

* **Select Disponent / Purchaser:**\
  Wybierz, czy przypisać dokument do **Disponenta**, czy **Purchasera**.
* **Select Fallback User:**\
  Wybierz użytkownika zapasowego z listy rozwijanej, który otrzyma dokument, jeśli podstawowe przypisanie nie będzie możliwe.

## **Podsumowanie:**

Karta przepływu pracy **"Assign Document to Disponent / Purchaser"** zapewnia, że dokument jest zawsze przypisany, albo do wybranego Disponenta/Purchasera, albo, w razie potrzeby, do użytkownika zapasowego. Minimalizuje to zakłócenia w przepływie pracy i zapewnia płynne kontynuowanie przetwarzania dokumentów.
