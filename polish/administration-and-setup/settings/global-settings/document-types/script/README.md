# Script

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2009.43.25.png" alt=""><figcaption></figcaption></figure>

{% embed url="https://youtu.be/n8NpWWIjmlA" %}
DocBits Document Scripts Explained: Automate Custom Logic in Your Document Workflow
{% endembed %}

#### Przegląd

Skrypty w Docbits są zazwyczaj pisane w języku skryptowym obsługiwanym przez system Python. Są one uruchamiane podczas przetwarzania dokumentu, aby zastosować złożoną logikę biznesową lub zapewnić integralność i dokładność danych przed dalszym przetwarzaniem lub przechowywaniem.

#### Główne funkcje i opcje

1. **Zarządzanie skryptem**:

* **Nazwa**: Każdy skrypt otrzymuje unikalną nazwę w celu identyfikacji.
* **Typ dokumentu**: Skojarza skrypt z określonym typem dokumentu, określając, do których dokumentów skrypt zostanie zastosowany.
* **Wyzwalacz**: Określa, kiedy skrypt jest uruchamiany (np. podczas przesyłania dokumentu, przed eksportem danych, po walidacji danych).
* **Status Aktywny/Nieaktywny**: Umożliwia administratorom aktywowanie lub dezaktywowanie skryptów bez ich usuwania, zapewniając elastyczność w testowaniu i wdrożeniu.

2. **Edytor skryptów**:

* Zapewnia interfejs, w którym skrypty mogą być pisane i edytowane. Edytor zazwyczaj obsługuje podświetlanie składni, podświetlanie błędów i inne funkcje wspomagające rozwój skryptu.
* **Przykładowy skrypt**: Skrypty mogą zawierać operacje takie jak iterowanie przez linie faktur w celu zweryfikowania sum lub usunięcia wpisów, które nie spełniają określonych kryteriów.

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2009.43.37.png" alt=""><figcaption></figcaption></figure>

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2498" %}
