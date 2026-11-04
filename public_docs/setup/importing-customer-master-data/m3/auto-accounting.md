# Auto Accounting

## **Prerequisites**

* Functioning M3 to DocBits dataflow
* Correctly configured DocBits environment

## **Infor Configuration**

In Infor, open the ION Desk application. In the left tab, go to Connect → Connection Points

![](https://lh7-us.googleusercontent.com/Gl49rTfnpYQjXjpUNF3SEouZiJ4pPeHVk60d7dyHizfPLT6sn4AoKVQPPvpgg2cD4ts40hDeWQRs3BqmKW-CAco7Dt0oWKF7ukQJUVDBgSUoMNHt_gRkqLxkF5CC_CNGpVRzrNs7rfF1msK320_J02g)

This is where you will create the connection point needed to import your data from M3 that is required for Auto Accounting.

Click on “+ADD” to create a new connection point, select the API option like below

![](https://lh7-us.googleusercontent.com/ctE76pck6mGmBVxRIMhHyn0TbSKKsiGjO7rO185fjndTIo7qYyvSZS3neUdV2CWPqBSangpJ4oG_g946_KyOwWyJvacZe5htWiQLTZQLzfNHvsHDhmMQmjh7MrGsqKp6sm-XPcGmEwrH2ZMYCd0bUl8)

You will need to configure the API connection point called:

* ChartOfAccounts

### **ChartOfAccounts**

The connection tab for your ChartOfAccounts connection point should look similar to what is illustrated below. Give the connection point an appropriate name and description, as well as import the Service Account you created.

![](https://lh7-us.googleusercontent.com/p-jly6_S96TsCmpFg9oOob0h7Q7NBlTxRKgNCphiy5QfbK_lrLMAR2miVUQh-fXrCfGdZr17ongp5c9bnK6HuHCVuDArHhYcmKDlAyO52tGcxg-VXBLXZ1ka8yqZ4DWnxFFMxUKkE7jgvCgr7P-nzdU)

![](https://lh7-us.googleusercontent.com/GkX20Q23htKae7OOcGnJ5J6f0L4I69vOU9jYBpY1m9bpDPdtsD584mh_9IaZF37Ne1OY2uOPgFxYYjwTrBOoZqahpJLlY3n3qmBn0sgzC0eVu91wE0NWBvESBFJmeVTITQoqUTEU56tHEj47-LQmI6E)

You will need to add two BODs in this section for this connection point. These being Sync.ChartOfAccounts and Sync.CodeDefinition, to add these BODs do the following:

#### **Sync.ChartOfAccounts**

* Click on the PLUS (+) icon

![](https://lh7-us.googleusercontent.com/hFWg7-4Osuy9Q0uZYqT9yfAPFYsBi7yitHj7BBxQ94vbsDVg-GuCeTBakvV2eQNjqMGwDAF90nO5h-OxFR8HtYEiYcALdBq5Fdj_Gl-wU8QePGV4Wr3_78OK22nUY35dfCQhUPQIp_qkdHN0wr7V-VY)

* Select “Send to API”

![](https://lh7-us.googleusercontent.com/jA97YupOjXJlRFRxduo_tYO4YYDZoT0mHxWaPWfJGyU4RTNSVNRAIAsR5mzRyLh1iusHl0cBKUxhYj3hQMzacGdN2QGsvPGy1vHeq_JNhDqxc-SI5HtZh_Z_zmaSjyJwmr2337tzYSWfqDl3JGkjBqY)

* Search for the Sync.ChartOfAccounts BOD

![](https://lh7-us.googleusercontent.com/hzuwy-VU8xpgQ85NGHAk9u-m-_Sw4iffT0SNtWTJw9iWHRIsIvGTEYQgJYi7CUoYC7_Yp2KDtsohRQkNtIgr1VutFbR8mTkT_5HmJ7ecgW8pcGuZTuwxtPDOlJpWuONq3WPIupRRBxBJPlsYQ9w-bxo)

![](https://lh7-us.googleusercontent.com/6p8nXaRAI0ucRzmyKfYYg3J8MmHXVgHs-KxcItxeZ6wbefK1YdMrYSblHwnXkSiajApB5ds_EgpJJWYjfbKOjHdsh-H49jG45weOX9v0YBSAqdXmKgoaBcP7A4zDyINMNVt7RWgbQ51WxNTsfBllvQ4)

* Switch to the ION API tab, copy the API name and search for the API Call by pressing the SELECT button

![](https://lh7-us.googleusercontent.com/aRXjuD3nkYsFNM2eYkfmHrshU3ycmN5G4OGSFFadbSToy3pHKYWMw6apbyMhJ9o-5xB6UDA4rbdPjZWAdP-OCH8gQFWV5vWXp0rqLxP9DozP4yMS074_nsHzirJUgBfkBkQ8Ydp_WjImf2bx3pDnLPE)

* At product, select the API Endpoint that you created for the environment you are working with, which you created in ION API. Search for the following API call, select the API call and press OK.

![](https://lh7-us.googleusercontent.com/LQWk7uiEPCxJcohMmIuRrg2p_wwE_h5GoEEP3Y2IdpKARppHoGB4Rt1KRM_2AiXyG0-ieIV7BM51IRN5exKkhG8eLTkKCftm88j2NLc15X50VLu9t1sZZnQ7DsIIvgUsxz7oryzVIkfmifw-m3qkLDY)

* Next, switch the Request Body tab

![](https://lh7-us.googleusercontent.com/0tnYxKvtW5Fw7yJfW0QBMclidw5kKJB4oi6M932hGO8ROokbMXbyFcjPQq_LSVe8hv3ZyVVWqjDO4vMMRgPm1L2iXV3pSoiyzrxGLvBTx4kwt5uo6XtHEt25PRVdM6aIddhHDrT7HGzx3JaZ1F02-YI)

* Here is where you will configure the field mapping for this BOD, your configuration should look like the following. The field mappings are available here.

![](https://lh7-us.googleusercontent.com/3giuZYeQjdZZHAg7W-pcAHB_69KP8Ukh_0NhATYBxvrS_Qy3yH58fQyrp6GKfOzi1xJms5KV-XVNnAWtX6VmIBwdxSVum9JA6-H9W3XIUYKiTEK3IWoKA560a5I2lwmYd0kitdfC4pRkQVULyWp9PpA)

Once you have completed the above steps, you will have successfully configured the Sync.ChartOfAccounts BOD. Click on the PLUS icon to add the next and final BOD.

#### **Sync.CodeDefinition**

The connection tab for your CodeDefinition connection point should look similar to what is illustrated below. Give the connection point an appropriate name and description, as well as import the Service Account you created.

* Select “Send to API”

![](https://lh7-us.googleusercontent.com/YLaFsc0K1Lzruo84Np3EdCTF1xsaQOLRypNpgZB7L9keTh1TwPOMnjBxJYnBOj8GrNSG_URcRGgv_p70-pjhBed-wvURRW08YtEWjmACMc3CleRPrHia6nihWQwVOUaZ3qHD_zLy2W_iMQ0I77cY_Bs)

* Search for the Sync.CodeDefinition BOD

![](https://lh7-us.googleusercontent.com/f3ikl4jh0PBhYmP3r80BrHuGGu9w9MHe-E0VmyXOCmFEkkK92cxgVimwyP8RF0kF2GruVaeDjiYRKuONX5bQ2ZBRmdKFx8Bf9cHvX5q-xYnXNH0a2xnR4eg1ynyWbRRRoY5xn28HJ_ziRiKcTN43aHQ)

![](https://lh7-us.googleusercontent.com/nXQZ1LLZsrndggHkAmRtMlV7YzFemnjC9CnS4AdUVDits4zNfzlaqKdHnNcLyTtDkQSX3SB8R3fnZhGBPd-By8C364IIYc4vE2VXNXzoa4LfHP6irTiAg_N_2BHSYBLzaQyMCN1w5LdFiiqeiiwAXuk)

* Switch to the ION API tab, copy the API name and search for the API Call by pressing the SELECT button

![](https://lh7-us.googleusercontent.com/LbHmVr1PimQkPu-t6VMvNVk9wVXeQBHOu-X4pW-9vGm-dON2buizVGbKekGL7tY1t4OkwQtzhl7uDhq908UxCfDCJaRDEukpk-07pJjLO-ezRUHgblp3REm0qrKF9wOtMkNWJlVVNVhmfzZ0TtUsqQQ)

![](https://lh7-us.googleusercontent.com/K-kDDTSaZiothC4o3JDihhVJFNt0PiBnLK7kF6RcBOX9EpzutfLHGstzvywBBqaEqm4WqOSQSxtvxRPtbVafPlhtf_YMVkXjhTkvnGwLzwH_p-YgRCGAu-DzA94MHjqQoAYTSBPgojcGlJs7tBRcpME)

* Next, switch the Request Body tab

![](https://lh7-us.googleusercontent.com/DfT6FtrbW7LbK4b4I6ssYDWOaPgUxkWsuTDpvQGw549tPFxgEU_gmh3UwXTbyKHZR8SOHXPHDdobEhA91RIMB57ZAVatrZEsad2QW6QHiUkdZoyW_yE_iIGDgs2IrY0I6qL1JTZxksYoaLKu0Il8smU)

* Here is where you will configure the field mapping for this BOD, your configuration should look like the following. The field mappings are available here.

![](https://lh7-us.googleusercontent.com/nqK7x1Km4wIP9aWnvMlSHl1_omw22GRKONfB-zc8ikn_rSsl60Ksml0oQacs8UNmPSLFSKPD7Eo9FsH42RjDo4oragvHZJHFW_yv62KXDrF3SKnDN2-X6vqYJ5a-3bYkkvPDlNJSxFylvtAFr-2Kt8Y)

Once you have completed the above steps, you will have successfully configured the Sync.CodeDefinition BOD for the M3FlexDimensions master data table.

## **Data Flow**

You will need to configure the following data flow for Auto Accounting:

* ChartOfAccounts

### **ChartOfAccounts**

An overview of this data flow looks as shown below (the amount of DocBits API connection points at the end depends on the amount of different environments you are configuring).

![](https://lh7-us.googleusercontent.com/RfkP8xiF2vDzQhBNa66L0NQHk7TGjj52aK3hWoisEnWbdG3l-SZKKw8mYJ3b28ShXZ9omPS6WdNiXaCpYRQzwfges0SKznwQal7K2ElILbGBJNYu3VFm6gDQJMHYRItAFX0cdRZjXgCk2FQqHJ4iSjY)

### **M3 Company**

![](https://lh7-us.googleusercontent.com/tqYoI-gLUpe0c0x1T-WhP0_FolVzPGHhFY8m52Fw38mJNzsDvjb7stRrBfWVjXLnFrJTTy2lyd9Dmva3_EPG5eRWyf5ATA2cTWvCj3Ksa4Fu4pHF6rNFjfd3Cjei0UlibT0HAQYE0V22bdTStjY61zk)

The configuration for this connection point depends on the M3 company which contains the master data you wish to import into DocBits, yours should look similar to what is shown below.

![](https://lh7-us.googleusercontent.com/wpSluEs21T5wXG0egZPfUCYBP6X_uUm6XAh-PyD8RrojTuIztzRJzhVYdzcNI5dQGGDsrhSKx_K2-y0JDmK9w41fVUXWcW1N2lz5rizXcMnn5BuiaGRy-TEOBryGxvP9mBGJTZ16lMisoC_YumwpS9Q)

### **Documents**

![](https://lh7-us.googleusercontent.com/uR6XaFI7TPQ4L8Suom25PBdtXdL4i100Juz7kRBxT5rdxhejZW7nPtVIlEGjWWnZLbo9ipx7G95NBFV8dd-g4vw_vM-uPApJ02QdxvCmX27bwAW_qUWUXajV6BFVmIfzTQ46Zj4DybsYKKblXjuWc6w)

The following documents need to be added to the data flow:

* Sync.ChartOfAccounts
* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/6Bq-yQ9Yaf2OJwjBxyFvqAMUitcovquo_iU4hc-pgag1iDwLcstggVjLsdY3bRl9XWNc3mKOwZrY1FSlu47IzxxUQHFkjIAl1r08Iw9UbKaaMh4WiWrqFuSObdTjEvCEI5IDvD_Pys8jAydydJgbsK8)

### **Filter**

![](https://lh7-us.googleusercontent.com/LyKGzQUEswTD1XfpNDPSHjChgqNFfs4guXfM0KNuW2fPoiaeUo4uPrlGgwt3RepWUGQmu_trUMiWb68cUjUAwXU9IRoWOsv9M2l5v4zFfBkEcioz5ok7Eoss7I-tBKtpD7wVUkGWi3U3ySrIQ_fDPiY)

For the second route of the dataflow (according to the routing in the data flow), we apply a filter with the following configuration.

![](https://lh7-us.googleusercontent.com/7xdqGdo9bS6_IIzTVYF_08woBXvhIVkA-c6-ZrDpDEzmEDFzDZSuxZ5LYHKVUhJqYq4Wlq1FXPfr5myjKFUsMbnJrefc_L7URD7AbEq_D90jEw7o8Yrhg5XZwLdU83OwlZVXqlYla61b0LyISXeBLWk)

![](https://lh7-us.googleusercontent.com/OdI-0FaqDaPKy2g9Mr8HUx_oGRZkDrkeI6P1rWqOounpDauMThaqzs2wOawmw3RwcMlQHgI6wj16RXQDAP_JNMGkxvmiEnPJ_bvse2CvMegPwinSIJRLmXaCzfjxtB1FDqnqPOMwrMYNKJyiC2sGUe8)

![](https://lh7-us.googleusercontent.com/RMPIV6ZWsUcBA6klny6Ln-_nhMGl1zdEHfUKK56owelabcG-6gM1S_eqWAVLTeOHdec3D5D6xVJeC5evnJC61L8daV6IbJbCmMashkWXSK4Tv4RdE_erjR-Mk2RihPodIG4HrqSOQ8hi7SG3xctXd-E)

### **DocBits (ChartOfAccounts)**

![](https://lh7-us.googleusercontent.com/Npm92rS_EO5roSy3tldC88hFIyiDnZjHnnVSkkKyfmNrOcbuVj4LPNrcsWvOT8IHNQKGMqIZymG9q3VMGG6RwvuRBqZgmhHxqXn1oieajDmz8giQxSr8wOFzb8TQTJJWwj912-sDRtkrDAXCr7ne-pk)

This is where you add the ChartOfAccounts API connection point which you created earlier, the configuration for this should look similar to this

![](https://lh7-us.googleusercontent.com/Dw4y6OMuMAYHZjH1etj_FqdsaFxaRhQyk6_PaxXrWLhrNirEn7xQc5uIpbDT6Wz85XvZgY02aNuWfbYKBzo6W9aavN_Asu5ENfr2dszWYQqs9sy6zl4o0NxRe3IPXodLIGf9JkbK2_UtYe4dVii0JbM)

## **BOD Triggering**

Once all the above is completed, you will need to navigate to Infor M3 and trigger the BODs in order for the various master data you need for Auto Accounting to arrive in DocBits.

Start by pressing Command + r, to open the prompt menu, type “evs006” and press enter.

![](https://lh7-us.googleusercontent.com/pzAL0cnM94AUE4KmTyBV8OPU9ft_g9o0-KB9Ib0AjrvG7Q59GHT-2biP4n7yFyXRxQ0gjy85G6MWMWUeMIWJcTQ9TKwzCEywd7I_6_vV-muepobkW0O-4-CZxsmjOEQ7uM1frZpTLqlLS3aSYkEuwAw)

The following menu will be displayed to you

![](https://lh7-us.googleusercontent.com/Wx41TNpg1zuaf1rXIBvSCVzSRf6q74rdLs91el21iErqQnDiF4cv7X0nyDaS2Gjimj7xbfAK-7mo6sXN6fkK934mHnCnivFTz9NqHi6dBoMYiRT_vLrkVUlFd_T4Oan3Zkq3WKLoI-kmsElHSKO7zY0)

To add the various BODs you will need to enter the BOD nouns and Table names for each BOD individually.

![](https://lh7-us.googleusercontent.com/5gVWRDm_8CSyoQRkq-7LuI8MLU1BjRN6Z6YCcVZp7G3Be62nQBht-eUNZreTzV2rFWYK_RcKiyzwTTlT5y5X8eGf-Z7qDavDyHML0zv6Yt6jGu2z9d-nL0K-m446nDZa2-aiFLnnzjAwk8pTT4RQK6Q)

The BODs you need to add include:

* ChartOfAccounts
* CodeDefinition
* CodeDefinitionAccountingDimension

To add the new BOD after, after entering the BOD Noun and Table Name, press the pLUS icon indicated below

![](https://lh7-us.googleusercontent.com/66wclj8g8RAYT9-UIgRMs0qnuA9srmWv21PdqdNm_q5icGmabL17-DpLOSs4pm6Nj3xJN-9xt7io_5GZGfzSQ2qt_8Y--CJFou6FaOdufiuxOdKHrUUYELNdGy9e-gnWg_hAMSfs_NJa6zYBMpoyTVs)

The BOD nouns and Table names are as follows.

**ChartOfAccounts**

* BOD Noun: ChartOfAccounts
* Table Name: FCHACC

**CodeDefinition**

* BOD Noun: CodeDefinitionAccountingDimension
* Table Name: FCHACC

### **Publish BODs**

After adding each BOD, right click on the BOD you added, select Related and then Run.

![](https://lh7-us.googleusercontent.com/225-ujyGzG_RJOXgbx8NOh_4s-Sn_o80b_h0DTsJqfr6OcyPUwkWLF2lfEyzFFFKddKmlWd32bb94qeYlOdVBTI8RL0r6ZfZKloVTrAYLNp-U5gL3aJhW4d72ExkkyM4AydLczsPvdE1cRDfGNKupdA)

You will be taken to this screen.

Change BOD Verb to “sync” and press NEXT.

![](https://lh7-us.googleusercontent.com/3DyjXUSlAF7msQT1OAO3aCr1U9R68XZj0oE_yJwsBrBj-FkiZR-oRYQYSClHG0iN0FXFdDdKQA1hOBlw3jc-lXQCWkiDFa0IweuQnoR8k-Mgyp1HeI5ImJqNogz-Q3b3P33ywb0B2o1pZ-TkZ7mAwZA)

Once you press NEXT, you will get a notification indicating that the BOD publishing process has begun.

### **CostingElement**

In order to import the m3costingelement table into DocBits, you need to do the following.

From the M3 Homepage, type Command + r and search the “PPS280” prompt.

Select any of the lines displayed to you. On the next menu, select TOOLS and “Export to Excel”

![](https://lh7-us.googleusercontent.com/I8SYWm-JwpyYRHFUp2obGtXcsa7m_blJ_lTrnhczztRIXIN5gfxCt3eRw6ZI42fH6AwnsKyv4ux5-rhaT505PsyDFFI_anUNvmACFyx_ssgxaqWq25vLt_E5s310HNoiPPLf35qJlYtstjpj5Cc4aB4)

Select “Export all Rows” and then press EXPORT.

![](https://lh7-us.googleusercontent.com/wtjHI9L4YUhf-yJFjcPGu218Vis_zELtCIfpmkIUKgasfrdfNW-dr_J1DqXlfD-SBrnVduDrMLAIAQh6UTlzBqEP_JPXP48elGMyGj0ByZbX7TpqlnIfRZ4ZoD0pyCo-AKigeKjlHN6cFcdpeClZ9L4)

Once downloaded, you will need to alter the excel file before converting it into a CSV file.

You will need to open the excel file, it will look similar to what is shown below.

![](https://lh7-us.googleusercontent.com/l4WbidK-5zSEQ6rwqhknudPBmmDji0f1WwTh-kHomSkgEOA7s4m72cLw8z-4nflqBvPp_2AajIEZDZz4dRLs8jlAeYHp4ee2tDysxYy8YBjj4ktHxdUXpxO_Z34c8_f0cNMX-9lp0lT5wOZoH1QUCgE)

From this excel sheet you only need the first 2 columns, alter the excel sheet so that the end result looks as follows.

![](https://lh7-us.googleusercontent.com/QaNRlKHrU6kZWFqmwYR8C__nLVOeqowAxJlvooSVBIAF5ayx2xZtUppsn0jzBcJVi90vemM3tZMZOjn549N3RzMuWuE3w911WLVS5NMuiUmnfXM_xUXbqmzBtiQZstnpEYj1dUSbs_IkAydlhBfdmcc)

Once this is done, save the file as a CSV.

Once you have your CSV file, go to the following webpage. This depends on which environment you are using:

* Prod: http://api.docbits.com/
* Sandbox: http://sandbox.api.docbits.com/
* Stage: http://stage.api.docbits.com/
* Demo: http://demo.api.docbits.com/
* Dev: http://dev.api.docbits.com/

Here you will manually upload the CostingElement table via an API. Click on the Authorise button.

![](https://lh7-us.googleusercontent.com/tyzOq3BR2QqTguQFKicxo0dE5j5hGsP-BhfVbS81O_mxN5bSVp40jYfgsVJcE_rBLFMDJNvbPkPIdjPqaqoNbHBBM-9hx0i-U4VAH9ISBYhpwKgqQeUEd67VV1E4izwNyxbAwwrhCmrAo1uIKhLherY)

Here you will need to insert the API Key from your DocBits environment. This is located in Settings under Integration.

![](https://lh7-us.googleusercontent.com/4ADnevq6kq_vbxUJpyPbHNcGvRvpO-l9Gwd8ZaYf_vO4uWhSl1jmKNpddmHGc9ZHMMbXCgLOElLDYbNwB3INmBDETecPrDnpI601IUOZQlT7tc7OLSPXwkooOJFNwML2i_gvBPuE8CvfwRpX-ZIlb_g)

Once complete, search for the API called master\_data\_lookup/import\_data and fill in the required information. Once complete, click EXECUTE to trigger the API.

![](https://lh7-us.googleusercontent.com/8UD4FhFv2dRB4cMjCDL4G9ndjH7laVMKWqdeMaJGgEo48-UVvucB1uOydzNdfFy0yPM5bb66mZB4k9uJR7TTiEREGFaV2EqW01gxJpTyuUfGNh5QmBjySkyhZ56gWV8sYs8WI5RnHcENtXgjTU0vg0Q)

If done correctly, the M3CostingElement table should now be in your DocBits environment. Auto Accounting for M3 has now been configured for your environment.
