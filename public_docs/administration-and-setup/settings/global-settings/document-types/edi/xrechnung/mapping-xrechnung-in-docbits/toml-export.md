# TOML 导出

**XRechnung 在 DocBits 中的映射方式**

**1. 标题配置 (export\_configuration.header)**

XRechnung 中的标题部分映射到 DocBits 中的字段如下：

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

  •  **SUNO**：供应商 ID，映射自 XRechnung 中的 \[supplier\_id]。

  •  **IVDT**：发票日期，映射到 \[invoice\_date]。

  •  **SINO**：发票编号，映射到 \[invoice\_id]。

  •  **总金额**、**货币**和**付款条件**等其他字段，也会以类似方式从 XRechnung 映射到 DocBits 字段。

**2. 税行 (export\_configuration.tax\_lines)**

税务相关信息使用以下配置进行映射：

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

  •  **GEOC**：地理代码，映射自 XRechnung 中对应的 \[geo\_code]。

  •  **TAXC**：税码，映射到 \[tax\_code]。

**3. 订单标题费用 (export\_configuration.order\_header\_charges)**

此部分用于处理需要添加到 XRechnung 标题级别的额外费用。

\[export\_configuration.order\_header\_charges]\
name = "order\_header\_charges"

&#x20; \[export\_configuration.order\_header\_charges.fields]\
&#x20; RDTP = "2"\
&#x20; DIVI = "RFP"\
&#x20; CONO = "001"\
&#x20; NLAM = "\[\[amount]]"\
&#x20; CEID = "\[\[costing\_element]]"\
&#x20; CDSE = "\[\[charge\_sequence]]"

  •  **NLAM**：订单费用金额。

  •  **CEID**：成本要素，可映射自特定的 XRechnung 元素。

**4. 收货行 (export\_configuration.receipt\_lines)**

收货行表示 XRechnung 中的行项目，处理方式如下：

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

  •  **IVQA**：数量，映射自 XRechnung 行项目中的 \[quantity]。

  •  **ITNO**：物料编号，映射到 \[item\_number]。

**5. 成本行 (export\_configuration.cost\_lines)**

XRechnung 中用于处理额外成本的成本行，按以下方式映射：

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
