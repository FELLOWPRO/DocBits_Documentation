# Obowiązkowe kanały PDP/PPF – PEPPOL wyłącznie jako transport w francuskim e-fakturowaniu 2026

## PDP lub PPF wymagane dla krajowych e-faktur B2B

Zgodnie z francuskim obowiązkiem e-fakturowania od 2026 roku firmy nie mogą polegać wyłącznie na sieci PEPPOL przy wymianie krajowych faktur B2B. Prawo wymaga, aby wszystkie faktury między francuskimi przedsiębiorstwami zarejestrowanymi jako podatnicy VAT były kierowane przez certyfikowaną platformę prywatną (PDP) lub państwowy portal fakturowania publicznego (PPF), co ma spełniać [wymogi](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform) prawne ￼. Innymi słowy, przedsiębiorstwa nie będą już wysyłać faktur bezpośrednio do klientów – muszą przekazywać je za pośrednictwem zatwierdzonej platformy e-fakturowania (PDP) lub przez [portal](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html) rządowy ￼. Dzięki temu organ podatkowy otrzymuje wymagane dane w czasie rzeczywistym. Samo wymienianie faktur przez PEPPOL bez udziału akredytowanej platformy PDP/PPF nie spełniałoby obowiązków w zakresie raportowania i przesyłania danych.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt=""><figcaption></figcaption></figure>

### Wprowadzenie do oferty usługi

Tryb API pozwala użytkownikom korzystać ze wszystkich dostępnych dla nich funkcji z poziomu narzędzi IT już wdrożonych w strukturach partnerów. Istnieją dwie metody integracji:

### ·       Integracja z systemami informatycznymi (IS):

Interfejsy API są integrowane bezpośrednio z systemami informatycznymi lub oprogramowaniem zarządczym stron wystawiających i odbierających faktury albo ich operatorów dematerializacji (OD). Użytkownicy mogą w ten sposób bezpośrednio korzystać z funkcji rozwiązania i ich aktualizacji ze swoich zwykłych narzędzi IT, wewnętrznych lub oferowanych przez ich OD.

Interfejsy API mogą być również integrowane z IS platform PDP, aby zapewnić im większą elastyczność (w porównaniu z trybem EDI), przy czym niektóre API są przeznaczone wyłącznie do ich użytku.

### ·       Integracja z oprogramowaniem zewnętrznym:

Wydawcy oprogramowania będą mogli oferować oprogramowanie oparte na API. W zależności od trybu wybranego przez wydawcę połączenie może być następnie realizowane przez wydawcę lub przez samego klienta podczas instalacji albo wdrożenia w jego IS. To oprogramowanie zewnętrzne uzupełni system informatyczny klienta, dodając warstwę komunikacji z PPF.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt=""><figcaption></figcaption></figure>

## PEPPOL wykorzystywany wyłącznie jako warstwa interoperacyjności

Francja przyjmuje PEPPOL jako część swojej infrastruktury, ale wyłącznie jako warstwę transportową w ramach systemu PDP, a nie jako niezależną ścieżkę zgodności.  Francuski organ podatkowy (DGFiP) zostaje organem Peppol Authority, aby ujednolicić sposób, w jaki platformy PDP się [łączą](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html) . Wszystkie certyfikowane platformy PDP mają obowiązek łączyć się przez sieć PEPPOL w celu wymiany [faktur](https://nymus.be/fr/facturation-electronique-en-france/) .  Oznacza to, że PEPPOL ułatwi interoperacyjność między autoryzowanymi platformami – nie zastąpi potrzeby korzystania z tych platform.  W praktyce firma może korzystać z PEPPOL wyłącznie za pośrednictwem platformy PDP (lub PPF działającego w ograniczonej roli), która używa PEPPOL do wysyłania lub odbierania faktur. Potwierdzają to oficjalne wytyczne: portal publiczny koncentruje się na gromadzeniu danych, natomiast dystrybucja faktur będzie odbywać się wyłącznie przez platformy PDP, które do [wymiany](https://nymus.be/fr/facturation-electronique-en-france/) wykorzystują sieci takie jak [PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) .

\


<figure><img src="../../.gitbook/assets/Picture 2.png" alt=""><figcaption></figcaption></figure>

## Połączenie przez hub:

Hub udostępnia swoim klientom rozwiązanie internetowe lub aplikacyjne, które umożliwia wykonywanie różnych wywołań API. **To zatem hub wykonuje wywołania API w imieniu wszystkich swoich klientów**. W takim przypadku każdy partner musi mieć konto techniczne, ale tylko hub potrzebuje aplikacji w PISTE i połączenia z PPF.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt=""><figcaption></figcaption></figure>



Źródło: Artykuł 91 francuskiej ustawy finansowej na 2024 rok (podsumowany przez EY) nakazuje wysyłanie e-faktur przez certyfikowaną platformę PDP lub portal państwowy .  Aktualizacje francuskiego organu podatkowego dodatkowo wyjaśniają, że po reformach z 2024 roku przedsiębiorstwa muszą korzystać z zarejestrowanej platformy PDP do e-fakturowania B2B (PPF nie będzie już służył jako bezpłatna platforma wymiany) .  PEPPOL jest wdrażany w celu połączenia tych platform PDP, a nie jako alternatywny kanał poza systemem .  Potwierdza to, że samo korzystanie z sieci PEPPOL jest niewystarczające – zgodność w ramach francuskiego reżimu e-fakturowania 2026 wymaga integracji z PPF lub certyfikowaną platformą PDP, przy czym PEPPOL służy wyłącznie jako podstawowa sieć dostarczania między tymi platformami.

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt=""><figcaption></figcaption></figure></div>
