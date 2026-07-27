# Topla (Min/Maksimum/Say)

Bu politika, eşleşen tüm kuralları toplar ve ya **minimum**, **maksimum** seçer ya da oluşumları **sayar**. Yalnızca **Return Type Value** için çalışır.

**Örnek:**

| Kural | Koşul                | Döndürülen Değer |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. **Topla (min)** seçeneği seçilirse, sonuç eşleşen kuralların **Döndürülen Değerlerinin** **minimumunu** döndürür.
   * **Total Amount = 2500** girdi değeri için, kuralların değerlendirmesi şu şekilde olur:
     * **Kural 1**: Total Amount <= 1000 (eşleşmez)
     * **Kural 2**: Total Amount <= 2000 (eşleşmez)
     * **Kural 3**: Total Amount <= 3000 (eşleşir, Döndürülen Değer = 3)
     * **Kural 4**: Total Amount <= 4000 (eşleşir, Döndürülen Değer = 4)
     * **Kural 5**: Total Amount <= 5000 (eşleşir, Döndürülen Değer = 5)
   * **Eşleşen kurallar** Kural 3, Kural 4 ve Kural 5 olup, **Döndürülen Değerleri** **3, 4 ve 5**'tir.
   * **Topla (min)** politikası uygulandığından, sonuç **minimum değer** olan **3** olur.
   * **Sonuç**: **3**
2. **Topla (maks)** seçeneği seçilirse, sonuç eşleşen kuralların **Döndürülen Değerlerinin** **maksimumunu** döndürür.
   * Yukarıdaki aynı değerlendirme için sonuç şu olur:
   * **Sonuç**: **5**
3. **Topla (sayım)** seçeneği seçilirse, sonuç **eşleşen kuralların sayısını** sayar.
   * Yukarıdaki aynı değerlendirme için sonuç şu olur:
   * **Sonuç**: **3** (3 kural eşleştiği için).
