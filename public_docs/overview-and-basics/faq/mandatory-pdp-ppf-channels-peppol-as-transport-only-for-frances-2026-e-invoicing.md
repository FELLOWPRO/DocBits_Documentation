# E-fakturowanie we Francji: zatwierdzone platformy i PEPPOL

## Aktualne zasady i harmonogram

Francuskie krajowe faktury B2B objęte reformą, wymieniane między przedsiębiorstwami podlegającymi VAT, muszą przechodzić przez **zatwierdzoną platformę (plateforme agréée, PA; wcześniej PDP)**. **Publiczny portal fakturowania (PPF)** pełni funkcje publicznego katalogu i gromadzenia danych podatkowych; nie jest alternatywną platformą wymiany tych faktur.

* **1 września 2026 r.:** Wszystkie przedsiębiorstwa objęte reformą muszą móc odbierać faktury elektroniczne. Duże przedsiębiorstwa (GE) i przedsiębiorstwa o pośredniej wielkości (ETI) muszą również od tego dnia wystawiać e-faktury i realizować obowiązki e-reportingu.
* **1 września 2027 r.:** Obowiązki wystawiania i e-reportingu obejmują małe i średnie przedsiębiorstwa (PME) oraz mikroprzedsiębiorstwa.

Właściwy obowiązek zależy od zakresu transakcji i kategorii przedsiębiorstwa. Sprawdź oficjalne [informacje o zatwierdzonych platformach](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees), [harmonogram wdrożenia](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation) i [odpowiedź ministerstwa](https://www.senat.fr/questions/base/2026/qSEQ260107185.html).

## PEPPOL i interoperacyjność

PEPPOL może zapewniać transport i interoperacyjność między połączonymi systemami i platformami. Korzystanie z niego nie zastępuje obowiązku użycia PA do wymiany faktur objętych francuskimi przepisami. Samo połączenie PEPPOL nie dowodzi spełnienia obowiązków wymiany faktur i przekazywania danych.

Katalog formatów DocBits opisuje strona [Przegląd standardów fakturowania elektronicznego](../../administration-and-setup/settings/global-settings/document-types/edi/currently-supported-e-invoice-standards/README.md).

## Historyczny kontekst techniczny

Sześć diagramów i poniższe opisy API zachowano jako kontekst techniczny wcześniejszych materiałów o PPF/PDP. Używają dawnej terminologii i architektury; nie opisują aktualnej możliwości wymiany obowiązkowych faktur B2B przez PPF. Przed wdrożeniem integracji sprawdź aktualne specyfikacje PA i usług publicznych.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt="Diagram cyklu życia francuskiego e-fakturowania obejmujący przygotowanie, odbiór, walidację i płatność, ze statusami dostawcy i nabywcy"><figcaption><p>Historyczny diagram cyklu życia: przygotowanie i wystawienie, odbiór, walidacja/zwrot i płatność, z etykietami statusu dostawcy i nabywcy widocznymi na każdym etapie.</p></figcaption></figure>

### Historyczny model usług API

Wcześniejszy model opisywał dostęp do funkcji z narzędzi informatycznych organizacji partnerskich za pomocą dwóch metod:

* **Systemy informatyczne (IS):** API integrowano z systemami wystawców, odbiorców lub operatorów dematerializacji (OD). Niektóre API przeznaczono dla systemów PDP jako alternatywę dla integracji EDI.
* **Oprogramowanie zewnętrzne:** Dostawcy mogli dodać warstwę komunikacji do systemu klienta. Dawne odniesienia do połączenia z PPF należą do tego historycznego modelu i nie stanowią aktualnego kanału wymiany faktur.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt="Diagram wystawcy i odbiorcy wymieniających faktury przez portale usług OD-PDP oraz PPF, z kontrolą i odzyskiwaniem danych"><figcaption><p>Historyczny diagram połączeń: wystawca i odbiorca są połączeni przez oprogramowanie zewnętrzne, portale usług i bloki OD/PDP wokół bloku PPF do kontroli i odzyskiwania danych.</p></figcaption></figure>

### Historyczny diagram połączeń

Diagram przedstawia wcześniejszy kontekst połączeń między platformami. Aktualna implementacja musi spełniać wymagania PA; nie stwierdza się tu ogólnego obowiązku używania jednej sieci transportowej do wszystkich wymian.

<figure><img src="../../.gitbook/assets/Picture 2.png" alt="Diagram kontroli przepływu, faktury i danych fakturowania: zgłoszenia dostawcy przechodzą kontrole techniczne, aplikacyjne i funkcjonalne, z odrzuceniami"><figcaption><p>Historyczny diagram kontroli: kontrole techniczne, aplikacyjne oraz funkcjonalne i biznesowe dla zgłoszeń ręcznych, przez API i EDI, wraz z wynikami: przepływ niedopuszczalny, dane fakturowania odrzucone i dane fakturowania odmówione.</p></figcaption></figure>

### Historyczne połączenie koncentratora

Wcześniejszy model opisywał rozwiązanie internetowe lub aplikacyjne, w którym **koncentrator wykonywał wywołania API w imieniu swoich klientów**. Przewidywał konto techniczne dla każdego partnera oraz aplikację w PISTE i połączenie z PPF dla koncentratora. Są to szczegóły historycznej architektury, a nie zweryfikowana aktualna procedura integracji.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt="Diagram partnerów z kontami technicznymi połączonych przez jeden koncentrator z jedną aplikacją w PISTE i jednym połączeniem"><figcaption><p>Historyczny diagram koncentratora: partnerzy z kontami technicznymi są połączeni przez jeden koncentrator z jedną aplikacją w PISTE i jednym połączeniem.</p></figcaption></figure>

### Historyczne źródła

Wcześniejszy materiał odwoływał się do [dawnego harmonogramu i omówienia prawnego](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform), [specyfikacji z 2022 r.](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html), [omówienia reformy z 2025 r.](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html), [kontekstu połączeń platform](https://nymus.be/fr/facturation-electronique-en-france/), [kontekstu PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) i [kontekstu wymiany](https://nymus.be/fr/facturation-electronique-en-france/). Te odnośniki i pozostałe diagramy zachowano jako kontekst historyczny. Aktualne obowiązki, w tym rozróżnienie między wymianą faktur przez PA a publicznymi funkcjami PPF, opisują powyższe źródła urzędowe. Dawne odniesienie do art. 91 ustawy finansowej na 2024 r. nie ustanawia aktualnej opcji wymiany przez PPF.

<figure><img src="../../.gitbook/assets/Picture 3.png" alt="Schemat blokowy procesu wystawiania: od przepływu EDI i odbioru przez API, przez kontrole przepływu, aplikacyjne i funkcjonalne, do wystawionej faktury"><figcaption><p>Historyczny schemat wystawiania: przychodzące przepływy EDI i API przechodzą kontrole przepływu, aplikacyjne i funkcjonalne, zanim dane fakturowania zostaną włączone; pokazano też ścieżki odrzucenia, przepływy wychodzące 1 i 2 oraz powiadomienia o cyklu życia.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Picture 4.png" alt="Schemat blokowy procesu odbioru: od przepływu EDI i odbioru przez API, przez kontrole z odrzuceniem lub odmową, do udostępnionej faktury"><figcaption><p>Historyczny schemat odbioru: kontrole techniczne, aplikacyjne i funkcjonalne obejmują szczegółowe reguły biznesowe, ze ścieżkami odrzucenia lub odmowy; zaakceptowane dane prowadzą do faktury otrzymanej i udostępnionej, obok przepływu odbiorcy 2 i powiadomień o cyklu życia.</p></figcaption></figure>
