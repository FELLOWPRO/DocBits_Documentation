# Validatie voor elk documenttype

Beheerders bepalen per documenttype of DocBits binnenkomende e-facturen valideert en of een mislukte controle het document blokkeert. Elke wijziging wordt bevestigd en vastgelegd in het [wijzigingslogboek](validation-change-log.md).

> Alleen **organisatiebeheerders** kunnen deze instellingen wijzigen. Andere gebruikers zien de tabel alleen-lezen of zien haar niet.

## De tabel

Ga naar **Instellingen → E-documenten → Validatie van elektronische facturen**. Het tabblad **Regels en beleid** begint met de tabel **Validatie voor elk documenttype**.

<figure><img src="../../../../../.gitbook/assets/einvoice-validation-settings-nl.png" alt="De tabel Validatie voor elk documenttype met de schakelaars Ingeschakeld en Blokkeren"><figcaption><p>Eén rij per documenttype met de schakelaars Ingeschakeld en Blokkeren. Voorbeeldorganisatie.</p></figcaption></figure>

| Schakelaar       | Wat hij doet                                                                                                                                                                                                                                 |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ingeschakeld** | DocBits valideert elke binnenkomende e-factuur van dit documenttype en slaat een [validatierapport](validation-report.md) op.                                                                                                                |
| **Blokkeren**    | Een bevinding die een fout is, stopt het document. Het krijgt de status **Fout**. Als blokkeren uit staat, slaat DocBits het rapport op en gaat het document verder. U kunt **Blokkeren** alleen inschakelen als **Ingeschakeld** aan staat. |

Als een documenttype overschrijvingen voor subtypen heeft, toont de tabel daarover een opmerking.

## Een instelling wijzigen

1. Selecteer de schakelaar die u wilt wijzigen.
2. DocBits toont **Bevestig de wijziging in de validatie** met het documenttype en de wijziging, bijvoorbeeld _QUOTE: Ingeschakeld → Op_.

<figure><img src="../../../../../.gitbook/assets/einvoice-validation-confirm-nl.png" alt="Het dialoogvenster Bevestig de wijziging in de validatie"><figcaption><p>Elke wijziging moet worden bevestigd</p></figcaption></figure>

3. Lees de opmerking: **Reeds opgeslagen rapporten blijven ongewijzigd.** De wijziging geldt alleen voor nieuwe controles, ook wanneer u de verwerking van een document opnieuw start.
4. Selecteer **Wijziging bevestigen**, of **Annuleren** om de oude instelling te behouden.

Als u de rechten niet hebt, toont DocBits een melding dat een organisatiebeheerder vereist is, en verandert er niets.

## Gerelateerde pagina's

* [Validatie van elektronische facturen](./)
* [Wijzigingslogboek](validation-change-log.md)
* [Validatie-instellingen en geaccepteerde versies](validation-setup.md)
* [Validatierapport](validation-report.md)
* [E-factuurvalidatie in- of uitschakelen](../#e-factuurvalidatie-in--of-uitschakelen)
