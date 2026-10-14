# Auto Accounting

## **Prerequisites**

* Functioning LN to DocBits dataflow
* Correctly configured DocBits environment

## **Infor Configuration**

### **ION Desk**

In Infor, open the ION Desk application. In the left tab, go to Connect → Connection Points

![](https://lh7-us.googleusercontent.com/tOzuXMmjVxByy-GQHBnNbFgP15YKIR0GNGoqrcqz87S3\_qBeZCvk92FA4PtD6UjLtUGBBKfmMd-W087C6TnORp7qptWzpDIEp4R2BbivWjQAsmStpZ4RcMgCY7s2CIV0AHErRtQDO2ePlMbNJSoIrmg)

This is where you will create the two connection points needed to import your data from LN that is required for Auto Accounting.

Click on “+ADD” to create a new connection point, select the API option like below

![](https://lh7-us.googleusercontent.com/C8l4LJ2WHIoPU7E\_uFhNIo8XakbizRx874hyTdJH9oHIW-PGd5tOhsnc1uJ6TW6P9BUQqmjoMrHL5WwQJ8IUJqufsbPFIdamKR9cF0EnnPOZD-TlJEQQAmcHKzoKrumCDQAexYZOQ1CpN1p\_bAnLNzI)

You will need to configure two separate API connection points, namely:

* ChartOfAccounts
* FinalFlexDimensions

#### **ChartOfAccounts**

The connection tab for your ChartOfAccounts connection point should look similar to what is illustrated below. Give the connection point an appropriate name and description, as well as import the Service Account you created.

![](https://lh7-us.googleusercontent.com/gJ1VStvYQ8cu1HBua2iA1Axo1M\_lXTS0VGYuqqtSDx-mtu-4xQQBjasNsGyiNSgjuYYQ0yYQkJN79\_HJcFF0vTyY4wLZWYIJQHC2oCColX43Va-g-E-KeCRyRQiV6eRDm932eFu6ic7g8OttWULPNUE)

![](https://lh7-us.googleusercontent.com/6zmLNSm7pLiS8dA9VceJv5pxwGpTE8WWZ1nmOt-UJA9qvW0wytcRZXB21jW2xa1BABB1YNNS5uWlxVWgEp4bWU5Rw4li3\_qr9potqxxXTY99V0VQQrp3kz4YyFE4jmibHYAEusc1qRtb8E-x9ilbR8c)

You will need to add two BODs in this section for this connection point. These being Sync.ChartOfAccounts and Sync.CodeDefinition, to add these BODs do the following:

**Sync.ChartOfAccounts**

* Click on the PLUS (+) icon

![](https://lh7-us.googleusercontent.com/aWwQaVreFHJsv5jd8-ZrVt-FAMvt00aO9W3n1KZ2XmUyxtaCGkg6yS6adPOwXJrqRGdFGTDpG4QsXXJG9V6IJeCrWKsKh6SRjl7ZOacLy9-i5K3dA5mWs6Ps6a91K2TNvdUx98OPwEDWWadz3BwaPiQ)

* Select “Send to API”

![](https://lh7-us.googleusercontent.com/uT-PjpDfv7MGB7wwvkYu0M9muSRXtAqMSjk3LKz3xWdtduWHr\_HT1m4ZoETyhP782zOaWBbnEiWxTC9PphoiqogrUNsM5e8PuYutjcwJPqQKAqAlXQMWHOpYru0b7nabzmt\_WqgxEp2Naz2hXViNWzY)

* Search for the Sync.ChartOfAccounts BOD

![](https://lh7-us.googleusercontent.com/yQQ92Nn3koBsPG32cPv2Pv9sjdmScGE0WGJ062YSg9q9RDyHnIg-qbh1RA6i7yhfKBeBhgbYEi3uJmR\_z6AdnR9pL49M41hvDoqzvijuPhGm3ZltHExmRtfXdccFc7Ogb44\_Y4gA8VDBXwt5lJsYEW0)

![](https://lh7-us.googleusercontent.com/WcK\_a7Lb61R-5fKGGqzVyR3lAAyyg9jgYunJYC8VNHCsU3Qopvz\_d7EJwXo6RZsbcEos05hv\_sILd-b29Ky4QVz9lNtzvoicT6bBykPKe-WIPPS-OtZ7yXg8VK6MHa5ZzNdqXvR1CUZmnR4WCu3MpSs)

* Switch to the ION API tab, copy the API name and search for the API Call by pressing the SELECT button

![](https://lh7-us.googleusercontent.com/364Jd0-EBMpWgpgPZukqcjdRlEoGfkgKkB\_U-Y2d87DlB13\_E-ovjnBaeRdPCi4rAMm6Ksc\_MRHAm75y1BPY21HQ12Fjdr6Q0j1YDTBI0Fo5l3LiIHSwL3ITsKbQ-VIBc5aO6O\_DAeKl1z8AUr8xhfo)

* At product, select the API Endpoint that you created for the environment you are working with, which you created in ION API. Search for the following API call, select the API call and press OK.

![](https://lh7-us.googleusercontent.com/NWfGZk5ttI0tWMli1DRZ4SdzC9xHa0LhGR1QbgaeJN1726FYoiqMg1Cb5\_x0TvYu4MlTyJqS9n6c6EfW2veKhcUdvpY-bkK\_uyfRJt6vESmRsVuIx93ipwuffd3YJr3y2sYX5fjFxjRNWEWzH9ojlr8)

* Next, switch the Request Body tab

![](https://lh7-us.googleusercontent.com/BNwExG0mPZ\_enovlnQh\_SWATS4wDEcOCXuyX98EJza80OxKvrhcFUZ\_l4v88XVBBI-iIjg6eprynpO-zjjNeNsCpgulcUCG8OpGA1SzC-1h\_OyPHTfHlF\_ZsWkpUhT5hz39ruI-TNPo4lelSsvz4jrc)

* Here is where you will configure the field mapping for this BOD, your configuration should look like the following. The field mappings are available at https://docbits.com/doc/field-mappings/.

![](https://lh7-us.googleusercontent.com/0O76spiOI\_ZofZiDYRtzuphCzPycktfvxzeEa9MTG3fxeI3bQPjREIyh2sVEwzyGthFzlwdHo1OPifIVpcSMS9yv2WjfIfacCdUQwgvCQu-dXf6aZutRYmrMSCoTFv4mCYtndtLL0-N8NjrlR6oIy-A)

Once you have completed the above steps, you will have successfully configured the Sync.ChartOfAccounts BOD. Click on the PLUS icon to add the next  and final BOD.

**Sync.CodeDefinition (TotalFlexDimensions)**

The connection tab for your CodeDefinition connection point should look similar to what is illustrated below. Give the connection point an appropriate name and description, as well as import the Service Account you created.

* Select “Send to API”

![](https://lh7-us.googleusercontent.com/h-HCsruFxSb6FVNKRRfLcbeiLnRXrQYDRmVH5cK\_N-PgIVkkA8zY1gd4T0w8Nq9f\_x7AFnR3D\_veVdI6In7DoIRebiFbXfIleXROV2AoAG\_\_C00UnvFapAFvPuGTwYxQfuZpeKk1yXsJE9\_dQ-mX2M4)

* Search for the Sync.CodeDefinition BOD

![](https://lh7-us.googleusercontent.com/WrXZYGIgQMRuWXG8pWHbI-6TQj6VyC9\_Opon05kup2gfDva-JwFShHzusw5sz78cq643hBF5dEJx4ZOqFXjUQm\_oqAB00O3Z\_Xd5Bdf\_4h\_Criq5g-8OeVIz69N6vqNraz\_zCfxZQur-37VT5VzWka0)

![](https://lh7-us.googleusercontent.com/5Mn6YBvca3Ejc9EIemE3UIHZ4sLzDObOr5RF4TsOucRPkFiIX-4ot7FSMb7TsspFsH\_ysbSZ8zB3xgM1zXboK5jBqqTbVDMNbsUEQOrwfzSkHfuhB44m2j9V0LRMalHJNtujOmz4FJd8Ey69VvdJ6EM)

* Switch to the ION API tab, copy the API name and search for the API Call by pressing the SELECT button

![](https://lh7-us.googleusercontent.com/lQNNzs9RNxvf85YGk0pq3-8vuwqXgzkfl-W4a8qcuFdThRTf4r6aJEmo3IXGp0cykwy6cml3AIRWwR3N8GZRbpL8yUynqKPeoTlmJ5CiKeJSmxm7Ea1aU3L8KXecM\_yv2mhDobYA09zaSV8kKAVs70A)

![](https://lh7-us.googleusercontent.com/1bE6Zgval5nkr9xxBGLgL0tk2f5IKN-OYng-9BzrPqX4aGq06emYHtICMgaIlAtXjP9sjQ8KHeL3Pa8gBgGMLFwmiArb9Lh9iX-mZ3X59Oblo7HRfZvD29jrifb0\_pJA4FMtHThpZq\_Vi\_nTeXB1XUQ)

* Next, switch the Request Body tab

![](https://lh7-us.googleusercontent.com/0MVLj442YbPOa83BtT8VwV9WG-Jl3DajGm4MGKwzsdD6QZLwtFhwhghCUX7ShlsbDogDmflsa4C5CmoxNqrFqNh\_ngxQ-rwoNAnWif4tYbwzTdEmAVy7kGRMs8v2VTDaAWsXk5nbRHFoszXeuCp8DGk)

* Here is where you will configure the field mapping for this BOD, your configuration should look like the following. The field mappings are available at https://docbits.com/doc/field-mappings/.

![](https://lh7-us.googleusercontent.com/tmDr3sAIr\_S7tRPebboyt9TPSGEBU4eC0zS04BcsDy4B4yQ3xdv8k-DlBjHXPy0P4slyLKYaRxM9s93Qx6Wf\_fI82St3XcmzsZwxKgRnXWHkzDcKj5oVYdtnW9I3dX8kM1rgxAYuRBIrWKSUhx8JZYk)

Once you have completed the above steps, you will have successfully configured the Sync.CodeDefinition BOD for the TotalFlexDimensions master data table.

#### **FinalFlexDimensions**

The connection tab for your FinalFlexDimensions connection point should look similar to what is illustrated below. Give the connection point an appropriate name and description, as well as import the Service Account you created.

![](https://lh7-us.googleusercontent.com/iOmkBrlLIeok6YuiHW\_qZl3jCr6HYB3-2FMiEtME1UUQFPHjjL1cBsRaHHtdpVveyQL3YHcV0FabTQWtQgS-gkB0q6ztI0QELrI5xX4fN1KfcGyjtOcmWbsFeHZ7tOw4ZjZjSJ4LXpTWGpVWZyBGji0)

![](https://lh7-us.googleusercontent.com/WOZFs6pSjqD3NFGMlv4PTu6UyZ9cHcAywiOccMn4h2TKqgF-Rz5ROXhCsFd97wPmtGtv0fvA902vcf6UUULhXAkyD22Vn3kUZwaLbCcOqjKbjeoKvPjcYemhi8qy\_pbc8hTNGhRj7oJCBBm8GOOenac)

You will need to add one BOD in this section for this connection point. This being the Sync.CodeDefinition, to add this BOD do the following:

The connection tab for your CodeDefinition connection point should look similar to what is illustrated below. Give the connection point an appropriate name and description, as well as import the Service Account you created.

* Select “Send to API”

![](https://lh7-us.googleusercontent.com/TjKLqUUaxoJSg7dUvkjKWKz7OYLfTKdFJT3pjsI5KKBcwB\_lGNQJz1hYQvM6KW9xIjryZbBUvRXLg5bKr3zNSgOPmXt9fl0BN1489jxnxXqRnS4vt9n3iCott-JOtm\_qUmMq1T5xXFD-reH8GYEDzio)

* Search for the Sync.CodeDefinition BOD

![](https://lh7-us.googleusercontent.com/s22p9SJWCFQmri9p-Pw4d2UjsZyWOWjEbXUOBJZwenL9AM1b8FMYy79TD\_c5SkXCZpDTYvaJkUGji1I6FJQSvPftQp5nf77KeMAoiwCH\_5Ucbmeis8WxOFiqjbjbZhzIBA5jsaUcu68LISJHgNwnkns)

![](https://lh7-us.googleusercontent.com/RBqwvAah2I4ZhiYetNXmb7i2LkPrCuIW-yxX\_HSvITXDoidf4vnVKsGEklsUGaZRgCR857iNPrj1uNGv1wU5k2KxA0Eyxv0kh5RZmQy5dbMKUls79nNHIHva91T3uZKAw6kwzDacIs8OTH3Yi-mM4hs)

* Switch to the ION API tab, copy the API name and search for the API Call by pressing the SELECT button

![](https://lh7-us.googleusercontent.com/s1he9mTSuxGSCO-5j9a1k6\_hCHfXkXa9k7e18mN-9c8-a9GQNmw4fYyYTlUFHJzPQRKhmTtNATxQ8qA8tI2uCazUEL1vlwG0ykgyQkONgAEKczn8UUheIsV5lpg9JN8UI93n8iq5yyAuRc0rNne0v2E)

![](https://lh7-us.googleusercontent.com/Oxair9LPtt\_3BF62GPXEy5WMCuSvm6L6oe\_C7W\_HbO\_s2IzfP2iKmDuk-gHvYifutl8JQjFMA87q5XBK3cwfYKac8UonGm7nHkHVMz8MuWsgY68bgzbJAuoE1GSLur4O0HeGb\_YQ3EyMopFl\_290NNI)

* Next, switch the Request Body tab

![](https://lh7-us.googleusercontent.com/LRDKhs2rq92Zef63nYy9NNK6bapmlPKUX10NSrRGBhvhdXIgBRte4sGunmOBUzymgnWnAv1O\_qV0AKsULSXsGT1kvorG0Pl0vQFW0exV2sqyUXhgiBMthRYTQbB10c6oI4P6Z139A8VqZVeg6c2HkZ4)

* Here is where you will configure the field mapping for this BOD, your configuration should look like the following. The field mappings are available at https://docbits.com/doc/field-mappings/.

![](https://lh7-us.googleusercontent.com/bjoXs4ZSra4dgpf2rC8GwA-uB\_Qp6INkdCapR7M03EV7cuqKzeVPWRCq4EHTZVeKpL92sdesL0iuHTHD1Ed5WHpr7Z15XOJMkPBlWgfbapzD4ZjfSre29Ii2SLGOvjs9-85SougBpDGzzTseAcWNVUo)

Once you have completed the above steps, you will have successfully configured the Sync.CodeDefinition BOD for the FinalFlexDimensions master data table.

## **Data Flows**

You will need to configure two separate data flows for Auto Accounting:

* ChartOfAccounts
* FinalFlexDimensions

### **ChartOfAccounts**

An overview of this data flow looks as shown below (the amount of DocBits API connection points at the end depends on the amount of different environments you are configuring).

![](https://lh7-us.googleusercontent.com/xog1wW9zE0PeVF\_SzaVS5qWxR2UuHKVR9cD4n6hxD9IAm\_jqJJHKGMCvmsF4V4bcVhd\_zaepEBrbK6wTd6kd7eqDL2Apwe799ewGo8TwMVrtRPwJcImuRjvWJxmcBiMvTjla0KgoGXhMD6oCeZFvOcM)

#### **LN Company**

![](https://lh7-us.googleusercontent.com/jaFn8KOdu907VI7vx2fkgtJZYiKw37LJ9ySqKWlgm5MLOuUcElJdOCpThwwa2NdE2eJ4iLWdfM\_Nlrkiq0BpIvrZDvyYJng94oZyaOpCIAhF5ZCTwQ0asfceY-KnIjZYrlQ5QsApnvU-hdMp8waQNeA)

The configuration for this connection point depends on the LN company which contains the master data you wish to import into DocBits, yours should look similar to what is shown below.

![](https://lh7-us.googleusercontent.com/k28OYp8vkZZcWCKJTiSFZkDE0SlfLgE\_S3o37OhuvNsOR7Tli3xCYzqN3fRTfrlgE9fF9tYkOXCiC7kZeweCGA86wEDEMj0wKRUO7Idba1d8mY-v15uJGpYlkhZEKSlUA83yPvSlp-aRn2e-pYckXyc)

#### **Document**

![](https://lh7-us.googleusercontent.com/n9ABWRQI8k7SVDk6RsYcvI\_\_r5CWXdMDn49fKkAy3T\_0s3TTJp4aMV5K4hsiGh56YKrxcUaqmUZfj3\_QBSS2eSZ1TAPCoI5-LnJCC-JYv8K5XEOZsJLXX77EKGZCs37qtKiFHD9P9KpW2jhOEX4bu1Y)

The following documents need to be added to the data flow:

* Sync.ChartOfAccounts
* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/c6Dhk5iR1fJXqjrXsbSMmkIDBl3eaRNoiijw9WMA69HSrXMKqOjMEKtRtqfXbHcy9fQH1etprR2IuZO6xpMBnY6EYuU6cyBCFjHx4yN2KxxRwTqX12TwSsUaF7wFySImLki86BUKRMW-0YKQJfQTWOw)

#### **DocBits (ChartOfAccounts)**

![](https://lh7-us.googleusercontent.com/JhBa8R1tRR\_GcoBmas\_mJ-QPT3XTNyGAdwh48N7pISM-fRNa3lfuZB7MhAScDbbCtpgGXtxx140w0bcEwgVdtMkGDh6S56uVsm039Z\_8FGA\_FwA2aSvJftr8MeHr3e9WPwRZqugKvRD\_kIVnQdexFek)

This is where you add the ChartOfAccounts API connection point which you created earlier, the configuration for this should look similar to this

![](https://lh7-us.googleusercontent.com/yyq6JularNBP\_GpUbDLQ-KWu6utcEZefLXcoHboFa6rcmbN1e8QrdLkab9h2QBWuW-V-i7edmqpTWJwtqWg14GKLDnukyLGuljKXue\_XH\_bLmL2dNz5dECDI\_lkg9hO84nFIDyYWYatkzRkxAYyJe6w)

### **FinalFlexDimensions**

An overview of this data flow looks as shown below (the amount of DocBits API connection points at the end depends on the amount of different environments you are configuring).

![](https://lh7-us.googleusercontent.com/MQyQxEHmvG0vX4VXSnpntbXBGQBtC5uvMeNXklp-EETOIMLZNOJqwOlZp9xm\_\_Lj--o3bJETADpxgZkajW0H0xOE2Gvib9OeU3BeV-mj4lpKFqPQ8A4fymQJDjTZNI8fzrOxYqa595I0\_C3b8QkoTb0)

#### **LN Company**

The configuration for this connection point depends on the LN company which contains the master data you wish to import into DocBits, yours should look similar to what is shown below.

![](https://lh7-us.googleusercontent.com/D25DTQRX3yecDDMmp\_UvmS9b6AWPYue8LdUueurlCTYg0qWw\_SyM0lCx1sn3VSK0m5MOilgmGWJ261YLr1MlTm9G452QyDQXbyN7DXsQpmmINEbVL5g-OIhpYKN14XQk6oEMqwoTgvpLNKS9\_MkU-sk)

![](https://lh7-us.googleusercontent.com/rGMdEdvYixTZ5wmS5ptBiGcxoOT0abpASTeSDzEFH3SSx-G97gSxIniXja2R3erYP4oIxyVezvL7VjqXKcKd5i6caNZHI-1gVIi2jrKfy\_yVFQ5T80n3ZpR1wSiPWCh\_8affNONcGAcuokvN69-Urfg)

#### **Document**

![](https://lh7-us.googleusercontent.com/WyltkYqwzyofXZpwm\_x1-SiM5MCbvDoKPQ9AVOT6nyxXnqXqQn4G-uM7BO2hNRJii91EODf5mjIwS85eOfJ\_UyATLAWqbXegd54leKsK\_zNlVWQNm79yoyTb\_Ok3605NEOM\_Hu\_ov-yaboAQ26PpmTk)

The following document needs to be added to the data flow:

* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/YIvKeqyGUDBZIoi7I6jhTIlUYtsgYEMeKA3h4Xm9KHz5pYWssDuIaq7343RQdEsxMznTNnReWEB2OCqBQGvgzi7HEOVGlX5EqPa2JEO5sC1LpUF-OXvYLO5a7LMbE2h2YY1Bk2rRnNbCjAZqIMuIxGw)

**DocBits (FlexDimensions)**

![](https://lh7-us.googleusercontent.com/zNJteyBB\_TcRKGE7GL3iPPlFaOqbij5ag37NdNW5GcZBz0xMmb9iev8EktCSJDSNkeZPOnCf-5nImxJjn6RIBTg3x8xJrLK-Z0Z48VTXXLPNIO-3NnmDEVVF-9oHteOQWIjCIMhhzKLK7iCL\_jVsfEY)

This is where you add the FinalFlexDimensions API connection point which you created earlier, the configuration for this should look similar to this

![](https://lh7-us.googleusercontent.com/ymjxWkOzchUu91ovhE1eE58mSRCyrclNKsNoK48gFcSwKRVuc9Zfy7QZzJ83ATXUWJO4sgPpcNEVPyYZX8dr-sJoEfYKez-WtScX\_hnmOfH-2wBcFKrhxy5wwBUSlKP-ayxcMnCiQ6DKrgqYkfL4xQg)

## **BOD Triggering (M3)**

Once all the above is completed, you will need to navigate to Infor LN and trigger the BODs in order for the various master data you need for Auto Accounting to arrive in DocBits.

![](https://lh7-us.googleusercontent.com/OG5eKwuynVhgRagfTwylC2hT6lYMKIgn0ogn1RPShzv7gbE2IO4lC8YzKWDmHa6l6waMREGwVLZmhsCOhUWNrp\_7rkkdrVgo5Z8s84V475UO927BPujEwsX8SY7kRsZBt3R0GUWD13hogj0LdgqNotU)

From the above menu, in the left menu tab, select Common → BOD-Messaging → Publish BODs → Publish Financial Master Data. From the following menu you will find the FlexDimensions and ChartOfAccounts BODs to publish.

![](https://lh7-us.googleusercontent.com/KWv\_YZ0BuoZrBvnp2MRzXKRRH1pID7V0iwjCkT4xt7NcbHYoZnFS6wnM\_itC3RzNNGJ95565KynkMFuPb-1NjY0zOGjvlINvVQIrJBcm8daOZa3UiDIB0zBPlt5BS5KavsmYcXHWBQZ9NytMg6NJezs)

Select the following BODs to publish by simply checking each box, no other changes need to be made as we want to publish all of these BODs so that the master data is complete in DocBits.

![](https://lh7-us.googleusercontent.com/cp9CKdRYofwTrRodTNbZDfMmi\_Q23jchyt\_w7hFkGvvoBo89uhSRoKz0uD2cm2M0tLDmrkb6-8qq9z5EfX-ciEmraWqyytxH09jMK8jVVunb8zjK9EkvGhyl07Igoa4sf8hCLvyGnIlHMVjeLzMFrD8)

![](https://lh7-us.googleusercontent.com/cu8PW0WenwC5jBBFa4trAua-d8zYxi60S2syvKHoBoL2Tk9jdQAOQTvUvGZWSR3cpErwDUZ3WHkm4cDCwS1ZhSJyiQltf43\_Re05WddfxQwJ69C3E\_z\_0bMhEwbq3NasV3Q2waKJlfyBk1oIWdVDjps)

Once both of the above BODs are selected, navigate to the Options tab

![](https://lh7-us.googleusercontent.com/imBr628dcJJoNBknxVfKjoWindKT\_\_5AzmYDVXIaHF\_n0RWQUSiK07EHH1df0L2xxCOC5z36UQOfsknF4-GwUgZ9tDZcwDosjxChqFft0GGvVo1JAkPpK\_St-GB7NW1RlBgTszID4YQteYiZlFKPuz4)

Once on the Option menu, select the following options and select PROCESS to publish the BODs.

![](https://lh7-us.googleusercontent.com/3LH3Me8kacFfp1QH0VFMIfzQtWyFt12IgRQzcAcJByoPQtjhxDnQKE3EjNLO349WeW2WINoFwwrpQJIOoSXBBM\_tmIecJLJEyLipUHXel5yRw7H98OdfydXJdZcChaHvnnwc86wihiblnthMobZyu\_s)

Once this is done you should see the three separate master data tables in your DocBits environment(s) under Master Data Lookup:

* chartofaccounts
* totalflexdimensions
* finalflexdimensions
