# TOML-export

**Hoe XRechnung in DocBits wordt gekoppeld**

**1. Kopconfiguratie (export\_configuration.header)**

De kopsectie van de XRechnung wordt als volgt aan DocBits-velden gekoppeld:

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

  •  **SUNO**: leveranciers-ID, gekoppeld aan \[supplier\_id] uit de XRechnung.

  •  **IVDT**: factuurdatum, gekoppeld aan \[invoice\_date].

  •  **SINO**: factuurnummer, gekoppeld aan \[invoice\_id].

  •  Andere velden, zoals **totaalbedrag**, **valuta** en **betalingsvoorwaarden**, worden op vergelijkbare wijze vanuit de XRechnung aan DocBits-velden gekoppeld.

**2. Belastingregels (export\_configuration.tax\_lines)**

Belastinggegevens worden met de volgende configuratie gekoppeld:

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

  •  **GEOC**: geografische code, gekoppeld aan de bijbehorende \[geo\_code] uit de XRechnung.

  •  **TAXC**: belastingcode, gekoppeld aan \[tax\_code].

**3. Kosten op orderkopniveau (export\_configuration.order\_header\_charges)**

Deze sectie verwerkt aanvullende kosten die op kopniveau aan de XRechnung moeten worden toegevoegd.

\[export\_configuration.order\_header\_charges]\
name = "order\_header\_charges"

&#x20; \[export\_configuration.order\_header\_charges.fields]\
&#x20; RDTP = "2"\
&#x20; DIVI = "RFP"\
&#x20; CONO = "001"\
&#x20; NLAM = "\[\[amount]]"\
&#x20; CEID = "\[\[costing\_element]]"\
&#x20; CDSE = "\[\[charge\_sequence]]"

  •  **NLAM**: bedrag van de orderkosten.

  •  **CEID**: kostenelement dat uit specifieke XRechnung-elementen kan worden gekoppeld.

**4. Ontvangstregels (export\_configuration.receipt\_lines)**

Ontvangstregels, die de regels in de XRechnung vertegenwoordigen, worden als volgt verwerkt:

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

  •  **IVQA**: hoeveelheid, gekoppeld aan \[quantity] uit de XRechnung-regels.

  •  **ITNO**: artikelnummer, gekoppeld aan \[item\_number].

**5. Kostenregels (export\_configuration.cost\_lines)**

Kostenregels voor aanvullende kosten in de XRechnung worden als volgt gekoppeld:

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
