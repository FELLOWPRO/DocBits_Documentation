---
description: "P1 : vérifier les appels API et l’utilisation des réponses"
---

# P1 : vérifier les appels API et l’utilisation des réponses

**Call API** v2 ajoute son chemin configuré à la base API DocBits et utilise l’organisation courante. **Send HTTPS Request** v2 emploie une URL externe et ses propres en-têtes. Une URL externe complète ne remplace pas un chemin Call API. Les deux cartes simulent l’envoi dans Advanced Test.

L’action HTTPS examinée journalise statut et texte de réponse, mais n’expose pas de stockage JSON librement nommé aux cartes suivantes. Call API convertit le texte de réponse en booléen. HTTP 200, JSON valide et traitement métier ultérieur réussi nécessitent donc des preuves distinctes. N’inventez pas de syntaxe telle que `api.response.cost_center`.

Pour un retour externe `{"cost_center":"4711"}`, convenez d’une écriture ou d’un callback explicitement pris en charge vers un champ documentaire. Vérifiez le champ enregistré et lisez-le dans l’exécution suivante prévue. Le transfert direct exige une carte ou extension au contrat de sortie documenté. Du JSON configuré ne prouve pas non plus les octets JSON effectivement envoyés.

Utilisez votre propre cible de test et inspectez méthode, en-têtes, corps réel, statut et schéma. Couvrez 4xx, 5xx, délai dépassé, JSON invalide et double déclenchement. Ne répétez une écriture qu’après contrôle de la première réception. L’URL d’exemple est un emplacement réservé et n’a pas été testée comme service accessible.

## Cartes et paramètres d’exemple

Ces valeurs décrivent des paramètres de cartes, pas un workflow complet importable. Remplacez YOUR_* par vos choix de test. Le concepteur gère l’ID caché de l’appelant. Catalogue : Dev, DocFlow 2.10.38, 21 octobre 2026 ; contrôlez versions et droits de votre organisation.

### `call_api` · v2

Identité: `6ca5e621-af72-4f55-aa2e-b3caa288722a`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `params` | `params:str` | `"{}"` |
| `api_endpoint` | `api_endpoint:str` | `"YOUR_RELATIVE_API_PATH"` |
| `data` | `data:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

### `action_https_request` · v2

Identité: `18d06ca4-3aca-4e49-b75c-566ade2fcb10`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `data` | `data` | `"{}"` |
| `params` | `params` | `"{}"` |
| `url` | `url:str` | `"https://training.example.invalid/status"` |
| `headers` | `headers:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

## Cas de test métier

| Cas | Entrée / configuration | Résultat attendu |
| --- | --- | --- |
| API-01 | Advanced Test | simulé ; aucune preuve de livraison |
| API-02 | HTTPS: 4xx / 5xx | error |
| API-03 | timeout | vérifier la réception avant répétition |
| API-04 | {"cost_center":"4711"} | aucun api.response.cost_center automatique |
| API-05 | POST × 2 | vérifier les doublons côté cible |

## Preuves et limites

Paramètres et comportement ont été confrontés au catalogue Dev et au code examiné. Les cas métier constituent une procédure de recette. Aucune approbation personnelle, modification réelle ou livraison n’a été réalisée pour ce chapitre.

[Poursuivre l’apprentissage](../workflow-learning-path.md) · [Kit de formation](../workflow-training-kit.md)
