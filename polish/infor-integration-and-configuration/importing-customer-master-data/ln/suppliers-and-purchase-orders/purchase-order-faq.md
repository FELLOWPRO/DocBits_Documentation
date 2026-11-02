# Zamówienie zakupu - FAQ

**Gdzie sprawdzić, czy aktualizacje synchronizacji PurchaseOrderBOD są wdrożone poprawnie?**

Przejdź do sesji _BOD Implementation Registration (bobod1100m000)_ w LN. Ta sesja umożliwia przeglądanie, modyfikowanie i rejestrowanie zarówno standardowych, jak i niestandardowych implementacji BOD, w tym PurchaseOrderBOD.

\


<figure><img src="../../../../.gitbook/assets/PO.png" alt=""><figcaption></figcaption></figure>

**Jak zidentyfikować konkretną implementację BOD, którą muszę zweryfikować?**

Szukaj pól BOD Implementation Identifier i BOD Name. Pole BOD Name zazwyczaj wskazuje typ BOD-a (np. PurchaseOrderBOD). BOD Implementation Identifier to unikalny identyfikator danej konfiguracji BOD.

\


**Co oznacza pole wyboru „Public” w sesji BOD Implementation Registration?**

Pole wyboru Public wskazuje, czy implementacja BOD jest dostępna do komunikacji zewnętrznej.

• Zaznaczone: BOD może być wymieniany poza LN (interfejs publiczny i chroniony).

• Odznaczone: BOD służy wyłącznie do wewnętrznego przetwarzania w LN (interfejs chroniony).

\


**Widzę pole „Parent BOD Name”. Do czego służy?**

Pole Parent BOD Name pokazuje nadrzędny BOD, jeśli bieżący BOD jest wersją pochodną lub zależną. Jeśli pole wyboru Public jest zaznaczone, to pole będzie puste. W przeciwnym razie pomaga zrozumieć hierarchię implementacji BOD.

\


**Skąd mam wiedzieć, czy implementacja BOD jest standardowa, czy niestandardowa?**

Sprawdź pole wyboru Standard.

• Zaznaczone: BOD jest standardową implementacją dostarczaną z LN.

• Odznaczone: BOD jest implementacją niestandardową, zdefiniowaną przez Twój zespół lub partnera.

\


**Jaki jest cel pola wyboru „Staging”?**

Zaznaczenie pola wyboru Staging oznacza, że BOD-y są najpierw umieszczane w obszarze przejściowym (staging), a nie publikowane od razu. Można je następnie opublikować w sesji _Publish Staged BODs (bobod2200m000)_.

Uwaga: W przypadku ProjectBudgetBOD staging jest obowiązkowy i nie można go zmienić. Dla standardowych BOD-ów danych podstawowych staging można włączyć ręcznie, a dla niestandardowych BOD-ów można go skonfigurować zawsze.

\


**Jak pole wyboru „Synchronous Processing” wpływa na obsługę przychodzących BOD-ów?**

Synchronous Processing określa działanie w przypadku niepowodzenia procesu następczego po odebraniu BOD-a.

• Zaznaczone: Przychodzący BOD i proces następczy muszą zakończyć się powodzeniem, w przeciwnym razie żaden z nich nie zostanie przetworzony.

• Odznaczone: Przychodzący BOD jest przetwarzany, ale jeśli proces następczy zakończy się niepowodzeniem, należy go obsłużyć ręcznie.

\


**Gdzie sprawdzić, czy funkcja „Stage” jest aktywna dla mojego BOD-a?**

W sesji _BOD Implementation Registration (bobod1100m000)_ sprawdź pole wyboru Staging. Jeśli nie jest zaznaczone, staging nie jest aktywny dla tego konkretnego BOD-a.

\


**Jeśli PurchaseOrderBOD nie jest wyzwalany przy wszystkich aktualizacjach, co jeszcze należy wziąć pod uwagę?**

• Upewnij się, że opcja Staging jest ustawiona zgodnie z zamierzeniem. Jeśli staging jest wyłączony, BOD powinien być publikowany natychmiast.

• Sprawdź, czy ustawienie Synchronous Processing jest prawidłowe dla Twojego przepływu pracy.

• Upewnij się, że BOD Implementation Identifier i BOD Name są poprawne i że pracujesz na właściwej konfiguracji BOD.

• Sprawdź, czy BOD jest standardowy, czy niestandardowy, oraz czy jakiekolwiek ustawienia niestandardowe nie zastępują zachowania standardowego.

\


**Czy istnieją scenariusze, w których aktualizacje PurchaseOrderBOD mogą nie być widoczne zgodnie z oczekiwaniami?**

Tak. Jeśli BOD nie jest poprawnie skonfigurowany (nieprawidłowe ustawienia Public, Staging lub Synchronous Processing) albo jest to niestandardowa implementacja BOD niezgodna z wymaganiami Twojego procesu, aktualizacje mogą nie być wyzwalane zgodnie z oczekiwaniami. Przejrzyj konfigurację w sesji _bobod1100m000_ i upewnij się, że wszystkie parametry odpowiadają zamierzonemu przepływowi procesu.
