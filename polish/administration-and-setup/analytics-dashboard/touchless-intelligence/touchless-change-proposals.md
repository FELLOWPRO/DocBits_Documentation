# Propozycje zmian i raporty

Rekomendacja może zawierać **propozycję zmiany** (change proposal), czyli pojedynczą zmianę ustawienia, która powinna pomóc. Administratorzy pracują z nią w czterech krokach:

1. **Podgląd** (Preview): pokazuje zmianę (obecna → proponowana wartość) i to, czego oczekuje DocBits. Nic nie jest zapisywane. **Zastosuj** jest możliwe dopiero po obejrzeniu podglądu.
2. **Zastosuj** (Apply): zapisuje dokładnie tę zmianę, która była w podglądzie. Jest to rejestrowane w logu.
3. **Mierz** (Measure): DocBits porównuje wskaźnik touchless tego samego typu dokumentu **przed i po**, w okresach o równej długości. W każdym okresie potrzeba co najmniej **20 dokumentów**, w przeciwnym razie wyświetla _not measurable_ (niemierzalne).
4. **Cofnij** (Undo): wycofuje zmianę.

{% hint style="warning" %}
Różnica przed/po jest **obserwacją**, a nie dowodem przyczyny. W tym samym czasie mogą zmieniać się inne rzeczy (nowy dostawca, sezonowy szczyt).
{% endhint %}

**Przykład.** Stosujesz _Włącz automatyczne dopasowanie PO i eksport_ dla faktur. Dwa tygodnie później **Historia zmian** (Change history) pokazuje: czysty wskaźnik przed 52 % (210 dokumentów), po 61 % (198 dokumentów). To +9 pp, wystarczająco dużo dokumentów, aby dało się to zmierzyć.

Administratorzy widzą też dwie sekcje między kluczowymi wskaźnikami a wykresami:

* **Prośby o usprawnienia** (Improvement requests): sugestie wysłane przez użytkowników z asystenta walidacji, w dwóch kartach **Otwarte** (Open) i **Historia** (History).
* **Propozycje nauczonych reguł** (Learned rule proposals): reguły, których DocBits nauczył się z korekt Twojego zespołu, na przykład „dla dostawcy X zamień wartość w polu Y". Zanim utworzysz regułę, sprawdź dokumenty, w których zastąpiłaby wartość zaakceptowaną przez Twój zespół. Sekcja **Po aktywacji** (After activation) pokazuje ręczne korekty pola docelowego przed i po wejściu reguły w życie.

<figure><img src="../../../.gitbook/assets/touchless-consulting-report-pl.png" alt="Raport doradczy z trzema najważniejszymi propozycjami, tabelą rankingową i problemami według domeny"><figcaption><p>Raport doradczy (Consulting report): najważniejsze propozycje, ranking wszystkich blokad z dokumentami i szacowanym wpływem miesięcznie oraz problemy według domeny. Przykładowa organizacja z danymi demonstracyjnymi; nazwy dostawców są fikcyjne.</p></figcaption></figure>

Administratorzy znajdą **Raport doradczy** na dole karty. Kliknij **Utwórz raport** (Create report), aby go załadować. Łączy on dla Twojej organizacji:

* **zmiany o największym efekcie**, uszeregowane, każda z domeną, problemem, zalecanym działaniem, liczbą dokumentów i **szacowanym** efektem miesięcznie,
* **domenę każdego problemu** (ekstrakcja, dane podstawowe, dopasowanie PO, automatyczne księgowanie, ustawienia, proces),
* **kontrole konfiguracji tabel**, na przykład _structured table output not used_ (nie używa się ustrukturyzowanego wyniku tabeli) lub _table column type mismatch_ (niezgodność typu kolumny tabeli) dla typu dokumentu i kolumny.

Wartości efektu są **szacunkami**. Jeśli raport odpowiada _forbidden_ (zabronione), Twoja rola na to nie pozwala.

## Powiązane strony

* [Touchless Intelligence](./)
* [Diagnoza dostawcy i klastry problemów](touchless-supplier-diagnosis.md)
* [Diagnoza dopasowania PO](touchless-po-matching-diagnosis.md)
