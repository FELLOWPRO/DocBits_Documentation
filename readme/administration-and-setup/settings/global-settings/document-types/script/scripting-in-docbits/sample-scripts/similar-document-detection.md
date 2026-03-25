# Detecção de Documentos Semelhantes (Pesquisa Vetorial)

{% hint style="info" %}
**Disponível a partir da versão 11.48.0** — Requer licença `OPENSEARCH_ENABLED`.
{% endhint %}

## O que faz este script?

Utiliza pesquisa de semelhança baseada em vetores para encontrar documentos semanticamente semelhantes ao atual. Se um documento com mais de 95% de semelhança for encontrado, o número da fatura é sinalizado como potencialmente fraudulento ou duplicado.

## Gatilho

`AFTER_FORMATTING` no tipo de documento **INVOICE**

## Script Completo

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)

for doc in similar:
    if doc["similarity_percent"] > 95:
        set_field_as_invalid(
            document_data, "invoice_id",
            f"95%+ similar to: {doc['name']} (Score: {doc['similarity_percent']}%)"
        )
        break
```

## Explicação Passo a Passo

1. **Obter o ID do documento atual** de `document_json`
2. **Encontrar documentos semelhantes** com `vector_search()` retornando os 5 vizinhos mais próximos
3. **Verificar limiar de semelhança**: Se algum documento exceder 95% de semelhança, sinalizá-lo
4. **Marcar como inválido** com o nome do documento semelhante e a pontuação de semelhança

## Como Funciona a Pesquisa Vetorial

O texto OCR de cada documento é convertido num embedding vetorial de 384 dimensões quando indexado. `vector_search()` encontra os vizinhos mais próximos neste espaço vetorial usando k-NN (k-Nearest Neighbors), retornando documentos cujo conteúdo é semanticamente semelhante — mesmo que as palavras exatas sejam diferentes.

**Casos de uso:**
- Detecção de fraude (faturas quase idênticas de diferentes "fornecedores")
- Detecção de duplicados que vai além da correspondência exata de texto
- Encontrar documentos relacionados em diferentes formatos ou idiomas

## Funções Utilizadas

- [vector\_search()](../fulltext-search-functions.md#vector\_search) — Encontrar documentos semanticamente semelhantes
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Mostrar erro de validação
