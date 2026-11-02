# DocFlow MCP

DocFlow udostepnia serwer **Model Context Protocol (MCP)**, ktory pozwala asystentom AI programistycznie zarzadzac przepływami pracy i kartami partnerskimi. Kazdy klient kompatybilny z MCP — Claude Code, Claude Desktop, OpenAI Codex lub niestandardowe integracje — moze sie podlaczyc i korzystac z tych narzedzi.

## Co mozesz zrobic?

Za pomoca DocFlow MCP mozesz:

- **Listowac, tworzyc, aktualizowac i usuwac** zaawansowane przepływy pracy
- **Testowac przepływy pracy** z rzeczywistymi lub fikcyjnymi dokumentami
- **Budowac niestandardowe karty** uzywajac Partner Card SDK
- **Walidowac, testowac, zatwierdzac i zarzadzac** zgloszeniami kart partnerskich
- **Importowac karty** bezposrednio z repozytoriow GitHub

## Przeglad narzedzi

DocFlow MCP grupuje swoje narzedzia w nastepujace kategorie. Wiekszosc narzedzi Workflow i Card SDK odwzorowuje istniejace endpointy REST — tam znajdziesz pelna dokumentacje API. Ponizsze kategorie obejmuja specyficzna dla MCP powierzchnie oraz koncepcje przepływow pracy potrzebne do korzystania z niej.

### Zarzadzanie przepływami pracy

| Narzedzie | Opis |
|------|-------------|
| `list_workflows` | Wyswietla wszystkie przepływy pracy biezacej organizacji |
| `get_workflow` | Pobiera szczegoly konkretnego przepływu pracy po ID |
| `create_advanced_workflow` | Tworzy nowy zaawansowany przepływ pracy z wezlami i krawedziami |
| `update_advanced_workflow` | Aktualizuje istniejacy zaawansowany przepływ pracy |
| `delete_workflow` | Usuwa przepływ pracy po ID |

### Testowanie przepływow pracy

| Narzedzie | Opis |
|------|-------------|
| `test_advanced_workflow` | Testuje wykonanie zaawansowanego przepływu pracy, opcjonalnie z dokumentem |
| `list_test_scenarios` | Wyswietla wszystkie scenariusze testowe przepływow pracy |
| `list_cards` | Wyswietla dostepne karty / akcje przepływu pracy |

### Zarzadzanie Card SDK

| Narzedzie | Opis |
|------|-------------|
| `sdk_list_submissions` | Wyswietla wszystkie zgloszenia kart partnerskich |
| `sdk_get_submission_status` | Pobiera status walidacji zgloszenia |
| `sdk_approve_card` | Zatwierdza zwalidowana karte partnerska (admin) |
| `sdk_reject_card` | Odrzuca zgloszenie karty partnerskiej (admin) |
| `sdk_delete_submission` | Dezaktywuje lub usuwa zgloszenie (admin) |
| `sdk_list_cards_picker` | Wyswietla wszystkie wlaczone karty z flagami rol |

### Rozwoj Card SDK

| Narzedzie | Opis |
|------|-------------|
| `sdk_create_card` | Tworzy nowa karte partnerska z kodu zrodlowego |
| `sdk_validate_card` | Uruchamia pipeline walidacyjny bez zapisywania |
| `sdk_test_card` | Wykonuje karte w srodowisku sandbox |
| `sdk_import_github` | Importuje aplikacje partnera z GitHub |

## Pierwsze kroki

1. [Skonfiguruj swojego klienta MCP](setup-and-configuration.md)
2. Poznaj [Workflow Tools](workflow-tools.md)
3. Zapoznaj sie z [Card SDK Tools](card-sdk-tools.md)
4. Przejrzyj [przyklady](examples.md) end-to-end

{% hint style="info" %}
DocFlow MCP uzywa transportu **Streamable HTTP**. Endpoint serwera to `/v3/mcp/` na hoscie DocFlow (np. `https://docflow.docbits.com/v3/mcp/`). Pelna liste URL znajdziesz w [Instalacja i Konfiguracja](setup-and-configuration.md).
{% endhint %}
