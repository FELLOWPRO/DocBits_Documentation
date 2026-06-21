_Treść w języku angielskim poniżej - Tłumaczenie oczekujące_

# Advanced Settings

In some documents, table structures can be complex—spanning multiple lines, containing grouped information, or including unnecessary extra rows. The _Advanced Settings_ in training mode allow you to fine-tune table extraction for such cases, improving accuracy and consistency.

To access these settings, activate **Training Mode** and click the **Settings** gear icon in the top action bar:

![advanced-settings](https://lh7-us.googleusercontent.com/W1cBx4IOjycKv6IZM9AX8Wggj1eEBgzBVJWgsyWkutX9dRRJuEjQtSCsPaNZuRndd9ewMVvfqSXr45C-2cO-pxXkYFdl_9eEGVW6-UBqqZCsuhia6alJjD1ZuZawwSbjS9Yeywe1wDK5yAcIOUH5QAw)

### Header Row Count

**Use this setting to define how many lines make up the table header.**

Some tables have multi-line headers. For example, this table’s header spans two lines:

![](https://lh7-us.googleusercontent.com/J_nYZKzUSJHcpJuNp1ykf6shnfetOuiIPhyhyTfSqh_cTsDT5obwOSIc21OsLkjF9tMBP7Q1GQ1ZQfBsEmQIrJpfX3QpdjHnLkzInsjpngeg2L7i_TAyl9MdVmgHsDpUvoURdxfqp8FOdJxuRAMCwhk)

Set the **Header row count** to match:

![header row count](https://lh7-us.googleusercontent.com/G8-QpKxnRin9PGPmkbtJ35r1EugXsD4_Yd5QvTkdbb7sXqRVC3a9t0cIlNILJHLr--GsykgAlMJmMYbJaUoMqHEPvAT3PlPNf-syCmPz_GVMFEMsbhcHI2DQBbT4MJXjS2Sx7M3xl4zAzcw3aa-XNms)

#### Why is this important?

If you don’t set this, DocBits may treat the second line as data instead of part of the header, leading to extraction errors:

**Before:**

![](https://lh7-us.googleusercontent.com/35BElgcq-zbs8wcGcguVSKHRpwQXqQG9dQmBaYa8BT4RNwJxd6g-jL5wlQgrnVLrMxtpncr8ayaasWVV3snGpBiDUWs4Zx7Tn2Dck-YFBpanlcN500yIWkVz9RJXQhoq6op0WbYcgklp_LsmE9LXt9k)

After:

![](https://lh7-us.googleusercontent.com/bPGn9eWPK3Mmbu_ab2N3tVVP8ODho4MW6r6ynSKJWiPxq-IPlP_0Q1ghfcwjN56Sp_HA0nV-fedAfzkZoAXsj5O5ata32PCXPHJQ-dizWZ1OdpdEPS5wSPNW9jjc7TSPKQiNnCGPjLtnXQDLCbwEj3U)

### Move Extra Rows to Trash

**Use this to discard unwanted multi-line entries, such as overflow descriptions.**

In this example, the description spills into multiple rows, but only the first line is relevant:

![](https://lh7-us.googleusercontent.com/AEFanKF7uUtS_78nxi5zESPW8WOESa0Do_sCQCsttC21KoFK-sB9TQgFHboJB7CMEpc_auEbeXINU4BpEh8XuNMBHDYhuwjVX40cRyygxECs3XogrurWKNdw4s4F1kxWXLGrrF4jSqd1bba0dKPVO2E)

Enable **Move Extra Rows to Trash** to remove the overflow:

![](https://lh7-us.googleusercontent.com/QdYUZ0ANpuFRkvNxVZzYfEhTRVf2fk1jPmoNUZcNotdkgL6VDHV1BgBXU2xqFfjBJ7W6uvB8TRZcpKEk7Qk_c0mIohiS4Jl9ZPRpG7HdS_EktuCcAtJ4KjJ_vYvYok7lv0nz2MfVMG08oDFqRSyFHy4)

**Result after mapping:**

![](https://lh7-us.googleusercontent.com/zto-P_Knp1YQmCUBU6_vCg2IEwaBiBeAao8Jvu30-89x_Sj2BLDSTQu31vUNBlaQp73DPVy2F-UZawn8j4hxycD6bpfCf_KXZYvrqH5w0cwGwsjatBelIh6gdenY-NpzmQ372jtthucHpMrsXNz3DcA)



### Minimum Grouped Rows

**Use this when rows need to be grouped together under one main row (e.g. line items with multiple sub-lines).**

Here, only three out of six rows are relevant. Two key columns are mapped (e.g. Position, Description), while others are treated as custom fields.

Start by setting **Header row count** and the **Minimum grouped rows**:

![](https://lh7-us.googleusercontent.com/p0k-n1IG3_FHexG4iAlISSmN4Yaq9xUjRO2cLpV3w6a67DpULRnxj4x291DOXBVx2SHqKp6Zs-ZXxr8KHKzT9O6oCwgEOkvfMqwpDGZUrfFpozdR16sbaybtrMEqDOXO1TsNmuPFz6mOKX0pR8I5RO8)

Also enable **Move Extra Rows to Trash** to clean up irrelevant data:

![](https://lh7-us.googleusercontent.com/P9Mbga3kWRkhRFYPRQKN6IXCYTnMHpfXr7GIBqbuwz-RYyq7fMuKRxJgzU0HVdxFxkI_5S2DA8ThYNveXlgrDYZ7JP_jOYf9wd9ldDzg1abzMD7HE0sN8NC-wrWdoZvm5M2q_XVWTi6epBMBtHvbFe0)

Then define the grouping key column, e.g. _Position_:

![](https://lh7-us.googleusercontent.com/5hy2YTNQRZ6plQZnc1HwAbAUXU7LKfNpLdlfr8sPnDXMryv0KoAGgkcqAWqjvznvBa1YwW0ecTrpStpm5AIc0qiFX1zB-I_y_crIx0jKS2t6QVKdAz66Wb3XMt9sRsEUHKIuk51_AatHNCRZjOghn4A)

**Result:**

<figure><img src="https://lh7-us.googleusercontent.com/xaorEjiOEeypLMAAOXvm3VAc5BVzhIujUeLdSt0SPwrEz5x_hd8sb3Hhc7OpnUpzj6qvjWWptOsefhxjF5pIzf12RVXah1wPhlMoa3Wwx7T3s_D7Pzw8cryaAzgh8SpN-uTxpl1FWke8v33dh2VNgJ0" alt="" width="563"><figcaption></figcaption></figure>

### Reverse Grouping

**Use this when the grouping row appears&#x20;**_**after**_**&#x20;the rows it should group.**

If the row that should be grouped with other data appears _above_ the grouping key, enable this option:

![](https://lh7-us.googleusercontent.com/iH7rDa637FWtr8wWtXpdqSh68xsaOFrb_vIWf-ZOpAjExmFPHVRaDGGipdwNy30gpLmEWT0UujjqlbcSlHU7ldQ5zhAy15pMxuqbDpS2xFSuL35EjbaXfFQTOSSO3QE_I37kvdL3i5k-N7F_9tedMss)

Enable **Reverse grouping**, group by a main column (e.g. Net amount), and use **Move Extra Rows to Trash** if needed:

![](https://lh7-us.googleusercontent.com/FJNKYXmELlMFi-Zh_0Pjgc0pcKI2-_UbDhF7b4D5p7GA4f9r-FqjruzkJw3nfJH4NA0G_BC2xQpJEzl26GbOlPt9fPyOkGowtGWgRWt5GJ62Vj-Qd04rDP0kzDFiJnRlpWF13d9YQ1e-FurQI-gHJx4)

**Final result:**\


<figure><img src="https://lh7-us.googleusercontent.com/e8x8gIUV10Y_FmPeW_X-UZw6uJ8P7alQTDy_m5OGGLZ8Ev7Ip-C-6fqtTixiSU0ZnLMIc4VR_f0xJV6beDnl7bFBIh4U2dME8KHB3qokj__SrQGp-3BXeOsN63SabFNd5miRCtK-jlf49nzcbbe8UJw" alt=""><figcaption></figcaption></figure>

### Summary

Use the _Advanced Settings_ to teach DocBits how to accurately handle more complex or inconsistent table structures. These settings improve extraction precision by accounting for:

* Multi-line headers
* Multi-row descriptions
* Grouped line items
* Reverse order of grouped data

Enabling these options during training ensures DocBits remembers the correct layout for future documents from the same supplier.
