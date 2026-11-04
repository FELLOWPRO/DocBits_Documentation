# Creating an IDM Mapping File

Once obtained, open the file in your applicable file editor of choice. For this walkthrough, VSCode will be used.

## Edit Mapping File

Check the document type code is as it is in DocBits (like with the BOD Mapping File it should match the name of the doc type in the URL of the field settings) and also check the name of the document type as it should be in Document Manager (IDM) in Infor.

![](https://lh7-us.googleusercontent.com/WHO0vg2W36yVFBq0ay0wBMFVzMfT6pNvHklt0o8N4tqUpM03jXJm2fykuYjyZh0z4wFTO4Eaeh39-D03re3a9utegrdVdsjHBfucmALA3B7YBWd92-9bcYr543G4MWftv0RosvTgFP3J6NNmLZAz5Dc)

**FYI**: It states that the name of the document type in IDM is M3\_SupplierInvoice, this is due to this being an example from an M3 instance. This can change depending on if you use LN or M3, as well as your specific IDM configuration.

Check the company ID, and check Entity ID (SF\_MDS\_EntityType) this value should be the same as it was in the BOD Mapping File.

Ensure the IndexFieldFromDocBits=IDMAttributeID (check if DocBits on the left in the field settings matches IDM on the right in Document Type → Attributes).

### Document Manager in Infor

Go to Document Manager and select the name of the current document type you are trying to export, for example, Supplier Invoice.

![](https://lh7-us.googleusercontent.com/EV3uw3R1L6\_RRANB7FRLwtUFMbv\_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Click the above icon and then click Administration → Document Type and then find the document type you need in the list

![](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j\_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

As shown below, you will then see the doc type name as it is in INFOR

![](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj\_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW\_dpRfw\_5BXm0WvAnw4HOALmw)

Make sure this is how the name is shown in the IDM Mapping File

## Upload File to DocBits

Once the file is prepared, upload it to your export configuration in DocBits. This is available at Settings → Export.

![](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F\_i5mZ42YDnjqZUYKYSJu1Cetc\_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)

