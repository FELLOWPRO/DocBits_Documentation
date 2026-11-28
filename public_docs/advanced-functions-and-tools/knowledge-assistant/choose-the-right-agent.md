# Choose the right agent

In **Chat** you choose an **agent** below the input field. The agent decides how your question is answered: with one quick look into your documents, or in several steps with tools. This page explains the five built-in agents and when to use which. The agents of the industry templates are covered at the end.

{% hint style="info" %}
We tested the assistants of the industry templates in detail. We did not test the five built-in agents systematically. Their descriptions below follow how they are set up. Check an answer against its source, whichever agent you use.
{% endhint %}

## The five built-in agents

<!-- sources: fork rag-dev tag 348516a, config/builtin_agents.yaml (agents: lines 11-181 and 183-224); config/prompt_templates/system_prompt.yaml 3-28; config/prompt_templates/agent_system_prompt.yaml 53-79, 81-106, 217-232; internal/types/custom_agent.go 159-165; frontend/src/utils/tool-capabilities.ts 77-93 -->

| Agent | Use it for | How it works | Speed and cost (rough) | Needs | Limits |
| --- | --- | --- | --- | --- | --- |
| **Quick Answer** (default) | A question about one or several documents: a value, a clause, a date. | Looks up the best passages in your knowledge bases and answers from them in one pass. Rewrites the question first to find more. <!-- builtin_agents.yaml 30-52: agent_mode quick-answer, enable_rewrite, enable_query_expansion --> | Usually the fastest agent. <!-- quick-answer is the single-pass RAG mode, custom_agent.go 159; ReAct loop of the others: builtin_agents.yaml 74-79 --> | Documents in a knowledge base. | One pass: it does not plan or compare step by step. Open the source to check the value. |
| **Smart Reasoning** | A question that needs several steps: compare documents, follow up on a first result, read a document in full. | Works in a loop: it thinks, searches, reads documents and repeats until it can answer. It can also look at the knowledge graph and ask you a question. <!-- builtin_agents.yaml 74-87: agent_mode smart-reasoning, max_iterations 50, allowed_tools search_knowledge, read_document, list_documents, query_knowledge_graph, ask_user --> | Generally slower than Quick Answer, because it works in several steps and calls the model more than once. | Documents in a knowledge base. | Can take longer and use more steps than the question needs. For a simple lookup use Quick Answer. |
| **Wiki Questioner** | Questions on a knowledge base that has a **Wiki**: generated, linked summary pages of your documents. | Searches and reads the Wiki pages and follows links. For exact quotes it opens the original document. <!-- agent_system_prompt.yaml 81-106; builtin_agents.yaml 203-215: wiki_search, wiki_read_page, read_document, wiki_flag_issue --> | Multi-step, like Smart Reasoning. | A knowledge base with the indexing "Wiki". <!-- tool-capabilities.ts 81: wiki_search needs the wiki capability --> | On a knowledge base without a Wiki it has nothing to search, as on the industry templates. |
| **DocBits Data Analyst** | Figures from a spreadsheet: totals, averages, shares, counts in a **CSV or Excel** document. | Reads the table structure, then calculates with read-only SQL queries instead of estimating. It states assumptions and checks that totals add up. <!-- builtin_agents.yaml 157-175: supported_file_types csv, xlsx; allowed_tools data_schema, data_analysis, ask_user; reflection_enabled true; agent_system_prompt.yaml 53-79: DuckDB, read-only query --> | Multi-step; the calculation is done by a query, not by the model. | A CSV or Excel document in a knowledge base. | Works on CSV and Excel files only. It is not a replacement for the DocBits dashboard. |
| **Knowledge Graph Expert** | Questions about **relationships across documents**: which contracts a party has, who is surety, which subsidiaries are involved. | Looks up the entity in the knowledge graph, then checks every name, number and date against the source passages. Falls back to a text search if the graph gives nothing. <!-- agent_system_prompt.yaml 217-232; builtin_agents.yaml 123-127: query_knowledge_graph, search_knowledge, read_document, list_documents --> | Multi-step. | A knowledge base with a **knowledge graph**. <!-- tool-capabilities.ts 77: query_knowledge_graph needs the graph capability --> | Only as good as the graph. Without a graph it is a text search. Does not give legal advice. |

## Which agent should I use?

1. **Is it a question about a value, a clause or a date in your documents?** Use **Quick Answer**.
2. **Does the answer need several steps, for example comparing two versions or following a reference?** Use **Smart Reasoning**, or an assistant of your industry template.
3. **Is the data a CSV or Excel table and do you need calculated figures?** Use **DocBits Data Analyst**.
4. **Does your knowledge base have a Wiki and do you want an overview or linked background?** Use **Wiki Questioner**.
5. **Do you ask how people, companies and contracts are connected across documents, and the knowledge base has a knowledge graph?** Use **Knowledge Graph Expert**.

If you are unsure, start with **Quick Answer** or the assistant of your template, and open the source.

## Assistants of the industry templates

The **Custom Agents** in the list are the assistants of your industry templates (see [Industry templates](industry-templates/README.md)). They are ready for the documents of one industry: each has fixed instructions and works with the knowledge bases of its template. All of them work in several steps and use search, reading documents and listing documents; some can also ask you a question. <!-- docbits/templates/*/agents.yaml: 24 agents, all mode smart-reasoning, tools search_knowledge, read_document, list_documents, 16 with ask_user -->

When you choose one, its knowledge bases appear as chips above the input field. For questions on the documents of your industry, choose the matching assistant instead of a built-in agent.

## Choose the knowledge bases

The built-in agents are set up to search all knowledge bases you may read. <!-- builtin_agents.yaml: kb_selection_mode "all" for the five agents (lines 40, 80, 121, 164, 209) --> The chips above the input field show which knowledge bases are used; you can remove one with its **×** to narrow the search. Fewer, matching knowledge bases give more precise answers.

## Wiki and knowledge graph: what to expect

The two specialist agents only help on knowledge bases that have the matching index. In the industry templates, the knowledge bases use the standard document search ("RAG Search"); they have neither a Wiki nor a knowledge graph. <!-- docbits/templates/*/knowledge_bases.yaml: no wiki or graph setting in any of the eight templates --> The Wiki option and the knowledge graph setting are offered in the knowledge base settings, and both agents appear in the agent list. We tested Wiki and knowledge graph only on a separate demo knowledge base, not on the industry templates and not end to end. <!-- docbitsEmbed.ts 187-243: wiki not hidden; graph shown only when the backend reports the graph capability -->

## What is not available

* An **own search provider with your own key** for web search is planned and not yet available. Web search itself is optional and off by default: see [Web search](web-search.md). <!-- web search: admin switch under Functions, default off; DocOperator route without key, best effort -->
* The agents do not run code in a sandbox, do not use chat channels and do not use your own language models. See [What it can and cannot do](what-it-can-and-cannot-do.md).

## How to recognize an agent in the list

Go by the **name**; it is the same in the list and below the input field. The icons help only a little: <!-- builtin_agents.yaml avatars: 102 graph, 139 chart, 184 books; none for Quick Answer and Smart Reasoning (lines 12, 55) --> Wiki Questioner, DocBits Data Analyst and Knowledge Graph Expert show a small picture (books, bar chart, network). Quick Answer and Smart Reasoning show a plain symbol. The custom agents of the industry templates show a colored letter tile with the first letter of their name.

See also: [Tasks and where to find them](tasks-and-where-to-find-them.md#ask-a-question-and-open-the-source) and [What it can and cannot do](what-it-can-and-cannot-do.md).
