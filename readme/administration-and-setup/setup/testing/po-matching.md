# Dopasowanie zamówień zakupu

Jeśli chodzi o testowanie zgodnej konfiguracji PO, będziesz musiał utworzyć zamówienie zakupu w LN/M3, aby sprawdzić, czy INFOR jest zsynchronizowane z DocBits.

## Tworzenie zamówienia zakupu w INFOR

{% embed url="https://youtu.be/hn_bkeUMxJg" %}
{% endembed %}


* LN: https://docs.infor.com/ln/10.4/en-us/lnolh/docs/ln\_10.4\_procpoug\_\_en-us.pdf&#x20;
* M3: https://docs.infor.com/m3udi/16.x/en-us/m3beud/default.html?helpcontent=ois610.html&#x20;

Po utworzeniu zamówienia przejdź do Ustawienia → Wyszukiwanie danych podstawowych i wyszukaj numer zamówienia zakupu dla właśnie utworzonego PO, który powinien teraz pojawiać się w danych podstawowych zamówienia w DocBits.

![Tabela Purchase order w danych głównych DocBits z kolumnami Warehouse Id, Supplier Name, Purchase Order Number, Line Number i Quantity](https://lh7-us.googleusercontent.com/JKGJdww6uF6U5mc1s1X\_uCcEMPYeqcikfrFOFjxpxpuaNjw-XmzNmIV2G2x6R-ZpwN2KlZACQe5Hs\_UB26klGU5XZyu6srVVLPVkS9AgEDZ1SO75YF-4ZTIt-aAuxoyyoW5sNPLsl0UxXwk193QNrFs)

Powinieneś zobaczyć tutaj swój unikalny numer PO, co oznacza, że DocBits i INFOR są poprawnie zsynchronizowane.

Teraz prześlij fakturę odpowiadającą ilości i cenom jednostkowym utworzonego zamówienia zakupu. Zatwierdź dokument i wybierz Dopasowanie zamówień zakupu na ekranie walidacji.

Pozycje zamówienia zakupu i faktury powinny zostać automatycznie dopasowane. Następnie wybierz eksport i sprawdź, czy dokument jest eksportowany bez błędów. W razie błędu eksportu utwórz zgłoszenie do zespołu wsparcia DocBits. Instrukcję tworzenia zgłoszeń znajdziesz w dokumentacji z przeglądem funkcji DocBits.

\
