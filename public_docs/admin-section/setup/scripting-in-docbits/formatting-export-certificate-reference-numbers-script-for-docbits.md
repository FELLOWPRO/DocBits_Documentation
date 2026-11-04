# Mise en forme du script de numéros de référence d'exportation pour Docbits

Ce document décrit le script "Mise en forme des numéros de référence d'exportation de certificat", visant à normaliser les numéros de référence sur l'ensemble des certificats d'exportation dans Docbits. Une mise en forme appropriée garantit que les numéros de référence sont conformes aux exigences des systèmes externes ou réglementaires.

### Objectif

L'objectif principal du script est de formater les numéros de référence sur les certificats d'exportation, en veillant à ce qu'ils respectent une longueur prédéfinie en les complétant avec des zéros initiaux. Cette cohérence contribue à maintenir un format standardisé pour tous les documents d'exportation traités via Docbits.

### Aperçu du script

Le script identifie le champ `reference_number` dans un certificat d'exportation, vérifie sa longueur, et si nécessaire, complète le numéro avec des zéros initiaux pour garantir qu'il respecte l'exigence de longueur minimale.

#### Extrait de code
```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Ensure the reference number meets a minimum length of 10 characters
if len(ref_number) < 10:
ref_number = ref_number.zfill(10)
set_field_value(fields_dict, 'reference_number', ref_number)
```

