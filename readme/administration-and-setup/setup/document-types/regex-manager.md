# Regex Manager

Ta funkcja DocBits jest alternatywą dla klasyfikacji modelowej: pozwala tworzyć przeszukiwalne wyrażenia regularne dla typu dokumentu, do klasyfikacji i innych celów.

**Typ dokumentu:** Regex Manager pozwala pisać wyrażenia regularne, a DocBits wyszukuje je w dokumencie. Jeśli dokument pasuje do wyrażenia regularnego zdefiniowanego dokumentu, zostaje sklasyfikowany do odpowiadającego mu typu dokumentu. Na przykład, jeśli napiszesz wyrażenie regularne znajdujące „Gutschrift”, DocBits zaklasyfikuje każdy dokument zawierający ten termin jako notę korygującą.

**Pochodzenie dokumentu:** Dzięki temu DocBits na podstawie wyrażeń regularnych rozpoznaje kraj pochodzenia dokumentu. Na przykład, jeśli wyrażenie regularne dla dokumentu hiszpańskiego zawiera termin „Factura”, a DocBits znajdzie ten termin w dokumencie, rozpozna hiszpańskie pochodzenie dokumentu i odpowiednio go sklasyfikuje.

## Dostęp do Regex Manager

Aby skorzystać z tej funkcji, przejdź do Ustawienia → Typy dokumentów i kliknij „Nowy”. W kreatorze „Utwórz nowy typ dokumentu” podaj nazwę typu dokumentu i wybierz jako metodę ekstrakcji „Wyrażenie regularne” zamiast „Automatyczny”, a następnie kontynuuj przyciskiem „Następny”.

<figure><img src="../../../.gitbook/assets/regex-manager-create-pl-20261006.png" alt="Kreator DocBits tworzenia nowego typu dokumentu z wpisaną nazwą i wybraną opcją „Wyrażenie regularne”."><figcaption><p>Kreator „Utwórz nowy typ dokumentu” z nazwą typu dokumentu i wyborem między „Automatyczny” a „Wyrażenie regularne”.</p></figcaption></figure>

## Dodawanie i usuwanie Regex

Krok Regex pokazuje tabelę istniejących wyrażeń regularnych z kolumnami Pochodzenie i Wzór oraz przycisk „Dodać”, którym tworzycie nowe wpisy regex.

<figure><img src="../../../.gitbook/assets/regex-manager-list-pl-20261006.png" alt="Tabela Regex Manager z istniejącymi wyrażeniami regularnymi według pochodzenia i wzoru."><figcaption><p>Krok Regex z tabelą istniejących wyrażeń regularnych i przyciskiem „Dodać”.</p></figcaption></figure>
