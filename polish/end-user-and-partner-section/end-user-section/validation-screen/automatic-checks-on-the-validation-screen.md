# Automatyczne Kontrole na Ekranie Walidacji

## Przegląd

Domyślnie, określone pola w procesie walidacji pól są automatycznie sprawdzane poprzez weryfikację ich wartości za pomocą formuł opartych na innych wyodrębnionych wartościach. Na tej stronie znajdziesz formularze używane do tych automatycznych obliczeń.

Zawsze możesz zweryfikować używaną formułę, najeżdżając kursorem na ikonę informacji.

<figure><img src="../../../.gitbook/assets/automatic_checks_1.png" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**Uwaga:**</mark> Ikona informacji jest widoczna tylko wtedy, gdy wartość została wyodrębniona dla odpowiadającego pola.

## Formularze do automatycznych kontroli:

### Kwota netto:

```
Kwota netto = Kwota podatku * 100 / Stawka VAT 
```

### Stawka VAT:

```
Stawka VAT = Kwota podatku * 100 / Kwota netto 
```

### Kwota podatku:

```
Kwota podatku = Kwota netto + Stawka VAT / 100
```

### Kwota netto zmniejszona:

```
Kwota netto zmniejszona = Obniżona kwota podatku * 100 / Obniżona stawka VAT
```

### Obniżona stawka VAT:

```
Obniżona stawka VAT = Obniżona kwota podatku * 100 / Kwota netto zmniejszona
```

### Obniżona kwota podatku:

```
Obniżona kwota podatku = Obniżona kwota podatku + Obniżona stawka VAT / 100
```

### Całkowita kwota netto:

```
Całkowita kwota netto = Kwota netto + Obniżona kwota podatku + Kwota netto wolna
```

### Całkowita kwota netto w USA:

```
Całkowita kwota netto w USA = Kwota netto + Koszty wysyłki + Opłaty różne + Dodatkowa kwota
```

### Całkowita kwota podatku:

```
Całkowita kwota podatku = Kwota podatku + Obniżona kwota podatku + Kwota podatku wolna 
```

### Całkowita kwota:

```
Całkowita kwota = Kwota netto + Kwota podatku
```

<mark style="color:red;">**Uwaga:**</mark> Jeśli wyodrębniona wartość i zweryfikowana wartość się nie zgadzają, dokument nie może być przetwarzany dalej. Pojawi się błąd **Niezgodność kwot** dla odpowiadającego pola.
