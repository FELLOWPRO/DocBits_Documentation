# TOML Export

**How XRechnung is Mapped in DocBits**

**1. Header Configuration (export\_configuration.header)**

The header section in the XRechnung is mapped to fields in DocBits as follows:

\[export\_configuration.header]\
name = "header"

\[export\_configuration.header.fields]\
DIVI = "RFP"\
IBTP = "20"\
IMCD = "0"\
CRTP = "1"\
CONO = "001"\
SUNO = "\[supplier\_id]"\
IVDT = "\[invoice\_date]"\
SINO = "\[invoice\_id]"\
SPYN = "\[supplier\_id]"\
CUCD = "\[currency]"\
CUAM = "\[total\_amount]"\
FTCO = "\[supplier\_country\_code]"\
PUNO = "\[purchase\_order]"\
CORI = "\[correlation\_id]"\
PAIN = "\[sqr\_field\_esr\_reference]"\
TCHG = "\[additional\_amount]"\
CDC1 = "\[negative\_amount]"\
APCD = "\[buyer\_id]"\
TEPY = "\[payment\_terms]"\
PYME = "\[payment\_method]"\
BKID = "\[bank\_id]"\
GEOC = "1"\
TECD = "\[discount\_term]"\
TXAP = "\[tax\_applicable]"\
TXIN = "\[tax\_included]"

  •  **SUNO**: Supplier ID, mapped to \[supplier\_id] from XRechnung.

  •  **IVDT**: Invoice Date, mapped to \[invoice\_date].

  •  **SINO**: Invoice Number, mapped to \[invoice\_id].

  •  Other fields such as **total amount**, **currency**, and **payment terms** are similarly mapped from the XRechnung to DocBits fields.

**2. Tax Lines (export\_configuration.tax\_lines)**

Tax-related information is mapped using the following configuration:

\[export\_configuration.tax\_lines]\
name = "tax\_lines"

\[export\_configuration.tax\_lines.fields]\
RDTP = "3"\
DIVI = "RFP"\
CONO = "001"\
TAXT = "2"\
GEOC = "\[\[geo\_code]]"\
TTXA = "\[\[amount]]"\
TAXC = "\[\[tax\_code]]"

  •  **GEOC**: Geo Code, mapped to the corresponding \[geo\_code] from XRechnung.

  •  **TAXC**: Tax Code, mapped to \[tax\_code].

**3. Order Header Charges (export\_configuration.order\_header\_charges)**

This section handles any additional charges that need to be added at the header level of the XRechnung.

\[export\_configuration.order\_header\_charges]\
name = "order\_header\_charges"

\[export\_configuration.order\_header\_charges.fields]\
RDTP = "2"\
DIVI = "RFP"\
CONO = "001"\
NLAM = "\[\[amount]]"\
CEID = "\[\[costing\_element]]"\
CDSE = "\[\[charge\_sequence]]"

  •  **NLAM**: Amount for the order charge.

  •  **CEID**: Costing Element, which can be mapped from specific XRechnung elements.

**4. Receipt Lines (export\_configuration.receipt\_lines)**

Receipt lines, which represent line items in the XRechnung, are handled as follows:

\[export\_configuration.receipt\_lines]\
name = "receipt\_lines"

\[export\_configuration.receipt\_lines.fields]\
RDTP = "1"\
DIVI = "RFP"\
RELP = "1"\
CONO = "001"\
IVQA = "\[\[quantity]]"\
PUUN = "\[\[unit]]"\
PUNO = "\[\[purchase\_order]]"\
PNLI = "\[\[line\_number]]"\
ITNO = "\[\[item\_number]]"\
POPN = "\[\[item\_number]]"\
SUDO = "\[\[packing\_slip]]"\
GRPR = "\[\[gross\_unit\_price]]"\
PPUN = "\[\[unit\_code\_price]]"\
TCHG = "\[\[charges]]"\
CDC1 = "\[\[discount]]"\
REPN = "\[\[receipt\_number]]"\
PNLS = "\[\[sub\_line\_number]]"

  •  **IVQA**: Quantity, mapped from the \[quantity] in the XRechnung line items.

  •  **ITNO**: Item Number, mapped to \[item\_number].

**5. Cost Lines (export\_configuration.cost\_lines)**

Cost lines, which handle additional costs in the XRechnung, are mapped using the following:

\[export\_configuration.cost\_lines]\
name = "cost\_lines"

\[export\_configuration.cost\_lines.fields]\
RDTP = "8"\
DIVI = "RFP"\
CONO = "001"\
NLAM = "\[\[amount]]"\
VTXT = "\[\[voucher\_text]]"\
AO01 = "\[\[accounting\_object\_1]]"\
AO02 = "\[\[accounting\_object\_2]]"\
AO03 = "\[\[accounting\_object\_3]]"\
AO04 = "\[\[accounting\_object\_4]]"\
AO05 = "\[\[accounting\_object\_5]]"\
AO06 = "\[\[accounting\_object\_6]]"\
AO07 = "\[\[accounting\_object\_7]]"\
AIT1 = "\[\[ledger\_account]]"\
AIT2 = "\[\[dimension\_2]]"\
AIT3 = "\[\[dimension\_3]]"\
AIT4 = "\[\[dimension\_4]]"\
AIT5 = "\[\[dimension\_5]]"\
AIT6 = "\[\[dimension\_6]]"\
AIT7 = "\[\[dimension\_7]]"
