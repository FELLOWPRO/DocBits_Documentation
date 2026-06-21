# Ustawienia zaawansowane

W niektórych dokumentach struktury tabel mogą być złożone — obejmować wiele wierszy, zawierać zgrupowane informacje lub zbędne dodatkowe wiersze. _Ustawienia zaawansowane_ w trybie trenowania pozwalają precyzyjnie dostroić ekstrakcję tabel w takich przypadkach, poprawiając dokładność i spójność.

Aby uzyskać dostęp do tych ustawień, włącz **Tryb trenowania** i kliknij ikonę koła zębatego **Ustawienia** na górnym pasku akcji:

![advanced-settings](https://lh7-us.googleusercontent.com/W1cBx4IOjycKv6IZM9AX8Wggj1eEBgzBVJWgsyWkutX9dRRJuEjQtSCsPaNZuRndd9ewMVvfqSXr45C-2cO-pxXkYFdl_9eEGVW6-UBqqZCsuhia6alJjD1ZuZawwSbjS9Yeywe1wDK5yAcIOUH5QAw)

### Liczba wierszy nagłówka

**Użyj tego ustawienia, aby określić, ile wierszy tworzy nagłówek tabeli.**

Niektóre tabele mają wielowierszowe nagłówki. Na przykład nagłówek tej tabeli obejmuje dwa wiersze:

![](https://lh7-us.googleusercontent.com/J_nYZKzUSJHcpJuNp1ykf6shnfetOuiIPhyhyTfSqh_cTsDT5obwOSIc21OsLkjF9tMBP7Q1GQ1ZQfBsEmQIrJpfX3QpdjHnLkzInsjpngeg2L7i_TAyl9MdVmgHsDpUvoURdxfqp8FOdJxuRAMCwhk)

Ustaw **Liczbę wierszy nagłówka** tak, aby pasowała:

![header row count](https://lh7-us.googleusercontent.com/G8-QpKxnRin9PGPmkbtJ35r1EugXsD4_Yd5QvTkdbb7sXqRVC3a9t0cIlNILJHLr--GsykgAlMJmMYbJaUoMqHEPvAT3PlPNf-syCmPz_GVMFEMsbhcHI2DQBbT4MJXjS2Sx7M3xl4zAzcw3aa-XNms)

#### Dlaczego jest to ważne?

Jeśli tego nie ustawisz, DocBits może potraktować drugi wiersz jako dane zamiast jako część nagłówka, co prowadzi do błędów ekstrakcji:

**Przed:**

![](https://lh7-us.googleusercontent.com/35BElgcq-zbs8wcGcguVSKHRpwQXqQG9dQmBaYa8BT4RNwJxd6g-jL5wlQgrnVLrMxtpncr8ayaasWVV3snGpBiDUWs4Zx7Tn2Dck-YFBpanlcN500yIWkVz9RJXQhoq6op0WbYcgklp_LsmE9LXt9k)

Po:

![](https://lh7-us.googleusercontent.com/bPGn9eWPK3Mmbu_ab2N3tVVP8ODho4MW6r6ynSKJWiPxq-IPlP_0Q1ghfcwjN56Sp_HA0nV-fedAfzkZoAXsj5O5ata32PCXPHJQ-dizWZ1OdpdEPS5wSPNW9jjc7TSPKQiNnCGPjLtnXQDLCbwEj3U)

### Przenieś dodatkowe wiersze do kosza

**Użyj tej opcji, aby odrzucić niechciane wielowierszowe wpisy, takie jak nadmiarowe opisy.**

W tym przykładzie opis rozlewa się na wiele wierszy, ale tylko pierwszy wiersz jest istotny:

![](https://lh7-us.googleusercontent.com/AEFanKF7uUtS_78nxi5zESPW8WOESa0Do_sCQCsttC21KoFK-sB9TQgFHboJB7CMEpc_auEbeXINU4BpEh8XuNMBHDYhuwjVX40cRyygxECs3XogrurWKNdw4s4F1kxWXLGrrF4jSqd1bba0dKPVO2E)

Włącz opcję **Przenieś dodatkowe wiersze do kosza**, aby usunąć nadmiar:

![](https://lh7-us.googleusercontent.com/QdYUZ0ANpuFRkvNxVZzYfEhTRVf2fk1jPmoNUZcNotdkgL6VDHV1BgBXU2xqFfjBJ7W6uvB8TRZcpKEk7Qk_c0mIohiS4Jl9ZPRpG7HdS_EktuCcAtJ4KjJ_vYvYok7lv0nz2MfVMG08oDFqRSyFHy4)

**Wynik po zmapowaniu:**

![](https://lh7-us.googleusercontent.com/zto-P_Knp1YQmCUBU6_vCg2IEwaBiBeAao8Jvu30-89x_Sj2BLDSTQu31vUNBlaQp73DPVy2F-UZawn8j4hxycD6bpfCf_KXZYvrqH5w0cwGwsjatBelIh6gdenY-NpzmQ372jtthucHpMrsXNz3DcA)



### Minimalna liczba zgrupowanych wierszy

**Użyj tej opcji, gdy wiersze muszą być grupowane razem pod jednym głównym wierszem (np. pozycje z wieloma podwierszami).**

W tym przypadku tylko trzy z sześciu wierszy są istotne. Dwie kluczowe kolumny są zmapowane (np. Pozycja, Opis), podczas gdy pozostałe są traktowane jako pola niestandardowe.

Zacznij od ustawienia **Liczby wierszy nagłówka** oraz **Minimalnej liczby zgrupowanych wierszy**:

![](https://lh7-us.googleusercontent.com/p0k-n1IG3_FHexG4iAlISSmN4Yaq9xUjRO2cLpV3w6a67DpULRnxj4x291DOXBVx2SHqKp6Zs-ZXxr8KHKzT9O6oCwgEOkvfMqwpDGZUrfFpozdR16sbaybtrMEqDOXO1TsNmuPFz6mOKX0pR8I5RO8)

Włącz również opcję **Przenieś dodatkowe wiersze do kosza**, aby usunąć nieistotne dane:

![](https://lh7-us.googleusercontent.com/P9Mbga3kWRkhRFYPRQKN6IXCYTnMHpfXr7GIBqbuwz-RYyq7fMuKRxJgzU0HVdxFxkI_5S2DA8ThYNveXlgrDYZ7JP_jOYf9wd9ldDzg1abzMD7HE0sN8NC-wrWdoZvm5M2q_XVWTi6epBMBtHvbFe0)

Następnie zdefiniuj kolumnę będącą kluczem grupowania, np. _Pozycja_:

![](https://lh7-us.googleusercontent.com/5hy2YTNQRZ6plQZnc1HwAbAUXU7LKfNpLdlfr8sPnDXMryv0KoAGgkcqAWqjvznvBa1YwW0ecTrpStpm5AIc0qiFX1zB-I_y_crIx0jKS2t6QVKdAz66Wb3XMt9sRsEUHKIuk51_AatHNCRZjOghn4A)

**Wynik:**

<figure><img src="https://lh7-us.googleusercontent.com/xaorEjiOEeypLMAAOXvm3VAc5BVzhIujUeLdSt0SPwrEz5x_hd8sb3Hhc7OpnUpzj6qvjWWptOsefhxjF5pIzf12RVXah1wPhlMoa3Wwx7T3s_D7Pzw8cryaAzgh8SpN-uTxpl1FWke8v33dh2VNgJ0" alt="" width="563"><figcaption></figcaption></figure>

### Grupowanie odwrócone

**Użyj tej opcji, gdy wiersz grupujący pojawia się&#x20;**_**po**_**&#x20;wierszach, które ma grupować.**

Jeśli wiersz, który powinien być zgrupowany z innymi danymi, pojawia się _nad_ kluczem grupowania, włącz tę opcję:

![](https://lh7-us.googleusercontent.com/iH7rDa637FWtr8wWtXpdqSh68xsaOFrb_vIWf-ZOpAjExmFPHVRaDGGipdwNy30gpLmEWT0UujjqlbcSlHU7ldQ5zhAy15pMxuqbDpS2xFSuL35EjbaXfFQTOSSO3QE_I37kvdL3i5k-N7F_9tedMss)

Włącz **Grupowanie odwrócone**, grupuj według głównej kolumny (np. Kwota netto) i w razie potrzeby użyj opcji **Przenieś dodatkowe wiersze do kosza**:

![](https://lh7-us.googleusercontent.com/FJNKYXmELlMFi-Zh_0Pjgc0pcKI2-_UbDhF7b4D5p7GA4f9r-FqjruzkJw3nfJH4NA0G_BC2xQpJEzl26GbOlPt9fPyOkGowtGWgRWt5GJ62Vj-Qd04rDP0kzDFiJnRlpWF13d9YQ1e-FurQI-gHJx4)

**Końcowy wynik:**\\


<figure><img src="https://lh7-us.googleusercontent.com/e8x8gIUV10Y_FmPeW_X-UZw6uJ8P7alQTDy_m5OGGLZ8Ev7Ip-C-6fqtTixiSU0ZnLMIc4VR_f0xJV6beDnl7bFBIh4U2dME8KHB3qokj__SrQGp-3BXeOsN63SabFNd5miRCtK-jlf49nzcbbe8UJw" alt=""><figcaption></figcaption></figure>

### Podsumowanie

Skorzystaj z _Ustawień zaawansowanych_, aby nauczyć DocBits dokładnego obsługiwania bardziej złożonych lub niespójnych struktur tabel. Ustawienia te poprawiają precyzję ekstrakcji, uwzględniając:

* Wielowierszowe nagłówki
* Wielowierszowe opisy
* Zgrupowane pozycje
* Odwróconą kolejność zgrupowanych danych

Włączenie tych opcji podczas trenowania sprawia, że DocBits zapamiętuje prawidłowy układ dla przyszłych dokumentów od tego samego dostawcy.
