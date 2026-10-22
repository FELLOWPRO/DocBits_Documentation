import re, sys

path = sys.argv[1]

M = {
"TaxCodes_1.png": ("Geöffnetes Einstellungen-Menü mit dem Bereich Dokumentenverarbeitung und dem Eintrag Liste von Werten",
                   "Einstellungen: Dokumentenverarbeitung > Liste von Werten"),
"TaxCodes_2.png": ("Seite Liste von Werten mit den vorhandenen Listen und der Schaltfläche Neu",
                   "Liste von Werten mit den vorhandenen Listen"),
"TaxCodes_3.png": ("Dialog Neue Liste mit dem Namen Tax_Country",
                   "Liste Tax_Country anlegen"),
"TaxCodes_28.png": ("Dialog Neue Liste mit dem Namen Tax_Code_Full",
                    "Liste Tax_Code_Full anlegen"),
"TaxCodes_29.png": ("Dialog Neue Liste mit dem Namen Tax_Code_Reduced",
                    "Liste Tax_Code_Reduced anlegen"),
"TaxCodes_30.png": ("Dialog Neue Liste mit dem Namen Tax_Code_Free",
                    "Liste Tax_Code_Free anlegen"),
"TaxCode_4.png": ("Seite Liste von Werten mit der Schaltfläche Zeile hinzufügen unter der geöffneten Liste",
                  "Eine Zeile zur geöffneten Liste hinzufügen"),
"TaxCodes_5.png": ("Dialog Werte anlegen mit einem eingetragenen LN-Steuercode im Feld Name",
                   "LN-Steuercode im Feld Name eintragen"),
"TaxCodes_27.png": ("Dialog Werte anlegen mit dem über Weitere Werte hinzugefügten Wert 800",
                    "Zweiten Wert über Weitere Werte hinzufügen"),
"TaxCodes_LN.png": ("Infor LN, Sitzung Steuercodes nach Land für Österreich mit den Spalten Steuercode und Steuerart",
                    "LN: Common > Taxation > Master Data > Tax Codes > Tax Codes by Country"),
"TaxCodes_6.png": ("Geöffnetes Menü Globale Einstellungen mit dem Eintrag Dokumenttypen",
                   "Einstellungen: Globale Einstellungen > Dokumenttypen"),
"TaxCodes_7.png": ("Seite Dokumenttypen mit dem Menü Felder unter jedem Dokumenttyp",
                   "Menü Felder des Dokumenttyps öffnen"),
"TaxCodes_8.png": ("Registerkarte Felder mit der Gruppe Mehrwertsteuer & Beträge und der Schaltfläche Neu erstellen",
                   "Registerkarte Felder: Gruppe Mehrwertsteuer & Beträge"),
"TaxCodes_10.png": ("Dialog Dokumentfelddetails für tax_country mit Feldtyp Dropdown und Liste Tax_Country",
                    "Feld tax_country: Dropdown, Liste Tax_Country"),
"TaxCodes_11.png": ("Dialog Dokumentfelddetails für tax_country_2 mit Titel Tax Country Reduced",
                    "Feld tax_country_2: Dropdown, Liste Tax_Country"),
"TaxCodes_12.png": ("Dialog Dokumentfelddetails für tax_country_3 mit Titel Tax Country Free",
                    "Feld tax_country_3: Dropdown, Liste Tax_Country"),
"TaxCodes_13.png": ("Dialog Dokumentfelddetails für tax_code_without_country mit Liste Tax_Code_Full",
                    "Feld tax_code_without_country: Dropdown, Liste Tax_Code_Full"),
"TaxCodes_14.png": ("Dialog Dokumentfelddetails für tax_code_without_country_2 mit Liste Tax_Code_Reduced",
                    "Feld tax_code_without_country_2: Dropdown, Liste Tax_Code_Reduced"),
"TaxCodes_15.png": ("Dialog Dokumentfelddetails für tax_code_without_country_3 mit Liste Tax_Code_Free",
                    "Feld tax_code_without_country_3: Dropdown, Liste Tax_Code_Free"),
"TaxCodes_20.png": ("Registerkarte Felder mit der Schaltfläche Einstellungen speichern über der Feldliste",
                    "Einstellungen speichern, um die neuen Felder zu übernehmen"),
"TaxCodes_19.png": ("Seite Dokumenttypen mit dem Link Layout bearbeiten unter jedem Dokumenttyp",
                    "Layout bearbeiten des Dokumenttyps öffnen"),
"TaxCodes_26.png": ("Layout-Builder mit der Auswahl des Dokumentursprungs und der Werkzeugleiste der Vorlage",
                    "Layout-Builder: Dokumentursprung auswählen"),
"TaxCodes_21.png": ("Layout-Builder mit der Gruppe Steuerdetails und ihren Feldern im Elementbaum",
                    "Zur Gruppe Steuerdetails scrollen"),
"TaxCodes_22.png": ("Layout-Builder mit aufgeklappter Auswahl Formularelemente",
                    "Formularelemente aufklappen"),
"TaxCodes_23.png": ("Layout-Builder mit dem in den Bereich Steuerdetails gezogenen Feld Tax Country",
                    "Tax Country in den Bereich Steuerdetails ziehen"),
"TaxCodes_24.png": ("Layout-Builder mit dem unter Tax Country abgelegten Feld Tax Code",
                    "Tax Code in den Bereich Steuerdetails ziehen"),
"TaxCodes_25.png": ("Layout-Builder mit gespeicherter Vorlage und beiden Steuerfeldern in der Gruppe Steuerdetails",
                    "Gespeicherte Vorlage mit beiden Steuerfeldern"),
"TaxCodes_31.png": ("Feldprüfung einer Rechnung mit ausgefüllten Auswahllisten Tax Country und Tax Code",
                    "Die neuen Auswahllisten in der Feldprüfung"),
"TaxCodesMulti_1.png": ("Layout-Builder mit dem Werkzeug Untergruppe in der Auswahl Formularelemente",
                        "Werkzeug Untergruppe auswählen"),
"TaxCodesMulti_2.png": ("Layout-Builder mit einer neuen leeren Untergruppe neben einem vorhandenen Feld",
                        "Untergruppe neben einem Feld ablegen"),
"TaxCodesMulti_3.png": ("Eigenschaftenbereich mit dem Feld Label der neuen Untergruppe",
                        "Untergruppe im Feld Label benennen"),
"TaxCodeMulti_4.png": ("Layout-Builder mit den in die neue Untergruppe verschobenen Steuerfeldern",
                       "Steuerfelder in die Untergruppe verschieben"),
"TaxCodeMulti_5.png": ("Layout-Builder mit Tax Country und Tax Code innerhalb der Untergruppe",
                       "Tax Country und Tax Code in der Untergruppe"),
"TaxCodeMulti_6.png": ("Layout-Builder mit drei Steueruntergruppen für vollen, reduzierten und steuerfreien Satz",
                       "Drei Untergruppen für voll, reduziert und steuerfrei"),
"TaxCodeMulti_7.png": ("Layout-Builder mit gespeicherter Vorlage für mehrere Steuercodes",
                       "Vorlage für mehrere Steuercodes speichern"),
"TaxCodeMulti_8.png": ("Feldprüfung mit drei getrennten Steuerabschnitten sowie Plus- und Entfernen-Schaltfläche",
                       "Drei Steuerabschnitte in der Feldprüfung"),
"TaxCodeMulti_9.png": ("Feldprüfung mit einem über die Plus-Schaltfläche duplizierten Steuerabschnitt",
                       "Weiteren Abschnitt über die Plus-Schaltfläche hinzufügen"),
"TaxCodesLN_2.png": ("Infor LN, Sitzung Steuerzeilen nach externer Rechnung mit der Spalte Steuerposition",
                     "LN: Tax Lines by External Invoice"),
"TaxCodesLN_3.png": ("Infor LN, Sitzung Steuerzeilen nach externer Rechnung mit der Positionsnummer",
                     "LN: die Positionsnummer wird als USt-Position exportiert"),
"TaxCodeMulti_10.png": ("Exportzuordnung mit dem Eintrag ICF_TaxLine neben den Rechnungskostenfeldern",
                        "Exportzuordnung: ICF_TaxLine = TF_position"),
"docbits_docbits_image_8.png": ("Seite Dokumenttypen mit dem Menü Felder unter jedem Dokumenttyp",
                                "Menü Felder des Dokumenttyps öffnen"),
}

src = open(path, encoding="utf-8").read()
missing = set()
count = 0
skip = 0

fig = re.compile(r'<img src="([^"]*)/([^/"]+)" alt="([^"]*)"([^>]*)><figcaption>([^<]*)</figcaption>')

def repl(m):
    global count, skip
    src_path, name, old_alt, rest, old_cap = m.groups()
    alt, cap = M.get(name, (None, None))
    if alt is None:
        missing.add(name)
        return m.group(0)
    if old_alt and old_alt not in ("DocBits Bild",):
        skip += 1
        return m.group(0)
    count += 1
    return '<img src="%s/%s" alt="%s"%s><figcaption>%s</figcaption>' % (
        src_path, name, alt, rest, cap)

new = fig.sub(repl, src)
open(path, "w", encoding="utf-8").write(new)

print("images fixed:", count, "| kept existing alt:", skip)
print("unknown files:", sorted(missing))
print("remaining empty alt:", new.count('alt=""'))
print("remaining empty caption:", new.count("<figcaption></figcaption>"))
