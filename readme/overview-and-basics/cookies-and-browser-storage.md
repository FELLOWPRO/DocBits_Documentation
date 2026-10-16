# Cookies en browseropslag

Gecontroleerd op **16 oktober 2026** voor vraag **4.15**. De openbare website, de DocBits-applicatie en deze documentatie gebruiken verschillende cookies en diensten.

## Beleid en doeleinden

Het [Privacybeleid van DocBits](https://docbits.com/en/privacy-policy/) bevat de onderdelen **Cookies** en **Consent with Borlabs Cookie**. Het beschrijft toestemming, noodzakelijke functies, botbescherming, Google Analytics, advertenties en Leadfeeder. Analyses kunnen rapporten over bezoeken, pagina's, interacties en prestaties opleveren; de verzameling beperkt zich niet tot anonieme, samengevoegde gegevens. Het websitebeleid bepaalt niet automatisch de cookie-inventaris van de applicatie.

## Cookie-inventaris

**Waargenomen** betekent een nieuw bezoek zonder inloggen of optionele toestemming te selecteren. **Broncode** betekent onderzochte code of infrastructuurinstellingen en bevestigt niet de kenmerken van iedere productierespons.

| Cookie / bereik | Doel en bewaartermijn | Bewijs en beveiligingskenmerken |
| --- | --- | --- |
| `__cf_bm` / website en app | Cloudflare-botbescherming; 30 minuten inactiviteit | Waargenomen: `Secure`, `HttpOnly`, `SameSite=None`. [Cloudflare](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/) versleutelt de botinformatie behalve tijdgegevens. |
| `pll_language` / website | Taalvoorkeur; ongeveer één jaar | Waargenomen: `Secure`, leesbaar via JavaScript, `SameSite=Lax`. |
| `_lfa` / website | Leadfeeder-analyse van bezoekers en bedrijven; ongeveer één jaar | Waargenomen: leesbaar via JavaScript, `SameSite=Lax`, **zonder `Secure`-kenmerk** tijdens dit bezoek. |
| Borlabs-toestemmingscookie / website | Bewaart toestemming en intrekking | Genoemd in het privacybeleid; naam, toegepaste kenmerken en termijn niet geverifieerd tijdens dit bezoek. |
| `session` / authenticatie | Sessiestatus voor authenticatieprocessen | Standaard in broncode: `Secure`, `HttpOnly`, `SameSite=None`; ondertekende Flask-sessiegegevens, niet versleuteld. Deploymentinstellingen kunnen deze waarden wijzigen. |
| `dbx_td` / authenticatie | Onthoudt desgewenst een vertrouwd apparaat na geslaagde MFA; 30 dagen | Broncode: `Secure`, `HttpOnly`, `SameSite=None`; willekeurig token waarvan een hash op de server wordt opgeslagen. |
| `prod-sticky` / productielastverdeling | Stuurt verzoeken naar dezelfde backend; ingestelde duur 300 seconden | Infrastructuurinstelling bevestigd; browserkenmerken niet geverifieerd. |
| `dontAsk` / app | Onthoudt een voorkeur voor een melding; geen expliciete vervaltijd in de onderzochte aanroep | Broncode: leesbaar via JavaScript; geen expliciete optie voor `Secure` of `SameSite` in deze aanroep. |

Tijdens een nieuw documentatiebezoek zijn geen cookies waargenomen. Dit is een gedateerde momentopname, geen volledige inventaris van ingelogde processen, optionele functies of externe embeds. Het beleid noemt meer analyse- en advertentiediensten waarvan dit bezoek de cookies niet bevestigde. Een volledige inventaris en controle op toestemmingshandhaving vereisen afzonderlijk onderzoek van die processen.

## Beveiliging en analyses

`Secure` beperkt verzending tot HTTPS. `HttpOnly` voorkomt uitlezen via JavaScript. `SameSite` regelt verzending tussen websites. Deze kenmerken versleutelen de inhoud niet. Een algemene uitspraak dat alle cookies versleuteld of identiek beveiligd zijn, zou onjuist zijn. Openbare applicatie-endpoints ondersteunen TLS 1.2 en 1.3; zie [Veilige opslag van inloggegevens](secure-storage-of-credentials.md).

Browseropslag wordt ook los van cookies gebruikt. De Grafana Faro-configuratie ondersteunt blijvende sessietracking, fouten, prestatiemetingen en traces, met beschikbare gebruikers- en organisatie-ID's. Verzameling hangt af van de uitgerolde collectorconfiguratie. Dit mag niet worden omschreven als uitsluitend anonieme, samengevoegde cookieanalyse. Taalvoorkeuren gebruiken ook lokale opslag.

Cookies en opslag kunnen via de browser worden verwijderd. Daarbij kunnen voorkeuren en de herkenning van vertrouwde apparaten verdwijnen. Voor een actuele inventaris of privacyvragen: **compliance@fellowpro.com**.
