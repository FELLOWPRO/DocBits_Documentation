# TOML Export

**How XRechnung is Mapped in DocBits**

**1. Header Configuration (export\_configuration.header)**

The header section in the XRechnung is mapped to fields in DocBits as follows:

\[export\_configuration.header]\
name = "header"

&#x20; \[export\_configuration.header.fields]\
&#x20; DIVI = "RFP"\
&#x20; IBTP = "20"\
&#x20; IMCD = "0"\
&#x20; CRTP = "1"\
&#x20; CONO = "001"\
&#x20; SUNO = "\[supplier\_id]"\
&#x20; IVDT = "\[invoice\_date]"\
&#x20; SINO = "\[invoice\_id]"\
&#x20; SPYN = "\[supplier\_id]"\
&#x20; CUCD = "\[currency]"\
&#x20; CUAM = "\[total\_amount]"\
&#x20; FTCO = "\[supplier\_country\_code]"\
&#x20; PUNO = "\[purchase\_order]"\
&#x20; CORI = "\[correlation\_id]"\
&#x20; PAIN = "\[sqr\_field\_esr\_reference]"\
&#x20; TCHG = "\[additional\_amount]"\
&#x20; CDC1 = "\[negative\_amount]"\
&#x20; APCD = "\[buyer\_id]"\
&#x20; TEPY = "\[payment\_terms]"\
&#x20; PYME = "\[payment\_method]"\
&#x20; BKID = "\[bank\_id]"\
&#x20; GEOC = "1"\
&#x20; TECD = "\[discount\_term]"\
&#x20; TXAP = "\[tax\_applicable]"\
&#x20; TXIN = "\[tax\_included]"

  •  **SUNO**: Supplier ID, mapped to \[supplier\_id] from XRechnung.

  •  **IVDT**: Invoice Date, mapped to \[invoice\_date].

  •  **SINO**: Invoice Number, mapped to \[invoice\_id].

  •  Other fields such as **total amount**, **currency**, and **payment terms** are similarly mapped from the XRechnung to DocBits fields.

**2. Tax Lines (export\_configuration.tax\_lines)**

Tax-related information is mapped using the following configuration:

\[export\_configuration.tax\_lines]\
name = "tax\_lines"

&#x20; \[export\_configuration.tax\_lines.fields]\
&#x20; RDTP = "3"\
&#x20; DIVI = "RFP"\
&#x20; CONO = "001"\
&#x20; TAXT = "2"\
&#x20; GEOC = "\[\[geo\_code]]"\
&#x20; TTXA = "\[\[amount]]"\
&#x20; TAXC = "\[\[tax\_code]]"

  •  **GEOC**: Geo Code, mapped to the corresponding \[geo\_code] from XRechnung.

  •  **TAXC**: Tax Code, mapped to \[tax\_code].

**3. Order Header Charges (export\_configuration.order\_header\_charges)**

This section handles any additional charges that need to be added at the header level of the XRechnung.

\[export\_configuration.order\_header\_charges]\
name = "order\_header\_charges"

&#x20; \[export\_configuration.order\_header\_charges.fields]\
&#x20; RDTP = "2"\
&#x20; DIVI = "RFP"\
&#x20; CONO = "001"\
&#x20; NLAM = "\[\[amount]]"\
&#x20; CEID = "\[\[costing\_element]]"\
&#x20; CDSE = "\[\[charge\_sequence]]"

  •  **NLAM**: Amount for the order charge.

  •  **CEID**: Costing Element, which can be mapped from specific XRechnung elements.

**4. Receipt Lines (export\_configuration.receipt\_lines)**

Receipt lines, which represent line items in the XRechnung, are handled as follows:

\[export\_configuration.receipt\_lines]\
name = "receipt\_lines"

&#x20; \[export\_configuration.receipt\_lines.fields]\
&#x20; RDTP = "1"\
&#x20; DIVI = "RFP"\
&#x20; RELP = "1"\
&#x20; CONO = "001"\
&#x20; IVQA = "\[\[quantity]]"\
&#x20; PUUN = "\[\[unit]]"\
&#x20; PUNO = "\[\[purchase\_order]]"\
&#x20; PNLI = "\[\[line\_number]]"\
&#x20; ITNO = "\[\[item\_number]]"\
&#x20; POPN = "\[\[item\_number]]"\
&#x20; SUDO = "\[\[packing\_slip]]"\
&#x20; GRPR = "\[\[gross\_unit\_price]]"\
&#x20; PPUN = "\[\[unit\_code\_price]]"\
&#x20; TCHG = "\[\[charges]]"\
&#x20; CDC1 = "\[\[discount]]"\
&#x20; REPN = "\[\[receipt\_number]]"\
&#x20; PNLS = "\[\[sub\_line\_number]]"

  •  **IVQA**: Quantity, mapped from the \[quantity] in the XRechnung line items.

  •  **ITNO**: Item Number, mapped to \[item\_number].

**5. Cost Lines (export\_configuration.cost\_lines)**

Cost lines, which handle additional costs in the XRechnung, are mapped using the following:

\[export\_configuration.cost\_lines]\
name = "cost\_lines"

&#x20; \[export\_configuration.cost\_lines.fields]\
&#x20; RDTP = "8"\
&#x20; DIVI = "RFP"\
&#x20; CONO = "001"\
&#x20; NLAM = "\[\[amount]]"\
&#x20; VTXT = "\[\[voucher\_text]]"\
&#x20; AO01 = "\[\[accounting\_object\_1]]"\
&#x20; AO02 = "\[\[accounting\_object\_2]]"\
&#x20; AO03 = "\[\[accounting\_object\_3]]"\
&#x20; AO04 = "\[\[accounting\_object\_4]]"\
&#x20; AO05 = "\[\[accounting\_object\_5]]"\
&#x20; AO06 = "\[\[accounting\_object\_6]]"\
&#x20; AO07 = "\[\[accounting\_object\_7]]"\
&#x20; AIT1 = "\[\[ledger\_account]]"\
&#x20; AIT2 = "\[\[dimension\_2]]"\
&#x20; AIT3 = "\[\[dimension\_3]]"\
&#x20; AIT4 = "\[\[dimension\_4]]"\
&#x20; AIT5 = "\[\[dimension\_5]]"\
&#x20; AIT6 = "\[\[dimension\_6]]"\
&#x20; AIT7 = "\[\[dimension\_7]]"

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;

&#x20;
