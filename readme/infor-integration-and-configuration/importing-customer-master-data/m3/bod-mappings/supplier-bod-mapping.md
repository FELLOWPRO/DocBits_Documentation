# Supplier BOD Mapping

Ta strona dokumentuje, jak DocBits pobiera dane główne dostawców z Infor M3 za pomocą BOD-ów `SyncSupplierPartyMaster` i `SyncRemitToPartyMaster`. Oba BOD-y wypełniają tę samą tabelę danych głównych `SUPPLIER` w DocBits.

{% file src="../../../../.gitbook/assets/Sync.SupplierPartyMaster.pdf" %}
SupplierPartyMaster — Oryginalna referencja mapowania BOD (PDF)
{% endfile %}

{% file src="../../../../.gitbook/assets/Sync.RemitToPartyMaster.pdf" %}
RemitToPartyMaster — Oryginalna referencja mapowania BOD (PDF)
{% endfile %}

## Zasady kluczowe

- **CONO + SUNO to klucz dopasowania.** Wiersz `supplier_header` w DocBits jest unikalnie identyfikowany przez `(customer_number = sharedCONO, supplier_number = sharedSUNO)`. Pozwala to jednej organizacji DocBits konsolidować wiele firm M3.
- **`variationID` chroni przed BOD-ami w nieodpowiedniej kolejności.** M3 może emitować ten sam rekord danych głównych wiele razy w krótkich odstępach; przychodzący `variationID` musi być większy niż przechowywany, aby aktualizacja została zaakceptowana. Oba BOD-y śledzą swoje `variationID` niezależnie (`variation_id_supplier_bod`, `variation_id_remit_to_party`).
- **Brak cichego nadpisywania.** SupplierPartyMaster i RemitToPartyMaster współdzielą kilka pól (nazwa, telefon, NIP, bank, status). Każdy BOD aktualizuje tylko pola, które posiada, i tylko jeśli jego `variationID` rośnie. W zestawie współdzielonym wygrywa BOD odebrany ostatnio (na typ BOD).
- **Synchronizacja wielu banków jest sterowana preferencją.** Zachowanie domyślne: ostatnia `FinancialParty` jest zapisywana w `bank_id` w nagłówku. Z włączoną preferencją `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` każdy wpis `FinancialParty` jest zapisywany w `supplier_account` (IBAN, ID konta, kod waluty, wskaźnik preferencji).
- **Opcjonalne przycinanie sufiksu CONO.** Niektóre instalacje M3 dodają sufiks dywizji do numeru firmy (np. `100_01`). Preferencja `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` obcina sufiksy `_*`, aby klucze DocBits pozostały spójne.

## Sync.SupplierPartyMaster

→ Tabela danych głównych DocBits: **SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//SupplierPartyMaster/PartyIDs/ID",
            "variationID": "//SupplierPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//SupplierPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//SupplierPartyMaster/PartyIDs/TaxID",
            "paymentTermId": "//SupplierPartyMaster/PaymentTermID",
            "paymentMethodCode": "//SupplierPartyMaster/PaymentMethodCode",
            "buyerPersonReferenceId": "//SupplierPartyMaster/BuyerPersonReference/IDs/ID",
            "buyerPersonReference": "//SupplierPartyMaster/BuyerPersonReference/Name",
            "supplier_category": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Categories']",
            "supplier_group": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Group']",
            "discount_terms_description": "//SupplierPartyMaster/UserArea/Property/NameValue[@name='eam.UDFCHAR06']",
            "status": "//SupplierPartyMaster/Status/Code",
            "bank_id": "//SupplierPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
        }
```

### Referencja pól

| Pole DocBits | Źródło M3 | Opis |
|---|---|---|
| `sharedCONO` | Numer firmy M3 | Mapuje na `customer_number` w `supplier_header`. Element klucza dopasowania. |
| `sharedSUNO` | `CIDMAS.IDSUNO` | Numer dostawcy M3. Element klucza dopasowania. |
| `variationID` | Atrybut BOD | Przechowywany jako `variation_id_supplier_bod`. Przychodzące BOD-y są akceptowane tylko jeśli ich `variationID` przewyższa wartość przechowywaną. Brak atrybutu jest traktowany jako `0` (force-update). |
| `supplierName` | `CIDMAS.IDSUNM` | Nazwa wyświetlana dostawcy. |
| `phone` | `CIDMAS.PHNO/PHN2/IDTFNO` | Numer telefonu z kanału `Phone`. |
| `vatNo` | `CIDMAS.IDVRNO` | Identyfikator VAT. Czytany z `PartyIDs/TaxID` (bez filtra `@schemeName` na ścieżce pobierania M3). |
| `paymentTermId` | `CIDVEN.IITEPY` | Identyfikator warunków płatności. |
| `paymentMethodCode` | — | Kod metody płatności, gdy dostarczony. |
| `buyerPersonReferenceId` / `buyerPersonReference` | `CIDVEN.IIBUYE` / `CSYUSR.CRRENM` | Przypisany kupiec (referencja użytkownika M3 i nazwa wyświetlana). |
| `supplier_category` | — | Czytane z `Classification/Codes/Code[@listID='Supplier Categories']`. Rozszerzenie UserArea specyficzne dla klienta; w standardowych instalacjach M3 pozostaje NULL. |
| `supplier_group` | `CIDVEN.IISUCL` | Grupa klasyfikacji dostawcy. |
| `discount_terms_description` | — | Rozszerzenie UserArea specyficzne dla klienta (`eam.UDFCHAR06`) używane przez kalkulator daty rabatu DocBits. Gdy dostawca dostarcza tu wartość dni rabatu, DocBits łączy ją z datą faktury, aby wyprodukować datę wymagalności rabatu dla zespołu AP. |
| `status` | `CIDMAS.IDSTAT` | Status aktywny/nieaktywny dostawcy, pobierany z `SupplierPartyMaster/Status/Code`. |
| `bank_id` | `CBANAC.BCBKNO` | Domyślne konto bankowe, pobierane z *ostatniej* `FinancialParty`. Włącz `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC`, aby zsynchronizować każdą `FinancialParty` w tabeli `supplier_account`. |

## Sync.RemitToPartyMaster

→ Tabela danych głównych DocBits: **SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//RemitToPartyMaster/PartyIDs/ID",
            "variationID": "//RemitToPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//RemitToPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//RemitToPartyMaster/PartyIDs/TaxID",
            "bank_id": "//RemitToPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
            "status": "//RemitToPartyMaster/Status/Code",
        }
```

### Referencja pól

| Pole DocBits | Źródło M3 | Opis |
|---|---|---|
| `sharedCONO` / `sharedSUNO` | Firma M3 / `CIDMAS.IDSUNO` | Ta sama semantyka co w `SupplierPartyMaster`. Łączy się z tym samym wierszem `supplier_header`. |
| `variationID` | Atrybut BOD | Przechowywany jako `variation_id_remit_to_party` — śledzony niezależnie od `variationID` SupplierPartyMaster. |
| `supplierName` | `CIDMAS.IDSUNM` | Nazwa wyświetlana strony remit-to. Zapisuje do współdzielonej kolumny `supplier_name`. |
| `phone` | `CIDREF.IRPHNO` | Numer telefonu z bloku komunikacji remit-to. |
| `vatNo` | `CIDMAS.IDCORG` | Identyfikator VAT strony remit-to. |
| `bank_id` | `CBANAC.BCBKNO` | Konto bankowe remit-to (`FinancialParty[last()]`). Stosuje się ta sama preferencja multi-bank. |
| `status` | `CIDMAS.IDSTAT` | Status aktywny/nieaktywny strony remit-to. |

## Jak oba BOD-y współpracują na współdzielonej tabeli `SUPPLIER`

Oba BOD-y wypełniają ten sam wiersz `supplier_header`. Dla pól, które współdzielą (`supplierName`, `phone`, `vatNo`, `bank_id`, `status`), DocBits stosuje następujące reguły:

1. Znajdź wiersz przez `(customer_number = sharedCONO, supplier_number = sharedSUNO)`.
2. Porównaj przychodzące `variationID` z przechowywanym `variationID` *dla tego samego typu BOD*.
3. Jeśli przychodzące `variationID` jest większe (lub `0`, force-update), zaktualizuj pola należące do tego BOD. W przeciwnym razie odrzuć BOD.
4. `variationID` drugiego typu BOD nie jest naruszane; jego wcześniej przechowywane wartości pozostają na miejscu.

Wiersze `supplier_address` i `supplier_account` powiązane z dostawcą są usuwane i ponownie wstawiane przy aktualizacji, dzięki czemu tabele wtórne zawsze odzwierciedlają najnowszy BOD.

## Częste pytania

### Dlaczego DocBits śledzi CONO, jeśli wszyscy moi dostawcy pochodzą z jednej firmy M3?

Routing CONO jest obowiązkowy, ponieważ DocBits jest z założenia multi-tenant: organizacja może pobierać BOD-y z wielu firm M3. CONO jest częścią klucza dopasowania, aby dostawcy z różnych firm się nie zderzali. Przy jednej firmie możesz zignorować wartość, ale kolumna klucza i tak jest wypełniana.

### Oba BOD-y zapisują w tym samym wierszu dostawcy — czy ostatni BOD nadpisuje wszystko?

Nie. Każdy typ BOD posiada tylko pola, które wysyła, a aktualizacje są sterowane niezależnym `variationID`. SupplierPartyMaster, który zmienia tylko nazwę dostawcy, nie cofa numeru telefonu, który zapisał późniejszy RemitToPartyMaster.

### `Supplier Categories` i `eam.UDFCHAR06` nigdy nie są dostarczane przez mój M3 — co robić?

Oba to rozszerzenia UserArea specyficzne dla klienta. Bez rozszerzenia kolumny pozostają NULL i żadna funkcja DocBits od nich nie zależy. Włącz logikę daty rabatu tylko wtedy, gdy twój M3 jest skonfigurowany do emitowania `eam.UDFCHAR06`.

### Czy `vatNo` powinno filtrować po `schemeName='TaxIdentificationNumber'`?

Ścieżka pobierania BOD M3 obecnie czyta `PartyIDs/TaxID` bez filtra `schemeName`. Filtr jest używany w ścieżkach XSLT e-faktury (Facturae, XRechnung, KSeF), nie w pobieraniu M3. Jeśli twój M3 emituje wiele elementów TaxID z różnymi atrybutami `schemeName`, skontaktuj się z nami z przykładowym BOD-em, zanim zaufasz zachowaniu bez filtra.

### Chcę synchronizować wszystkie konta bankowe dostawcy, nie tylko ostatnie. Jak?

Włącz preferencję `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC`. Z włączoną flagą każda `FinancialParty` z BOD jest zapisywana w tabeli `supplier_account` (IBAN, ID konta finansowego, kod waluty, wskaźnik preferencji). Kolumna legacy `bank_id` w nagłówku nadal przechowuje ostatni wpis dla wstecznej kompatybilności.
