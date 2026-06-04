# Confirmed Delivery Date

<figure><img src="../../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

Cel: Ta karta DocBits służy do zapewnienia, że potwierdzone daty dostawy na fakturach lub dokumentach wysyłkowych są zgodne z zaakceptowanymi datami dostawy określonymi w tabeli wyszukiwania danych podstawowych. Pomaga zarządzać oczekiwaniami i przestrzeganiem zaplanowanych dostaw w ramach łańcucha dostaw.

Funkcjonalność:

* Confirmed Delivery Date: Ten komponent karty przechwytuje datę dostawy potwierdzoną na fakturze lub dokumentacji wysyłkowej.
* Master Data Table Lookup: Karta odwołuje się do tabeli wyszukiwania danych podstawowych określonej przez użytkownika (identyfikowanej przez parametr \<Master Data Table>). Tabela ta zawiera zaakceptowane daty dostawy do porównania.
* Operator Value: Użytkownicy mogą określić, w jaki sposób potwierdzona data dostawy powinna być porównywana z zaakceptowaną datą dostawy z tabeli danych podstawowych. Dostępne operatory obejmują:
*
  * Equals (=): Zapewnia, że potwierdzona data dostawy jest taka sama jak zaakceptowana data dostawy.
  * Not Equal (≠): Wskazuje rozbieżność między potwierdzoną a zaakceptowaną datą dostawy.
  * Before (<): Weryfikuje, że potwierdzona data dostawy jest wcześniejsza niż zaakceptowana data dostawy.
  * After (>): Sprawdza, czy potwierdzona data dostawy jest późniejsza niż zaakceptowana data dostawy.

Zastosowanie: Ta karta jest nieoceniona dla menedżerów ERP i księgowych finansowych, którzy muszą monitorować i zapewniać zgodność z harmonogramami dostaw. Jest szczególnie przydatna w sektorach, w których terminowość dostaw jest kluczowa, takich jak produkcja, handel detaliczny i dystrybucja.

Przykładowy scenariusz:

* Faktura wymienia potwierdzoną datę dostawy 10 czerwca. Tabela danych podstawowych pokazuje jednak zaakceptowaną datę dostawy 15 czerwca. Ustawiając operator na "Before", karta potwierdza, że towary są zaplanowane do wcześniejszej dostawy, umożliwiając odpowiednie dostosowanie planowania logistycznego.

Wdrażając kartę "Compare with Purchase Order: Confirmed vs. Accepted Delivery Dates", organizacje mogą proaktywnie zarządzać swoim łańcuchem dostaw, zapewniając, że dostawy są planowane i realizowane zgodnie z uzgodnionymi terminami, zwiększając tym samym efektywność operacyjną i zadowolenie klientów.

\
\
