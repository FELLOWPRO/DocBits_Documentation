# DocFlow MCP

DocFlow udostepnia serwer **Model Context Protocol (MCP)**, ktory pozwala asystentom AI programistycznie zarzadzac przepływami pracy i kartami partnerskimi. Kazdy klient kompatybilny z MCP — Claude Code, Claude Desktop, OpenAI Codex lub niestandardowe integracje — moze sie podlaczyc i korzystac z tych narzedzi.

## Co mozesz zrobic?

Dzieki DocFlow MCP mozesz:

- **Wyswietlac, tworzyc, aktualizowac i usuwac** zaawansowane przeplywy pracy
- **Testowac przeplywy pracy** z prawdziwymi lub symulowanymi dokumentami
- **Budowac niestandardowe karty** przy uzyciu Partner Card SDK
- **Walidowac, testowac, zatwierdzac i zarzadzac** zgloszeniami kart partnerskich
- **Importowac karty** bezposrednio z repozytoriow GitHub

## Przeglad narzedzi

DocFlow MCP udostepnia **18 narzedzi** w czterech kategoriach:

### Zarzadzanie przepływami pracy

| Narzedzie | Opis |
|-----------|------|
| `list_workflows` | Wyswietla wszystkie przepływy pracy dla biezacej organizacji |
| `get_workflow` | Pobiera szczegoly konkretnego przepływu pracy po ID |
| `delete_workflow` | Usuwa przepływ pracy po ID |

### Testowanie przepływow pracy

| Narzedzie | Opis |
|-----------|------|
| `test_advanced_workflow` | Testuje wykonanie zaawansowanego przepływu pracy z opcjonalnym dokumentem |
| `list_test_scenarios` | Wyswietla wszystkie scenariusze testowe przepływow pracy |
| `list_cards` | Wyswietla dostepne karty/akcje przepływow pracy |

### Zarzadzanie Card SDK

| Narzedzie | Opis |
|-----------|------|
| `sdk_list_submissions` | Wyswietla wszystkie zgloszenia kart partnerskich |
| `sdk_get_submission_status` | Pobiera status walidacji zgloszenia |
| `sdk_approve_card` | Zatwierdza zwalidowana karte partnerska (administrator) |
| `sdk_reject_card` | Odrzuca zgloszenie karty partnerskiej (administrator) |
| `sdk_delete_submission` | Dezaktywuje lub usuwa zgloszenie (administrator) |
| `sdk_list_cards_picker` | Wyswietla wszystkie wlaczone karty z flagami rol |

### Rozwoj Card SDK

| Narzedzie | Opis |
|-----------|------|
| `sdk_create_card` | Tworzy nowa karte partnerska z kodu zrodlowego |
| `sdk_validate_card` | Uruchamia 5-etapowa walidacje bez zapisywania |
| `sdk_test_card` | Wykonuje karte w srodowisku sandbox |
| `sdk_import_github` | Importuje aplikacje partnerska z GitHub |

## Pierwsze kroki

1. [Skonfiguruj swojego klienta MCP](setup-and-configuration.md)
2. Poznaj [Narzedzia przepływow pracy](workflow-tools.md)
3. Odkryj [Narzedzia Card SDK](card-sdk-tools.md)
4. Postepuj wedlug kompleksowych [Przykładow](examples.md)

{% hint style="info" %}
DocFlow MCP uzywa transportu **Streamable HTTP**. Punkt koncowy serwera to `/api/mcp/` na Twoim hoscie DocBits API.
{% endhint %}
