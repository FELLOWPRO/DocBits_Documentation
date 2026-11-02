# 字段映射

下面列出了从 Infor 导入主数据到 DocBits 所需的字段映射。

## 自动会计（LN）

### 科目表

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

### 总柔性维度

```javascript
{
    "ID": "//DataArea/CodeDefinition/DisplayID",
    "Description": "//DataArea/CodeDefinition/Description",
    "DimensionID": "//DataArea/CodeDefinition/ReportingSlot",
    "Name": "//DataArea/CodeDefinition/Name"
}
```

### 最终柔性维度

```javascript
{
    "ID": "//DataArea/CodeDefinition/ReportingSlot",
    "Name": "//DataArea/CodeDefinition/ListID"
}
```

## 自动会计（M3）

### 科目表

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

### 柔性维度（代码定义）

```javascript
{
    "ID": "//DataArea/CodeDefinition/DocumentID/ID",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

## 税码

### 标准税率（Full）

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

### 减免

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

### 免税

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
