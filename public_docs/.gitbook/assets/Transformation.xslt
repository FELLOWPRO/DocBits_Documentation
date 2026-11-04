<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0" xmlns:fn="http://example.com/functions">
    <xsl:output method="xml" />
    
    <xsl:template name="DateTimeString">
        <xsl:param name="date" />
        <xsl:variable name="year" select="substring($date, 1, 4)" />
        <xsl:variable name="month" select="substring($date, 6, 2)" />
        <xsl:variable name="day" select="substring($date, 9, 2)" />
        <xsl:value-of select="concat($day, '.', $month, '.', $year)" />
    </xsl:template>


    <xsl:template match="/">
        <INVOICE>
            <SUPPLIER>
                <ELECTRONIC_ADDRESS>
                    <xsl:value-of select="//AccountingSupplierParty/Party/EndpointID/text()" />
                </ELECTRONIC_ADDRESS>
                <ELECTRONIC_ADDRESS_SCHEME_ID>
                    <xsl:value-of select="//AccountingSupplierParty/Party/EndpointID/@schemeID" />
                </ELECTRONIC_ADDRESS_SCHEME_ID>

                <xsl:for-each select="//AccountingSupplierParty/Party/PartyIdentification">
                    <PARTYIDENTIFICATION>
                        <ID>
                            <xsl:value-of select="ID/text()" />
                        </ID>
                        <ID_SCHEME_ID>
                            <xsl:value-of select="ID/@schemeID" />
                        </ID_SCHEME_ID>
                    </PARTYIDENTIFICATION>
                </xsl:for-each>

                <NAME>
                    <xsl:value-of select="//AccountingSupplierParty/Party/PartyName/Name/text()" />
                </NAME>
                <ADDRESS_LINE_1>
                    <xsl:value-of select="//AccountingSupplierParty/Party/PostalAddress/StreetName/text()" />
                </ADDRESS_LINE_1>
                <ADDRESS_LINE_2>
                    <xsl:value-of select="//AccountingSupplierParty/Party/PostalAddress/AdditionalStreetName/text()" />
                </ADDRESS_LINE_2>
                <ADDRESS_LINE_3>
                    <xsl:value-of select="//AccountingSupplierParty/Party/PostalAddress/AddressLine/Line/text()" />
                </ADDRESS_LINE_3>
                <VAT_ID>
                    <xsl:value-of select="//AccountingSupplierParty/Party/PartyTaxScheme/CompanyID/text()" />
                </VAT_ID>
                <TAX_SCHEME>
                    <xsl:value-of select="//AccountingSupplierParty/Party/PartyTaxScheme/TaxScheme/ID/text()" />
                </TAX_SCHEME>
                <LEGAL_NAME>
                    <xsl:value-of select="//AccountingSupplierParty/Party/PartyLegalEntity/RegistrationName/text()" />
                </LEGAL_NAME>
                <LEGAL_ID>
                    <xsl:value-of select="//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/text()" />
                </LEGAL_ID>
                <LEGAL_ID_SCHEME_ID>
                    <xsl:value-of select="//AccountingSupplierParty/Party/PartyLegalEntity/CompanyID/@schemeID" />
                </LEGAL_ID_SCHEME_ID>
                <LEGAL_FORM>
                    <xsl:value-of select="//AccountingSupplierParty/Party/PartyLegalEntity/CompanyLegalForm/text()" />
                </LEGAL_FORM>
                <POST_CODE>
                    <xsl:value-of select="//AccountingSupplierParty/Party/PostalAddress/PostalZone/text()" />
                </POST_CODE>
                <CITY>
                    <xsl:value-of select="//AccountingSupplierParty/Party/PostalAddress/CityName/text()" />
                </CITY>
                <COUNTRY_SUBENTITY>
                    <xsl:value-of select="//AccountingSupplierParty/Party/PostalAddress/CountrySubentity/text()" />
                </COUNTRY_SUBENTITY>
                <COUNTRY_CODE>
                    <xsl:value-of select="//AccountingSupplierParty/Party/PostalAddress/Country/IdentificationCode/text()" />
                </COUNTRY_CODE>
                <CONTACT>
                    <NAME>
                    <xsl:value-of select="//AccountingSupplierParty/Party/Contact/Name/text()" />
                    </NAME>
                    <TELEPHONE>
                    <xsl:value-of select="//AccountingSupplierParty/Party/Contact/Telephone/text()" />
                    </TELEPHONE>
                    <EMAIL>
                    <xsl:value-of select="//AccountingSupplierParty/Party/Contact/ElectronicMail/text()" />
                    </EMAIL>
                </CONTACT>
            </SUPPLIER>

            <BUYER>
               <ELECTRONIC_ADDRESS>
                    <xsl:value-of select="//AccountingCustomerParty/Party/EndpointID/text()" />
                </ELECTRONIC_ADDRESS>
                <ELECTRONIC_ADDRESS_SCHEME_ID>
                    <xsl:value-of select="//AccountingCustomerParty/Party/EndpointID/@schemeID" />
                </ELECTRONIC_ADDRESS_SCHEME_ID>

                <xsl:for-each select="//AccountingCustomerParty/Party/PartyIdentification">
                    <PARTYIDENTIFICATION>
                        <ID>
                            <xsl:value-of select="ID/text()" />
                        </ID>
                        <ID_SCHEME_ID>
                            <xsl:value-of select="ID/@schemeID" />
                        </ID_SCHEME_ID>
                    </PARTYIDENTIFICATION>
                </xsl:for-each>

                <NAME>
                    <xsl:value-of select="//AccountingCustomerParty/Party/PartyName/Name/text()" />
                </NAME>
                <ADDRESS_LINE_1>
                    <xsl:value-of select="//AccountingCustomerParty/Party/PostalAddress/StreetName/text()" />
                </ADDRESS_LINE_1>
                <ADDRESS_LINE_2>
                    <xsl:value-of select="//AccountingCustomerParty/Party/PostalAddress/AdditionalStreetName/text()" />
                </ADDRESS_LINE_2>
                <ADDRESS_LINE_3>
                    <xsl:value-of select="//AccountingCustomerParty/Party/PostalAddress/AddressLine/Line/text()" />
                </ADDRESS_LINE_3>
                <VAT_ID>
                    <xsl:value-of select="//AccountingCustomerParty/Party/PartyTaxScheme/CompanyID/text()" />
                </VAT_ID>
                <TAX_SCHEME>
                    <xsl:value-of select="//AccountingCustomerParty/Party/PartyTaxScheme/TaxScheme/ID/text()" />
                </TAX_SCHEME>
                <LEGAL_NAME>
                    <xsl:value-of select="//AccountingCustomerParty/Party/PartyLegalEntity/RegistrationName/text()" />
                </LEGAL_NAME>
                <LEGAL_ID>
                    <xsl:value-of select="//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/text()" />
                </LEGAL_ID>
                <LEGAL_ID_SCHEME_ID>
                    <xsl:value-of select="//AccountingCustomerParty/Party/PartyLegalEntity/CompanyID/@schemeID" />
                </LEGAL_ID_SCHEME_ID>
                <LEGAL_FORM>
                    <xsl:value-of select="//AccountingCustomerParty/Party/PartyLegalEntity/CompanyLegalForm/text()" />
                </LEGAL_FORM>
                <POST_CODE>
                    <xsl:value-of select="//AccountingCustomerParty/Party/PostalAddress/PostalZone/text()" />
                </POST_CODE>
                <CITY>
                    <xsl:value-of select="//AccountingCustomerParty/Party/PostalAddress/CityName/text()" />
                </CITY>
                <COUNTRY_SUBENTITY>
                    <xsl:value-of select="//AccountingCustomerParty/Party/PostalAddress/CountrySubentity/text()" />
                </COUNTRY_SUBENTITY>
                <COUNTRY_CODE>
                    <xsl:value-of select="//AccountingCustomerParty/Party/PostalAddress/Country/IdentificationCode/text()" />
                </COUNTRY_CODE>
                <CONTACT>
                    <NAME>
                    <xsl:value-of select="//AccountingCustomerParty/Party/Contact/Name/text()" />
                    </NAME>
                    <TELEPHONE>
                    <xsl:value-of select="//AccountingCustomerParty/Party/Contact/Telephone/text()" />
                    </TELEPHONE>
                    <EMAIL>
                    <xsl:value-of select="//AccountingCustomerParty/Party/Contact/ElectronicMail/text()" />
                    </EMAIL>
                </CONTACT>
            </BUYER>

            <PAYEE>
                <xsl:for-each select="//PayeeParty/PartyIdentification">
                    <PARTYIDENTIFICATION>
                        <ID>
                            <xsl:value-of select="ID/text()" />
                        </ID>
                        <ID_SCHEME_ID>
                            <xsl:value-of select="ID/@schemeID" />
                        </ID_SCHEME_ID>
                    </PARTYIDENTIFICATION>
                </xsl:for-each>

                <NAME>
                    <xsl:value-of select="//PayeeParty/PartyName/Name/text()" />
                </NAME>
                <LEGAL_ID>
                    <xsl:value-of select="//PayeeParty/PartyLegalEntity/CompanyID/text()" />
                </LEGAL_ID>
                <LEGAL_ID_SCHEME_ID>
                    <xsl:value-of select="//PayeeParty/PartyLegalEntity/CompanyID/@schemeID" />
                </LEGAL_ID_SCHEME_ID>
            </PAYEE>

            <TAX_REPRESENTATIVE_PARTY>
                <NAME>
                    <xsl:value-of select="//TaxRepresentativeParty/PartyName/Name/text()" />
                </NAME>
                 <ADDRESS_LINE_1>
                    <xsl:value-of select="//TaxRepresentativeParty/PostalAddress/StreetName/text()" />
                </ADDRESS_LINE_1>
                <ADDRESS_LINE_2>
                    <xsl:value-of select="/TaxRepresentativeParty/PostalAddress/AdditionalStreetName/text()" />
                </ADDRESS_LINE_2>
                <ADDRESS_LINE_3>
                    <xsl:value-of select="//TaxRepresentativeParty/PostalAddress/AddressLine/Line/text()" />
                </ADDRESS_LINE_3>
                <VAT_ID>
                    <xsl:value-of select="//TaxRepresentativeParty/PartyTaxScheme/CompanyID/text()" />
                </VAT_ID>
                <TAX_SCHEME>
                    <xsl:value-of select="//TaxRepresentativeParty/PartyTaxScheme/TaxScheme/ID/text()" />
                </TAX_SCHEME>
                <CITY>
                    <xsl:value-of select="//TaxRepresentativeParty/PostalAddress/CityName/text()" />
                </CITY>
                <POST_CODE>
                    <xsl:value-of select="//TaxRepresentativeParty/PostalAddress/PostalZone/text()" />
                </POST_CODE>
                <COUNTRY_SUBENTITY>
                    <xsl:value-of select="//TaxRepresentativeParty/PostalAddress/CountrySubentity/text()" />
                </COUNTRY_SUBENTITY>
                <COUNTRY_CODE>
                    <xsl:value-of select="//TaxRepresentativeParty/PostalAddress/Country/IdentificationCode/text()" />
                </COUNTRY_CODE>
            </TAX_REPRESENTATIVE_PARTY>

            <INVOICE_TYPE>Invoice</INVOICE_TYPE>
            <INVOICE_SUB_TYPE>Purchase Invoice</INVOICE_SUB_TYPE>
            
            <INVOICE_ID>
                <xsl:value-of select="//ID/text()" />
            </INVOICE_ID>
            <INVOICE_TYPE_CODE>
                <xsl:value-of select="//InvoiceTypeCode/text()" />
            </INVOICE_TYPE_CODE>
            <INVOICE_DATE>
                <xsl:call-template name="DateTimeString">
                     <xsl:with-param name="date" select="normalize-space(//IssueDate/text())" />
                </xsl:call-template>
            </INVOICE_DATE>
            <DUE_DATE>
                <xsl:call-template name="DateTimeString">
                     <xsl:with-param name="date" select="normalize-space(//DueDate/text())" />
                </xsl:call-template>
            </DUE_DATE>
            <TAX_POINT_DATE>
                <xsl:if test="//TaxPointDate/text()">
                    <xsl:call-template name="DateTimeString">
                        <xsl:with-param name="date" select="normalize-space(//TaxPointDate/text())" />
                    </xsl:call-template>   
                </xsl:if>
            </TAX_POINT_DATE>
            <INVOICE_NOTE>
                    <xsl:value-of select="//Note/text()" />
            </INVOICE_NOTE>
            <DOCUMENT_CURRENCY_CODE>
                    <xsl:value-of select="//DocumentCurrencyCode/text()" />
            </DOCUMENT_CURRENCY_CODE>
            <TAX_CURRENCY_CODE>
                    <xsl:value-of select="//TaxCurrencyCode/text()" />
            </TAX_CURRENCY_CODE>
            <ACCOUNTING_COST>
                    <xsl:value-of select="//AccountingCost/text()" />
            </ACCOUNTING_COST>
            <INVOCICE_PERIOD>
                <START_DATE>
                <xsl:call-template name="DateTimeString">
                     <xsl:with-param name="date" select="normalize-space(//InvoicePeriod/StartDate/text())" />
                </xsl:call-template>
                </START_DATE>
                <END_DATE>
                    <xsl:call-template name="DateTimeString">
                        <xsl:with-param name="date" select="normalize-space(//InvoicePeriod/EndDate/text())" />
                    </xsl:call-template>
                </END_DATE>
                <DESCRIPTION_CODE>
                    <xsl:value-of select="//InvoicePeriod/DescriptionCode/text()" />
                </DESCRIPTION_CODE>   
            </INVOCICE_PERIOD>
            <PURCHASE_ORDER>
                <xsl:value-of select="//OrderReference/ID/text()" />
            </PURCHASE_ORDER>
            <SALES_ORDER>
                <xsl:value-of select="//OrderReference/SalesOrderID/text()" />
            </SALES_ORDER>
            <BUYER_REFERENCE>
                <xsl:value-of select="//BuyerReference/text()" />
            </BUYER_REFERENCE>

            <xsl:for-each select="//BillingReference">
             <BILLING_REFERENCE>
                <PRECEDING_INVOCIE_NUMBER>
                    <xsl:value-of select="InvoiceDocumentReference/ID/text()" />
                </PRECEDING_INVOCIE_NUMBER>
                <PRECEDING_INVOICE_ISSUE_DATE>
                    <xsl:value-of select="InvoiceDocumentReference/IssueDate/text()" />
                </PRECEDING_INVOICE_ISSUE_DATE>
            </BILLING_REFERENCE>
            </xsl:for-each>

            <DESPATCH_DOCUMENT_REFERENCE>
                <xsl:value-of select="//DespatchDocumentReference/ID/text()" />
            </DESPATCH_DOCUMENT_REFERENCE>
            <RECEIPT_DOCUMENT_REFERENCE>
                <xsl:value-of select="//ReceiptDocumentReference/ID/text()" />
            </RECEIPT_DOCUMENT_REFERENCE>
            <ORIGINATOR_DOCUMENT_REFERENCE>
                <xsl:value-of select="//OriginatorDocumentReference/ID/text()" />
            </ORIGINATOR_DOCUMENT_REFERENCE>
            <CONTRACT_DOCUMENT_REFERENCE>
                <xsl:value-of select="//ContractDocumentReference/ID/text()" />
            </CONTRACT_DOCUMENT_REFERENCE>
            <PROJECT_REFERENCE>
                <xsl:value-of select="//ProjectReference/ID/text()" />
            </PROJECT_REFERENCE>

            <xsl:for-each select="//AdditionalDocumentReference">
                <ADDITIONAL_DOCUMENT_REFERENCE>
                    <ID>
                        <xsl:value-of select="ID/text()" />
                    </ID>
                    <SCHEME_ID>
                        <xsl:value-of select="ID/@schemeID" />
                    </SCHEME_ID>
                    <DOCUMENT_TYPE_CODE>
                        <xsl:value-of select="DocumentTypeCode/text()" />
                    </DOCUMENT_TYPE_CODE>
                    <DOCUMENT_DESCRIPTION>
                        <xsl:value-of select="DocumentDescription/text()" />
                    </DOCUMENT_DESCRIPTION>
                    <ATTACHMENT>
                        <EMBEDDED_DOCUMENT_BINARY_OBJECT>
                            <xsl:value-of select="Attachment/EmbeddedDocumentBinaryObject/text()" />
                        </EMBEDDED_DOCUMENT_BINARY_OBJECT>
                        <MIME_CODE>
                            <xsl:value-of select="Attachment/EmbeddedDocumentBinaryObject/@mimeCode" />
                        </MIME_CODE>
                        <FILENAME>
                            <xsl:value-of select="Attachment/EmbeddedDocumentBinaryObject/@filename" />
                        </FILENAME>
                        <EXTERNAL_REFERENCE_URL>
                            <xsl:value-of select="Attachment/ExternalReference/URI/text()" />
                        </EXTERNAL_REFERENCE_URL>
                    </ATTACHMENT>
                </ADDITIONAL_DOCUMENT_REFERENCE>
            </xsl:for-each>


             <DELIVERY_DATE>
                <xsl:value-of select="//Delivery/ActualDeliveryDate/text()" />
            </DELIVERY_DATE>
            <DELIVERY_LOCATION>
                <ID>
                    <xsl:value-of select="//Delivery/DeliveryLocation/ID/text()" />
                </ID>
                <ID_SCHEME_ID>
                    <xsl:value-of select="//Delivery/DeliveryLocation/ID/@schemeID" />
                </ID_SCHEME_ID>
                <ADDRESS_LINE_1>
                    <xsl:value-of select="//Delivery/DeliveryLocation/Address/StreetName/text()" />
                </ADDRESS_LINE_1>
                <ADDRESS_LINE_2>
                    <xsl:value-of select="//Delivery/DeliveryLocation/Address/AdditionalStreetName/text()" />
                </ADDRESS_LINE_2>
                <ADDRESS_LINE_3>
                    <xsl:value-of select="//Delivery/DeliveryLocation/Address/AddressLine/Line/text()" />
                </ADDRESS_LINE_3>
                <CITY>
                    <xsl:value-of select="//Delivery/DeliveryLocation/Address/AddressLine/CityName/text()" />
                </CITY>
                <POST_CODE>
                    <xsl:value-of select="//Delivery/DeliveryLocation/Address/AddressLine/PostalZone/text()" />
                </POST_CODE>
                <COUNTRY_SUBENTITY>
                    <xsl:value-of select="//Delivery/DeliveryLocation/Address/AddressLine/CountrySubentity/text()" />
                </COUNTRY_SUBENTITY>
                <COUNTRY_CODE>
                    <xsl:value-of select="//Delivery/DeliveryLocation/Address/AddressLine/Country/IdentificationCode/text()" />
                </COUNTRY_CODE>
            </DELIVERY_LOCATION>
            <DELIVERY_PARTY_NAME>
                <xsl:value-of select="//Delivery/DeliveryParty/PartyName/Name/text()" />
            </DELIVERY_PARTY_NAME>

            <xsl:for-each select="//PaymentMeans">
                <PAYMENT_MEANS>
                    <CODE>
                        <xsl:value-of select="PaymentMeansCode/text()" />
                    </CODE>
                    <TEXT>
                        <xsl:value-of select="PaymentMeansCode/@name" />
                    </TEXT>
                    <PAYMENT_ID>
                        <xsl:value-of select="PaymentID/text()" />
                    </PAYMENT_ID>
                    <PRIMARY_ACCOUNT_NUMBER_ID>
                        <xsl:value-of select="CardAccount/PrimaryAccountNumberID/text()" />
                    </PRIMARY_ACCOUNT_NUMBER_ID>
                    <NETWORK_ID>
                        <xsl:value-of select="CardAccount/NetworkID/text()" />
                    </NETWORK_ID>
                    <CARD_HOLDER_NAME>
                        <xsl:value-of select="CardAccount/CardHolderName/text()" />
                    </CARD_HOLDER_NAME>
                    <IBAN>
                        <xsl:value-of select="PayeeFinancialAccount/ID/text()" />
                    </IBAN>
                    <ACCOUNT_NAME>
                        <xsl:value-of select="PayeeFinancialAccount/Name/text()" />
                    </ACCOUNT_NAME>
                    <BIC>
                        <xsl:value-of select="PayeeFinancialAccount/FinancialInstitutionBranch/ID/text()" />
                    </BIC>
                    <MANDATE_REFERENCE_ID>
                        <xsl:value-of select="PaymentMandate/ID/text()" />
                    </MANDATE_REFERENCE_ID>
                    <DEBITED_ACCOUNT_ID>
                        <xsl:value-of select="PaymentMandate/PayerFinancialAccount/ID/text()" />
                    </DEBITED_ACCOUNT_ID>
                </PAYMENT_MEANS>
            </xsl:for-each>

            <PAYMENT_TERMS>
                    <xsl:value-of select="//PaymentTerms/Note/text()" />
            </PAYMENT_TERMS>

            <xsl:for-each select="//AllowanceCharge">
                <DOCUMENT_LEVEL_ALLOWANCE_CHARGE>
                    <CHARGE_INDICATOR>
                        <!-- true = charge / false = allowance -->
                        <xsl:value-of select="ChargeIndicator/text()" />
                    </CHARGE_INDICATOR>
                    <REASON_CODE>
                        <xsl:value-of select="AllowanceChargeReasonCode/text()" />
                    </REASON_CODE>
                    <REASON>
                        <xsl:value-of select="AllowanceChargeReason/text()" />
                    </REASON>
                    <ALLOWANCE_CHARGE_PERCENTAGE>
                        <xsl:value-of select="MultiplierFactorNumeric/text()" />
                    </ALLOWANCE_CHARGE_PERCENTAGE>
                    <AMOUNT>
                        <xsl:value-of select="Amount/text()" />
                    </AMOUNT>
                    <AMOUNT_CURRENCY_ID>
                        <xsl:value-of select="Amount/@currencyID" />
                    </AMOUNT_CURRENCY_ID>
                    <BASE_AMOUNT>
                        <xsl:value-of select="BaseAmount/text()" />
                    </BASE_AMOUNT>
                    <BASE_AMOUNT_CURRENCY_ID>
                        <xsl:value-of select="BaseAmount/@currencyID" />
                    </BASE_AMOUNT_CURRENCY_ID>
                    <VAT_CATEGORY_CODE>
                        <xsl:value-of select="TaxCategory/ID/text()" />
                    </VAT_CATEGORY_CODE>
                    <VAT_RATE>
                        <xsl:value-of select="TaxCategory/Percent/text()" />
                    </VAT_RATE>
                    <TAX_SCHEME>
                        <xsl:value-of select="TaxCategory/TaxScheme/ID/text()" />
                    </TAX_SCHEME>
                </DOCUMENT_LEVEL_ALLOWANCE_CHARGE>
            </xsl:for-each>
            
            <TOTAL_TAX>
                <TOTAL_AMOUNT>
                        <xsl:value-of select="//TaxTotal/TaxAmount/text()" />
                </TOTAL_AMOUNT>
                <TOTAL_AMOUNT_CURRENCY_ID>
                        <xsl:value-of select="//TaxTotal/TaxAmount/@currencyID" />
                </TOTAL_AMOUNT_CURRENCY_ID>

                
                    <xsl:for-each select="//TaxSubtotal">
                        <TAX_SUB_TOTAL>
                            <TAXABLE_AMOUNT>
                                <xsl:value-of select="TaxableAmount/text()" />
                            </TAXABLE_AMOUNT>
                            <TAXABLE_AMOUNT_CURRENCY_ID>
                                <xsl:value-of select="TaxableAmount/@currencyID" />
                            </TAXABLE_AMOUNT_CURRENCY_ID>
                            <SUB_TOTAL_AMOUNT>
                                <xsl:value-of select="TaxAmount/text()" />
                            </SUB_TOTAL_AMOUNT>
                            <SUB_TOTAL_AMOUNT_CURRENCY_ID>
                                <xsl:value-of select="TaxAmount/@currencyID" />
                            </SUB_TOTAL_AMOUNT_CURRENCY_ID>
                            <VAT_CATEGORY_CODE>
                                <xsl:value-of select="TaxCategory/ID/text()" />
                            </VAT_CATEGORY_CODE>
                            <VAT_CATEGORY_RATE>
                                <xsl:value-of select="TaxCategory/Percent/text()" />
                            </VAT_CATEGORY_RATE>
                            <EXEMPTION_REASON_CODE>
                                <xsl:value-of select="TaxCategory/TaxExemptionReasonCode/text()" />
                            </EXEMPTION_REASON_CODE>
                            <EXEMPTION_REASON>
                                <xsl:value-of select="TaxCategory/TaxExemptionReason/text()" />
                            </EXEMPTION_REASON>
                            <TAX_SCHEME_ID>
                                <xsl:value-of select="TaxCategory/TaxScheme/ID/text()" />
                            </TAX_SCHEME_ID>
                        </TAX_SUB_TOTAL>
                    </xsl:for-each>
                
            </TOTAL_TAX>

            <TOTAL_LINE_NET_AMOUNT>
                <xsl:value-of select="//LegalMonetaryTotal/LineExtensionAmount/text()" />
            </TOTAL_LINE_NET_AMOUNT>
            <TOTAL_LINE_NET_AMOUNT_CURRENCY_CODE>
                <xsl:value-of select="//LegalMonetaryTotal/LineExtensionAmount/@currencyID" />
            </TOTAL_LINE_NET_AMOUNT_CURRENCY_CODE>

            <TAX_EXCLUSIVE_AMOUNT>
                <xsl:value-of select="//LegalMonetaryTotal/TaxExclusiveAmount/text()" />
            </TAX_EXCLUSIVE_AMOUNT>
            <TAX_EXCLUSIVE_AMOUNT_CURRENCY_CODE>
                <xsl:value-of select="//LegalMonetaryTotal/TaxExclusiveAmount/@currencyID" />
            </TAX_EXCLUSIVE_AMOUNT_CURRENCY_CODE>

            <TAX_INCLUSIVE_AMOUNT>
                <xsl:value-of select="//LegalMonetaryTotal/TaxInclusiveAmount/text()" />
            </TAX_INCLUSIVE_AMOUNT>
            <TAX_INCLUSIVE_AMOUNT_CURRENCY_CODE>
                <xsl:value-of select="//LegalMonetaryTotal/TaxInclusiveAmount/@currencyID" />
            </TAX_INCLUSIVE_AMOUNT_CURRENCY_CODE>

            <ALLOWANCE_TOTAL_AMOUNT>
                <xsl:value-of select="//LegalMonetaryTotal/AllowanceTotalAmount/text()" />
            </ALLOWANCE_TOTAL_AMOUNT>
            <ALLOWANCE_TOTAL_AMOUNT_CURRENCY_CODE>
                <xsl:value-of select="//LegalMonetaryTotal/AllowanceTotalAmount/@currencyID" />
            </ALLOWANCE_TOTAL_AMOUNT_CURRENCY_CODE>

            <CHARGE_TOTAL_AMOUNT>
                <xsl:value-of select="//LegalMonetaryTotal/ChargeTotalAmount/text()" />
            </CHARGE_TOTAL_AMOUNT>
            <CHARGE_TOTAL_AMOUNT_CURRENCY_CODE>
                <xsl:value-of select="//LegalMonetaryTotal/ChargeTotalAmount/@currencyID" />
            </CHARGE_TOTAL_AMOUNT_CURRENCY_CODE>

            <PREPAID_AMOUNT>
                <xsl:value-of select="//LegalMonetaryTotal/PrepaidAmount/text()" />
            </PREPAID_AMOUNT>
            <PREPAID_AMOUNT_CURRENCY_CODE>
                <xsl:value-of select="//LegalMonetaryTotal/PrepaidAmount/@currencyID" />
            </PREPAID_AMOUNT_CURRENCY_CODE>

            <PAYABLE_ROUNDING_AMOUNT>
                <xsl:value-of select="//LegalMonetaryTotal/PayableRoundingAmount/text()" />
            </PAYABLE_ROUNDING_AMOUNT>
            <PAYABLE_ROUNDING_AMOUNT_CURRENCY_CODE>
                <xsl:value-of select="//LegalMonetaryTotal/PayableRoundingAmount/@currencyID" />
            </PAYABLE_ROUNDING_AMOUNT_CURRENCY_CODE>

            <PAYABLE_AMOUNT>
                <xsl:value-of select="//LegalMonetaryTotal/PayableAmount/text()" />
            </PAYABLE_AMOUNT>
            <PAYABLE_AMOUNT_CURRENCY_CODE>
                <xsl:value-of select="//LegalMonetaryTotal/PayableAmount/@currencyID" />
            </PAYABLE_AMOUNT_CURRENCY_CODE>
            



            <INVOICE_LINES>

                <xsl:for-each select="//InvoiceLine">

                    <INVOICE_LINE>
                        <POSITION>
                            <xsl:value-of select="ID/text()" />
                        </POSITION>
                        <NOTE>
                            <xsl:value-of select="Note/text()" />
                        </NOTE>
                        <QUANTITY>
                            <xsl:value-of select="InvoicedQuantity/text()" />
                        </QUANTITY>
                        <UNIT_CODE>
                            <xsl:value-of select="InvoicedQuantity/@unitCode" />
                        </UNIT_CODE>
                        <NET_AMOUNT>
                            <xsl:value-of select="LineExtensionAmount/text()" />
                        </NET_AMOUNT>
                        <NET_AMOUNT_CURRENCY_CODE>
                            <xsl:value-of select="LineExtensionAmount/@currencyID" />
                        </NET_AMOUNT_CURRENCY_CODE>
                        <BUYER_ACCOUNTING_REFERENCE>
                            <xsl:value-of select="AccountingCost/text()" />
                        </BUYER_ACCOUNTING_REFERENCE>
                        <INVOCIE_PERIOD>
                            <START_DATE>
                                <xsl:value-of select="InvoicePeriod/StartDate/text()" />
                            </START_DATE>
                            <END_DATE>
                                <xsl:value-of select="InvoicePeriod/EndDate/text()" />
                            </END_DATE>
                        </INVOCIE_PERIOD>
                        <PURCHASE_ORDER>
                            <xsl:value-of select="OrderLineReference/LineID/text()" />
                        </PURCHASE_ORDER>
                        <DOCUMENT_REFERENCE>
                            <DOCUMENT_ID>
                                 <xsl:value-of select="DocumentReference/ID/text()" />
                            </DOCUMENT_ID>
                            <DOCUMENT_ID_SCHEME_ID>
                                 <xsl:value-of select="DocumentReference/ID/@schemeID" />
                            </DOCUMENT_ID_SCHEME_ID>
                            <DOCUMENT_TYPE_CODE>
                                 <xsl:value-of select="DocumentReference/DocumentTypeCode/text()" />
                            </DOCUMENT_TYPE_CODE>
                        </DOCUMENT_REFERENCE>
                        
                        <xsl:for-each select="AllowanceCharge">
                            <xsl:choose>
                                <xsl:when test="ChargeIndicator = 'false'">
                                    <ALLOWANCE>
                                        <INDICATOR>
                                            <!-- true = charge / false = allowance -->
                                            <xsl:value-of select="ChargeIndicator/text()" />
                                        </INDICATOR>
                                        <REASON_CODE>
                                            <xsl:value-of select="AllowanceChargeReasonCode/text()" />
                                        </REASON_CODE>
                                        <REASON>
                                            <xsl:value-of select="AllowanceChargeReason/text()" />
                                        </REASON>
                                        <PERCENTAGE>
                                            <xsl:value-of select="MultiplierFactorNumeric/text()" />
                                        </PERCENTAGE>
                                        <AMOUNT>
                                            <xsl:value-of select="Amount/text()" />
                                        </AMOUNT>
                                        <AMOUNT_CURRENCY_ID>
                                            <xsl:value-of select="Amount/@currencyID" />
                                        </AMOUNT_CURRENCY_ID>
                                        <BASE_AMOUNT>
                                            <xsl:value-of select="BaseAmount/text()" />
                                        </BASE_AMOUNT>
                                        <BASE_AMOUNT_CURRENCY_CODE>
                                            <xsl:value-of select="BaseAmount/@currencyID" />
                                        </BASE_AMOUNT_CURRENCY_CODE>
                                    </ALLOWANCE>
                                </xsl:when>
                                <xsl:otherwise>
                                <CHAGRE>
                                    <INDICATOR>
                                        <!-- true = charge / false = allowance -->
                                        <xsl:value-of select="ChargeIndicator/text()" />
                                    </INDICATOR>
                                    <REASON_CODE>
                                        <xsl:value-of select="AllowanceChargeReasonCode/text()" />
                                    </REASON_CODE>
                                    <REASON>
                                        <xsl:value-of select="AllowanceChargeReason/text()" />
                                    </REASON>
                                    <PERCENTAGE>
                                        <xsl:value-of select="MultiplierFactorNumeric/text()" />
                                    </PERCENTAGE>
                                    <AMOUNT>
                                        <xsl:value-of select="Amount/text()" />
                                    </AMOUNT>
                                    <AMOUNT_CURRENCY_ID>
                                        <xsl:value-of select="Amount/@currencyID" />
                                    </AMOUNT_CURRENCY_ID>
                                    <BASE_AMOUNT>
                                        <xsl:value-of select="BaseAmount/text()" />
                                    </BASE_AMOUNT>
                                    <BASE_AMOUNT_CURRENCY_CODE>
                                        <xsl:value-of select="BaseAmount/@currencyID" />
                                    </BASE_AMOUNT_CURRENCY_CODE>
                                </CHAGRE>
                                </xsl:otherwise>
                            </xsl:choose>
                        </xsl:for-each>

                        <ITEM>
                            <DESCRIPTION>
                                <xsl:value-of select="Item/Description/text()" />
                            </DESCRIPTION>
                            <NAME>
                                <xsl:value-of select="Item/Name/text()" />
                            </NAME>
                            <BUYERS_IDENTIFIER>
                                <xsl:value-of select="Item/BuyersItemIdentification/ID/text()" />
                            </BUYERS_IDENTIFIER>
                            <SELLERS_IDENTIFIER>
                                <xsl:value-of select="Item/SellersItemIdentification/ID/text()" />
                            </SELLERS_IDENTIFIER>
                            <STANDARD_IDENTIFIER>
                                <xsl:value-of select="Item/StandardItemIdentification/ID/text()" />
                            </STANDARD_IDENTIFIER>
                            <STANDARD_IDENTIFIER_SCHEME_ID>
                                <xsl:value-of select="Item/StandardItemIdentification/ID/@schemeID" />
                            </STANDARD_IDENTIFIER_SCHEME_ID>
                            <COUNTRY_IDENTIFIERE>
                                <xsl:value-of select="Item/OriginCountry/IdentificationCode/text()" />
                            </COUNTRY_IDENTIFIERE>
                            <xsl:for-each select="//Item/CommodityClassification">
                                <ITEM_CLASSIFICATION_IDENTIFIER>
                                    <xsl:value-of select="ItemClassificationCode/text()" />
                                </ITEM_CLASSIFICATION_IDENTIFIER>
                                <ITEM_CLASSIFICATION_IDENTIFIER_SCHEME_ID>
                                    <xsl:value-of select="ItemClassificationCode/@listID" />
                                </ITEM_CLASSIFICATION_IDENTIFIER_SCHEME_ID>
                                <ITEM_CLASSIFICATION_IDENTIFIER_VERSION_SCHEME_ID>
                                    <xsl:value-of select="ItemClassificationCode/@listVersionID" />
                                </ITEM_CLASSIFICATION_IDENTIFIER_VERSION_SCHEME_ID>
                            </xsl:for-each>

                            <VAT_CODE>
                                <xsl:value-of select="Item/ClassifiedTaxCategory/ID/text()" />
                            </VAT_CODE>
                            <VAT_RATE>
                                <xsl:value-of select="Item/ClassifiedTaxCategory/Percent/text()" />
                            </VAT_RATE>
                            <TAX_SCHEME_ID>
                                <xsl:value-of select="Item/ClassifiedTaxCategory/TaxScheme/ID/text()" />
                            </TAX_SCHEME_ID>

                            <xsl:for-each select="AdditionalItemProperty">
                                <MORE_INFO>
                                    <ATRIBUTE_NAME>
                                        <xsl:value-of select="Name/text()" />
                                    </ATRIBUTE_NAME>
                                    <ATRIBUTE_VALUE>
                                        <xsl:value-of select="Value/text()" />
                                    </ATRIBUTE_VALUE>
                                </MORE_INFO>
                            </xsl:for-each>

                            
                            <PRICE_INFO>
                                <NET_PRICE>
                                    <xsl:value-of select="Price/PriceAmount/text()" />
                                </NET_PRICE>
                                <NET_PRICE_CURRENCY_ID>
                                    <xsl:value-of select="Price/PriceAmount/@currencyID" />
                                </NET_PRICE_CURRENCY_ID>
                                <BASE_QUANTITY>
                                    <xsl:value-of select="Price/BaseQuantity/text()" />
                                </BASE_QUANTITY>
                                <BASE_QUANTITY_UNIT_CODE>
                                    <xsl:value-of select="Price/BaseQuantity/@unitCode" />
                                </BASE_QUANTITY_UNIT_CODE>
                                <CHARGE_INDICATOR>
                                    <xsl:value-of select="Price/AllowanceCharge/ChargeIndicator/text()" />
                                </CHARGE_INDICATOR>
                                <CHARGE_AMOUNT>
                                    <xsl:value-of select="Price/AllowanceCharge/Amount/text()" />
                                </CHARGE_AMOUNT>
                                <CHARGE_AMOUNT_CURRENCY_ID>
                                    <xsl:value-of select="Price/AllowanceCharge/Amount/@currencyID" />
                                </CHARGE_AMOUNT_CURRENCY_ID>
                                <CHARGE_BASE_AMOUNT>
                                    <xsl:value-of select="Price/AllowanceCharge/BaseAmount/text()" />
                                </CHARGE_BASE_AMOUNT>
                                <CHARGE_BASE_AMOUNT_CURRENCY_ID>
                                    <xsl:value-of select="Price/AllowanceCharge/BaseAmount/@currencyID" />
                                </CHARGE_BASE_AMOUNT_CURRENCY_ID>

                            </PRICE_INFO>
                            
                            
                        </ITEM>

                    </INVOICE_LINE>

                </xsl:for-each>

            </INVOICE_LINES>


        </INVOICE>


    </xsl:template>
</xsl:stylesheet>