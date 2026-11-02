---
description: Prise en charge des documents électroniques MEXICO CFDI 3.3 dans DocBits
---

# 🇲🇽 MEXICO CFDI 3.3

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [Mexique](countries/mexico.md). Vérifiez l’espace de noms, la version et TipoDeComprobante. Un montant négatif ne suffit pas à identifier un avoir ; l’analyse du fichier ne certifie pas la validation par le SAT.
{% endhint %}

| Propriété | Valeur |
| --------- | ------ |
| **Pays / Région** | Mexique |
| **Types de documents** | Facture, Note de crédit, Reçu de paiement |
| **Format** | XML |
| **Norme** | CFDI 3.3 (Comprobante Fiscal Digital por Internet) |

CFDI 3.3 est la génération précédente de la norme mexicaine de reçu fiscal numérique émise par le SAT (Servicio de Administración Tributaria). Bien qu'elle ait été remplacée par CFDI 4.0, de nombreuses factures historiques utilisent encore cette version. Elle comprend l'UUID (folio fiscal), les identifiants RFC et les calculs de taxes IEPS/IVA.

## Statut de prise en charge

| Composant | Statut |
| --------- | ------ |
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/mexico-cfdi-3-3-preview.png" alt="Aperçu d'une facture Mexico CFDI 3.3 dans DocBits"><figcaption><p>Aperçu DocBits par défaut d'une facture Mexico CFDI 3.3</p></figcaption></figure>

## Voir aussi

* [Documents électroniques pris en charge](./)
