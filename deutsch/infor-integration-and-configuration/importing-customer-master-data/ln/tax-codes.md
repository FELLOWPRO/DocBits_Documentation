# Tax Codes

## **Create DocBits Connection Point(s)**

Open ION Desk → Connect → Connection Points

![](https://lh7-us.googleusercontent.com/QLQB17W\_hywZWBqme8Wio-orbdOdFHXLv5zTd89B3EkeS0WCuuo5Pv1CndLRQ2rFUefvQYM95U2Unhrl3YU3WAR23Ij\_tDw\_TOEVenWjyCh-9H8CPFSezF2gmED7u5QTR7q9WV4CSXRvDqkmKJYPqAI)

You will need 4 connection points for this dataflow, 3 API connection points for the different tax code categories (full, reduced and free) and an Application connection point representing your LN company.

&#x20;In order to create new connection points, select the “+ADD” button”

![](https://lh7-us.googleusercontent.com/cECLuIswRSK3WWhUMi1n3tm2AIcrksZdpz7ZCO6-H\_MzaKe9CDT0w1b7GKJ8GtT\_d6nvvDe4ukLJfWcMocbHZ5dSSCw25Ky7-JUdrYb893GYYyaHL9tTjG1ZniORJPLSu1zJxL3c-1VQRw4IC0LpYuA)

Select “API” at the bottom of the list of options

![](https://lh7-us.googleusercontent.com/bpeLxdmi8b10LLMGy02vMRXuLoic9kFLywnpd6SSYV0fNv82dQahyvaA85mC1PEVScNW4m63fOw89vkhQr0-ou8VWOSjkwGWG5GnP7GQl77THtjXWP3YNo8LUzAstpCs0Q5fOjxaoT\_\_ZKM4jciHA5I)

You will be taken to the following page

![](https://lh7-us.googleusercontent.com/4pcN0B7aibjn\_Qn8nMgkzRc\_NiXev-c1wJudDKo2V5r0ORuajVzfzAWnWu0Wt68hKMKSLYkieUhOYChkcZuCZDWkg-F22Rq2WvVqgPweSg3by2TGrrJHweKWTlf\_DK1X2pCkoNU4yoGo3DyHsoqcGjg)

This is where you will enter all the details of the TaxCode connection point. For each of the three connection points you will be creating do the following

* Enter a Name: TaxCodeFull, TaxCodeReduced, TaxCodeFree
* Description: This can be the same as the Name or similar
* Import a service account you created.

Switch to the “Documents” tab and select the PLUS icon to add the BOD we need, like below

![](https://lh7-us.googleusercontent.com/byhA18LzkcY9ZyfnzyDlru5qBx88E8U1yggMNNkoHGsYVCbNkflNFXGVvJwMvE\_104VCjoYOM0SQIJVniyBBdn5UKasVR0uat6UvmCmpzz9ZYsY2Wv14B4ElOwqcg2qklxYAQVU84UOG70l3fMLRrwo)

Search for the BOD

![](https://lh7-us.googleusercontent.com/DAKzvEsjCmk1jy7L6GwrVY2DWg3\_InluNftWnR7hGlnyeBxSDW6XTDPBMLqtJuUc9Lq3Nga6-EKS4tZpOjE09h5FUJaTm\_E70UdA4l17jWGQ6BSr121lC3LzhffUXi6Bsk5EZEz4XHyjekk1Njb3H4I)

Search for the BOD called “Sync.LnTaxCode”, click on it and press “OK” to add the BOD.

![](https://lh7-us.googleusercontent.com/7BLwrq8kr9OTHleI2anmAr2-4ChksQ0pptddwm1quFHquGfnMBEW32RFx31ETGbrxf0KGVr-VzlZC9h9heD3ymTq9L5NZEV1b9E67IIR0is18UGBCoJ5j7KIMmF533EDMvZzgi4LXqAkV9zgCyl0\_Lk)

Move on to the ION API section. Under API Call Name you can use the name of the BOD, Sync.LnTaxCode

Press the “SELECT” button

![](https://lh7-us.googleusercontent.com/7MukO6oUAzVBFMPhFepwMvugqnhDDMhX9j7wZRU7BU0OusW3CKpMgqQNC7uNlehPp6eFniVxrX3DxjgsGZ\_Tmt\_cQOWGGiBfXAQfCC85amOGp1VY8RGo3nPABCiwzaIkYmnQF6t3FPVZ1fPV6fLazNc)

Select the API you configured for the environment you are working with and search for the following API. Once you have selected it, press “OK”.

![](https://lh7-us.googleusercontent.com/IpUUqJaXF0MmIeR6gtE9GDCccLfNsQLZ-RSHhQGVwJEj8WJwI-twgiHpFomBKhbnTUUKrhxJ0EUZ7F\_21MCSBjNS2VQq3azprekoxctRJZ-NJUHhb4J9rHUSRDoR\_OCzDHTG5q5KTwWMHOR5qNoNd38)

Next, switch to the Request Body tab.

Here is where there will be a slight change for each connection point, this is seen in the field mappings you will assign to each tax code as they differ slightly.

![](https://lh7-us.googleusercontent.com/f4c-1M9mgCci2jjxkhaCDFX9bRWzMDaRwVv4XiaUH7BpHchPklvMnWoP\_ILSm6VB7GoFJNJzHsEPzk3eCFyLm1Kc3QI8OufjQ1mr7PqowjzViFDWc2opiNE1ODICtI9yEyUOi\_d\_hzN8CGo8gu6Ec84)

In the field\_mappings row, under value, is where you will put the specific field mappings for the specific tax code connection point you are creating (full, reduced or free). These mappings are available at https://docbits.com/doc/field-mappings/.

The end result should look the same or similar to the image above. Once this is done, click the SAVE option located here.

![](https://lh7-us.googleusercontent.com/LSYrbElw6BgQbbIdSstbakfwLENZ\_09WQcQhjO7kbb2U3jSK\_\_wFnr43tIj2hTHYegQ9lrSZBuJ9N7MNewr2W3yjPCrrVLeP9UAZjvrKKBzeY9h-q6FrVd5gPtlH0iP0GpMcvhGxjAnHN7BlY8CmT3c)

## **Data Flow Configuration**

Navigate to ION Desk → Connect → Data Flows

![](https://lh7-us.googleusercontent.com/cpWAepQyLP8V0b-Oj7djzl21eZLU2JdnJPEMPs53Uq-adZbaCegl35RjguLx8rsP2E87ZmwbNgISFIpAy6kOeahaBCSygDVSJzmv1GQGn1w1MgR8N08mnnfhb02XjsLnt\_rVJKr4Y0UtiTf14NqTHLQ)

Click on “+ADD” and select document flow

![](https://lh7-us.googleusercontent.com/HYqc\_P2DQjBoc-mpsyZ\_nlPFNiU17ZCLHfiOa282-Sa5JSA3Hv1XlwFjmlPhVGnAaEAqqalJ5ka43AJOzEO3uljwVAogAHkTVer7Q9JgI0WaOVX2Uo5Z8KGEqoa3BH\_zZwup7Bh4lKe4O5kr6hmAZm4)

Create the following data flow by dragging and dropping the components from the to menu

![](https://lh7-us.googleusercontent.com/V\_aJHPhFJssPUQ4mAHU20SVPSfhqhjU8BOQ2Ws1MtaauKp6OVAENLXod2uQe6Zbuc5JKZx6Bp3WyJtkQtkbnDluZZS5GLMGcaC9EuCrV8cn2aJk2y-Cih3PP2dg-umW0iDhak5UXNUuPxwkgqVg-mvk)

### **Application (LN)**

![](https://lh7-us.googleusercontent.com/2CCNlz0S-Z8p\_l9kPPUMqPkreoO3aLy8MkqY6UFMIABJRNFXGTFMXbaw78E42g8fEO4ZxFL\_oJMf2QnWn2xZLtS4zjN8AzCS\_B2i2x-tjWmmjyVLa1jSLQAnSB8-EhNfNISzf2uuX9kcqN-QixUUXvw)

Here is where you will select your LN company, the final result should look similar to the following

![](https://lh7-us.googleusercontent.com/b5pb4YfbZMCSi2X-xT4mj-Yw\_Uu77zNyJGl3rntVdqf907PwgX6Z9uQJIoHA2FS5M\_mVbdQgkh0HWgsOgtkoySmtrT7W8CrqsqlCnPEt6hv\_yODGulfp1qdxXvrB1HL-en3W9bY285fC3kARLZfSfck)

### **Document**

![](https://lh7-us.googleusercontent.com/U8cqu3jABU3RQLGEGsS5qCnDkc-boTpAdZEVIUA9AlmD9Oz33JvnzD43SBTmLY55i8Bsr4lbi6udeIimCcRG1NgWbynv6OllCLaJPC50kJ0gPq7rsR5Rvj50yKngMiNvnYoLLT\_Hzn5cyhp18jq\_IyI)

This is where you will add the Sync.LnTaxCode BOD from earlier, the result looks as follows

![](https://lh7-us.googleusercontent.com/bgC1y3NtmX09XBjng\_pKmP5VQ5w0E\_VuFOfMF1rYs3iGGL5OaMHkKoyQJNtcVtbS6bEvF4KdtFNaX0VxT9MF0P-zTDnOnt5mhA0Gxcs4eMcRLtbXl5a\_8y84XyLyvh61-LdoQ7f15j-wE1nl\_TSYSDg)

### **Filters**

![](https://lh7-us.googleusercontent.com/1Cv1XxqdpiNfonz6jdFgz9zGibQTRLd\_0ONFHf3FvzPB9-sQuX4lTUyuDWzm-RffuPf5jDmZAZwUqbXX-1kers1sEb9ykRMHeYYP6zGgF8yZ247Dx0nG04kSYUTTKSwt3NLS-3TwXA5tbvy5z8HA2bw)

#### **Filter 1 (top) – Full**

The Name and Description will depend on the environment you are using and your preferences.

![](https://lh7-us.googleusercontent.com/WVKWUme9uUjRRn7dZ5c\_RyPk\_GCTFEfiNxU\_H5aA979k5hOv2coDYEJHu4K1EaTLUf8\_Pd9ffOk757DaflF0Se0gZ1ZYvRk4QHlpKP0IeirfNr-L6JU3Z\_xFZJ2eeFI-Rhcctwk9QOHRORGNt1oIEpE)

![](https://lh7-us.googleusercontent.com/1gCPbUtC7KknzEHVZqIMKyjQGmNyNnR4c1mJ5x0LCJnAjd8D3SdW3W6nPMTsLokL-W2-XjoSM9MU1mJ77K12g887r\_jHoHBwquN1Ore2AmyjCaf\_YVT78KiKtY\_itlr-vyMvJrU7YV6ErgVSYbw5SEU)

![](https://lh7-us.googleusercontent.com/ijzGaLt9Uhzw6Wf66ah3auWo5TbkCnM-xGDYezsXXjPEkdCe5RO1wWfhhhG0qRuKbojijLKUm-WUV21eRdq36moWu9Ft0ujexe\_1lTUUEQbfXPvtrzP7iudkSaG\_oiX\_LV7AqZRGlNAp0OXnN8BXRIM)

#### **Filter 2 (middle) – Reduced**

The Name and Description will depend on the environment you are using and your preferences.

![](https://lh7-us.googleusercontent.com/pKLo6q5zCQOZQhiRppyd8M-nlIrX5leGUiCct4Xn-4teIZTip5GAJVP0EFc2PrJ6EeDmU2KVOHRKVCaaML4sK8jCnsgTmxbTYjc-9CNd6bOfU-WD9tySeKL7gSRltjzoTEI5Ozrd\_s-7qj2KVNOWN7s)

![](https://lh7-us.googleusercontent.com/87PoQQ5q\_35buL\_VNcvz3v-um1upk1U579LDASCJptnnC8ip5mwXxz89d1YmtIK59dOUhl9dfz6BrXBLSNUy6EnWU5uPmUEzbLQv-MwzR0dDkuM1BJ477yre-X4QeJzkkzprF9y5wCWY4zvaooMwIZ0)

![](https://lh7-us.googleusercontent.com/Pa19AN6Mhxbn6bHSc5qKEGM0xRsEV6v77ooyeg5-91i8qGhaThb4328nr\_g6a\_z-7BOCJmWpo8Gbd2twl9FQkOf1Q8QZqOkJmxsIxaTP0R6dASgZdIV6z7p8PFYPYUJ1eKp8btYOBapliANstQSUgAQ)

#### **Filter 3 (bottom) – Free**

The Name and Description will depend on the environment you are using and your preferences.

![](https://lh7-us.googleusercontent.com/c\_SuWaZ3gF-FbOPWkxB\_eFgkT-TGJEYwV\_fQT05wGWHFNzI9SDZRQfauVMeBl0rn79QdU-W3kRgN-hWsYkfdMSevlYyiNPxxT\_3RxXcETo-lkjvI5TCygUag91PFJycrRdMA5hSQJCuzt8FekMwpu98)

![](https://lh7-us.googleusercontent.com/HGZ8fR6XgYtZ46i8Rov8xIr5J4z8DmGFfJkeovDGzT7S68VYI-OdG5jpMdoOiROIZckYMbVIlPQmS\_kWQazJVbco1t4ZH5Sr73b4xePlisnbm9ZLJrOPwtXn7-90F1FcFH99P6ZKI0hCWdI6z4d7qNA)

![](https://lh7-us.googleusercontent.com/\_APmMO6A2AG2km4H4em-ZMrn6\_XRpO3zxRhZwftiaKi5uoDhv3TTzCBfi8WVDCf6mOQNgtcEJ-z-BmP28J86noGJ5dgqVni2QIxePaO5-LU8fdwRqySUQt\_6wmFWiOFzTMmItcClQPRaSKUaosgWwNk)

### **APIs**

![](https://lh7-us.googleusercontent.com/XDhVCKHYaxrRIFyYfq0guXwnZH6jK-WZIFj2i0Wkr4kxyNcdCH1TzKd0Pb3-H6qs-b7JZ3UUIGm0BVHiUL7Aya-D7YOSV8p8tnwQeAfBN30T4fW5-ANePN1TcvUr1gzLJPwj7rRO4Hw4ziuyYrqZBX8)

This is where you select the API connection points you created earlier, this is done by selecting the API under the “Select ION API Connector” drop down menu.

#### **API 1 (top) – Full**

The Name and Description will depend on the environment you are using and your preferences.

![](https://lh7-us.googleusercontent.com/90c2E47fMC9CKNVY8DtgyaNUAqAnQmfErZm\_R-njUlEdIX6mafMUOk3GcAooaWfCzD4-OmdPUq5VSuMXmTSNjVEc924ASIPqmTxAQXqsq6eKs5y82rvwHxqnsT4S-sEm2mQRNwleiubkwIO\_kS9Vwzg)

#### **API 2 (middle) – Reduced**

The Name and Description will depend on the environment you are using and your preferences.

![](https://lh7-us.googleusercontent.com/vw1hM3W4eCt\_8OG7Ht203tckaWarPOLi463WvQzGgixTMnfk7iC27JzL3iNgd5LmvBzWTFnYa3QNy5y\_oNSHJ9R-Ck5CAgLoBmGurbCn1RZ32jiSJr-LUnL3b0nhHctBqcCx\_25L1Ce-\_va3ZgfKXY8)

#### **API 3 (bottom) – Free**

The Name and Description will depend on the environment you are using and your preferences.

![](https://lh7-us.googleusercontent.com/C0wmqAkrlgyXlMjKsGMOqre4MPLuHawrZB1oYDzkGFocperUB5dKea7kx44hrA\_Kz6Ptx495cQbwq\_EHfEGNvvpr\_0dvCuUS2zz0-SARyuNbf2gKsK3vTdd4Sfg3jWtE1YAN3o0VpoK\_HRn7T-fFOR8)

Once all the above is done, SAVE and ACTIVATE the data flow by pressing the following buttons

![](https://lh7-us.googleusercontent.com/f8gkYY1Z\_W1if2h1es9vbjebtDX0zGiqY4p9OD68gKSAcNU6si-guvyIg8hzdjP7TulZ6Yq8NcbT2EyuHleVeNxpY\_6TDlbgIUaxDJ72ILcy8kVvFuSja7FT6gpYhMLFGw7wv-r0XyFN8xIrQ3OuUGI)

## **BOD Triggering (LN)**

Open LN in Infor

![](https://lh7-us.googleusercontent.com/aAKRLInqsogQLv9nye2rHLtVFlW4yaCpnQ8A4cKG5A2145Tl6poOxthfo2InYimNk5dd8RabYrX9xP7sPO0aJ5ThF07ZVfKvUXBqVoxRJg53IhpeOeiA4B\_CGOpeLKWlPbCf4EaFXjgzmBOcezocF9k)

Navigate to Common → BOD Messaging → Publish BODs → Publish Financial Master Data

![](https://lh7-us.googleusercontent.com/pMAgPzyhBNrEsFkTm8-iniHBhEXIPswoJ8URt\_v0fv\_7dSayrS8UkN7F9WMAOZQB9Q6sCe9faRl4rRDDft3VdrzfNUT-IbWxE6GyWPPKZh4R67JRmXmJ2NsTVPdjLo6uJdCpki7QDpgiY\_azWtqaqKA)

Select MORE and click on LnTaxCode

![](https://lh7-us.googleusercontent.com/MtjE7Glgv7e\_F\_CJ4LXMuWk6SaInmNFlKzhGJu71iGgxRWtjI96lX5J0gqxRcj3y1u4E6Aq-xNEpuf83dsjHh6op0qeH89oBMvlVTTD\_VhGs10-gjuIb0eyc9b3dcCk75Wa5sASreXKW6SbQPYrs8sM)

Tick the checkbox to select the LnTaxCode BODs

![](https://lh7-us.googleusercontent.com/VTFntcBK0GVsUdr\_fZBUaN8rXYdufObLE7PnwwNg9QU69zYwKHvwFZ7En9WZ6p\_WGIkVdqEjBBYeIYSuHHJWBWYonwd6Edtr0ZZuGsX3qhNMDWQWefOaGfrYxrq\_yLm6\_gEw967PGp3HK0hzO-G2XiQ)

Navigate back to the OPTIONS tab, your configuration should look as follows

![](https://lh7-us.googleusercontent.com/2tr7VHNOLActJCiLGC6jyWsdyqwZV7Je6UsekeoBo57qNpOBDYtOQuoelKOdvLMRo6uQJWn1S4ir\_zRZHAx2C96NyKp4ZjIUyFCYt58T59TqO3ml0ZfiEtSLwdRPp9g8pkMemN0xDS5ao8DL5xgosWE)

When you would like to publish the BODs, select PROCESS.

The end result should give you a similar table in your DocBits environment.

![](https://lh7-us.googleusercontent.com/4wK-mfKl0UNqvp5ngolE54miiwAKxAcOERO2mSDWzZ5t838VhFZrZGzCMeIyg7WDPpHvNzkeWRJV7ZZdsaxwXiFS9uxm29QZUYHhs9gU2v6QgSz07vfjpHXW3oTb5ZiiiTjI93gmV9MDTHbNWJmrvHY)

