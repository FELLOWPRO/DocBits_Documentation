# Zadania i powiadomienia

### Przegląd

Ustawienie **Zadania i powiadomienia** włącza wbudowane zarządzanie zadaniami w DocBits. Po włączeniu członkowie zespołu mogą tworzyć zadania, przypisywać sobie nawzajem dokumenty (np. do walidacji, korekty lub zatwierdzenia) i otrzymywać powiązane powiadomienia.

To ustawienie jest **domyślnie wyłączone**. Po jego włączeniu poniżej pojawiają się cztery dodatkowe opcje:

* **Liczba zadań na pulpicie**: pokazuje na stronie **Panel**, które dokumenty mają otwarte zadania.
* **Zezwalaj na filtr „Wszystkie” dla użytkowników niebędących administratorami**: pozwala użytkownikom, którzy nie są administratorami, widzieć wszystkie zadania.
* **Usuwanie zadań przez użytkowników niebędących administratorami**: określa, które zadania mogą usuwać użytkownicy niebędący administratorami.
* **Zamykanie zadań przez użytkowników niebędących administratorami**: określa, które zadania mogą zamykać użytkownicy niebędący administratorami.

Administratorów organizacji te opcje nigdy nie ograniczają.

### Co robi to ustawienie?

* **Włączone**: Funkcje Zadania i powiadomienia stają się dostępne w DocBits. Użytkownicy mogą przypisywać zadania, śledzić ich status i otrzymywać powiadomienia, gdy coś wymaga ich uwagi.
* **Wyłączone**: Przypisywanie zadań i powiązane powiadomienia są wyłączone. Wyłączenie tego ustawienia wyłącza również opcję **Liczba zadań na pulpicie**.

### Liczba zadań na pulpicie

**Liczba zadań na pulpicie** określa, czy strona **Panel** pokazuje, które dokumenty mają otwarte zadania.

* **Włączone**: Dokument, który ma zadania o statusie **Otwarte** lub **W toku**, ma ikonę zadania na liście na stronie **Panel**. Po najechaniu kursorem na ikonę widać, ile otwartych zadań ma dokument, np. „2 Otwarte zadanie(a)”. Zadania wykonane, odrzucone lub usunięte nie są liczone.
* **Wyłączone**: Ikona jest ukryta. Zadania nadal działają normalnie.

{% hint style="info" %}
**Liczba zadań na pulpicie** zależy od ustawienia **Zadania i powiadomienia**. Jeśli wyłączysz Zadania i powiadomienia, liczba zadań na pulpicie również zostanie wyłączona.
{% endhint %}

### Zezwalaj na filtr „Wszystkie” dla użytkowników niebędących administratorami

Przegląd zadań ma filtr **Przypisany do** z opcjami **Wszystko** i **Przypisane do mnie**. Administratorzy zawsze mają obie opcje.

* **Włączone**: Również użytkownicy, którzy nie są administratorami, mogą wybrać **Wszystko** i widzieć wszystkie zadania organizacji.
* **Wyłączone** (domyślnie): Użytkownicy, którzy nie są administratorami, mają tylko opcję **Przypisane do mnie**, więc przegląd pokazuje zadania przypisane do nich.

### Usuwanie zadań przez użytkowników niebędących administratorami
**Usuwanie zadań przez użytkowników niebędących administratorami** określa, które zadania i powiadomienia mogą usuwać użytkownicy niebędący administratorami. Administratorzy zawsze mogą usunąć każde zadanie.

| Opcja | Użytkownicy niebędący administratorami mogą usuwać |
| --- | --- |
| **Żadne** | Żadnych zadań. |
| **Tylko utworzone zadania** | Zadania, które sami utworzyli. |
| **Utworzone i przypisane zadania** | Zadania, które sami utworzyli, oraz zadania przypisane do nich lub do jednej z ich grup. Obowiązuje, jeśli opcja nigdy nie była zmieniana. |
| **Wszystkie zadania** | Każde zadanie. |

Użytkownicy zawsze mogą usuwać zadania, które sami utworzyli, z wyjątkiem opcji **Żadne**. Zadanie, które nie jest nikomu przypisane, może więc usunąć tylko użytkownik, który je utworzył, administratorzy albo użytkownicy przy opcji **Wszystkie zadania**. Zadanie bez zapisanego twórcy, na przykład utworzone przez system, mogą usunąć tylko użytkownicy, do których jest przypisane (przy opcji **Utworzone i przypisane zadania**), administratorzy albo użytkownicy przy opcji **Wszystkie zadania**.

{% hint style="warning" %}
Usunięcie zadania usuwa je z listy zadań bez podjęcia decyzji. Jeśli zadania mają być zamykane wyłącznie na podstawie decyzji, ustaw w **Usuwanie zadań przez użytkowników niebędących administratorami** opcję **Żadne**, a w **Zamykanie zadań przez użytkowników niebędących administratorami** (patrz niżej) opcję **Tylko dla administratorów**.
{% endhint %}

### Zamykanie zadań przez użytkowników niebędących administratorami
**Zamykanie zadań przez użytkowników niebędących administratorami** określa, którzy użytkownicy niebędący administratorami mogą zamknąć zadanie, czyli ustawić je na **Zrobione** lub **Odrzucony**. Administratorzy zawsze mogą zamykać zadania, niezależnie od wybranej tu opcji.

| Opcja | Kto może zamknąć zadanie |
| --- | --- |
| **Domyślne zachowanie** | Ustawienie nie wprowadza żadnych ograniczeń. Użytkownicy mogą zamykać zadania przypisane do nich lub do jednej z ich grup, tak jak przed wprowadzeniem tego ustawienia. Obowiązuje, jeśli opcja nigdy nie była zmieniana. |
| **Administratorzy i przypisani użytkownicy** | Administratorzy oraz użytkownicy, do których zadanie jest przypisane bezpośrednio lub przez jedną z ich grup. Zadania przypisanego do kogoś innego lub do nikogo inni użytkownicy nie mogą zamknąć. DocBits sprawdza to również wtedy, gdy zadanie jest zmieniane przez API. |
| **Tylko dla administratorów** | Tylko administratorzy. |

Przy opcji **Administratorzy i przypisani użytkownicy** lub **Tylko dla administratorów** użytkownik, który nie może zamknąć zadania:

* nie widzi zielonego przycisku **Zrobione** na stronie zadania, a lista statusów oferuje tam tylko **Otwarte** i **W toku**;
* nie może kliknąć kółka statusu zadania w panelu zadań dokumentu. Po najechaniu na nie kursorem wyświetla się komunikat „Nie masz możliwości oznaczenia tego zadania jako wykonanego lub odrzuconego.”;
* nie widzi opcji **Oznacz jako wykonane** dla tego zadania na liście zadań, a **Oznacz jako wykonane** dla zaznaczonych zadań jest ukryte, dopóki takie zadanie jest zaznaczone;
* nie może przeciągnąć zadania do kolumny **Zrobione** ani **Odrzucony** na tablicy zadań. Karta wraca do swojej kolumny i wyświetla się ten sam komunikat.

Ustawienie ogranicza wyłącznie zamykanie zadań. Użytkownicy zachowują wszystkie inne uprawnienia, które mieli wcześniej: użytkownicy, do których zadanie jest przypisane, nadal mogą je edytować, zapisywać, przenosić między statusami **Otwarte** i **W toku** oraz ponownie otworzyć po wykonaniu. Użytkownicy, do których zadanie nie jest przypisane, wcześniej nie mogli zmieniać jego statusu i nadal nie mogą.

W przypadku typów dokumentów z włączoną opcją **Historia zatwierdzeń** akcja **Zatwierdzić** nadal kończy otwarte zadania dokumentu, niezależnie od wybranej tu opcji: zadania przypisane do zatwierdzającego lub do jednej z jego grup oraz zadania nieprzypisane nikomu. Jeśli zatwierdzający jest administratorem, kończone są wszystkie otwarte zadania dokumentu.

#### Zadania na dokumentach odesłanych do walidacji

Ponieważ przy opcji **Administratorzy i przypisani użytkownicy** lub **Tylko dla administratorów** użytkownicy nie mogą sami zamknąć swoich zadań, DocBits sam porządkuje otwarte zadania dokumentu, gdy dokument oczekujący na zatwierdzenie zostaje odesłany do walidacji:

* **Uruchom ponownie przepływ pracy** na ekranie zatwierdzania: wszystkie otwarte zadania dokumentu zostają odrzucone.
* **Odrzuć i popraw**: wszystkie otwarte zadania dokumentu zostają odrzucone.
* **Zatwierdź i popraw**: zadania, które zakończyłaby akcja **Zatwierdzić** (patrz wyżej), zostają zakończone, tylko w przypadku typów dokumentów z włączoną opcją **Historia zatwierdzeń**. Wszystkie pozostałe otwarte zadania zostają odrzucone.

Otwarte zadania są porządkowane, zanim dokument wróci do walidacji. Przepływy pracy uruchamiane przy zmianie statusu mogą następnie utworzyć nowe zadania dla wszystkiego, co nadal wymaga uwagi.

Przy opcji **Domyślne zachowanie** otwarte zadania pozostają otwarte po odesłaniu dokumentu, tak jak dotychczas.

### Korzyści

* **Jasna odpowiedzialność**: Dokumenty można przypisać właściwej osobie zamiast polegać na e-mailu.
* **Nic nie zostaje zapomniane**: Powiadomienia przypominają użytkownikom o dokumentach wymagających ich działania.
* **Otwarta praca na pierwszy rzut oka**: Dzięki opcji Liczba zadań na pulpicie strona Panel pokazuje, które dokumenty wciąż mają otwarte zadania.
* **Decyzje pozostają możliwe do prześledzenia**: Dzięki opcjom usuwania i zamykania zadania opuszczają kolejkę tylko na podstawie decyzji lub przez administratora.

### Jak używać

1. Przejdź do **Ustawienia**.
2. Wybierz **Przetwarzanie dokumentów**.
3. Wybierz **Moduł**.
4. Otwórz sekcję **Typ dokumentu**.
5. Włącz **Zadania i powiadomienia**.
6. (Opcjonalnie) Włącz opcję **Liczba zadań na pulpicie**, aby wyświetlać ikonę zadania na stronie **Panel**.
7. (Opcjonalnie) Włącz opcję **Zezwalaj na filtr „Wszystkie” dla użytkowników niebędących administratorami**, jeśli wszyscy użytkownicy mają widzieć wszystkie zadania.
8. (Opcjonalnie) W **Usuwanie zadań przez użytkowników niebędących administratorami** wybierz, które zadania użytkownicy mogą usuwać.
9. (Opcjonalnie) W **Zamykanie zadań przez użytkowników niebędących administratorami** wybierz, kto może zamykać zadania.

Opcje usuwania i zamykania zadań są zapisywane, gdy tylko wybierzesz wartość.

### Kiedy używać tej funkcji

* **Zespoły dzielące się pracą nad dokumentami**: Włącz, gdy kilka osób waliduje lub zatwierdza dokumenty i musi przekazywać sobie pracę.
* **Widoczność obciążenia**: Włącz również opcję Liczba zadań na pulpicie, gdy zespół ma widzieć na stronie Panel, które dokumenty wciąż mają otwarte zadania.
* **Zadania, które może zamknąć tylko administrator lub decyzja**: Ustaw **Zamykanie zadań przez użytkowników niebędących administratorami** na **Tylko dla administratorów** lub **Administratorzy i przypisani użytkownicy**, a **Usuwanie zadań przez użytkowników niebędących administratorami** na **Żadne**, jeśli użytkownicy nie mogą usuwać zadań, które w rzeczywistości nie zostały wykonane.
* **Konfiguracje jednoosobowe lub w pełni zautomatyzowane**: Możesz pozostawić wyłączone, jeśli nikt nie musi przypisywać dokumentów ani śledzić zadań.
