# Przepływ Dokumentów

**Przepływ Dokumentów** pokazuje kroki przetwarzania jednego dokumentu. Użyj go, aby zobaczyć, które kroki zostały ukończone, który oczekuje, i jak długo trwało przetwarzanie. Poniższy przykład używa syntetycznej faktury w polskojęzycznym Sandbox.

## Otwieranie z pulpitu

Na **Pulpicie** znajdź dokument. W kolumnie **Akcje** wybierz trzy kropki, a następnie **Przepływ dokumentów**. Opcja otwiera przepływ tego dokumentu; nie zmienia dokumentu.

<figure><img src="../../../.gitbook/assets/document-flow-dashboard-menu-pl-20261008.png" alt="Pulpit w języku polskim z otwartym menu Akcje dla syntetycznej faktury; pozycja Przepływ dokumentów znajduje się pod Przypisz do."><figcaption><p>Wybierz Przepływ dokumentów z menu Akcje dokumentu.</p></figcaption></figure>

## Otwieranie z Walidacji Pola

Otwórz dokument. W **Walidacji Pola** wybierz trzy kropki na prawym pasku akcji, a następnie **Przepływ dokumentów** w menu **Więcej opcji**.

<figure><img src="../../../.gitbook/assets/document-flow-validation-menu-pl-20261008.png" alt="Ekran Walidacja Pola w języku polskim z otwartym menu Więcej opcji i pozycją Przepływ dokumentów obok syntetycznej faktury."><figcaption><p>Ten sam przepływ jest dostępny z widoku dokumentu.</p></figcaption></figure>

## Czytanie przepływu

Panel **Process Statistics** po lewej stronie podsumowuje liczbę kroków, kroki ukończone i oczekujące, ponowne uruchomienia, całkowity czas, bieżący status oraz postęp całkowity. Każda ponumerowana karta pokazuje krok przetwarzania i jego bieżący stan. Przewiń w dół, aby zobaczyć późniejsze kroki.

<figure><img src="../../../.gitbook/assets/document-flow-overview-pl-20261008.png" alt="Przepływ Dokumentów w języku polskim z panelem Process Statistics po lewej i pierwszymi ponumerowanymi kartami kroków: IMPORTOWANY, OCR_COMPLETED i SKLASYFIKOWANY."><figcaption><p>Pierwsze kroki przepływu syntetycznej faktury.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/document-flow-later-steps-pl-20261008.png" alt="Przepływ Dokumentów w języku polskim po przewinięciu w dół; późniejsze karty obejmują między innymi FIELDS_EXTRACTED, TABLES_EXTRACTED, TRANSFORMED, METADATA_POPULATED, LOOKUP_COMPLETED i oczekujący krok QUEUED."><figcaption><p>Przewijaj, aby śledzić kolejność przez późniejsze kroki.</p></figcaption></figure>

Wybierz kartę kroku, aby otworzyć panel **Step Details** po lewej stronie. Pokazuje on moduł i jego status. Po prawej stronie może również otworzyć się panel **Task Logs**; szczegóły logów zależą od tego, co jest dostępne dla tego zadania. Wybierz **×** w panelu Step Details, aby go zamknąć.

<figure><img src="../../../.gitbook/assets/document-flow-step-details-pl-20261008.png" alt="Przepływ Dokumentów w języku polskim z wybraną kartą OCR_COMPLETED; panel Step Details pod Process Statistics pokazuje MODULE ocr_completed i STATUS Completed."><figcaption><p>Step Details wyjaśnia status wybranego modułu.</p></figcaption></figure>
