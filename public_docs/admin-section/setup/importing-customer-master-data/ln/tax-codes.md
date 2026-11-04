# Códigos de Imposto

## **Criar Ponto(s) de Conexão do DocBits**

Abra o ION Desk → Conectar → Pontos de Conexão

![](https://lh7-us.googleusercontent.com/QLQB17W_hywZWBqme8Wio-orbdOdFHXLv5zTd89B3EkeS0WCuuo5Pv1CndLRQ2rFUefvQYM95U2Unhrl3YU3WAR23Ij_tDw_TOEVenWjyCh-9H8CPFSezF2gmED7u5QTR7q9WV4CSXRvDqkmKJYPqAI)

Você precisará de 4 pontos de conexão para este fluxo de dados, 3 pontos de conexão de API para as diferentes categorias de código de imposto (completo, reduzido e livre) e um ponto de conexão de Aplicativo representando sua empresa LN.

&#x20;Para criar novos pontos de conexão, selecione o botão “+ADICIONAR”

![](https://lh7-us.googleusercontent.com/cECLuIswRSK3WWhUMi1n3tm2AIcrksZdpz7ZCO6-H_MzaKe9CDT0w1b7GKJ8GtT_d6nvvDe4ukLJfWcMocbHZ5dSSCw25Ky7-JUdrYb893GYYyaHL9tTjG1ZniORJPLSu1zJxL3c-1VQRw4IC0LpYuA)

Selecione “API” na parte inferior da lista de opções

![](https://lh7-us.googleusercontent.com/bpeLxdmi8b10LLMGy02vMRXuLoic9kFLywnpd6SSYV0fNv82dQahyvaA85mC1PEVScNW4m63fOw89vkhQr0-ou8VWOSjkwGWG5GnP7GQl77THtjXWP3YNo8LUzAstpCs0Q5fOjxaoT__ZKM4jciHA5I)

Você será levado para a seguinte página

![](https://lh7-us.googleusercontent.com/4pcN0B7aibjn_Qn8nMgkzRc_NiXev-c1wJudDKo2V5r0ORuajVzfzAWnWu0Wt68hKMKSLYkieUhOYChkcZuCZDWkg-F22Rq2WvVqgPweSg3by2TGrrJHweKWTlf_DK1X2pCkoNU4yoGo3DyHsoqcGjg)

Aqui é onde você irá inserir todos os detalhes do ponto de conexão do Código de Imposto. Para cada um dos três pontos de conexão que você estará criando, faça o seguinte

* Insira um Nome: TaxCodeFull, TaxCodeReduced, TaxCodeFree
* Descrição: Isso pode ser o mesmo que o Nome ou similar
* Importe uma conta de serviço que você criou.

Mude para a aba “Documentos” e selecione o ícone de MAIS para adicionar o BOD que precisamos, como abaixo

![](https://lh7-us.googleusercontent.com/byhA18LzkcY9ZyfnzyDlru5qBx88E8U1yggMNNkoHGsYVCbNkflNFXGVvJwMvE_104VCjoYOM0SQIJVniyBBdn5UKasVR0uat6UvmCmpzz9ZYsY2Wv14B4ElOwqcg2qklxYAQVU84UOG70l3fMLRrwo)

Procure pelo BOD

![](https://lh7-us.googleusercontent.com/DAKzvEsjCmk1jy7L6GwrVY2DWg3_InluNftWnR7hGlnyeBxSDW6XTDPBMLqtJuUc9Lq3Nga6-EKS4tZpOjE09h5FUJaTm_E70UdA4l17jWGQ6BSr121lC3LzhffUXi6Bsk5EZEz4XHyjekk1Njb3H4I)

Procure pelo BOD chamado “Sync.LnTaxCode”, clique nele e pressione “OK” para adicionar o BOD.

![](https://lh7-us.googleusercontent.com/7BLwrq8kr9OTHleI2anmAr2-4ChksQ0pptddwm1quFHquGfnMBEW32RFx31ETGbrxf0KGVr-VzlZC9h9heD3ymTq9L5NZEV1b9E67IIR0is18UGBCoJ5j7KIMmF533EDMvZzgi4LXqAkV9zgCyl0_Lk)

Avance para a seção ION API. Sob o Nome da Chamada de API, você pode usar o nome do BOD, Sync.LnTaxCode

Pressione o botão “SELECIONAR”

![](https://lh7-us.googleusercontent.com/7MukO6oUAzVBFMPhFepwMvugqnhDDMhX9j7wZRU7BU0OusW3CKpMgqQNC7uNlehPp6eFniVxrX3DxjgsGZ_Tmt_cQOWGGiBfXAQfCC85amOGp1VY8RGo3nPABCiwzaIkYmnQF6t3FPVZ1fPV6fLazNc)

Selecione a API que você configurou para o ambiente com o qual está trabalhando e procure pela seguinte API. Depois de selecioná-la, pressione “OK”.

![](https://lh7-us.googleusercontent.com/IpUUqJaXF0MmIeR6gtE9GDCccLfNsQLZ-RSHhQGVwJEj8WJwI-twgiHpFomBKhbnTUUKrhxJ0EUZ7F_21MCSBjNS2VQq3azprekoxctRJZ-NJUHhb4J9rHUSRDoR_OCzDHTG5q5KTwWMHOR5qNoNd38)

Em seguida, mude para a aba Corpo da Solicitação.

Aqui é onde haverá uma pequena alteração para cada ponto de conexão, isso é visto nos mapeamentos de campo que você atribuirá a cada código de imposto, pois eles diferem ligeiramente.

![](https://lh7-us.googleusercontent.com/f4c-1M9mgCci2jjxkhaCDFX9bRWzMDaRwVv4XiaUH7BpHchPklvMnWoP_ILSm6VB7GoFJNJzHsEPzk3eCFyLm1Kc3QI8OufjQ1mr7PqowjzViFDWc2opiNE1ODICtI9yEyUOi_d_hzN8CGo8gu6Ec84)

Na linha de mapeamentos de campo, sob o valor, é onde você colocará os mapeamentos de campo específicos para o ponto de conexão de código de imposto específico que você está criando (completo, reduzido ou livre). Esses mapeamentos estão disponíveis em https://docbits.com/doc/field-mappings/.

O resultado final deve parecer o mesmo ou similar à imagem acima. Depois disso, clique na opção SALVAR localizada aqui.

![](https://lh7-us.googleusercontent.com/LSYrbElw6BgQbbIdSstbakfwLENZ_09WQcQhjO7kbb2U3jSK__wFnr43tIj2hTHYegQ9lrSZBuJ9N7MNewr2W3yjPCrrVLeP9UAZjvrKKBzeY9h-q6FrVd5gPtlH0iP0GpMcvhGxjAnHN7BlY8CmT3c)
## **Configuração do Fluxo de Dados**

Acesse ION Desk → Conectar → Fluxos de Dados

![](https://lh7-us.googleusercontent.com/cpWAepQyLP8V0b-Oj7djzl21eZLU2JdnJPEMPs53Uq-adZbaCegl35RjguLx8rsP2E87ZmwbNgISFIpAy6kOeahaBCSygDVSJzmv1GQGn1w1MgR8N08mnnfhb02XjsLnt\_rVJKr4Y0UtiTf14NqTHLQ)

Clique em “+ADICIONAR” e selecione fluxo de documento

![](https://lh7-us.googleusercontent.com/HYqc\_P2DQjBoc-mpsyZ\_nlPFNiU17ZCLHfiOa282-Sa5JSA3Hv1XlwFjmlPhVGnAaEAqqalJ5ka43AJOzEO3uljwVAogAHkTVer7Q9JgI0WaOVX2Uo5Z8KGEqoa3BH\_zZwup7Bh4lKe4O5kr6hmAZm4)

Crie o seguinte fluxo de dados arrastando e soltando os componentes do menu

![](https://lh7-us.googleusercontent.com/V\_aJHPhFJssPUQ4mAHU20SVPSfhqhjU8BOQ2Ws1MtaauKp6OVAENLXod2uQe6Zbuc5JKZx6Bp3WyJtkQtkbnDluZZS5GLMGcaC9EuCrV8cn2aJk2y-Cih3PP2dg-umW0iDhak5UXNUuPxwkgqVg-mvk)

### **Aplicação (LN)**

![](https://lh7-us.googleusercontent.com/2CCNlz0S-Z8p\_l9kPPUMqPkreoO3aLy8MkqY6UFMIABJRNFXGTFMXbaw78E42g8fEO4ZxFL\_oJMf2QnWn2xZLtS4zjN8AzCS\_B2i2x-tjWmmjyVLa1jSLQAnSB8-EhNfNISzf2uuX9kcqN-QixUUXvw)

Aqui é onde você selecionará sua empresa LN, o resultado final deve ser semelhante ao seguinte

![](https://lh7-us.googleusercontent.com/b5pb4YfbZMCSi2X-xT4mj-Yw\_Uu77zNyJGl3rntVdqf907PwgX6Z9uQJIoHA2FS5M\_mVbdQgkh0HWgsOgtkoySmtrT7W8CrqsqlCnPEt6hv\_yODGulfp1qdxXvrB1HL-en3W9bY285fC3kARLZfSfck)

### **Documento**

![](https://lh7-us.googleusercontent.com/U8cqu3jABU3RQLGEGsS5qCnDkc-boTpAdZEVIUA9AlmD9Oz33JvnzD43SBTmLY55i8Bsr4lbi6udeIimCcRG1NgWbynv6OllCLaJPC50kJ0gPq7rsR5Rvj50yKngMiNvnYoLLT\_Hzn5cyhp18jq\_IyI)

Aqui é onde você adicionará o BOD Sync.LnTaxCode anteriormente, o resultado é o seguinte

![](https://lh7-us.googleusercontent.com/bgC1y3NtmX09XBjng\_pKmP5VQ5w0E\_VuFOfMF1rYs3iGGL5OaMHkKoyQJNtcVtbS6bEvF4KdtFNaX0VxT9MF0P-zTDnOnt5mhA0Gxcs4eMcRLtbXl5a\_8y84XyLyvh61-LdoQ7f15j-wE1nl\_TSYSDg)

### **Filtros**

![](https://lh7-us.googleusercontent.com/1Cv1XxqdpiNfonz6jdFgz9zGibQTRLd\_0ONFHf3FvzPB9-sQuX4lTUyuDWzm-RffuPf5jDmZAZwUqbXX-1kers1sEb9ykRMHeYYP6zGgF8yZ247Dx0nG04kSYUTTKSwt3NLS-3TwXA5tbvy5z8HA2bw)

#### **Filtro 1 (top) – Completo**

O Nome e a Descrição dependerão do ambiente que você está usando e de suas preferências.

![](https://lh7-us.googleusercontent.com/WVKWUme9uUjRRn7dZ5c\_RyPk\_GCTFEfiNxU\_H5aA979k5hOv2coDYEJHu4K1EaTLUf8\_Pd9ffOk757DaflF0Se0gZ1ZYvRk4QHlpKP0IeirfNr-L6JU3Z\_xFZJ2eeFI-Rhcctwk9QOHRORGNt1oIEpE)

![](https://lh7-us.googleusercontent.com/1gCPbUtC7KknzEHVZqIMKyjQGmNyNnR4c1mJ5x0LCJnAjd8D3SdW3W6nPMTsLokL-W2-XjoSM9MU1mJ77K12g887r\_jHoHBwquN1Ore2AmyjCaf\_YVT78KiKtY\_itlr-vyMvJrU7YV6ErgVSYbw5SEU)

![](https://lh7-us.googleusercontent.com/ijzGaLt9Uhzw6Wf66ah3auWo5TbkCnM-xGDYezsXXjPEkdCe5RO1wWfhhhG0qRuKbojijLKUm-WUV21eRdq36moWu9Ft0ujexe\_1lTUUEQbfXPvtrzP7iudkSaG\_oiX\_LV7AqZRGlNAp0OXnN8BXRIM)

#### **Filtro 2 (meio) – Reduzido**

O Nome e a Descrição dependerão do ambiente que você está usando e de suas preferências.

![](https://lh7-us.googleusercontent.com/pKLo6q5zCQOZQhiRppyd8M-nlIrX5leGUiCct4Xn-4teIZTip5GAJVP0EFc2PrJ6EeDmU2KVOHRKVCaaML4sK8jCnsgTmxbTYjc-9CNd6bOfU-WD9tySeKL7gSRltjzoTEI5Ozrd\_s-7qj2KVNOWN7s)

![](https://lh7-us.googleusercontent.com/87PoQQ5q\_35buL\_VNcvz3v-um1upk1U579LDASCJptnnC8ip5mwXxz89d1YmtIK59dOUhl9dfz6BrXBLSNUy6EnWU5uPmUEzbLQv-MwzR0dDkuM1BJ477yre-X4QeJzkkzprF9y5wCWY4zvaooMwIZ0)

![](https://lh7-us.googleusercontent.com/Pa19AN6Mhxbn6bHSc5qKEGM0xRsEV6v77ooyeg5-91i8qGhaThb4328nr\_g6a\_z-7BOCJmWpo8Gbd2twl9FQkOf1Q8QZqOkJmxsIxaTP0R6dASgZdIV6z7p8PFYPYUJ1eKp8btYOBapliANstQSUgAQ)
#### **Filtro 3 (inferior) - Gratuito**

O Nome e a Descrição dependerão do ambiente que você está usando e de suas preferências.

![](https://lh7-us.googleusercontent.com/c_SuWaZ3gF-FbOPWkxB_eFgkT-TGJEYwV_fQT05wGWHFNzI9SDZRQfauVMeBl0rn79QdU-W3kRgN-hWsYkfdMSevlYyiNPxxT_3RxXcETo-lkjvI5TCygUag91PFJycrRdMA5hSQJCuzt8FekMwpu98)

![](https://lh7-us.googleusercontent.com/HGZ8fR6XgYtZ46i8Rov8xIr5J4z8DmGFfJkeovDGzT7S68VYI-OdG5jpMdoOiROIZckYMbVIlPQmS_kWQazJVbco1t4ZH5Sr73b4xePlisnbm9ZLJrOPwtXn7-90F1FcFH99P6ZKI0hCWdI6z4d7qNA)

![](https://lh7-us.googleusercontent.com/_APmMO6A2AG2km4H4em-ZMrn6_XRpO3zxRhZwftiaKi5uoDhv3TTzCBfi8WVDCf6mOQNgtcEJ-z-BmP28J86noGJ5dgqVni2QIxePaO5-LU8fdwRqySUQt_6wmFWiOFzTMmItcClQPRaSKUaosgWwNk)

### **APIs**

![](https://lh7-us.googleusercontent.com/XDhVCKHYaxrRIFyYfq0guXwnZH6jK-WZIFj2i0Wkr4kxyNcdCH1TzKd0Pb3-H6qs-b7JZ3UUIGm0BVHiUL7Aya-D7YOSV8p8tnwQeAfBN30T4fW5-ANePN1TcvUr1gzLJPwj7rRO4Hw4ziuyYrqZBX8)

Aqui é onde você seleciona os pontos de conexão da API que você criou anteriormente, isso é feito selecionando a API no menu suspenso "Selecionar Conector de API ION".

#### **API 1 (superior) - Completo**

O Nome e a Descrição dependerão do ambiente que você está usando e de suas preferências.

![](https://lh7-us.googleusercontent.com/90c2E47fMC9CKNVY8DtgyaNUAqAnQmfErZm_R-njUlEdIX6mafMUOk3GcAooaWfCzD4-OmdPUq5VSuMXmTSNjVEc924ASIPqmTxAQXqsq6eKs5y82rvwHxqnsT4S-sEm2mQRNwleiubkwIO_kS9Vwzg)

#### **API 2 (meio) - Reduzido**

O Nome e a Descrição dependerão do ambiente que você está usando e de suas preferências.

![](https://lh7-us.googleusercontent.com/vw1hM3W4eCt_8OG7Ht203tckaWarPOLi463WvQzGgixTMnfk7iC27JzL3iNgd5LmvBzWTFnYa3QNy5y_oNSHJ9R-Ck5CAgLoBmGurbCn1RZ32jiSJr-LUnL3b0nhHctBqcCx_25L1Ce-_va3ZgfKXY8)

#### **API 3 (inferior) - Gratuito**

O Nome e a Descrição dependerão do ambiente que você está usando e de suas preferências.

![](https://lh7-us.googleusercontent.com/C0wmqAkrlgyXlMjKsGMOqre4MPLuHawrZB1oYDzkGFocperUB5dKea7kx44hrA_Kz6Ptx495cQbwq_EHfEGNvvpr_0dvCuUS2zz0-SARyuNbf2gKsK3vTdd4Sfg3jWtE1YAN3o0VpoK_HRn7T-fFOR8)

Depois de concluído o acima, SALVE e ATIVE o fluxo de dados pressionando os seguintes botões

![](https://lh7-us.googleusercontent.com/f8gkYY1Z_W1if2h1es9vbjebtDX0zGiqY4p9OD68gKSAcNU6si-guvyIg8hzdjP7TulZ6Yq8NcbT2EyuHleVeNxpY_6TDlbgIUaxDJ72ILcy8kVvFuSja7FT6gpYhMLFGw7wv-r0XyFN8xIrQ3OuUGI)

## **Desencadeamento BOD (LN)**

Abra LN no Infor

![](https://lh7-us.googleusercontent.com/aAKRLInqsogQLv9nye2rHLtVFlW4yaCpnQ8A4cKG5A2145Tl6poOxthfo2InYimNk5dd8RabYrX9xP7sPO0aJ5ThF07ZVfKvUXBqVoxRJg53IhpeOeiA4B_CGOpeLKWlPbCf4EaFXjgzmBOcezocF9k)

Navegue até Comum → Mensagens BOD → Publicar BODs → Publicar Dados Mestres Financeiros

![](https://lh7-us.googleusercontent.com/pMAgPzyhBNrEsFkTm8-iniHBhEXIPswoJ8URt_v0fv_7dSayrS8UkN7F9WMAOZQB9Q6sCe9faRl4rRDDft3VdrzfNUT-IbWxE6GyWPPKZh4R67JRmXmJ2NsTVPdjLo6uJdCpki7QDpgiY_azWtqaqKA)

Selecione MAIS e clique em LnTaxCode

![](https://lh7-us.googleusercontent.com/MtjE7Glgv7e_F_CJ4LXMuWk6SaInmNFlKzhGJu71iGgxRWtjI96lX5J0gqxRcj3y1u4E6Aq-xNEpuf83dsjH6op0qeH89oBMvlVTTD_VhGs10-gjuIb0eyc9b3dcCk75Wa5sASreXKW6SbQPYrs8sM)

Marque a caixa de seleção para selecionar os BODs LnTaxCode

![](https://lh7-us.googleusercontent.com/VTFntcBK0GVsUdr_fZBUaN8rXYdufObLE7PnwwNg9QU69zYwKHvwFZ7En9WZ6p_WGIkVdqEjBBYeIYSuHHJWBWYonwd6Edtr0ZZuGsX3qhNMDWQWefOaGfrYxrq_yLm6_gEw967PGp3HK0hzO-G2XiQ)

Navegue de volta para a aba OPÇÕES, sua configuração deve parecer como segue

![](https://lh7-us.googleusercontent.com/2tr7VHNOLActJCiLGC6jyWsdyqwZV7Je6UsekeoBo57qNpOBDYtOQuoelKOdvLMRo6uQJWn1S4ir_zRZHAx2C96NyKp4ZjIUyFCYt58T59TqO3ml0ZfiEtSLwdRPp9g8pkMemN0xDS5ao8DL5xgosWE)

Quando desejar publicar os BODs, selecione PROCESSAR.

O resultado final deve lhe fornecer uma tabela semelhante em seu ambiente DocBits.

![](https://lh7-us.googleusercontent.com/4wK-mfKl0UNqvp5ngolE54miiwAKxAcOERO2mSDWzZ5t838VhFZrZGzCMeIyg7WDPpHvNzkeWRJV7ZZdsaxwXiFS9uxm29QZUYHhs9gU2v6QgSz07vfjpHXW3oTb5ZiiiTjI93gmV9MDTHbNWJmrvHY)
