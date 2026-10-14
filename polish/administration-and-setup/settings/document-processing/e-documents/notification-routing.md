# Routing powiadomień

<figure><img src="../../../../.gitbook/assets/edoc_notification_routing.png" alt="Trasy powiadomień"><figcaption><p>Przypisywanie wyników walidacji do agentów</p></figcaption></figure>

Strona **Routing powiadomień** (**Dokumenty elektroniczne → Akcje**) przypisuje wyniki walidacji do **agentów AI Workforce**. Każdy blokujący wynik uruchamia dokładnie jednego agenta — tego, którego prefiks kodu pasuje najdłużej. Wszystko bez dopasowania wraca do domyślnego agenta powiadomień dostawcy.

## Trasy powiadomień

Wybierz, kto obsługuje każdy rodzaj problemu z fakturą. Wszystko, co nie jest wymienione, trafia do agenta domyślnego:

| Trasa | Obsługiwane wyniki |
|-------|--------------------|
| **Kolumbijskie reguły biznesowe** | Wyniki reguł biznesowych specyficznych dla Kolumbii. |
| **Niemieckie reguły biznesowe** | Wyniki reguł biznesowych specyficznych dla Niemiec. |
| **Kontrole IBAN / konta bankowego** | Wyniki dotyczące danych płatności (suma kontrolna IBAN, długość, kraj). |
| **Kontrole numeru VAT** | Wyniki dotyczące formatu numeru VAT. |
| **Wszystko inne** | Domyślny element zastępczy dla wszystkiego, co nie pasuje powyżej. |

Dla każdej trasy wybierz obsługującego agenta z listy rozwijanej. **Zaawansowane (własne reguły kodu)** umożliwia routing według dokładnego kodu wyniku, gdy potrzebujesz dokładniejszej kontroli.

## Dostępni agenci

<figure><img src="../../../../.gitbook/assets/edoc_notification_agents.png" alt="Rejestr dostępnych agentów"><figcaption><p>Rejestr agentów AI Workforce tylko do odczytu</p></figcaption></figure>

Sekcja **Dostępni agenci** to rejestr tylko do odczytu agentów AI Workforce dostarczonych z Twoim wdrożeniem, na przykład:

| Agent | Przeznaczenie |
|-------|---------------|
| **Domyślne powiadomienie dostawcy** | Ogólny e-mail powiadomienia dostawcy; agent uniwersalny, gdy żaden bardziej szczegółowy agent nie pasuje. |
| **Banking Bot** | Wyspecjalizowany szablon dla wyników danych płatności (korekty IBAN/BIC). |
| **Tax Bot** | Powiadomienie dostawcy specyficzne dla numeru VAT. |
| **Compliance Bot** | Obsługuje wyniki dotyczące zgodności. |

Każdy agent pokazuje swoje zadanie Celery oraz prefiksy kodów wyników, które obsługuje domyślnie.
