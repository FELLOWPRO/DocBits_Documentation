# Workflow Logs

## **Pregled**

**Workflow Logs** omogućavaju korisnicima da analiziraju koji su radni tokovi izvršeni za dokument, da razumeju rezultate izvršavanja i da se udube u detalje na nivou uslova radi otklanjanja grešaka ili validacije.

## **Pristup zapisima radnih tokova**

Za pristup zapisima radnih tokova:

1. Idite na **Dashboard**.
2. Kliknite na **Actions menu** (ikonica sa tri tačke) pored željenog dokumenta.
3. Izaberite **Workflow Logs** iz menija.
   * <mark style="color:red;">**Napomena**</mark>: Funkcija Workflow mora biti omogućena da biste pristupili ovoj opciji.
4.  Otvara se **bočni panel** koji prikazuje rezime izvršenih radnih tokova.\\

    <div align="left"><figure><img src="../../.gitbook/assets/image (8).png" alt="" width="563"><figcaption></figcaption></figure></div>

## **Komponente panela Workflow Logs**

#### **1. Brojači rezimea radnih tokova**

Nalaze se na vrhu panela sa zapisima:

* **Plavo**: Ukupan broj izvršenih radnih tokova.
* **Crveno**: Radni tokovi koji su se završili **greškama**.
* **Žuto**: Radni tokovi koji **nisu završeni** zbog neslaganja uslova.
* **Zeleno**: Uspešno **izvršeni** radni tokovi.

#### **2. Tabela izvršavanja radnih tokova**

Svaki red u tabeli predstavlja jedno izvršavanje radnog toka i uključuje:

* **Workflow Name**
* **Timestamp** (Created On)
* **Runtime** (u sekundama)
* **Result Icon**:
  * Zelena kvačica: Radni tok je uspešno izvršen.
  * Crveni krstić: Radni tok je izvršen sa greškom.
  * Narandžasta crtica: Izvršavanje je zaustavljeno jer uslov nije ispunjen

Klik na **strelicu** sa leve strane svakog reda proširuje **detaljan prikaz radnog toka**.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="" width="563"><figcaption></figcaption></figure></div>

### **Detaljan prikaz radnog toka**

Klik na određeni red radnog toka otvara njegov **detaljan zapis izvršavanja**, koji prikazuje:

#### **Evaluaciju uslova**

* Blok **When...**: Početni uslov.
* Blok(ovi) **And...**: Dodatni uslovi.
* Blok(ovi) **Then...**: Akcije koje se izvršavaju kada su svi uslovi ispunjeni.

Svaka linija uslova prikazuje:

* **Zelena kvačica**: Uslov je ispunjen.
* **Narandžasta crtica**: Uslov nije ispunjen.
* **Crveni krstić**: Uslov nije uspeo **zbog greške**

### **Važna napomena o ponašanju**

Ako uslov u radnom toku **nije ispunjen**, sistem **prestaje da evaluira sve dalje kartice radnog toka** u okviru tog radnog toka. Ovo ponašanje sprečava nepotrebnu obradu\
Kao vizuelni indikator, kartica koja **nije ispunila svoj uslov** prikazuje se **sivom bojom**, a sve **naredne kartice** u istom radnom toku takođe će biti prikazane **sivom bojom**, što ukazuje na to da **nisu izvršene**.
