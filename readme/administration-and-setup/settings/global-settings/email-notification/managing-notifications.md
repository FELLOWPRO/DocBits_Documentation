# Zarządzanie powiadomieniami

Otwórz **Ustawienia → Powiadomienie e-mail**, aby zobaczyć reguły swojej organizacji. Reguła łączy status dokumentu z szablonem e-mail i odbiorcą. Poniższy przykład używa reguły demonstracyjnej dla faktur i pozostaje **nieaktywna** w piaskownicy DocBits.

## Przykład: faktura jest gotowa do walidacji

Zanim utworzysz regułę, przygotuj szablon e-mail dla typu **Invoice** w **Ustawienia → Szablony e-maili**. W tym przykładzie szablon nazywa się **Docs Demo Invoice Notification**. Szablon dostarcza temat i treść wiadomości e-mail.

1. Wybierz **+ Nowy** na stronie **Powiadomienie e-mail**.
2. Wpisz **Docs Demo Invoice Validation** jako nazwę, wybierz **Invoice** jako typ dokumentu i wskaż przygotowany szablon e-mail.
3. Wybierz **Ready for validation** jako status i **Wysoki** jako priorytet. Ustaw **Jednostka czasu** na **PROTOKÓŁ** i **Opóźnienie** na **10**. Minimalne opóźnienie dla minut wynosi pięć.
4. Wybierz **Wyślij e-mail do przypisanego użytkownika/grupy**. Włącz **Nie powtarzaj**, jeśli wiadomość ma zostać wysłana tylko raz. Sprawdź odbiorcę i czas, a następnie wybierz **Ratować**.

<figure><img src="../../../../.gitbook/assets/dbdc-164-example-form-pl-20261011.png" alt="Wypełniona reguła powiadomień dla Invoice, Ready for validation, opóźnienie dziesięciu minut i przypisany użytkownik lub grupa"><figcaption><p>Zapisana reguła przykładu otwarta do edycji. Jej wartości pokazują, kiedy i do kogo powiadomienie zostałoby wysłane.</p></figcaption></figure>

Reguła pojawia się teraz na liście. Przykład dokumentacyjny został następnie wyłączony, dlatego jego menu **Actions** oferuje **Aktywować**. Przed aktywacją reguły sprawdź w własnej liście nazwę, typ dokumentu, status, opóźnienie i odbiorcę.

<figure><img src="../../../../.gitbook/assets/dbdc-164-example-list-pl-20261011.png" alt="Lista Powiadomienie e-mail z przykładowymi regułami zamiast pustej tabeli"><figcaption><p>Lista pokazuje zapisane reguły, które możesz znaleźć i zarządzać nimi.</p></figcaption></figure>

## Edytuj, aktywuj lub usuń regułę

Otwórz menu **Actions** wiersza. **Redagować** otwiera regułę z jej bieżącymi wartościami. **Aktywować** włącza ten nieaktywny przykład; aktywna reguła oferuje zamiast tego **Dezaktywować**. **Dzienniki** otwiera historię powiadomień reguły. **Usuwać** usuwa regułę po potwierdzeniu. Przed aktywacją lub zmianą reguły sprawdź odbiorców i czas.

<figure><img src="../../../../.gitbook/assets/dbdc-164-example-actions-pl-20261011.png" alt="Menu Actions nieaktywnej reguły demonstracyjnej z Redagować, Aktywować, Dzienniki i Usuwać"><figcaption><p>Dostępne działania zależą od tego, czy reguła jest aktywna.</p></figcaption></figure>

Jeśli lista pokazuje **No Record Found!**, najpierw utwórz regułę. Jeśli lista **Typ Dokumentu** lub szablonów e-mail jest pusta, skonfiguruj aktywny typ dokumentu i pasujący szablon, zanim wrócisz do tego formularza.

Więcej informacji o początkowej konfiguracji znajdziesz w sekcji [Konfigurowanie powiadomień](konfigurowanie-powiadomien.md). Jeśli e-male nie docierają zgodnie z oczekiwaniami, zobacz [Rozwiązywanie problemów](rozwiazywanie-problemow.md).
