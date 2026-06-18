# Uvoz

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 10.48.36.png" alt=""><figcaption></figcaption></figure>

"Uvoz" postavke u vašem sistemu za obradu dokumenata omogućavaju vam da konfigurišete kako se dokumenti uvoze u sistem sa različitih izvora, uključujući postavke za FTP (File Transfer Protocol) i e-poštu. Evo detaljnog pregleda ovih postavki:

1. **Postavke Dokumenata**:
* **Ograničenje na stranice**: Ovo vam omogućava da ograničite obradu na određeni broj stranica iz svakog dokumenta.
* **Uslovi plaćanja u danima**: Definiše podrazumevane uslove plaćanja (u danima) koji se mogu primeniti na dokumenta.
* **Obrazac datuma**: Postavlja obrazac za prepoznavanje i formatiranje datuma unutar uvezenih dokumenata.
2. **FTP Uvoz**:

* **Tip**: Definiše tip FTP protokola koji se koristi (npr. SFTP).
* **URL servera**: Adresa servera sa koje će se dokumenti preuzimati.
* **Korisničko ime i port**: Podaci za prijavu i broj porta za pristup FTP serveru.
* **Podrazumevani direktorijum**: Određuje direktorijum na FTP serveru sa kog će se uvoziti fajlovi.

Dodatna opcija za dodavanje novih podataka uključuje polja kao što su:

* **Lozinka**: Za autentikaciju.
* **Obrasci podudaranja imena fajlova**: Da biste odredili koje fajlove uvesti na osnovu njihovih imena.
* **Podorganizacije**: Izaberite kojoj podorganizaciji treba primeniti postavke uvoza.

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 10.48.45.png" alt=""><figcaption></figcaption></figure>

1. **E-pošta Uvoz**:

* **Adresa e-pošte**: Podesite e-poštanski nalog na koji se dokumenti mogu poslati radi uvoza.
* **Korisničko ime i lozinka**: Podaci za pristup e-poštanskom nalogu.
* **Protokol i enkripcija**: Odredite protokol (IMAP, POP3) i tip enkripcije.
* **Spajanje priloženih dokumenata**: Opcija za kombinovanje svih priloženih dokumenata u jedan dokument prilikom uvoza.

Ovo takođe omogućava određivanje podorganizacija za precizniju kontrolu nad usmeravanjem e-pošte unutar vaše organizacione strukture.

{% hint style="info" %}
**Napomena:** uvoze se samo prilozi sledećih tipova:

* `.pdf`
* `.tiff` / `.tif`
* `.eml`
* `.dat`
* `.xml`
* `.edi`
* `.purchaseorder`

**Kako se prilozi prepoznaju:** pored navedenih ekstenzija, DocBits prepoznaje dokument i po **stvarnom sadržaju datoteke** (potpisu), ne samo po tipu koji navodi pošiljaočev mejl-server. Ovo je važno za **prosleđene** poruke: posredni mejl-serveri/gejtveji često ponovo označe prilog generičkim tipom (`application/octet-stream`) umesto npr. `application/pdf` ili `application/xml`. DocBits ih i dalje ispravno prepoznaje i uvozi.

* Prosleđene **`.eml`** poruke i Outlook **`winmail.dat`** (TNEF) prilozi se raspakuju i dokumenti unutar njih se uvoze.
* **Zanemaruje se:** ugrađene slike (logotipi potpisa / grafika — PNG, JPG, GIF, BMP) se tiho preskaču i ne računaju se kao neuspeli uvoz.

Ako se prilog ne može uvesti i opcija **„Odgovori na ovaj mejl ako uvoz nije moguć"** je uključena, obaveštenje se šalje na podešenu adresu.
{% endhint %}

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 10.48.56.png" alt=""><figcaption></figcaption></figure>
