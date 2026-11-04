# Configurazione LN

## Prerequisiti

Hai creato:

* Un Endpoint API ION
* Un File API ION
* Un File di Mappatura BOD
* Un File di Mappatura IDM

## Importare i File di Mappatura

Prima di configurare il flusso dati, è necessario importare i file di mappatura in InforOS

In ION Desk → Connetti e apri Mappature

![](https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ_aAIxcJil5LNiep4U6KZr3_tBfs1RRwXoW749q3FUxurXy_pT_k)

Clicca sull'icona di Importazione

![](https://lh7-us.googleusercontent.com/d_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn_Vd_b6rJaQng8A92JTa5YKBms4RuIvwmb0)

* Da qui devi selezionare i vari file di mappatura di cui hai bisogno, tra cui: SyncCaptDoc_SyncSuppInv, SyncSupplierInvoice_LoadSupplierInvoice e LoadSupplierInvoice_ProcessSupplierInvoice.
* Una volta importati tutti i file di mappatura, assicurati di approvare ciascuno di essi cliccando sull'icona di spunta all'interno di ciascun quadrato nella dashboard di Mappatura.

## DocBits a LN

Il passo successivo è configurare il Flusso Dati in ION Desk, vai all'applicazione ION Desk e seleziona Flusso Dati → + AGGIUNGI → Flusso Documenti come mostrato di seguito

![](https://lh7-us.googleusercontent.com/rjPVR1EFKw_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a_Fn3s1HSYDRmQVvgZtX_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I)

Vedrai quindi questa pagina, qui costruirai il flusso di informazioni da DocBits a M3

![](https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x_-lVRbK6tpTxvbRYKvwyWO_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8)

Un flusso dati LN assomiglierà a quanto mostrato di seguito (ci sono percorsi multipli a causa di ciascun percorso individuale che è destinato a un tipo di documento specifico, per questa spiegazione ci concentreremo sul flusso dati della fattura).

![](https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD_3myQY4Qcd9motySYh9U)

Tutte le parti della catena vengono trascinate e rilasciate dalla sezione superiore

Nella catena, DocBits e LN sono entrambe Applicazioni mentre tra di esse ci sono mappature che convertono i dati in una forma comprensibile dalla sezione successiva del flusso dati e "mappano" le informazioni in modo che vadano dove sono necessarie o destinate.

![](https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM)

### Applicazione DocBits

Assegna il nome appropriato come "DocBits" quindi seleziona il segno più e cerca il punto di connessione creato in precedenza come DocBits_Export o simile e cliccaci sopra.

Per creare questo punto di connessione, vai a ION Desk → Connetti → Punti di Connessione

![](https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530)

Clicca su "+ Aggiungi"

![](https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ_vj_-XPdegP1P0ySdos)

Seleziona "IMS tramite API Gateway" e compila le seguenti informazioni

![](https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I)

L'ID Cliente API ION si trova nel File API ION che hai creato in Come Creare un File API ION sotto il valore "ci".

Passa alla scheda documento e aggiungi il BOD Sync.CaptureDocument al punto di connessione DocBits come mostrato di seguito.

![](https://lh7-us.googleusercontent.com/Wy2BIr1z_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE_333uCWuKvKiVoo99FrXVg)

Quindi salva il punto di connessione premendo sull'icona del disco nell'angolo in alto a sinistra.

Torna alla sezione Flusso Dati di ION Desk per accedere al tuo flusso dati. La tua applicazione DocBits dovrebbe assomigliare a quanto mostrato di seguito.

![](https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw)
### Mappatura 1

Il primo nodo di mappatura dovrebbe apparire come segue

![](https://lh7-us.googleusercontent.com/9tlIun_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY)

### Mappatura 2

Il secondo nodo di mappatura dovrebbe apparire come segue

![](https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao)

### Applicazione LN

Dovrebbe già essere stato creato un punto di connessione LN o simile (per l'azienda LN appropriata) in INFOR, quindi, proprio come l'Applicazione DocBits, selezionalo facendo clic sul segno “+” e dovrebbe apparire come segue

![](https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE)

### BODs

![](https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk)

Le seguenti configurazioni dovrebbero apparire come segue:

#### Primo

![](https://lh7-us.googleusercontent.com/rj_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn_lmxtqUDVTm_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY)

#### Secondo

![](https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y_MF_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8)

#### Terzo

![](https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q_epAj9_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ_rbCCixhWcaJg2kHyyYw)

L'ultima icona dovrebbe essere vuota in quanto non contiene alcun documento o informazione.

Una volta aggiunti tutti i nodi necessari al flusso di dati, premi questo pulsante per attivare il flusso di dati

![](https://lh7-us.googleusercontent.com/WjQeGz_effl_RlkWC4CdJS9Dg_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o)
