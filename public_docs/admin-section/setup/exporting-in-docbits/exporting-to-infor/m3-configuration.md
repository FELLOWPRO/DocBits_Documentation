# Konfiguracja M3

## Wymagania wstępne

Utworzyłeś:

* Punkty końcowe interfejsu API ION
* Plik interfejsu API ION
* Plik mapowania BOD
* Plik mapowania IDM

## Importowanie plików mapowania

Przed skonfigurowaniem przepływu danych musisz zaimportować pliki mapowania do InforOS.

W ION Desk → Połącz i otwórz Mappings

![](https://lh7-us.googleusercontent.com/EV8z6b_W9tjTgML0j3qJAYHCTYLd4N5yLrArdIECftYpMOCRTRJ_a7eADEzljFM4XHxMUJ6Nx9Z6EN3Hmzote5F0HrM5zd4p1BS0NYicUWDnkhQFX-_3MGbblEYi6x2a1K25SclYYttgW3cWQbOjvfQ)

Kliknij ikonę Importuj

![](https://lh7-us.googleusercontent.com/agBHtjNitneogoZsSG1791QAARbvesv9eSriAkw0HL9Fy372Ty6SmQG1sKJjOYZCuE0SnGT3agHAFRJYjgGNxJrN1CMJj9L-fSPhNmXxN78iDKqrrdgEVYFHxsNwy9XLiUFpBCQ1wnWlwyeFH08DsWI)

Następnie musisz wybrać różne pliki mapowania, które będą potrzebne, w tym: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice i LoadSupplierInvoice\_ProcessSupplierInvoice.

Po zaimportowaniu wszystkich plików mapowania upewnij się, że zatwierdzisz każdy z nich, klikając ikonę zaznaczenia w każdym z kwadratów na pulpicie mapowania.

## DocBits do M3

Następnym krokiem jest skonfigurowanie przepływu danych w ION Desk, przejdź do aplikacji ION Desk i wybierz Przepływ danych → + DODAJ → Przepływ dokumentów jak poniżej

![](https://lh7-us.googleusercontent.com/Kkro7w2LPfnwf-JPMmPI2DzrSRNEi_F9aWW02KDtBvAZz_R7j9DZ71Nqw3ETPSQqDuxBzJ1TU8Uuzz5jU9rOO_tvDBf9abVF-FDSxln_pjr-HMRdYBnGMwgcM6hg-pC2B7FgdBkXibivMB4PptvZ6fk)

Następnie zobaczysz tę stronę, tutaj zbudujesz przepływ informacji z DocBits do M3

![](https://lh7-us.googleusercontent.com/K0B1lC_KLO5RZqGqAltp6JnZZ1sfZG4wg-i_nxZCnLjML33yvViRUHOInK3iHYbzbV4I0uqDY8JpsZMxssD8bbJy24A1zKr9PfQEyqVxewx_L87RCIwzn5MDRjMqgx4X42vkKthbyz--5DDe1H0rvHQ)

Przepływ danych M3 będzie wyglądał podobnie jak pokazano poniżej (istnieją 3 aplikacje i interfejsy API DocBits ze względu na ich użycie w 3 osobnych środowiskach).

![](https://lh7-us.googleusercontent.com/6Oy_UBzYNml-7_sayDEKhqYF92yDzlUNzmGLQSWZOfDT-avvfg3oNUnv_DtXNSP0XF43D-zgIizIuTrCXl6ockLU2uQLYFJna72fzL5BP-T89xjF4oWz2eAz9w0hsoVieyTpgSw_Prvj--89Kc4Kqoo)

Wszystkie części łańcucha są przeciągane i upuszczane z górnej sekcji

W łańcuchu DocBits i M3 są obie aplikacje, podczas gdy pomiędzy nimi znajdują się mapowania, które konwertują dane na formę zrozumiałą przez następną sekcję pociągu i "mapują" informacje, tak aby trafiły tam, gdzie są potrzebne lub mają trafić.

![](https://lh7-us.googleusercontent.com/1kjgKNmIQ-NbM_JukcPsj7qmyiMB9b693ixg6Dh1kOlZ6NKgBXViYwn0MNUBHt0WKKWf_1gpRvxgqjIaqpqcy-SyXoYjhJLt3m_bv7wbVADzqHRsx8TYXWyIQO82X-Ixfl5b7iI7nxTRkw06sX3xsBM)

### Aplikacja DocBits

Nadaj jej odpowiednią nazwę, na przykład "DocBits", a następnie wybierz znak plus i wyszukaj punkt połączenia, który utworzyłeś wcześniej, na przykład DocBits\_Export lub podobny, i kliknij na niego.

Aby utworzyć ten punkt połączenia, przejdź do ION Desk → Połącz → Punkty połączenia

![](https://lh7-us.googleusercontent.com/8qsMIUKMrgmcYqqJPL2zF4GVeHuvSHvn8Z7dfonRuvKFPcXmN4hx2PIrXko4lvW7ayD7s2VRFOMvWkQSxfAH5tTuhg0XhzYmSzlsgnowWRw8GmQC2y5BjcS9X2MjDzLSutgoHg2VN59kCYRunMSxkIY)

Kliknij "+ Dodaj"

![](https://lh7-us.googleusercontent.com/-3-3TzgEQppYmX64-clxjp1JBjNz9fsA2FDPqirgNF0wL8DsDJACzUBuSw5wBL2k9JanqvMzAG352CWafOdtjhMfZalJnBFVSjaWA1AszhCjKtCsTvLUUqq1WwMfF-PqL-u7LRo4TPbj4fP2_j48240)

Wybierz "IMS za pośrednictwem bramy API" i wypełnij następujące informacje

![](https://lh7-us.googleusercontent.com/wImUEi9mXiQjW5O6mp7_IrKk4CTaHFs903DJ6TXqUEcjGq45TnUWdusFTGH1jzpBPP_TC7rokyjrkYWmh3emSKBQs05qYbO80TO87De0C5OveVURykQMCLFRRYakEMoFHpoeXzxH5QIbKJdjxujeY98)

ID klienta interfejsu API ION znajduje się w pliku interfejsu API ION, który utworzyłeś w Jak utworzyć plik interfejsu API ION, można go znaleźć pod wartością "ci".

Przełącz się na kartę dokumentu i dodaj BOD Sync.CaptureDocument do punktu połączenia DocBits jak poniżej.

![](https://lh7-us.googleusercontent.com/ga1q0Uwdi2GNwuiz22NvDtCzGL0krSkBPLsEVxE-mtoMV7CtEU8TPO0PhF40oB9NB9iv7DCJi9niLnsKjpqarWJsgGRdc1W0pFl9rTDm7i2_BS...
### Mapowanie 1

Pierwszy węzeł mapowania powinien wyglądać następująco

![](https://lh7-us.googleusercontent.com/F9AcE4V-s9vs-0kRz8BcCtdHUUQoaooyK3GqOj8pAQWuvIguoUO-tJx7WBEW6_GmzwNsJp8VUYezGCiLPXvPhEynac3FPh_NJOvqs1SXtMIUsF5_HjWmcvY3VC-eZsjG0ZE8HmsKsFhocadr96drSbY)

### Mapowanie 2

Drugi węzeł mapowania powinien wyglądać następująco

![](https://lh7-us.googleusercontent.com/8M_V2BtkOGyqV-828ct5c2QvSs5n5_RtLjlH717kspZwlgtfjbz6tpOJCCXDelruBenMjxsJPqncQ5hUw2bQkM3ya7_WrVyEBz3UnaU-C9oVOWB8nNtXA20RBYgO3EBMon2TfgpefY0lSPBzF9NoTeU)

### Mapowanie 3

Trzeci węzeł mapowania powinien wyglądać następująco

![](https://lh7-us.googleusercontent.com/x9QUHTgQrNaeKnTeMIUflkWjcBr2c3LgsYe2BZBjv01hXiEkvsLtU0GzYt5KppcE12ZqxWeBJ1kbLOC6qA3yKHhujCZt3sFpDNE5yERkHHMJJEjFl0jJE90nQ-iXeMLbR-Bk6G0NIL8AqG3U48Seiuc)

### Aplikacja M3

W INFOR powinien już istnieć punkt połączenia o nazwie M3 lub podobnej, więc tak jak w przypadku aplikacji DocBits, wybierasz go, klikając znak "+" i powinno to wyglądać następująco

![](https://lh7-us.googleusercontent.com/JTXIN5QxidvFJyjegxSw8kA7yVfHfuypxi5yX21CsSlGtOVgykc52U2r0077-cKqNhc0B4zSSZotlipFesmLo371kho3wUSRPzmwEir-stbxyZV1PwCDXkq6qJMm4PNXt_wGarDMixGIU0tu-eAqV5Y)

### DocBits API

Najpierw musisz utworzyć to API jako punkt połączenia, co robisz przez:

ION Desk → Połącz → Punkty połączenia

![](https://lh7-us.googleusercontent.com/VOXW6LixmcKjHW0CTOO5L8fK6r-4k3jqk0AnoR6DEVoGgJMbx65hS3yKSgMWItypdz4Ha82T-bKCN0aMv34gif-b0Aw7zpDFPBK9G-K6x9_csrM9xyKcpmWam15tKqO1_rwKtMsJ2CSoWqdpLxCD5tA)

Kliknij "+ Dodaj" i wybierz API

![](https://lh7-us.googleusercontent.com/c1RAUNoA3YBhvf6FLJ_L3ouyZwHK-3bBRU83eL3oAQXjG6SjWEO9O-gDKPItPm8AI_YhadaCZU-GxY-qUXNuQMiRiKUhBYUtJ8kOFVg_YYpzJDSoJ68NYSaEtHBSyyfnq0VbHUdWY1e8lBQ0j_G5xvI)

Informacje, które wpisujesz, powinny wyglądać następująco

![](https://lh7-us.googleusercontent.com/h2KU6pKeKl9wX8oyul0KmbL_kg-iPQJpBqbf29l64ED2e-Z4tNj8-m4hBN_4SSiNPf2TrE92TD4H0-0AZ0eWxMFmDV22IdPlU9NO4XlQF9k0Swg0X3Sm1HMsSPvWi7Q1HUr8uy8j3aDRheFxZqZ2Gbc)

Przełącz się na kartę dokumentu i dodaj następującą konfigurację

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_api_docs1-1024x279.png)

**Acknowledge.SupplierInvoice**

Konfiguracja tego BOD wygląda następująco

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_ack_11.png)

Upewnij się, że wybrano opcję "Wyślij do API" w powyższym menu.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_ack_2-1024x338.png)

Na koniec upewnij się, że zmienisz również treść żądania, aby wyglądała tak.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_ack_3-1024x260.png)

Powtórz ten proces dla pozostałych BOD, każda konfiguracja jest pokazana poniżej.

**Sync.PurchaseOrder**

Konfiguracja tego BOD wygląda następująco

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_po_1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_po_2-1024x359.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_po_3-1024x297.png)

**Sync.RemitToPartyMaster**

Konfiguracja tego BOD wygląda następująco

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_remit_1-1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_remit_2-1024x351.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_remit_3-1024x299.png)

**Sync.SupplierPartyMaster**

Konfiguracja tego BOD wygląda następująco

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_sup_1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_sup_2.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Exp_M3_sup_3-1024x295.png)

### BODs

![](https://lh7-us.googleusercontent.com/zaDSnm844wXqyefN58Y1DvuJOnMaoOrYQ_12Z5ZSng8-TPy38Th2ZPdAD6hyIYCOvBKGPDSvGpTmtBPq4K5IwyGtsKyMvk-CKOuY-hzD-RL7UrsG39qLN7m3_IDcDS66KeIQF5e70OWlHO1cbVvQUXM)

Następujące konfiguracje powinny wyglądać następująco:
#### Pierwszy

![](https://lh7-us.googleusercontent.com/5gLpbQEYYW90dVLkSc5V60LeToMe2wcOcHHtwTdIdT0o0Gktu8T_7i7zfNikjgETM3QmzAsJAknlEGeB0W0YFLLi56g2PKPwyr2zPcHaKdu8XJWHgaC1u4--_CHNYfd1wQ__3kZpv1_PwyZty3JEyak)

#### Drugi

![](https://lh7-us.googleusercontent.com/xbWTcP8hYA72Ijt7_IV6l-9jKeSalbRPvTn7aNVcnWYMQcD2RDjM-EzKpBKjSIKF_-r8BaxmmCo9uz6-E-vC9flKb4toU3SH24EPLgbXc-VcfJeDdJKglf5P6WV6XYZg0cZVWAoyvS8qgtuR6ZqJYlI)

#### Trzeci

![](https://lh7-us.googleusercontent.com/F8wVWXuHkLLW2kuu_7Dxe9LhyYdm04tl__Sp6FjeTyk_JFUzhCIUhVlKS_cq3I3FP_h2ksV4zEJHFC_KXK6sSZ5iz5yhTFZcPnH1HS_RvZb2Nr-UXYQ1H316UMoj6eRv6wMn3wHX842B5WVfPHVnJ74)

#### Czwarty

![](https://lh7-us.googleusercontent.com/myhi9y2sCvS5ZFkIJa5ysLbu7p0X6CYqbiuJ3sQ5-O-2QWlfAseunjwhXK0kakmAofplm0zmh_H1Np7bA559w0-jdurQUsZwYF9CyKYSKSeGnQaIit0HQ5iN-3Xv8CIC-5nk6mMj3JTDS97SlzbsOFE)

#### Piąty

![](https://lh7-us.googleusercontent.com/c-5iaUhhx0swH-mQfXE5Mdwe4J0skGt7mst4kJdOpjL3Uat329TZmKM5Af-lGQWmcmBht-ib_aUj4dVG7GaUAHHULjly3jxsR8MJNnLDcu5eZB268Vy-dXPxHmkVB8dMZTRhU5SUB59AREurJlW-K6o)

Ostatnia ikona powinna być pusta, ponieważ nie przenosi żadnego dokumentu ani informacji.

Po dodaniu wszystkich niezbędnych węzłów do przepływu danych, naciśnij ten przycisk, aby aktywować przepływ danych (po zapisaniu przepływu danych, naciskając ikonę dysku twardego).

![](https://lh7-us.googleusercontent.com/WIecHktG7e5dbVScLbR8hUcZUdCEWXBW4xWDEuq0IqTMmguA_Ih_oRymvpk6CzowWFG5TTSCPIH-68ICnPSOPxeZksc-n4bmpvuH8dvHuHFU1DlppGRno3PKjCSJiK12p9bNlo_9cN2t9Ps3nbqF3xE)
