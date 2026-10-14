# Przepływ Wykonywania Lokalnie

Dla klientów korzystających z Operatora DocBits lokalnie, poniższa sekwencja opisuje, jak przetworzony dokument wyzwalają i wykonuje polecenie Operatora za pośrednictwem lokalnego Agenta DocBits.

1. **Przesyłanie i Przetwarzanie Dokumentu** Dokument jest przesyłany do DocBits i przechodzi przez standardowe przetwarzanie (Ekstrakcja, walidacja, itp.).
2. **Wyzwalacz Przepływu** Po zakończeniu przetwarzania skonfigurowany Przepływ w DocBits ocenia swoje warunki wyzwalające. Gdy warunki te są spełnione, Przepływ tworzy nowe **Zadanie Operatora**.
3. **Tworzenie i Wysyłka Zadania**
   * Przepływ wysyła tekst skryptu, zmienne, maksymalną liczbę kroków, maksymalną liczbę ponownych prób jako ładunek zadania do wspólnej Puli Roboczej.
4. **Pętla Odpytywania Agenta**
   * Agent DocBits lokalnie (zainstalowany w środowisku klienta) odpytuje Pula Roboczą co 5 minut. Jeśli nie zostaną znalezione żadne zadania, agent pozostaje bezczynny i ponawia próby po upływie interwału.
5. **Wykonywanie Zadania**
   * Gdy zadanie pojawi się w Pulie Roboczej, Agent je pobiera i rozpoczyna wykonanie.
6. **Generowanie Logów**
   * Dla każdego kroku—sukcesu lub niepowodzenia—agent rejestruje szczegółowe logi (działania, statusy, znaczniki czasu). Po zakończeniu kompiluje pełny dziennik i ostateczny status.
7. **Zwracanie i Wyświetlanie Wyników**
   * Agent wysyła logi i status z powrotem do DocBits. Historia uruchomień pierwotnego przepływu jest aktualizowana, a użytkownicy mogą przejrzeć szczegóły w zakładce **Logi Przepływu**.
