# Mappatura dei campi

Di seguito troverai le mappature dei campi necessarie per importare i dati principali da Infor a DocBits.

## Contabilità automatica (LN)

### Piano dei conti
```javascript
{
"ID": "//DataArea/ChartOfAccounts/IDs/ID",
"NominalAccount": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/GLNominalAccount",
"AccountType": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/AccountType",
"Description": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/Description",
"DebitCreditFlag": "//DataArea/ChartOfAccounts/DebitCreditFlag",
"UnitCode": "//DataArea/ChartOfAccounts/MemoUnit/UnitCode",
"ClassificationCode1": "//DataArea/ChartOfAccounts/Classification/Codes/Code[@sequence='1']",
"ClassificationCode2": "//DataArea/ChartOfAccounts/Classification/Codes/Code[@sequence='2']",
"ClassificationCode3": "//DataArea/ChartOfAccounts/Classification/Codes/Code[@sequence='3']",
"ClassificationCode4": "//DataArea/ChartOfAccounts/Classification/Codes/Code[@sequence='4']",
"FlexDimensions": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/ID"
}
```
### DimensioniTotaliFlessibili
```javascript
{
"ID": "//DataArea/CodeDefinition/DisplayID",
"Description": "//DataArea/CodeDefinition/Description",
"DimensionID": "//DataArea/CodeDefinition/ReportingSlot",
"Name": "//DataArea/CodeDefinition/Name"
}
```
### Dimensioni Finali Flessibili
```javascript
{
"ID": "//DataArea/CodeDefinition/ReportingSlot",
"Name": "//DataArea/CodeDefinition/ListID"
}
```
## Contabilità automatica (M3)

### Piano dei conti
```javascript
{
"ID": "//DataArea/ChartOfAccounts/IDs/ID",
"NominalAccount": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/GLNominalAccount",
"AccountType": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/AccountType",
"Description": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/Description",
"DimensionProfile": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/ID",
"Dimension1": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[0]/ListID",
"Usage1": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[0]/Usage",
"Dimension2": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[1]/ListID",
"Usage2": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[1]/Usage",
"Dimension3": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[2]/ListID",
"Usage3": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[2]/Usage",
"Dimension4": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[3]/ListID",
"Usage4": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[3]/Usage",
"Dimension5": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[4]/ListID",
"Usage5": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[4]/Usage",
"Dimension6": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[5]/ListID",
"Usage6": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[5]/Usage",
"Dimension7": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[6]/ListID",
"Usage7": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[6]/Usage"
}
```
### Dimensioni flessibili (DefinizioneCodice)
```javascript
{
"ID": "//DataArea/CodeDefinition/DocumentID/ID",
"Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
"ListID": "//DataArea/CodeDefinition/ListID",
"CodeValue": "//DataArea/CodeDefinition/CodeValue",
"Description": "//DataArea/CodeDefinition/Description"
}
```
## Codice Fiscale

### Completo
```javascript
{
"ID": "//DataArea/LnTaxCode/DocumentID/ID",
"TaxCodeIDFull": "//DataArea/LnTaxCode/TaxCode",
"CountryCode": "//DataArea/LnTaxCode/CountryCode",
"TaxCodeFull": "//DataArea/LnTaxCode/DisplayID",
"Description": "//DataArea/LnTaxCode/Description",
"TaxType": "//DataArea/LnTaxCode/TaxTypeCode",
"TaxRateFull": "number(concat('0',//DataArea/LnTaxCode/SingularRatesGroup/SingularRate[1]/RateNumeric))*100"
}
```
### Ridotto
```javascript
{
"ID": "//DataArea/LnTaxCode/DocumentID/ID",
"TaxCodeIDReduced": "//DataArea/LnTaxCode/TaxCode",
"CountryCode": "//DataArea/LnTaxCode/CountryCode",
"TaxCodeReduced": "//DataArea/LnTaxCode/DisplayID",
"Description": "//DataArea/LnTaxCode/Description",
"TaxType": "//DataArea/LnTaxCode/TaxTypeCode",
"TaxRateReduced": "number(concat('0',//DataArea/LnTaxCode/SingularRatesGroup/SingularRate[1]/RateNumeric))*100"
}
```
### Gratuito
```javascript
{
"ID": "//DataArea/LnTaxCode/DocumentID/ID",
"TaxCodeIDFree": "//DataArea/LnTaxCode/TaxCode",
"CountryCode": "//DataArea/LnTaxCode/CountryCode",
"TaxCodeFree": "//DataArea/LnTaxCode/DisplayID",
"Description": "//DataArea/LnTaxCode/Description",
"TaxType": "//DataArea/LnTaxCode/TaxTypeCode",
"TaxRateFree": "number(concat('0',//DataArea/LnTaxCode/SingularRatesGroup/SingularRate[2]/RateNumeric))*100"
}
```

