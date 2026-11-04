---
description: Jak skonfigurować PowerBI
---

# Łączenie DocBits z Power BI

Dane DocBits możesz połączyć z Power BI na dwa różne sposoby. Właściwa metoda zależy od tego, jak chcesz wykorzystać dane.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}

### Kiedy którego połączenia użyć:

* **Metoda 1: Połączenie przez ClickHouse**&#x20;
  * **Analizy dużych wolumenów danych**.
  * **Trendy historyczne i pulpity**.

{% content-ref url="powerbi/powerbi.md" %}
[powerbi.md](powerbi/powerbi.md)
{% endcontent-ref %}

* **Metoda 2: Połączenie przez bazę danych tylko do odczytu**
  * **Dane operacyjne lub niemal w czasie rzeczywistym**.
  * **Bezpośredni dostęp do bieżących tabel DocBits**.

{% content-ref url="powerbi/connect-via-read-only-database.md" %}
[connect-via-read-only-database.md](powerbi/connect-via-read-only-database.md)
{% endcontent-ref %}
