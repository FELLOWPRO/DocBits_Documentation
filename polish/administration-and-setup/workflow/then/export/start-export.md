# Start Export

<figure><img src="../../../../.gitbook/assets/image (285).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Start Export"** służy do zainicjowania procesu eksportu dokumentu. Karta ta działa jako wyzwalacz w przepływie pracy, aby bezproblemowo rozpocząć operację eksportu, gdy warunki w poprzedzających sekcjach są spełnione.

## **Komponenty karty:**

1. **Action**
   1. **Opis**: Inicjuje proces eksportu dokumentu.
   2. **Szczegóły**: Karta używa skonfigurowanych ustawień eksportu w systemie do przetworzenia i wyeksportowania dokumentu.

## **Funkcjonalność:**

* **Ocena warunku**: System ocenia warunki ustawione w sekcjach **"Where"** i **"And Sections"** przepływu pracy. Jeśli wszystkie warunki są prawdziwe, proces eksportu się rozpoczyna.
* **Eksport dokumentu**: Dokument jest przetwarzany i eksportowany przy użyciu domyślnej lub wcześniej zdefiniowanej konfiguracji eksportu.

## **Konfiguracja:**

Ta karta nie wymaga szczególnej konfiguracji, ponieważ używa ustawień eksportu już zdefiniowanych w systemie. Użytkownicy muszą zapewnić, że:

1. Warunki w sekcjach **"Where"** i **"And Sections"** są prawidłowo skonfigurowane, ponieważ karta wykonuje się tylko wtedy, gdy te warunki są prawdziwe.
2. Z dokumentem w systemie powiązana jest prawidłowa konfiguracja eksportu.

## **Podsumowanie:**

Karta przepływu pracy **"Start Export"** zapewnia usprawniony i zautomatyzowany sposób wyzwalania procesu eksportu. Opierając się na wstępnie skonfigurowanych ustawieniach i ocenach warunkowych, zapewnia efektywne i dokładne przetwarzanie dokumentów.
