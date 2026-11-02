# Pour les développeurs

Cette page s'adresse aux développeurs et aux responsables CI qui écrivent des modèles en JSON ou démarrent des tests depuis du code.

## Le JSON d'un modèle en bref

Un modèle est un document JSON (schema version 1 ; les schemas 1.1 à 1.3 ajoutent d'autres étapes et paramètres). Exportez n'importe quel modèle avec l'icône de téléchargement pour voir un exemple complet.

```json
{
  "schemaVersion": 1,
  "id": "my-testing-page-check",
  "name": "Testing page check",
  "category": "smoke",
  "version": "1.0.0",
  "timeoutMs": 60000,
  "allowWrites": false,
  "params": {
    "document_id": { "type": "string", "required": true, "description": "Document to open" }
  },
  "steps": [
    { "id": "open", "action": "navigate", "route": "/settings/testing" },
    { "id": "badge", "action": "waitFor", "target": "testing.environment-badge", "state": "visible" }
  ]
}
```

* `id` et `version` identifient un modèle ; une version enregistrée ne change jamais, enregistrez les modifications sous une nouvelle `version`.
* `params` déclare les valeurs qu'une entrée fournit ; les étapes y font référence avec `{{params.<name>}}`. À partir du schema 1.3, une étape peut mémoriser une valeur (`captureValue`, `as`) et les étapes suivantes l'utilisent sous la forme `{{vars.<name>}}`.
* `section` (`prepare`, `check`, `cleanup`) range une étape dans une phase. À partir du schema 1.3, les étapes `cleanup` doivent être les dernières étapes et s'exécutent même après un échec. `reload` (schema 1.3) recharge la page et l'exécution se poursuit ensuite.
* `allowWrites: true` est obligatoire pour les modèles qui téléversent, exportent, suppriment ou approuvent.
* Les étapes désignent les éléments par des ID de test stables (`target`), jamais par le texte visible, de sorte qu'un modèle fonctionne dans toutes les langues de l'interface.
* Validez avant d'enregistrer : **Importer du JSON → Valider**, ou `POST /live-tests/validate`.

## Démarrer une entrée via REST ou Playwright

Prérequis : un jeton d'administrateur de l'organisation, l'ID de l'organisation, l'ID de l'entrée et le `session_id` d'un onglet de navigateur
pour lequel **Autoriser les démarrages de l'extérieur** est activé.

```http
POST https://eu.api.docbits.com/testing/start
Authorization: Bearer <token>
X-ORG-ID: <organisation id>
Content-Type: application/json

{ "input_id": "<input id>", "session_id": "<session id>", "source": "playwright" }
```

La réponse est `202` avec `log_id`, `run_id` et `status`. Interrogez `GET /testing/logs/<log_id>` jusqu'à ce que le résultat soit définitif.
Ajoutez `"confirm_writes": true` uniquement pour un modèle qui écrit des données, et seulement si c'est voulu.

```ts
// Playwright test (API request context)
const res = await request.post(`${API}/testing/start`, {
  headers: { Authorization: `Bearer ${token}`, 'X-ORG-ID': orgId },
  data: { input_id: inputId, session_id: sessionId, source: 'playwright' },
});
expect(res.status()).toBe(202);
const { log_id } = await res.json();
// poll `${API}/testing/logs/${log_id}` until the result is PASS, FAIL or BLOCKED
```

Utilisez l'hôte d'API de votre région (voir [DocBits MCP](../../../../advanced-functions-and-tools/docbits-mcp/README.md) pour la liste des hôtes).
CSV des journaux : `GET /testing/logs/export.csv` (mêmes filtres que la liste) et `GET /testing/logs/<log_id>/export.csv`.

## Démarrer via MCP

Le serveur MCP DocBits propose les outils Testing `testing_list_templates`, `testing_list_inputs`, `testing_start`,
`testing_get_log` et `testing_list_logs`, ainsi que `list_test_sessions` pour les onglets enregistrés. `testing_start` exige un
`session_id` explicite ; `confirm_writes` n'est défini qu'une fois que l'utilisateur a donné son accord. Les valeurs confidentielles sont transmises pour l'exécution
uniquement et ne sont jamais stockées.

## Limites de l'exécuteur du navigateur

* Les tests s'exécutent en tant que personne ayant enregistré l'onglet : pas de connexion, pas de changement de rôle.
* Un rechargement complet de la page met fin à l'exécution, sauf l'étape `reload` propre au modèle (schema 1.3).
* Les boîtes de dialogue natives du navigateur (sélecteur de fichiers, impression, alertes) ne peuvent pas être pilotées ; les téléversements de fichiers utilisent les fichiers de l'organisation ou les fichiers de test du serveur.
* Les étapes de capture d'écran sont ignorées (l'exécution devient **Bloqué**).
Pour tout ce qui va au-delà, utilisez directement Playwright.
