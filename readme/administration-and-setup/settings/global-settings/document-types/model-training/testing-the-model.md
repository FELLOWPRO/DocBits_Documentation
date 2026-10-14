# Testowanie modelu

## Kroki uruchamiania testów klasyfikacji w celu oceny dokładności i gotowości operacyjnej modelu

Aby przetestować wytrenowany model oraz ocenić jego dokładność i gotowość operacyjną, możesz wykonać poniższe kroki:



**Przygotowanie danych testowych:**&#x20;

* Zbierz reprezentatywną próbkę danych testowych obejmującą różne typy dokumentów i scenariusze, które model będzie obsługiwał w środowisku produkcyjnym. Upewnij się, że dane testowe są wysokiej jakości i poprawnie oznaczone.



**Uruchamianie testów klasyfikacji:**&#x20;

* Uruchom testy klasyfikacji na przygotowanych danych testowych.&#x20;
* Przekaż dane testowe do modelu i pozwól mu przewidzieć klasyfikację dokumentów.

<figure><img src="../../../../../.gitbook/assets/image (91).png" alt="" width="375"><figcaption><p>Setting</p></figcaption></figure>

* Dodaj nową regułę klasyfikacji lub edytuj istniejącą.

<figure><img src="../../../../../.gitbook/assets/image (92).png" alt=""><figcaption><p>Settings: Classification and Extraction </p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (90).png" alt="" width="276"><figcaption><p>Configure classification Rule</p></figcaption></figure>

**Ocena dokładności modelu:**&#x20;

* Porównaj przewidywania modelu z rzeczywistymi klasyfikacjami danych testowych. Oblicz metryki takie jak dokładność (accuracy), precyzja (precision), czułość (recall) i miara F1, aby ocenić wydajność modelu. Metryki te pokazują, jak dobrze model sklasyfikował dokumenty i jak jest niezawodny.

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto 2024-05-22 um 08.53.41.png" alt=""><figcaption></figcaption></figure>



**Analiza błędów:**&#x20;

* Zbadaj błędy popełnione przez model podczas klasyfikowania danych testowych i przeanalizuj ich przyczyny. Zidentyfikuj wzorce lub tendencje w błędach i w razie potrzeby wprowadź zmiany w modelu, aby poprawić jego wydajność.



**Optymalizacja modelu**:&#x20;

* Na podstawie wyników testów klasyfikacji i analizy błędów możesz zoptymalizować model, dodając dane treningowe, dostosowując parametry trenowania lub zmieniając architekturę modelu. Powtórz proces testowania, aby sprawdzić, czy optymalizacje poprawiły wydajność modelu.



**Dokumentowanie wyników:**&#x20;

* Udokumentuj wyniki testów klasyfikacji oraz wszelkie zmiany lub optymalizacje wprowadzone w modelu. Pomoże Ci to śledzić postępy modelu w czasie i zapewnić jego stałe doskonalenie.

Regularnie uruchamiając testy klasyfikacji i oceniając wydajność modelu, możesz zapewnić, że nadaje się on do użytku produkcyjnego i dostarcza dokładne wyniki.



