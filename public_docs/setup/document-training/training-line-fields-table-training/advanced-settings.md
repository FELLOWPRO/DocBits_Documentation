# Advanced Settings

In the table extraction view, you will find the menu item Settings in the upper action bar (make sure that the training mode is activated). If you click on the gear icon, a window will open in which you will find the Advanced Settings.

![advanced-settings](https://lh7-us.googleusercontent.com/W1cBx4IOjycKv6IZM9AX8Wggj1eEBgzBVJWgsyWkutX9dRRJuEjQtSCsPaNZuRndd9ewMVvfqSXr45C-2cO-pxXkYFdl\_9eEGVW6-UBqqZCsuhia6alJjD1ZuZawwSbjS9Yeywe1wDK5yAcIOUH5QAw)

![](https://lh7-us.googleusercontent.com/MOAM0PpIjknkZQUFZzOXPT8kWan5x05WXe6zUjmzKLjUaKSPPknR6HEVZ5oRBVEMpha3bL87k1\_B2cgt4Iv0jH3MyU6BrcmD6gz3KoGMZHVTGGburr9uHU7\_VziztQ2i5RiZr\_wAqTqVG1JunX314sk)

Below functionalities are available in general settings:

## Header row count

Here you can define the number of lines of a table header. For example, the table header line can be two lines:

![](https://lh7-us.googleusercontent.com/J\_nYZKzUSJHcpJuNp1ykf6shnfetOuiIPhyhyTfSqh\_cTsDT5obwOSIc21OsLkjF9tMBP7Q1GQ1ZQfBsEmQIrJpfX3QpdjHnLkzInsjpngeg2L7i\_TAyl9MdVmgHsDpUvoURdxfqp8FOdJxuRAMCwhk)

Accordingly, the value in “Header row count” is set to two

![header row count](https://lh7-us.googleusercontent.com/G8-QpKxnRin9PGPmkbtJ35r1EugXsD4\_Yd5QvTkdbb7sXqRVC3a9t0cIlNILJHLr--GsykgAlMJmMYbJaUoMqHEPvAT3PlPNf-syCmPz\_GVMFEMsbhcHI2DQBbT4MJXjS2Sx7M3xl4zAzcw3aa-XNms)

Why is this needed? It might be that DocBits does not recognize the second line in the table header as part of the header line. In this case, it incorrectly inserts it into the table as an extracted value. This can be easily prevented with this function.

Example before

![](https://lh7-us.googleusercontent.com/35BElgcq-zbs8wcGcguVSKHRpwQXqQG9dQmBaYa8BT4RNwJxd6g-jL5wlQgrnVLrMxtpncr8ayaasWVV3snGpBiDUWs4Zx7Tn2Dck-YFBpanlcN500yIWkVz9RJXQhoq6op0WbYcgklp\_LsmE9LXt9k)

Example after

![](https://lh7-us.googleusercontent.com/bPGn9eWPK3Mmbu\_ab2N3tVVP8ODho4MW6r6ynSKJWiPxq-IPlP\_0Q1ghfcwjN56Sp\_HA0nV-fedAfzkZoAXsj5O5ata32PCXPHJQ-dizWZ1OdpdEPS5wSPNW9jjc7TSPKQiNnCGPjLtnXQDLCbwEj3U)

## Move Extra Rows to Trash

In this example, the item description in the table spans several rows, but you only need the first one. To extract only this and include it in the Description column, select Move Extra Rows to Trash.

![](https://lh7-us.googleusercontent.com/AEFanKF7uUtS\_78nxi5zESPW8WOESa0Do\_sCQCsttC21KoFK-sB9TQgFHboJB7CMEpc\_auEbeXINU4BpEh8XuNMBHDYhuwjVX40cRyygxECs3XogrurWKNdw4s4F1kxWXLGrrF4jSqd1bba0dKPVO2E)

![](https://lh7-us.googleusercontent.com/QdYUZ0ANpuFRkvNxVZzYfEhTRVf2fk1jPmoNUZcNotdkgL6VDHV1BgBXU2xqFfjBJ7W6uvB8TRZcpKEk7Qk\_c0mIohiS4Jl9ZPRpG7HdS\_EktuCcAtJ4KjJ\_vYvYok7lv0nz2MfVMG08oDFqRSyFHy4)

After naming the columns and mapping them to position, you get the following result

![](https://lh7-us.googleusercontent.com/zto-P\_Knp1YQmCUBU6\_vCg2IEwaBiBeAao8Jvu30-89x\_Sj2BLDSTQu31vUNBlaQp73DPVy2F-UZawn8j4hxycD6bpfCf\_KXZYvrqH5w0cwGwsjatBelIh6gdenY-NpzmQ372jtthucHpMrsXNz3DcA)

The functionalities below are available in the advanced settings:

![](https://lh7-us.googleusercontent.com/JnMLehG6RHTYtaP5dQx3UMrTzIpDRmyWj3\_1o-ITkYfNboSmFQxPmHuQQ2CZ0UwW6scXLEv8wxdZIh1J1VkzoAbKalI5D\_WO-G0GssfuVjmm\_mi29j7h42HQiDN08yJiEuMKEjFOIpi6nO5GcYIpDKU)

## Minimum grouped rows

Enter the minimum number of rows in your grouped column here.

![](https://lh7-us.googleusercontent.com/11D-KFXDqc-u5GQeGvTHfxYbbhLYDX12vFHK9Xkv8YmIcBuWVbFw3CMEhzep\_zyQpr2G9bP1Q0G9mfBj6twopQ-2aRfncbBVbTibXoynkxWYsvD9EnGVO-SfRxHwuPxMqXl4lzjuDoSaYop1HLa7biU)

In this table you see six rows of which only three are relevant for you. In the first two columns there are two criteria that have to be extracted separately. These will be your mapped columns all the other ones have to be trained as custom columns.\
And this is how it works step by step:

Select the two header rows as well as two minimum grouped rows as these should be grouped to one row.

![](https://lh7-us.googleusercontent.com/p0k-n1IG3\_FHexG4iAlISSmN4Yaq9xUjRO2cLpV3w6a67DpULRnxj4x291DOXBVx2SHqKp6Zs-ZXxr8KHKzT9O6oCwgEOkvfMqwpDGZUrfFpozdR16sbaybtrMEqDOXO1TsNmuPFz6mOKX0pR8I5RO8)

![](https://lh7-us.googleusercontent.com/7tlMcXBDrGjolEnBZNJT7bo4AoqPXYdltMzwjuycwCVSEaXIimXUw0aKyXpHdfpVw9POwNFtb47OwlreB400BgyiXLl3e1LGRLTPklU\_ETRN1quuRu9j9-NC9Eyq-fR\_5BpWdru1pgj\_kTfn9aLOiRM)

Also select the Move extra rows to Trash option to be able to train all the other columns as custom columns.

![](https://lh7-us.googleusercontent.com/P9Mbga3kWRkhRFYPRQKN6IXCYTnMHpfXr7GIBqbuwz-RYyq7fMuKRxJgzU0HVdxFxkI\_5S2DA8ThYNveXlgrDYZ7JP\_jOYf9wd9ldDzg1abzMD7HE0sN8NC-wrWdoZvm5M2q\_XVWTi6epBMBtHvbFe0)

Name the first column Position and group on that one.

![](https://lh7-us.googleusercontent.com/5hy2YTNQRZ6plQZnc1HwAbAUXU7LKfNpLdlfr8sPnDXMryv0KoAGgkcqAWqjvznvBa1YwW0ecTrpStpm5AIc0qiFX1zB-I\_y\_crIx0jKS2t6QVKdAz66Wb3XMt9sRsEUHKIuk51\_AatHNCRZjOghn4A)

After naming all the columns and training the values, this is your result:

![](https://lh7-us.googleusercontent.com/xaorEjiOEeypLMAAOXvm3VAc5BVzhIujUeLdSt0SPwrEz5x\_hd8sb3Hhc7OpnUpzj6qvjWWptOsefhxjF5pIzf12RVXah1wPhlMoa3Wwx7T3s\_D7Pzw8cryaAzgh8SpN-uTxpl1FWke8v33dh2VNgJ0)

## Reverse grouping

If you want to combine all the rows above the grouped attribute, check the box here.

In this example, the table starts with a row that is above all other information but also needs to be extracted along with the information below it. It could be that DocBits (DOC²) extracts this row as an additional row and the grouping of the information, e.g. by position, does not work properly.

![](https://lh7-us.googleusercontent.com/iH7rDa637FWtr8wWtXpdqSh68xsaOFrb\_vIWf-ZOpAjExmFPHVRaDGGipdwNy30gpLmEWT0UujjqlbcSlHU7ldQ5zhAy15pMxuqbDpS2xFSuL35EjbaXfFQTOSSO3QE\_I37kvdL3i5k-N7F\_9tedMss)

![](https://lh7-us.googleusercontent.com/xGHtg5jLUIzvQHuJ3bRovFzkicMO2NL5jESXeTtZueRX-BkP3AvYSsnywrc\_80aMwqchwo8WggqI\_6sNFk6aLE7TAeEJwNikKI6QC2k51e9iK9bxyT9nh9eRgeK\_YgWUeqUgp6p8UadEAnQRhKYFpOQ)

After grouping on net amount, checking the box, selecting the Move extra rows to Trash option

![](https://lh7-us.googleusercontent.com/FJNKYXmELlMFi-Zh\_0Pjgc0pcKI2-\_UbDhF7b4D5p7GA4f9r-FqjruzkJw3nfJH4NA0G\_BC2xQpJEzl26GbOlPt9fPyOkGowtGWgRWt5GJ62Vj-Qd04rDP0kzDFiJnRlpWF13d9YQ1e-FurQI-gHJx4)

After naming all the columns, this is your result.

![](https://lh7-us.googleusercontent.com/e8x8gIUV10Y\_FmPeW\_X-UZw6uJ8P7alQTDy\_m5OGGLZ8Ev7Ip-C-6fqtTixiSU0ZnLMIc4VR\_f0xJV6beDnl7bFBIh4U2dME8KHB3qokj\_\_SrQGp-3BXeOsN63SabFNd5miRCtK-jlf49nzcbbe8UJw)

