# Configurações Avançadas

Em alguns documentos, as estruturas de tabela podem ser complexas - abrangendo várias linhas, contendo informações agrupadas ou incluindo linhas extras desnecessárias. As _Configurações Avançadas_ no modo de treinamento permitem ajustar a extração de tabelas para esses casos, melhorando a precisão e consistência.

Para acessar essas configurações, ative o **Modo de Treinamento** e clique no ícone de engrenagem **Configurações** na barra de ação superior:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FW1cBx4IOjycKv6IZM9AX8Wggj1eEBgzBVJWgsyWkutX9dRRJuEjQtSCsPaNZuRndd9ewMVvfqSXr45C-2cO-pxXkYFdl_9eEGVW6-UBqqZCsuhia6alJjD1ZuZawwSbjS9Yeywe1wDK5yAcIOUH5QAw\&width=768\&dpr=4\&quality=100\&sign=4bf6ac31\&sv=2)

## Contagem de Linhas de Cabeçalho

**Use essa configuração para definir quantas linhas compõem o cabeçalho da tabela.**

Algumas tabelas têm cabeçalhos com várias linhas. Por exemplo, o cabeçalho desta tabela abrange duas linhas:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FJ_nYZKzUSJHcpJuNp1ykf6shnfetOuiIPhyhyTfSqh_cTsDT5obwOSIc21OsLkjF9tMBP7Q1GQ1ZQfBsEmQIrJpfX3QpdjHnLkzInsjpngeg2L7i_TAyl9MdVmgHsDpUvoURdxfqp8FOdJxuRAMCwhk\&width=768\&dpr=4\&quality=100\&sign=554fa70\&sv=2)

Defina a **Contagem de linhas de cabeçalho** para corresponder:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FG8-QpKxnRin9PGPmkbtJ35r1EugXsD4_Yd5QvTkdbb7sXqRVC3a9t0cIlNILJHLr--GsykgAlMJmMYbJaUoMqHEPvAT3PlPNf-syCmPz_GVMFEMsbhcHI2DQBbT4MJXjS2Sx7M3xl4zAzcw3aa-XNms\&width=768\&dpr=4\&quality=100\&sign=a487f5a9\&sv=2)

### Por que isso é importante?

Se você não definir isso, o DocBits pode tratar a segunda linha como dados em vez de parte do cabeçalho, levando a erros de extração:

**Antes:**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F35BElgcq-zbs8wcGcguVSKHRpwQXqQG9dQmBaYa8BT4RNwJxd6g-jL5wlQgrnVLrMxtpncr8ayaasWVV3snGpBiDUWs4Zx7Tn2Dck-YFBpanlcN500yIWkVz9RJXQhoq6op0WbYcgklp_LsmE9LXt9k\&width=768\&dpr=4\&quality=100\&sign=7c68faf7\&sv=2)

Depois:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FbPGn9eWPK3Mmbu_ab2N3tVVP8ODho4MW6r6ynSKJWiPxq-IPlP_0Q1ghfcwjN56Sp_HA0nV-fedAfzkZoAXsj5O5ata32PCXPHJQ-dizWZ1OdpdEPS5wSPNW9jjc7TSPKQiNnCGPjLtnXQDLCbwEj3U\&width=768\&dpr=4\&quality=100\&sign=b032f2da\&sv=2)

## Mover Linhas Extras para o Lixo

**Use isso para descartar entradas de várias linhas indesejadas, como descrições que transbordam.**

Neste exemplo, a descrição se estende por várias linhas, mas apenas a primeira linha é relevante:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FAEFanKF7uUtS_78nxi5zESPW8WOESa0Do_sCQCsttC21KoFK-sB9TQgFHboJB7CMEpc_auEbeXINU4BpEh8XuNMBHDYhuwjVX40cRyygxECs3XogrurWKNdw4s4F1kxWXLGrrF4jSqd1bba0dKPVO2E\&width=768\&dpr=4\&quality=100\&sign=926d60ed\&sv=2)

Habilite **Mover Linhas Extras para o Lixo** para remover o excesso:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FQdYUZ0ANpuFRkvNxVZzYfEhTRVf2fk1jPmoNUZcNotdkgL6VDHV1BgBXU2xqFfjBJ7W6uvB8TRZcpKEk7Qk_c0mIohiS4Jl9ZPRpG7HdS_EktuCcAtJ4KjJ_vYvYok7lv0nz2MfVMG08oDFqRSyFHy4\&width=768\&dpr=4\&quality=100\&sign=135061e3\&sv=2)

**Resultado após mapeamento:**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fzto-P_Knp1YQmCUBU6_vCg2IEwaBiBeAao8Jvu30-89x_Sj2BLDSTQu31vUNBlaQp73DPVy2F-UZawn8j4hxycD6bpfCf_KXZYvrqH5w0cwGwsjatBelIh6gdenY-NpzmQ372jtthucHpMrsXNz3DcA\&width=768\&dpr=4\&quality=100\&sign=741cbfd1\&sv=2)

## Mínimo de Linhas Agrupadas

**Use isso quando as linhas precisam ser agrupadas sob uma linha principal (por exemplo, itens de linha com várias sublinhas).**

Aqui, apenas três de seis linhas são relevantes. Duas colunas principais são mapeadas (por exemplo, Posição, Descrição), enquanto outras são tratadas como campos personalizados.

Comece definindo a **Contagem de linhas de cabeçalho** e o **Mínimo de linhas agrupadas**:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fp0k-n1IG3_FHexG4iAlISSmN4Yaq9xUjRO2cLpV3w6a67DpULRnxj4x291DOXBVx2SHqKp6Zs-ZXxr8KHKzT9O6oCwgEOkvfMqwpDGZUrfFpozdR16sbaybtrMEqDOXO1TsNmuPFz6mOKX0pR8I5RO8\&width=768\&dpr=4\&quality=100\&sign=e19a8ef6\&sv=2)

Também habilite **Mover Linhas Extras para o Lixo** para limpar dados irrelevantes:

<figure><img src="../../../../.gitbook/assets/image.png" alt="" width="522"><figcaption></figcaption></figure>

Em seguida, defina a coluna-chave de agrupamento, por exemplo, _Posição_:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F5hy2YTNQRZ6plQZnc1HwAbAUXU7LKfNpLdlfr8sPnDXMryv0KoAGgkcqAWqjvznvBa1YwW0ecTrpStpm5AIc0qiFX1zB-I_y_crIx0jKS2t6QVKdAz66Wb3XMt9sRsEUHKIuk51_AatHNCRZjOghn4A\&width=768\&dpr=4\&quality=100\&sign=6ca2a12e\&sv=2)

**Resultado:**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FxaorEjiOEeypLMAAOXvm3VAc5BVzhIujUeLdSt0SPwrEz5x_hd8sb3Hhc7OpnUpzj6qvjWWptOsefhxjF5pIzf12RVXah1wPhlMoa3Wwx7T3s_D7Pzw8cryaAzgh8SpN-uTxpl1FWke8v33dh2VNgJ0\&width=768\&dpr=4\&quality=100\&sign=e955b28f\&sv=2)

## Agrupamento Reverso

**Use isso quando a linha de agrupamento aparece** _**após**_ **as linhas que devem ser agrupadas.**

Se a linha que deve ser agrupada com outros dados aparecer _acima_ da chave de agrupamento, habilite esta opção:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FiH7rDa637FWtr8wWtXpdqSh68xsaOFrb_vIWf-ZOpAjExmFPHVRaDGGipdwNy30gpLmEWT0UujjqlbcSlHU7ldQ5zhAy15pMxuqbDpS2xFSuL35EjbaXfFQTOSSO3QE_I37kvdL3i5k-N7F_9tedMss\&width=768\&dpr=4\&quality=100\&sign=95d583b1\&sv=2)

Habilite **Agrupamento Reverso**, agrupe por uma coluna principal (por exemplo, Valor líquido) e use **Mover Linhas Extras para o Lixo** se necessário:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FFJNKYXmELlMFi-Zh_0Pjgc0pcKI2-_UbDhF7b4D5p7GA4f9r-FqjruzkJw3nfJH4NA0G_BC2xQpJEzl26GbOlPt9fPyOkGowtGWgRWt5GJ62Vj-Qd04rDP0kzDFiJnRlpWF13d9YQ1e-FurQI-gHJx4\&width=768\&dpr=4\&quality=100\&sign=4b2677ae\&sv=2)

**Resultado final:**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fe8x8gIUV10Y_FmPeW_X-UZw6uJ8P7alQTDy_m5OGGLZ8Ev7Ip-C-6fqtTixiSU0ZnLMIc4VR_f0xJV6beDnl7bFBIh4U2dME8KHB3qokj__SrQGp-3BXeOsN63SabFNd5miRCtK-jlf49nzcbbe8UJw\&width=768\&dpr=4\&quality=100\&sign=f7571dde\&sv=2)

## Resumo

Use as _Configurações Avançadas_ para ensinar ao DocBits como lidar com precisão estruturas de tabela mais complexas ou inconsistentes. Essas configurações melhoram a precisão da extração ao considerar:

* Cabeçalhos de várias linhas
* Descrições de várias linhas
* Itens de linha agrupados
* Ordem reversa de dados agrupados

Habilitar essas opções durante o treinamento garante que o DocBits lembre o layout correto para futuros documentos do mesmo fornecedor.
