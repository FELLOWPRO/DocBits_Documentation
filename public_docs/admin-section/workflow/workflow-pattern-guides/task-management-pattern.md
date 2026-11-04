# Wzorzec zarządzania zadaniami

**Typ wzorca:** Zarządzanie przepływem pracy
**Złożoność:** Niska-Średnia
**Szacowany czas konfiguracji:** 30-45 minut
**Typowe przypadki użycia:** Przepływy pracy zatwierdzania, zadania przeglądu, obsługa wyjątków, eskalacja

---

## Przegląd wzorca

Ten wzorzec pokazuje, jak tworzyć, przypisywać, śledzić i zarządzać zadaniami w ramach przepływów pracy DocBits. Zadania to możliwe do wykonania elementy pracy przypisane użytkownikom lub grupom, które wymagają ukończenia przed kontynuowaniem przepływu pracy dokumentu.

**What This Pattern Does:**
1. Tworzy zadania na podstawie warunków przepływu pracy
2. Przypisuje zadania do odpowiednich użytkowników lub grup
3. Ustawia właściwości zadań (priorytet, termin, opis)
4. Wysyła powiadomienia po utworzeniu zadań
5. Śledzi status i zakończenie zadań
6. Kieruje dokumenty na podstawie wyników zadań

---

## Kiedy używać tego wzorca

Użyj tego wzorca, gdy musisz:
- ✅ Tworzyć przepływy pracy zatwierdzania
- ✅ Przypisywać zadania przeglądu użytkownikom
- ✅ Obsługiwać wyjątki wymagające interwencji człowieka
- ✅ Eskalować problemy do menedżerów
- ✅ Tworzyć wielopoziomowe łańcuchy zatwierdzania
- ✅ Śledzić, kto co musi zrobić
- ✅ Ustalać terminy działań

---

## Przykładowe wdrożenie krok po kroku

### Krok 1: Sprawdź próg kwotowy

**Karta:** CONDITION_DOC_FIELD_AMOUNT

**Konfiguracja:**
```
Pole: Kwota_Calkowita
Operator: JEST WIĘKSZA NIŻ
Wartość: 1000
Waluta: PLN
```

---

### Krok 2: Utwórz zadanie zatwierdzenia przez menedżera

**Karta:** tasks_create

**Konfiguracja:**
```json
{
  "task_type": "Approval",
  "task_title": "Zatwierdź fakturę {{DOCUMENT_NUMBER}} - {{Total_Amount}} PLN",
  "task_description": "Proszę o zatwierdzenie faktury od {{Supplier_Name}}",
  "priority": "Medium",
  "deadline_days": 3,
  "assign_to": "{{DOCUMENT_FIELD:Approving_Manager}}"
}
```

---

### Krok 3: Wyślij powiadomienie e-mail

**Karta:** ACTION_SEND_EMAIL_TO_GROUPS

---

### Krok 4: Śledź status zadania

**Karta:** CONDITION_TASK_STATUS

---

## Lista kontrolna testów

- [ ] Zadanie utworzone pomyślnie
- [ ] Zadanie przypisane do właściwego użytkownika/grupy
- [ ] Wysłano powiadomienie e-mail
- [ ] Zadanie pojawia się na liście zadań użytkownika
- [ ] Właściwości zadania są poprawne (tytuł, opis, priorytet, termin)
- [ ] Użytkownik może ukończyć zadanie
- [ ] Przepływ pracy jest kontynuowany po zakończeniu zadania
- [ ] Przepływ zatwierdzania działa poprawnie
- [ ] Przepływ odrzucenia działa poprawnie
- [ ] Eskalacja uruchamia się we właściwym czasie
- [ ] Wszystkie powiadomienia e-mail zostały wysłane

---

**Wersja wzorca:** 1.0
**Ostatnia aktualizacja:** 23 października 2025 r.
**Trudność:** Niska-Średnia
