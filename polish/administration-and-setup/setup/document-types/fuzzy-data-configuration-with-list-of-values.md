---
hidden: true
---

# Konfiguracja danych rozmytych z listą wartości

### **Przegląd**

Każdy typ dokumentu ma własne konfiguracje listy wartości (List of Values, LoV), które trzeba skonfigurować osobno. W przeciwieństwie do **danych rozmytych z danymi podstawowymi (Fuzzy Data with Master Data)**, **lista wartości** nie zawiera domyślnych grup wyszukiwania.

### Aby skonfigurować listę wartości, przejdź do:

Ustawienia → Ustawienia globalne → Typy dokumentów → Faktura → Pola → Ustawienia danych podstawowych → LOV Dane podstawowe

### **Tworzenie nowej konfiguracji listy wartości**

Konfigurację listy wartości można utworzyć na dwa sposoby:

**1. Powielenie istniejącego wyszukiwania**

* Kopiuje wszystkie informacje i pola z istniejącej grupy.
* Wystarczy podać **nową nazwę**.

**2. Utworzenie wyszukiwania od podstaw**

* Kliknij **"Create List of Values"**.
* Wypełnij wymagane dane:
  * **Configuration Name** → Nazwa listy wartości.
  * **Lookup Table** → Tabela, z której będą pobierane wartości.
  * **Conflict Handler** → Wybierz jedną z opcji:
    * Best Score
    * Return None
    * Return First
  * **Context Type** → Określa, czy lista wartości dotyczy poziomu **nagłówka (Header)**, czy **pozycji (Line)**.
  * **Match All** → _(Potrzebne dodatkowe szczegóły)_

### **Zarządzanie polami w grupie listy wartości**

Każda grupa LoV zawiera pola, które można **dodawać, usuwać lub edytować.**

**Dodawanie nowego pola**

Aby dodać nowe pole w grupie:

* Kliknij **"Create"** w odpowiedniej grupie.
* Podaj następujące dane:
  * **Lookup Field** → Nazwa kolumny z tabeli wyszukiwania.
  * **Validation Field** → Odpowiadające pole DocBits.
  * **Parent Field** → _(Potrzebne dodatkowe szczegóły)_
  * **Search Operator** → Wybierz jedną z opcji:
    * Smart
    * Contains
    * Exact
    * Starts with
    * Ends with
  * **Pola wyboru:**
    * **Auto Trigger** → Gdy opcja jest włączona, a inne pole w innej konfiguracji wyszukiwania korzysta z tej samej kolumny, to pole zostanie zaktualizowane **automatycznie** przy każdej aktualizacji tamtego pola.
    * **Searchable** → Włącza pole jako pole **listy wartości**, umożliwiając wyszukiwanie w tabeli wyszukiwania.

#### **Ostatni krok: dodanie pól do układu**

Po skonfigurowaniu pól listy wartości **pamiętaj, aby dodać je do układu za pomocą Layout Builder**. Pola, które nie zostały dodane do układu, nie będą dostępne do użycia.
