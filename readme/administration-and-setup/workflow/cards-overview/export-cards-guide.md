# Karty eksportu przepływu pracy i status dokumentu

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-11f244132c25-pl.png" alt="Karty dostępne w wybranej kategorii. Uzupełnij pola przed użyciem. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs."><figcaption><p>Karty dostępne w wybranej kategorii. Uzupełnij pola przed użyciem. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs.</p></figcaption></figure>

Wybierz, czy chcesz wyeksportować natychmiast, czy też ustawić konfigurację w kolejce do końcowego eksportu na koniec przebiegu. Te opcje są niezależne od statusu, jaki powinien mieć dokument po pomyślnym eksporcie.

| Karta | Po uruchomieniu eksportu | Ważne ustawienia |
| --- | --- | --- |
| Rozpocznij eksport z walidacją (`EXPORT`) | Rozpoczyna eksport przy użyciu skonfigurowanych ustawień eksportu dokumentu. | Walidacja i, od wersji 4, status po eksporcie. |
| Eksportuj z konfiguracją eksportu (`ACTION_EXPORT_WITH`) | Eksportuje przy użyciu wybranej konfiguracji podczas wykonywania karty. | Eksportuj konfigurację, Ignoruj oczekujące zadania i, od wersji 3, Stan po eksporcie. |
| Eksport kolejki z konfiguracją (`ACTION_EXPORT_WITH_CONFIG_DEFERRED`) | Zbiera konfigurację do końcowego eksportu na koniec przebiegu. Dodanie żądania eksportu do kolejki nie oznacza, że ​​końcowy eksport się powiódł. | Eksportuj konfigurację, Ignoruj oczekujące zadania i, od wersji 3, Stan po eksporcie. |
| Alternatywny eksport (`ACTION_ALTERNATE_EXPORT`) | Korzysta z alternatywnej trasy eksportu udokumentowanej na swojej karcie. | Nie zakładaj, że ma tę samą wersję lub opcje statusu, co trzy powyższe karty. |

## Stan po eksporcie

| Wartość | Znaczy po udanym eksporcie | Typowe zastosowanie |
| --- | --- | --- |
| `finished` | Wyeksportowany i zamknięty. | Przetwarzanie zostało zakończone. |
| `exported` | Wyeksportowany, ale pozostaje otwarty do dalszego przetwarzania. | Nadal musi nastąpić zatwierdzenie lub inny przepływ pracy. |

Rozpocznij eksport v4, eksport z konfiguracją eksportu v3 i eksport do kolejki v3 oferują ten wybór. Wcześniejsze wersje zachowują `finished`. Brakujący wybór wraca do `finished` i jest rejestrowany; nieprawidłowa wartość zostanie odrzucona przed eksportem. Zapisana stara karta nie uzyskuje nowego zachowania tylko dlatego, że istnieje nowa wersja szablonu. Sprawdź wersję karty i przetestuj ponownie wszelkie jawne aktualizacje.

Warunki statusu dokumentu i status zmiany oferują również `exported` w wersjach zawierających odpowiednią aktualizację statusu. Sama zmiana statusu nie powoduje wykonania eksportu. Skorzystaj z wyników eksportu i dzienników, aby ustalić, czy dane rzeczywiście dotarły do ​​miejsca docelowego.

## Natychmiastowy eksport z konfiguracją

1. Dodaj kartę w obszarze Następnie i wybierz prawidłową konfigurację eksportu.
2. Wybierz, czy ignorować oczekujące zadania. Pozostaw tę opcję wyłączoną, jeśli zadania muszą blokować eksport.
3. W wersji 3 celowo wybierz `finished` lub `exported`.
4. Przetestuj z dokumentem o dozwolonym statusie przetwarzania, a następnie sprawdź wynik karty i miejsce docelowe.

Jeżeli oczekujące zadania uniemożliwiają eksport, na karcie zostanie zarejestrowana odmowa eksportu. Rozwiąż zadania i zorganizuj zamierzony wyzwalacz przepływu pracy lub spróbuj ponownie. Ta karta nie obiecuje czekać i automatycznie wznowić. Przekroczenie limitu czasu również nie dowodzi, że system zdalny nic nie zrobił; sprawdź historię eksportu przed powtórzeniem operacji, która może spowodować utworzenie duplikatów.

## Eksport kolejki z konfiguracją

Dodaj tę kartę, gdy eksport powinien zostać zebrany na ostatnim etapie przebiegu. Wybierz konfigurację, zasady zadań oczekujących i status wyników. Karta rejestruje żądaną konfigurację; osobno sprawdzić końcowy wynik eksportu. Wiadomość potwierdzająca żądanie oczekujące w kolejce nie jest potwierdzeniem zaksięgowania księgowego.

Na przykład wybierz `exported`, gdy pomyślny eksport musi pozostawić dokument dostępny do późniejszego zatwierdzenia. Wybierz `finished`, gdy dalsze przetwarzanie nie jest wymagane. Sprawdź ponownie stan końcowy oraz miejsce docelowe eksportu.

## Wymagane kontrole

Przetestuj prawidłową konfigurację, brakującą konfigurację, oczekujące zadania z obydwoma ustawieniami i obydwoma stanami wyników. Przetestuj wersję już używaną w istniejącym przepływie pracy przed jej zmianą. W przypadku eksportu w kolejce sprawdź ostateczne wykonanie; dla natychmiastowego eksportu sprawdź swój własny wynik. Przejrzyj [Dzienniki przepływu pracy](../workflow-logs.md) i nie myl pominiętej karty z sukcesem.

<!-- workflow-card-complete-example-20261021 action_export_with_config_deferred -->

### Przykład odroczonego eksportu

**Konfiguracja:** W wersji 3 wybierz konfigurację testową `DEMO_EXPORT`, pozostaw opcję Ignoruj oczekujące zadania wyłączoną i wybierz `exported` jako status po eksporcie. Umieść kartę na zamierzonej zatwierdzonej trasie.

**Oczekiwany wynik i kontrprzykład:** Karta zbiera żądanie eksportu w celu zakończenia wykonywania przepływu pracy. Tylko pomyślne wykonanie końcowe stwierdza, że ​​odbiorca otrzymał dane i że dokument pozostaje otwarty jako `exported`. Sam sukces karty w kolejce nie dowodzi eksportu; nierozwiązane zadanie blokujące nie może być traktowane jako doręczenie.

To jest ilustracyjna konfiguracja testu i oczekiwany wynik; nie zostało ono wykonane. Skorzystaj z danych i odbiorców skonfigurowanych w Twojej organizacji testowej.
