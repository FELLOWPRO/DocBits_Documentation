# E-fakturowanie we Francji: zatwierdzone platformy i PEPPOL

## Aktualne zasady i harmonogram

Francuskie krajowe faktury B2B objęte reformą, wymieniane między przedsiębiorstwami podlegającymi VAT, muszą przechodzić przez **zatwierdzoną platformę (plateforme agréée, PA; wcześniej PDP)**. **Publiczny portal fakturowania (PPF)** pełni funkcje publicznego katalogu i gromadzenia danych podatkowych; nie jest alternatywną platformą wymiany tych faktur.

* **1 września 2026 r.:** Wszystkie przedsiębiorstwa objęte reformą muszą móc odbierać faktury elektroniczne. Duże przedsiębiorstwa (GE) i przedsiębiorstwa o pośredniej wielkości (ETI) muszą również od tego dnia wystawiać e-faktury i realizować obowiązki e-reportingu.
* **1 września 2027 r.:** Obowiązki wystawiania i e-reportingu obejmują małe i średnie przedsiębiorstwa (PME) oraz mikroprzedsiębiorstwa.

Właściwy obowiązek zależy od zakresu transakcji i kategorii przedsiębiorstwa. Sprawdź oficjalne [informacje o zatwierdzonych platformach](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees), [harmonogram wdrożenia](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation) i [odpowiedź ministerstwa](https://www.senat.fr/questions/base/2026/qSEQ260107185.html).

## PEPPOL i interoperacyjność

PEPPOL może zapewniać transport i interoperacyjność między połączonymi systemami i platformami. Korzystanie z niego nie zastępuje obowiązku użycia PA do wymiany faktur objętych francuskimi przepisami. Samo połączenie PEPPOL nie dowodzi spełnienia obowiązków wymiany faktur i przekazywania danych.

## Historyczny kontekst techniczny

Sześć diagramów i poniższe opisy API zachowano jako kontekst techniczny wcześniejszych materiałów o PPF/PDP. Używają dawnej terminologii i architektury; nie opisują aktualnej możliwości wymiany obowiązkowych faktur B2B przez PPF. Przed wdrożeniem integracji sprawdź aktualne specyfikacje PA i usług publicznych.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt="Diagram cyklu życia faktury od dostawcy przez stany Submitted, Received by the platform i Made available aż do wyników Rejected, Refused, Disputed, Partially approved, In hand i Completed"><figcaption></figcaption></figure>

### Historyczny model usług API

Wcześniejszy model opisywał dostęp do funkcji z narzędzi informatycznych organizacji partnerskich za pomocą dwóch metod:

* **Systemy informatyczne (IS):** API integrowano z systemami wystawców, odbiorców lub operatorów dematerializacji (OD). Niektóre API przeznaczono dla systemów PDP jako alternatywę dla integracji EDI.
* **Oprogramowanie zewnętrzne:** Dostawcy mogli dodać warstwę komunikacji do systemu klienta. Dawne odniesienia do połączenia z PPF należą do tego historycznego modelu i nie stanowią aktualnego kanału wymiany faktur.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt="Diagram Issuer OD-PDP i Receiver OD-PDP połączonych przez portale usług i oprogramowanie stron trzecich, z krokiem kontroli i odzyskiwania danych pomiędzy nimi"><figcaption></figcaption></figure>

### Historyczny diagram połączeń

Diagram przedstawia wcześniejszy kontekst połączeń między platformami. Aktualna implementacja musi spełniać wymagania PA; nie stwierdza się tu ogólnego obowiązku używania jednej sieci transportowej do wszystkich wymian.

<figure><img src="../../.gitbook/assets/Picture 2.png" alt="Diagram trzech ponumerowanych warstw kontroli: kontroli technicznych, kontroli aplikacji oraz kontroli funkcjonalnych i biznesowych, z których każda zasila kolejny krok procesu"><figcaption></figcaption></figure>

### Historyczne połączenie koncentratora

Wcześniejszy model opisywał rozwiązanie internetowe lub aplikacyjne, w którym **koncentrator wykonywał wywołania API w imieniu swoich klientów**. Przewidywał konto techniczne dla każdego partnera oraz aplikację w PISTE i połączenie z PPF dla koncentratora. Są to szczegóły historycznej architektury, a nie zweryfikowana aktualna procedura integracji.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt="Diagram modelu hub z jednym partnerem, jednym kontem technicznym, hubem, jedną aplikacją w ramach PISTE i jednym połączeniem"><figcaption></figcaption></figure>

### Historyczne źródła

Wcześniejszy materiał odwoływał się do [dawnego harmonogramu i omówienia prawnego](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform), [specyfikacji z 2022 r.](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html), [omówienia reformy z 2025 r.](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html), [kontekstu połączeń platform](https://nymus.be/fr/facturation-electronique-en-france/), [kontekstu PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) i [kontekstu wymiany](https://nymus.be/fr/facturation-electronique-en-france/). Te odnośniki i pozostałe diagramy zachowano jako kontekst historyczny. Aktualne obowiązki oraz rozróżnienie między wymianą przez PA a publicznymi funkcjami PPF opisują powyższe źródła urzędowe. Dawne odniesienie do art. 91 ustawy finansowej na 2024 r. nie ustanawia aktualnej opcji wymiany przez PPF.

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt="Diagram odbioru przepływu EDI i przepływu 2 przez API przechodzących kontrole funkcjonalne formatu semantycznego, katalogu i spójności danych przed włączeniem danych fakturowania i wynikiem przesłanej faktury"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt="Diagram przepływu EDI i przepływu API przechodzących kontrole funkcjonalne i specyficzne reguły biznesowe przed odrzuceniem lub odmową faktury albo przed otrzymaniem faktury i udostępnieniem jej"><figcaption></figcaption></figure></div>
