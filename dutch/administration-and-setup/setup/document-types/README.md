# Document Types

If a customer requires a new document type or additional fields to be added to an existing document type layout, this section will go through all the information required to do so.

In DocBits you will find the SETTINGS menu in the upper bar on the DASHBOARD.

![](https://lh7-us.googleusercontent.com/ZIJTRkBGeJ29Iw8XSbZKJ3GQifWbtWFYPhSg7v4LjCKWJ-szz7R7nlcbiom5ZB25p201BCnqoaaCsKH3UKQfqaAQlpgf4MCe1joA8OLV8dZ6r6v4-skFkGlUw8U51jwPeGqi59GPQMgpMaLGZGwnCk4)

If you are logged in to DocBits as an admin, you will find all fields of a document that can be extracted under the respective document type.

Open the menu for Document Types.

![](https://lh7-us.googleusercontent.com/fqNQTnQSPJ19w3YBOf6-E_sLmKo3LPBeGyRE0jqjhodZjtGxyi7YCg0yrMVfz1VQjsbyQ9S6Lllhn891A8yWD7YJ66pXJ_EsBlf_meTFf57snc3r5Ko88kmzgXUYA7DIzaPtxSJBNC3Z7Avh17l_1fo)

In the following overview you will find all standard document types available for you

![](https://lh7-us.googleusercontent.com/Syml6WLOpBNjz1NUcYv6ooJZXhqBKXYOUfWah2jdnTAceLTNr0RYYNW8mXM91wutSH7BAnQ7MVxcNaQE7mDiWtR6xlwVzz45hYzotHEEOPSzoTSFwzno9zrJe8dVCuTHiTftm7HpcSxj9YgcRXR65q0)

**Activate/Extraction Type**

To the right of each document type, you will see Activate and Extraction Type sliders.

Activate: This document type is active in your DocBits environment.

Extraction Type: This slider allows you to enable or disable a set of predefined rules for the document type when it is processed by DocBits. By selecting the gear icon to the right of the slider, the following menu will appear.

![](https://lh7-us.googleusercontent.com/VAf5NNfmfs_EsV3-LzQmif4Vp_hSjhWOgoehrzHya-8eXgeWSRz6tArWNtQZW4SPkelwufuXFkSl5jGywDnxh5Ll5BYLSXrTmUYi2AxBOj38suzgoJiLSqX2ENYJHpGbpkt1kUX7vcATShHfG0Jw20s)

To see which fields can be extracted, for example from an invoice, click on FIELDS for this document type.

![](https://lh7-us.googleusercontent.com/DRJV3CLSSHjjFrqQD0LtzvMRu4n-_RZ_w5d-2d9q7MsZur-2_cj-_9VYjeOCmDIZ6_C_dZKDonfyFUip8NCqeXEkw5gch0MaK2u-5_kCGg6_zNMhYj2gW-JUXoQORzoJdUmKwa7PuMz_mnF3FuzkXDc)

**Field Settings**

Here you will find all the fields that can be extracted

![](https://lh7-us.googleusercontent.com/NRhL2RPgVJqbdxoKnnEtcB8D1yYXfHqifMFttmiju6OQkMKdrndsZ17EFhYEOh5bJg2ctOPyzy60CwqKme0RQbDmKWhq3EBTuqGDzDzNdcx1PPMkC4a-N1yJFmbs-ZcM3kfFt_j9Z3QdofcuXJqTN7U)

You can also CREATE FIELDS like freight, postage or any field with an amount you want to extract from your invoices.

For each field you can check the boxes if they are:

* REQUIRED: Here you can define if the field must contain a value to continue.
* READ ONLY: Here you can define if a field can only be displayed but not edited.
* HIDDEN: Here you can define whether a field should be hidden or displayed in the extraction view.
* FORCE VALIDATION: Here you can define whether a field must always be validated manually, even if it has been read 100% by DocBits.
* OCR and MATCH SCORE: Setting as described below, per field.
* FORMULA: Creation of a formula per field.

![](https://lh7-us.googleusercontent.com/rbyXMCvWQx10lEGKb4xzu7eM6-l2yNZ3SO9Mj4pIIqfAZzt68on8j1KpSnrisMgVgKKB3QhymZNDpxYEVMVQplEsesk1gWAEAeriPDaQxL5v4eWPd9oFnyYN5QiA5uymT4ED6JHEew5FAlC_bgU9Mho)

If all settings are made and should be saved, please confirm this with the SAVE SETTINGS button at the bottom of the page, otherwise the settings will not be applied.

![](https://lh7-us.googleusercontent.com/4nXll-tHCDUUbA_hsi_RXa7ll7qxkNFk2Htjx56-rBnIrZGu3H_VJtjjtuUlXGBFUQUcXAa8WdJXFdWZN6geHCWsUnq0MUF1Q8_RvpdpqYDq_rNoFraomSK0sUTeKAyeOo7CZ1QiSs2rnIIXak4fGG4)

**Recognition Settings**

![](https://lh7-us.googleusercontent.com/nEAjFqWdbJci2U0lHCL8Bv-51Uur1QxT0etiKaR4kUNp2G4jtlsbR2ikAee--XvyoKDZ8Tx5l3hLa-a-FdY1lL35lxFegwg6D8xPw27ObwrZRRBhXDOmQOa3y_1bhcwzXF418PsASkx3jjEIQXqtBnc)

**OCR**

Here you can set the sensitivity of the OCR (Optical Character Recognition) function for all fields at once. This value determines the sensitivity with which a field is marked in red if it could not be extracted with 100% certainty (OCR related!).

**Match Score**

This is where you can set the sensitivity of the MATCH SCORE function for all fields at once. This value determines when a field is marked in red if DocBits has not extracted the field with 100% probability. In this case the field needs to be validated manually.

The button RESTORE DEFAULTS will set back both values to “50”.

**Profile**

Here you can define the profile that shall be used. Either Default or ZUGFeRD.\
In profile ZUGFeRD there are predefined fields that are mandatory for this type of invoice.\
If you do not explicitly use ZUGFeRD, please select “Default”.

![](https://lh7-us.googleusercontent.com/jxQMt3SJdQcMD15ntBN2vowRpAZxybGYZtr_6w8ANER4XgvkDf09tN-H9wZqApYj3ka1-E-KvALZp5dw4GFK5SswWWe3MAv3eiCWcRyb3lxk0f9erN4FfOTPkPK0lburKvib5hTntUHWUFikBGBQV1Y)
