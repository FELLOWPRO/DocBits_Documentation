# Den richtigen Agenten wählen

Im **Chat** wählen Sie unter dem Eingabefeld einen **Agenten**. Der Agent bestimmt, wie Ihre Frage beantwortet wird: mit einem schnellen Blick in Ihre Dokumente oder in mehreren Schritten mit Werkzeugen. Diese Seite erklärt die fünf integrierten Agenten und wann Sie welchen nehmen. Die Agenten der Branchenvorlagen stehen am Ende.

{% hint style="info" %}
Die Assistenten der Branchenvorlagen haben wir ausführlich getestet. Die fünf integrierten Agenten haben wir nicht systematisch getestet. Ihre Beschreibungen unten folgen ihrer Einrichtung. Prüfen Sie eine Antwort immer an der Quelle, welchen Agenten Sie auch nutzen.
{% endhint %}

## Die fünf integrierten Agenten

In der Agentenauswahl heißen sie **Schnelle Antwort**, **Intelligentes Schlussfolgern**, **Wiki Questioner**, **DocBits Data Analyst** und **Knowledge Graph Expert**. Unter dem Eingabefeld steht für den Standardagenten die Bezeichnung „Quick Answer“.

<!-- sources: fork rag-dev tag 348516a, config/builtin_agents.yaml (agents: lines 11-181 and 183-224); config/prompt_templates/system_prompt.yaml 3-28; config/prompt_templates/agent_system_prompt.yaml 53-79, 81-106, 217-232; internal/types/custom_agent.go 159-165; frontend/src/utils/tool-capabilities.ts 77-93 -->

| Agent | Wofür | So arbeitet er | Tempo und Aufwand (grob) | Voraussetzung | Grenzen |
| --- | --- | --- | --- | --- | --- |
| **Schnelle Antwort** (Quick Answer, Standard) | Eine Frage zu einem oder mehreren Dokumenten: ein Wert, eine Klausel, ein Datum. | Sucht die besten Textstellen in Ihren Wissensdatenbanken und antwortet daraus in einem Durchgang. Formuliert die Frage vorher um, um mehr zu finden. <!-- builtin_agents.yaml 30-52: agent_mode quick-answer, enable_rewrite, enable_query_expansion --> | In der Regel der schnellste Agent. <!-- quick-answer ist der einstufige RAG-Modus, custom_agent.go 159; Schleife der übrigen: builtin_agents.yaml 74-79 --> | Dokumente in einer Wissensdatenbank. | Ein Durchgang: Er plant nicht und vergleicht nicht Schritt für Schritt. Öffnen Sie die Quelle, um den Wert zu prüfen. |
| **Intelligentes Schlussfolgern** (Smart Reasoning) | Eine Frage, die mehrere Schritte braucht: Dokumente vergleichen, einem ersten Ergebnis nachgehen, ein Dokument ganz lesen. | Arbeitet in einer Schleife: Er denkt, sucht, liest Dokumente und wiederholt das, bis er antworten kann. Er kann auch den Wissensgraphen ansehen und Ihnen eine Rückfrage stellen. <!-- builtin_agents.yaml 74-87: agent_mode smart-reasoning, max_iterations 50, allowed_tools search_knowledge, read_document, list_documents, query_knowledge_graph, ask_user --> | Im Allgemeinen langsamer als Schnelle Antwort, weil er in mehreren Schritten arbeitet und das Modell mehrfach aufruft. | Dokumente in einer Wissensdatenbank. | Kann länger dauern und mehr Schritte nutzen, als die Frage braucht. Für eine einfache Suche nehmen Sie Schnelle Antwort. |
| **Wiki Questioner** | Fragen an eine Wissensdatenbank mit **Wiki**: erzeugte, verknüpfte Zusammenfassungsseiten Ihrer Dokumente. | Durchsucht und liest die Wiki-Seiten und folgt Verknüpfungen. Für genaue Zitate öffnet er das Originaldokument. <!-- agent_system_prompt.yaml 81-106; builtin_agents.yaml 203-215: wiki_search, wiki_read_page, read_document, wiki_flag_issue --> | Mehrschrittig, wie Intelligentes Schlussfolgern. | Eine Wissensdatenbank mit der Indexierung „Wiki“. <!-- tool-capabilities.ts 81: wiki_search braucht die Wiki-Fähigkeit --> | Auf einer Wissensdatenbank ohne Wiki hat er nichts zu durchsuchen, so wie bei den Branchenvorlagen. |
| **DocBits Data Analyst** | Zahlen aus einer Tabelle: Summen, Mittelwerte, Anteile, Anzahlen in einem **CSV- oder Excel-**Dokument. | Liest die Tabellenstruktur und rechnet dann mit schreibgeschützten SQL-Abfragen, statt zu schätzen. Er nennt seine Annahmen und prüft, ob Summen aufgehen. <!-- builtin_agents.yaml 157-175: supported_file_types csv, xlsx; allowed_tools data_schema, data_analysis, ask_user; reflection_enabled true; agent_system_prompt.yaml 53-79: DuckDB, read-only query --> | Mehrschrittig; die Rechnung macht eine Abfrage, nicht das Modell. | Ein CSV- oder Excel-Dokument in einer Wissensdatenbank. | Arbeitet nur mit CSV- und Excel-Dateien. Er ersetzt nicht das DocBits-Dashboard. |
| **Knowledge Graph Expert** | Fragen zu **Beziehungen über Dokumente hinweg**: welche Verträge eine Partei hat, wer Bürge ist, welche Töchter beteiligt sind. | Schlägt die Entität im Wissensgraphen nach und prüft dann jeden Namen, jede Zahl und jedes Datum an den Quellstellen. Fällt auf eine Textsuche zurück, wenn der Graph nichts liefert. <!-- agent_system_prompt.yaml 217-232; builtin_agents.yaml 123-127: query_knowledge_graph, search_knowledge, read_document, list_documents --> | Mehrschrittig. | Eine Wissensdatenbank mit **Wissensgraph**. <!-- tool-capabilities.ts 77: query_knowledge_graph braucht die Graph-Fähigkeit --> | Nur so gut wie der Graph. Ohne Graph ist er eine Textsuche. Er gibt keine Rechtsberatung. |

## Welchen Agenten soll ich nehmen?

1. **Ist es eine Frage nach einem Wert, einer Klausel oder einem Datum in Ihren Dokumenten?** Nehmen Sie **Schnelle Antwort**.
2. **Braucht die Antwort mehrere Schritte, zum Beispiel zwei Fassungen vergleichen oder einem Verweis folgen?** Nehmen Sie **Intelligentes Schlussfolgern** oder einen Assistenten Ihrer Branchenvorlage.
3. **Ist die Datenquelle eine CSV- oder Excel-Tabelle und brauchen Sie berechnete Zahlen?** Nehmen Sie **DocBits Data Analyst**.
4. **Hat Ihre Wissensdatenbank ein Wiki und möchten Sie einen Überblick oder verknüpften Hintergrund?** Nehmen Sie **Wiki Questioner**.
5. **Fragen Sie, wie Personen, Firmen und Verträge über Dokumente hinweg zusammenhängen, und die Wissensdatenbank hat einen Wissensgraphen?** Nehmen Sie **Knowledge Graph Expert**.

Sind Sie unsicher, beginnen Sie mit **Schnelle Antwort** oder dem Assistenten Ihrer Vorlage und öffnen Sie die Quelle.

## Assistenten der Branchenvorlagen

Die **Eigenen Agenten** in der Liste sind die Assistenten Ihrer Branchenvorlagen (siehe [Branchenvorlagen](industry-templates/README.md)). Sie sind auf die Dokumente einer Branche eingerichtet: Jeder hat feste Anweisungen und arbeitet mit den Wissensdatenbanken seiner Vorlage. Alle arbeiten in mehreren Schritten und nutzen Suchen, Dokumente lesen und Dokumente auflisten; einige können Ihnen auch eine Rückfrage stellen. <!-- docbits/templates/*/agents.yaml: 24 Agenten, alle mode smart-reasoning, Werkzeuge search_knowledge, read_document, list_documents, 16 mit ask_user -->

Wählen Sie einen davon, erscheinen seine Wissensdatenbanken als Chips über dem Eingabefeld. Für Fragen zu den Dokumenten Ihrer Branche wählen Sie den passenden Assistenten statt eines integrierten Agenten.

## Die Wissensdatenbanken wählen

Die integrierten Agenten sind so eingerichtet, dass sie alle Wissensdatenbanken durchsuchen, die Sie lesen dürfen. <!-- builtin_agents.yaml: kb_selection_mode "all" bei den fünf Agenten (Zeilen 40, 80, 121, 164, 209) --> Die Chips über dem Eingabefeld zeigen, welche Wissensdatenbanken genutzt werden; mit dem **×** entfernen Sie eine und grenzen die Suche ein. Wenige, passende Wissensdatenbanken liefern genauere Antworten.

## Wiki und Wissensgraph: was Sie erwarten können

Die beiden Spezialagenten helfen nur bei Wissensdatenbanken, die den passenden Index haben. In den Branchenvorlagen nutzen die Wissensdatenbanken die normale Dokumentensuche („RAG Search“); sie haben weder ein Wiki noch einen Wissensgraphen. <!-- docbits/templates/*/knowledge_bases.yaml: keine Wiki- oder Graph-Einstellung in einer der acht Vorlagen --> Die Wiki-Option und die Einstellung für den Wissensgraphen werden in den Einstellungen der Wissensdatenbank angeboten, und beide Agenten erscheinen in der Agentenliste. Wiki und Wissensgraph haben wir nur an einer eigenen Demo-Wissensdatenbank getestet, nicht an den Branchenvorlagen und nicht durchgängig. <!-- docbitsEmbed.ts 187-243: Wiki nicht ausgeblendet; Graph nur sichtbar, wenn das Backend die Graph-Fähigkeit meldet -->

## Was nicht verfügbar ist

* **Websuche** wird im Wissensassistenten nicht angeboten. <!-- ROADMAP-RAG.md Zeile 10: Websuche nicht gebaut; Input-field.vue 496-507: Suchknopf nur mit konfigurierter Suchmaschine -->
* Die Agenten führen keinen Code in einer Sandbox aus, nutzen keine Chat-Kanäle und keine eigenen Sprachmodelle. Siehe [Was er kann und was nicht](what-it-can-and-cannot-do.md).

## Woran Sie einen Agenten in der Liste erkennen

Orientieren Sie sich am **Namen**; er ist in der Liste und unter dem Eingabefeld derselbe. Die Symbole helfen nur wenig: <!-- builtin_agents.yaml avatars: 102 Graph, 139 Diagramm, 184 Bücher; keine bei Quick Answer und Smart Reasoning (Zeilen 12, 55) --> Wiki Questioner, DocBits Data Analyst und Knowledge Graph Expert zeigen ein kleines Bild (Bücher, Balkendiagramm, Netz). Schnelle Antwort und Intelligentes Schlussfolgern zeigen ein schlichtes Symbol. Die eigenen Agenten der Branchenvorlagen zeigen eine farbige Kachel mit dem Anfangsbuchstaben ihres Namens.

Siehe auch: [Aufgaben und wo Sie sie finden](tasks-and-where-to-find-them.md#eine-frage-stellen-und-die-quelle-öffnen) und [Was er kann und was nicht](what-it-can-and-cannot-do.md).
