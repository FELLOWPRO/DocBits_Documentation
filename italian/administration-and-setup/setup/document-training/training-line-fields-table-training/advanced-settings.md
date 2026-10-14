# Impostazioni Avanzate

In alcuni documenti, le strutture delle tabelle possono essere complesse, con più righe, contenenti informazioni raggruppate o includendo righe extra non necessarie. Le _Impostazioni Avanzate_ in modalità di addestramento ti consentono di ottimizzare l'estrazione delle tabelle per tali casi, migliorando precisione e coerenza.

Per accedere a queste impostazioni, attiva la **Modalità di Addestramento** e clicca sull'icona a ingranaggio **Impostazioni** nella barra delle azioni in alto:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FW1cBx4IOjycKv6IZM9AX8Wggj1eEBgzBVJWgsyWkutX9dRRJuEjQtSCsPaNZuRndd9ewMVvfqSXr45C-2cO-pxXkYFdl_9eEGVW6-UBqqZCsuhia6alJjD1ZuZawwSbjS9Yeywe1wDK5yAcIOUH5QAw\&width=768\&dpr=4\&quality=100\&sign=4bf6ac31\&sv=2)

## Conteggio Righe Intestazione

**Usa questa impostazione per definire quante righe compongono l'intestazione della tabella.**

Alcune tabelle hanno intestazioni su più righe. Ad esempio, l'intestazione di questa tabella si estende su due righe:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FJ_nYZKzUSJHcpJuNp1ykf6shnfetOuiIPhyhyTfSqh_cTsDT5obwOSIc21OsLkjF9tMBP7Q1GQ1ZQfBsEmQIrJpfX3QpdjHnLkzInsjpngeg2L7i_TAyl9MdVmgHsDpUvoURdxfqp8FOdJxuRAMCwhk\&width=768\&dpr=4\&quality=100\&sign=554fa70\&sv=2)

Imposta il **Conteggio righe intestazione** di conseguenza:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FG8-QpKxnRin9PGPmkbtJ35r1EugXsD4_Yd5QvTkdbb7sXqRVC3a9t0cIlNILJHLr--GsykgAlMJmMYbJaUoMqHEPvAT3PlPNf-syCmPz_GVMFEMsbhcHI2DQBbT4MJXjS2Sx7M3xl4zAzcw3aa-XNms\&width=768\&dpr=4\&quality=100\&sign=a487f5a9\&sv=2)

### Perché è importante?

Se non imposti questo, DocBits potrebbe considerare la seconda riga come dati anziché parte dell'intestazione, portando a errori di estrazione:

**Prima:**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F35BElgcq-zbs8wcGcguVSKHRpwQXqQG9dQmBaYa8BT4RNwJxd6g-jL5wlQgrnVLrMxtpncr8ayaasWVV3snGpBiDUWs4Zx7Tn2Dck-YFBpanlcN500yIWkVz9RJXQhoq6op0WbYcgklp_LsmE9LXt9k\&width=768\&dpr=4\&quality=100\&sign=7c68faf7\&sv=2)

Dopo:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FbPGn9eWPK3Mmbu_ab2N3tVVP8ODho4MW6r6ynSKJWiPxq-IPlP_0Q1ghfcwjN56Sp_HA0nV-fedAfzkZoAXsj5O5ata32PCXPHJQ-dizWZ1OdpdEPS5wSPNW9jjc7TSPKQiNnCGPjLtnXQDLCbwEj3U\&width=768\&dpr=4\&quality=100\&sign=b032f2da\&sv=2)

## Sposta Righe Extra nel Cestino

**Usa questa opzione per eliminare voci su più righe non desiderate, come descrizioni troppo lunghe.**

In questo esempio, la descrizione si estende su più righe, ma solo la prima riga è rilevante:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FAEFanKF7uUtS_78nxi5zESPW8WOESa0Do_sCQCsttC21KoFK-sB9TQgFHboJB7CMEpc_auEbeXINU4BpEh8XuNMBHDYhuwjVX40cRyygxECs3XogrurWKNdw4s4F1kxWXLGrrF4jSqd1bba0dKPVO2E\&width=768\&dpr=4\&quality=100\&sign=926d60ed\&sv=2)

Abilita **Sposta righe extra nel Cestino** per rimuovere il testo superfluo:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FQdYUZ0ANpuFRkvNxVZzYfEhTRVf2fk1jPmoNUZcNotdkgL6VDHV1BgBXU2xqFfjBJ7W6uvB8TRZcpKEk7Qk_c0mIohiS4Jl9ZPRpG7HdS_EktuCcAtJ4KjJ_vYvYok7lv0nz2MfVMG08oDFqRSyFHy4\&width=768\&dpr=4\&quality=100\&sign=135061e3\&sv=2)

**Risultato dopo la mappatura:**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fzto-P_Knp1YQmCUBU6_vCg2IEwaBiBeAao8Jvu30-89x_Sj2BLDSTQu31vUNBlaQp73DPVy2F-UZawn8j4hxycD6bpfCf_KXZYvrqH5w0cwGwsjatBelIh6gdenY-NpzmQ372jtthucHpMrsXNz3DcA\&width=768\&dpr=4\&quality=100\&sign=741cbfd1\&sv=2)

## Numero Minimo di Righe Raggruppate

**Usa questa opzione quando le righe devono essere raggruppate sotto una riga principale (es. articoli con più sottorighe).**

Qui, solo tre righe su sei sono rilevanti. Due colonne chiave sono mappate (es. Posizione, Descrizione), mentre altre sono considerate campi personalizzati.

Inizia impostando il **Conteggio righe intestazione** e il **Numero minimo di righe raggruppate**:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fp0k-n1IG3_FHexG4iAlISSmN4Yaq9xUjRO2cLpV3w6a67DpULRnxj4x291DOXBVx2SHqKp6Zs-ZXxr8KHKzT9O6oCwgEOkvfMqwpDGZUrfFpozdR16sbaybtrMEqDOXO1TsNmuPFz6mOKX0pR8I5RO8\&width=768\&dpr=4\&quality=100\&sign=e19a8ef6\&sv=2)

Abilita anche **Sposta righe extra nel Cestino** per pulire i dati non rilevanti:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FP9Mbga3kWRkhRFYPRQKN6IXCYTnMHpfXr7GIBqbuwz-RYyq7fMuKRxJgzU0HVdxFxkI_5S2DA8ThYNveXlgrDYZ7JP_jOYf9wd9ldDzg1abzMD7HE0N8NC-wrWdoZvm5M2q_XVWTi6epBMBtHvbFe0\&width=768\&dpr=4\&quality=100\&sign=128029db\&sv=2)

Successivamente, definisci la colonna chiave di raggruppamento, ad es. _Posizione_:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F5hy2YTNQRZ6plQZnc1HwAbAUXU7LKfNpLdlfr8sPnDXMryv0KoAGgkcqAWqjvznvBa1YwW0ecTrpStpm5AIc0qiFX1zB-I_y_crIx0jKS2t6QVKdAz66Wb3XMt9sRsEUHKIuk51_AatHNCRZjOghn4A\&width=768\&dpr=4\&quality=100\&sign=6ca2a12e\&sv=2)

**Risultato:**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FxaorEjiOEeypLMAAOXvm3VAc5BVzhIujUeLdSt0SPwrEz5x_hd8sb3Hhc7OpnUpzj6qvjWWptOsefhxjF5pIzf12RVXah1wPhlMoa3Wwx7T3s_D7Pzw8cryaAzgh8SpN-uTxpl1FWke8v33dh2VNgJ0\&width=768\&dpr=4\&quality=100\&sign=e955b28f\&sv=2)

## Raggruppamento Inverso

**Usa questa opzione quando la riga di raggruppamento appare** _**dopo**_ **le righe che dovrebbe raggruppare.**

Se la riga che dovrebbe essere raggruppata con altri dati appare _sopra_ la chiave di raggruppamento, abilita questa opzione:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FiH7rDa637FWtr8wWtXpdqSh68xsaOFrb_vIWf-ZOpAjExmFPHVRaDGGipdwNy30gpLmEWT0UujjqlbcSlHU7ldQ5zhAy15pMxuqbDpS2xFSuL35EjbaXfFQTOSSO3QE_I37kvdL3i5k-N7F_9tedMss\&width=768\&dpr=4\&quality=100\&sign=95d583b1\&sv=2)

Abilita il **Raggruppamento inverso**, raggruppa per una colonna principale (es. Importo Netto), e usa **Sposta righe extra nel Cestino** se necessario:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FFJNKYXmELlMFi-Zh_0Pjgc0pcKI2-_UbDhF7b4D5p7GA4f9r-FqjruzkJw3nfJH4NA0G_BC2xQpJEzl26GbOlPt9fPyOkGowtGWgRWt5GJ62Vj-Qd04rDP0kzDFiJnRlpWF13d9YQ1e-FurQI-gHJx4\&width=768\&dpr=4\&quality=100\&sign=4b2677ae\&sv=2)

**Risultato finale:**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fe8x8gIUV10Y_FmPeW_X-UZw6uJ8P7alQTDy_m5OGGLZ8Ev7Ip-C-6fqtTixiSU0ZnLMIc4VR_f0xJV6beDnl7bFBIh4U2dME8KHB3qokj__SrQGp-3BXeOsN63SabFNd5miRCtK-jlf49nzcbbe8UJw\&width=768\&dpr=4\&quality=100\&sign=f7571dde\&sv=2)

## Riassunto

Utilizza le _Impostazioni Avanzate_ per insegnare a DocBits come gestire con precisione strutture di tabelle più complesse o inconsistenti. Queste impostazioni migliorano la precisione dell'estrazione tenendo conto di:

* Intestazioni su più righe
* Descrizioni su più righe
* Articoli di linea raggruppati
* Ordine inverso dei dati raggruppati

Abilitare queste opzioni durante l'addestramento garantisce che DocBits ricordi il layout corretto per i documenti futuri dello stesso fornitore.
