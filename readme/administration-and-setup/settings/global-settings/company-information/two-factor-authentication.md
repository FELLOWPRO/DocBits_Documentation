# Authentification à deux facteurs (Admin)

## Vue d'ensemble

En tant qu'administrateur d'organisation, vous pouvez **exiger que chaque membre utilise l'authentification à deux facteurs (2FA)** lorsqu'il se connecte avec un mot de passe. Lorsque l'exigence est activée, un membre qui n'a pas encore configuré de second facteur est guidé à travers l'enregistrement avant de pouvoir terminer sa connexion.

Les connexions par authentification unique (SSO) — Google, Microsoft, SAML — sont **exemptées** : leur fournisseur d'identité applique déjà sa propre MFA, de sorte que l'exigence n'affecte que les connexions par mot de passe.

Ce paramètre se trouve dans **Paramètres → Paramètres globaux → Informations sur l'entreprise → Authentification à deux facteurs** et n'est accessible qu'aux administrateurs d'organisation.

## Exiger la MFA pour votre organisation

1. Accédez à **Paramètres → Paramètres globaux → Informations sur l'entreprise**.
2. Ouvrez la section **Authentification à deux facteurs**.
3. Activez **Exiger l'authentification à deux facteurs pour tous les membres** et cliquez sur **Enregistrer**.

<figure><img src="../../../../.gitbook/assets/mfa-admin-requirement.png" alt="Le commutateur d'exigence de MFA de l'organisation et le rapport d'adoption"><figcaption><p>Activez l'exigence pour tous les membres, et surveillez l'adoption ci-dessous.</p></figcaption></figure>

Une fois enregistré, le changement prend effet en moins d'une minute. À partir de ce moment :

* Un membre **disposant** d'un second facteur se le voit demander après son mot de passe, comme d'habitude.
* Un membre **ne disposant pas** d'un second facteur est tenu d'en enregistrer un avant de recevoir une session.
* Les connexions SSO / sociales ne sont pas affectées.

{% hint style="warning" %}
Activer ce paramètre bloque les connexions par mot de passe pour les membres qui n'ont pas de second facteur jusqu'à ce qu'ils terminent l'enregistrement. Communiquez le changement à votre équipe, et envisagez de l'activer en dehors des heures de pointe.
{% endhint %}

## Rapport d'adoption de la MFA

Sous le commutateur, le panneau **Adoption de la MFA** montre l'ampleur de l'utilisation de la 2FA dans votre organisation avant de l'imposer :

* le **pourcentage d'adoption** global et une barre de progression,
* combien de vos membres ont la 2FA activée (par ex. *0 sur 74 membres*),
* une répartition par facteur — **Application d'authentification**, **E-mail**, et **Clé d'accès**.

<figure><img src="../../../../.gitbook/assets/mfa-adoption-report.png" alt="Le rapport d'adoption de la MFA"><figcaption><p>Le rapport d'adoption de la MFA : pourcentage global, membres enregistrés, et une répartition par facteur.</p></figcaption></figure>

Utilisez-le pour évaluer l'état de préparation : augmentez d'abord l'adoption, puis activez l'exigence avec moins de membres bloqués à l'étape d'enregistrement.

## Ce que voient les membres

Un membre tenu de s'enregistrer est dirigé vers la configuration de la 2FA lors de sa prochaine connexion et choisit une méthode (application d'authentification, code par e-mail, ou clé d'accès). Les étapes destinées à l'utilisateur final sont décrites dans [Authentification à deux facteurs (2FA)](../../../../overview-and-basics/two-factor-authentication.md).

## Contrôles de sécurité associés

L'exigence de MFA à l'échelle de l'organisation complète les protections intégrées qui s'appliquent toujours dès qu'un utilisateur a activé la 2FA : codes de connexion à usage unique, une protection contre la relecture TOTP, des limites de tentatives par défi et par compte (un compte est temporairement verrouillé après un trop grand nombre de tentatives échouées), et la révocation automatique des appareils de confiance lorsqu'un membre change son mot de passe.
