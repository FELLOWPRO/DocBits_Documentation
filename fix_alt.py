import re, sys

path = sys.argv[1]

M = {
"TaxCodes_1.png": ("Settings menu open with the Document Processing group and the List of Values entry",
                   "Settings: Document Processing > List of Values"),
"TaxCodes_2 (1).png": ("List of Values page with the existing lists and the New button",
                       "List of Values page with the existing lists"),
"TaxCodes_3.png": ("Create New list dialog with the name Tax_Country entered",
                   "Create the list Tax_Country"),
"TaxCodes_28.png": ("Create New list dialog with the name Tax_Code_Full entered",
                    "Create the list Tax_Code_Full"),
"TaxCodes_29.png": ("Create New list dialog with the name Tax_Code_Reduced entered",
                    "Create the list Tax_Code_Reduced"),
"TaxCodes_30.png": ("Create New list dialog with the name Tax_Code_Free entered",
                    "Create the list Tax_Code_Free"),
"TaxCode_4.png": ("List of Values page with the Add Row button below the opened list",
                  "Add a row to the opened list"),
"TaxCodes_5.png": ("Create values dialog with one LN tax code entered in the Name field",
                   "Enter the LN tax code in the Name field"),
"TaxCodes_27.png": ("Create values dialog with the value 800 added through Add More Values",
                    "Add a second value with Add More Values"),
"TaxCodes_LN.png": ("Infor LN Tax Codes by Country session for Austria with the Tax Code and Kind of Tax columns",
                    "LN: Common > Taxation > Master Data > Tax Codes > Tax Codes by Country"),
"TaxCodes_6.png": ("Global Settings menu open with the Document Types entry",
                   "Settings: Global Settings > Document Types"),
"TaxCodes_7.png": ("Document Types page with the Fields menu below each document type",
                   "Open the Fields menu of the document type"),
"TaxCodes_8.png": ("Fields tab with the VAT & Amounts group and the Create New button",
                   "Fields tab: the VAT & Amounts group"),
"TaxCodes_10 (1).png": ("Document field details dialog for tax_country with field type Dropdown and list Tax_Country",
                        "Field tax_country: Dropdown, list Tax_Country"),
"TaxCodes_11 (1).png": ("Document field details dialog for tax_country_2 with title Tax Country Reduced",
                        "Field tax_country_2: Dropdown, list Tax_Country"),
"TaxCodes_12.png": ("Document field details dialog for tax_country_3 with title Tax Country Free",
                    "Field tax_country_3: Dropdown, list Tax_Country"),
"TaxCodes_13 (1).png": ("Document field details dialog for tax_code_without_country with list Tax_Code_Full",
                        "Field tax_code_without_country: Dropdown, list Tax_Code_Full"),
"TaxCodes_14 (1).png": ("Document field details dialog for tax_code_without_country_2 with list Tax_Code_Reduced",
                        "Field tax_code_without_country_2: Dropdown, list Tax_Code_Reduced"),
"TaxCodes_15 (1).png": ("Document field details dialog for tax_code_without_country_3 with list Tax_Code_Free",
                        "Field tax_code_without_country_3: Dropdown, list Tax_Code_Free"),
"TaxCodes_20 (2).png": ("Fields tab with the Save Settings button above the field list",
                        "Save Settings to apply the new fields"),
"TaxCodes_19.png": ("Document Types page with the Edit layout link below each document type",
                    "Open Edit layout of the document type"),
"TaxCodes_26.png": ("Layout Builder with the Document Origin selector and the template toolbar",
                    "Layout Builder: select the Document Origin"),
"TaxCodes_21.png": ("Layout Builder with the Tax Details group and its fields in the element tree",
                    "Scroll to the Tax Details group"),
"TaxCodes_22 (1).png": ("Layout Builder with the Form Elements dropdown expanded",
                        "Expand Form Elements"),
"TaxCodes_23 (2).png": ("Layout Builder with the Tax Country field dropped into the Tax Details area",
                        "Drag Tax Country into the Tax Details area"),
"TaxCodes_24 (1).png": ("Layout Builder with the Tax Code field placed below Tax Country",
                        "Drag Tax Code into the Tax Details area"),
"TaxCodes_25.png": ("Layout Builder with the saved template and both tax fields in the Tax Details group",
                    "Saved template with the two tax fields"),
"TaxCodes_31.png": ("Field validation view of an invoice with the Tax Country and Tax Code dropdowns filled",
                    "The new dropdowns in the validation view"),
"TaxCodesMulti_1.png": ("Layout Builder with the Sub Group tool in the Form Elements dropdown",
                        "Select the Sub Group tool"),
"TaxCodesMulti_2.png": ("Layout Builder with a new empty subgroup next to an existing field",
                        "Drop the subgroup next to a field"),
"TaxCodesMulti_3.png": ("Properties panel with the Label field of the new subgroup",
                        "Name the subgroup in the Label field"),
"TaxCodeMulti_4.png": ("Layout Builder with the tax fields moved into the new subgroup",
                       "Move the tax fields into the subgroup"),
"TaxCodeMulti_5.png": ("Layout Builder with Tax Country and Tax Code inside the subgroup",
                       "Tax Country and Tax Code in the subgroup"),
"TaxCodeMulti_6.png": ("Layout Builder with three tax subgroups for full, reduced and free rates",
                       "Three subgroups for full, reduced and free"),
"TaxCodeMulti_7.png": ("Layout Builder with the saved multi-tax template",
                       "Save the multi-tax template"),
"TaxCodeMulti_8.png": ("Field validation view with three separate tax sections and the plus and remove buttons",
                       "Three tax sections in the validation view"),
"TaxCodeMulti_9.png": ("Field validation view with one tax section duplicated by the plus button",
                       "Add another section with the plus button"),
"TaxCodesLN_2.png": ("Infor LN Tax Lines by External Invoice session with the tax position column",
                     "LN: Tax Lines by External Invoice"),
"TaxCodesLN_3.png": ("Infor LN Tax Lines by External Invoice session showing the position number",
                     "LN: the position number is exported as USt Position"),
"TaxCodeMulti_10.png": ("Export mapping file with the ICF_TaxLine entry next to the invoice cost fields",
                        "Export mapping: ICF_TaxLine = TF_position"),
}

src = open(path, encoding="utf-8").read()
missing = set()
count = 0

fig = re.compile(r'<img src="([^"]*)/([^/"]+)" alt=""([^>]*)><figcaption></figcaption>')

def repl(m):
    global count
    src_path, name, rest = m.group(1), m.group(2), m.group(3)
    alt, cap = M.get(name, (None, None))
    if alt is None:
        missing.add(name)
        return m.group(0)
    count += 1
    return '<img src="%s/%s" alt="%s"%s><figcaption>%s</figcaption>' % (
        src_path, name, alt, rest, cap)

new = fig.sub(repl, src)
open(path, "w", encoding="utf-8").write(new)

print("images fixed:", count)
print("unknown files:", sorted(missing))
print("remaining empty alt:", new.count('alt=""'))
print("remaining empty caption:", new.count("<figcaption></figcaption>"))
