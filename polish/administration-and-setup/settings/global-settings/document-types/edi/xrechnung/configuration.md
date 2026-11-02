# XRechnung

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits Poradnik dotyczący e-faktury: Przetwarzaj XRechnung / ZUGFeRD (Factur-X), sprawdzaj poprawność danych i automatyzuj przepływy pracy
{% endembed %}

## Przegląd

W panelu administracyjnym XRechnung znajdziesz następujące kluczowe komponenty:

## 1. Transformacja

### Cel

Proces Transformacji jest niezbędny do konwersji surowych danych, zwykle w formacie XML, na ustrukturyzowany format spełniający określone wymagania, np. wygenerowanie faktury. W XRechnung osiąga się to głównie za pomocą XSLT (przekształcenia języka rozszerzalnego arkusza stylów). XSLT to język przeznaczony do przekształcania dokumentów XML na dokumenty innego typu, takie jak inny XML, HTML lub zwykły tekst.

### Jak to działa

• Szablon XSLT: Plik XSLT definiuje sposób przetwarzania danych XML i jak powinien wyglądać końcowy wynik. Stosuje reguły i szablony do wyodrębniania, manipulowania i wyprowadzania danych z dokumentu XML.

• Elementy i atrybuty: Plik XSLT zawiera określone elementy i atrybuty kontrolujące proces transformacji. Na przykład \<xsl:value-of> służy do wyodrębnienia wartości określonego węzła z dokumentu XML.

### Funkcje administratora

• Modifying the XSLT:

• Edytuj istniejące szablony: Administrator może modyfikować istniejące szablony XSLT, aby zmienić sposób przekształcania danych wejściowych XML. Na przykład, jeśli istnieje potrzeba wyodrębnienia dodatkowych informacji z dokumentu XML, administrator może dodać nowe reguły w pliku XSLT.

• Utwórz nowe wersje: Jeśli wymagane są zmiany, administrator może utworzyć nową wersję szablonu XSLT. Dzięki temu poprzednie wersje pozostaną nienaruszone do celów historycznych lub do przywrócenia, jeśli zajdzie taka potrzeba.

### Przykład:

Załóżmy, że szablon XSLT wyodrębnia fakturę ID przy użyciu:

```xml
<xsl:value-of select="//INVOICE/INVOICE_ID/text()" />
```

Jeśli konieczne jest wyodrębnienie nowego pola, takiego jak numer referencyjny klienta, administrator może dodać:

```xml
<xsl:value-of select="//INVOICE/CUSTOMER_REFERENCE_NUMBER/text()" />
```

## 2. Podgląd

### Cel

Funkcja podglądu umożliwia administratorom przeglądanie wyników wygenerowanych przez transformację XSLT przed jej sfinalizowaniem. Ten krok jest kluczowy dla zapewnienia prawidłowego działania reguł transformacji i spełnienia wymaganych standardów.

### Jak to działa

• Walidacja w czasie rzeczywistym: Funkcja podglądu zapewnia renderowanie w czasie rzeczywistym wyglądu przekształconych danych po zastosowaniu ich do rzeczywistego dokumentu (np. faktury). Pomaga to we wczesnym wykryciu błędów lub problemów z formatowaniem.

• Korekty: Jeżeli podgląd wykazuje rozbieżności lub błędy, można dokonać korekt bezpośrednio w pliku transformacji (XSLT).

### Funkcje administratora

• Dostosowywanie podglądu:

• Modyfikuj ustawienia podglądu: Administrator może dostosować, które części transformacji mają być przeglądane. Na przykład mogą skupić się na określonych sekcjach dokumentu lub przetestować nowe reguły dodane do szablonu XSLT.

• Zapisz i wykonaj iterację: Po dokonaniu zmian podgląd można odświeżyć, aby zobaczyć zmiany. Ten iteracyjny proces umożliwia precyzyjne dostrajanie aż do osiągnięcia pożądanego wyniku.

### Przykład:

Jeśli administrator zauważy, że format daty w podglądzie jest nieprawidłowy (np. wyświetla YYYY-MM-DD zamiast DD-MM-YYYY), może zmodyfikować XSLT, aby poprawnie sformatować datę i natychmiast zobaczyć wynik w podglądzie.

## 3. Ścieżki wyodrębniania

### Cel

Ścieżki ekstrakcji definiują konkretne ścieżki w strukturze XML lub JSON, z których powinny zostać wyodrębnione dane. Proces ten jest niezbędny do wyodrębnienia kluczowych informacji w dokumencie, które zostaną wykorzystane w transformacji lub w innych zadaniach przetwarzania.

### Jak to działa

• XPath i JSONPath: Ścieżki wyodrębniania wykorzystują języki takie jak XPath (dla XML) lub JSONPath (dla JSON) w celu określenia lokalizacji danych w dokumencie. Ścieżki te mają kluczowe znaczenie, ponieważ informują system dokładnie, gdzie znaleźć i jak wyodrębnić wymagane informacje.

### Funkcje administratora

• Definiowanie i modyfikowanie ścieżek:

• Modyfikuj istniejące ścieżki: Administrator może modyfikować ścieżki wyodrębniania, jeśli zmieni się struktura danych lub jeśli konieczne będzie wyodrębnienie dodatkowych danych. Może to obejmować zmianę wyrażeń XPath lub JSONPath.

• Dodaj nowe ścieżki: W przypadku nowych pól lub punktów danych administrator może zdefiniować nowe ścieżki wyodrębniania. Wymagałoby to określenia poprawnej ścieżki w dokumencie XML lub JSON.

### Przykład:

W dokumencie faktury XML, jeśli ścieżka do faktury ID jest zdefiniowana jako:

```json
"invoice_id": "//INVOICE/INVOICE_ID/text()"
```

Należy dodać nowe pole, takie jak adres wysyłki, administrator może dodać:

```json
"shipping_address": "//INVOICE/SHIPPING/ADDRESS/text()"
```

## Faktycznie używane reguły i aktywacja

Reguły specyficzne dla organizacji mają pierwszeństwo przed regułami domyślnymi dla wykrytego formatu eDoc. Sprawdź aktywną TRANSFORMATION i sprawdź, który węzeł dostarcza invoice_type w przekształconym pliku XML; ścieżka zależy od formatu. Save zapisuje wersję roboczą; po testach użyj znacznika wyboru, aby ją aktywować. Wygenerowany Preview nie potwierdza zapisanego typu dokumentu. [Przewodnik rozwiązywania problemów z klasyfikacją](../credit-note-recognized-as-invoice.md) opisuje kody 381/261, późniejsze skrypty i środki ostrożności przy ponownym przetwarzaniu.
