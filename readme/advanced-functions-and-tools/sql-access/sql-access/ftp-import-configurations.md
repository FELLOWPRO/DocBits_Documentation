# Configuraties voor FTP-import

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `sub_org_id`: intern
* `server_url`: intern
* `username`: intern
* `password`: intern
* `is_active`: boolean
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `deleted_on`: tijdstempel met tijdzone
* `port`: integer
* `default_directory`: intern
* `ftp_type`: intern
* `token`: intern
* `file_name_matching_patterns`: intern
* `last_mtime`: intern
* `auth_failed_count`: integer
* `auth_message`: tekst
* `ignore_certificate`: boolean
* `move_after_import`: boolean
* `destination_directory`: intern
* `import_directory`: intern
* `include_subfolder_content`: boolean

## Analyse & Beschrijving

```markdown
# Documentatie voor de Tabel FTP Import Configurations

## Inleiding

De tabel `public.ftp_import_configurations` is ontworpen om configuratiedetails voor FTP-importprocessen op te slaan. Deze tabel bevat de informatie die nodig is voor verbinding met FTP-servers, het beheren van authenticatie en het afhandelen van bestandsimporten. Het ondersteunt zowel FTP- als SFTP-protocollen en bevat velden voor FTP-serverdetails, authenticatiegegevens en operationele instellingen, zoals of bestanden na import moeten worden verplaatst en of de inhoud van submappen moet worden opgenomen.

## Kolombeschrijvingen

### id
- **Betekenis**: Unieke identificatie voor elk FTP-importconfiguratierecord.
- **Rol**: Primaire sleutel.
- **Typische Inhoud**: UUID-formaat, bijv. `9862d8c6-bb61-4373-9616-d5f8c125eeb8`.

### org_id
- **Betekenis**: Identificatie voor de organisatie die aan deze configuratie is gekoppeld.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: UUID-formaat.

### sub_org_id
- **Betekenis**: Identificatie voor een suborganisatie, indien van toepassing.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: UUID-formaat of `null` indien niet van toepassing.

### server_url
- **Betekenis**: De URL of het IP-adres van de FTP-server.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Domeinnaam of IP-adres, bijv. `sftp.it.doxee.com`.

### username
- **Betekenis**: Gebruikersnaam die wordt gebruikt voor authenticatie bij de FTP-server.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Gebruikersnaam in platte tekst.

### password
- **Betekenis**: Wachtwoord dat wordt gebruikt voor authenticatie bij de FTP-server.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Versleutelde wachtwoordreeks.

### is_active
- **Betekenis**: Geeft aan of de configuratie momenteel actief is.
- **Rol**: Statusvlag.
- **Typische Inhoud**: `True` of `False`.

### created_by
- **Betekenis**: Identificatie voor de gebruiker die de configuratie heeft aangemaakt.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Integer die de gebruikers-ID vertegenwoordigt.

### created_on
- **Betekenis**: Tijdstempel wanneer de configuratie is aangemaakt.
- **Rol**: Auditveld.
- **Typische Inhoud**: Datum en tijd met tijdzone-informatie.

### last_modified_on
- **Betekenis**: Tijdstempel van de laatste wijziging van de configuratie.
- **Rol**: Auditveld.
- **Typische Inhoud**: Datum en tijd met tijdzone-informatie.

### is_deleted
- **Betekenis**: Geeft aan of de configuratie als verwijderd is gemarkeerd.
- **Rol**: Statusvlag.
- **Typische Inhoud**: `True` of `False`.

### deleted_on
- **Betekenis**: Tijdstempel wanneer de configuratie als verwijderd is gemarkeerd.
- **Rol**: Auditveld.
- **Typische Inhoud**: Datum en tijd met tijdzone-informatie of een standaarddatum voor niet-verwijderde records.

### port
- **Betekenis**: Poortnummer dat wordt gebruikt om verbinding te maken met de FTP-server.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Integer, bijv. `22` voor SFTP.

### default_directory
- **Betekenis**: Het standaardmappad op de FTP-server.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Reeks met het mappad.

### ftp_type
- **Betekenis**: Type FTP-protocol dat wordt gebruikt (bijv. FTP, SFTP).
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: `FTP` of `SFTP`.

### token
- **Betekenis**: Beveiligingstoken voor aanvullende authenticatie of identificatie.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Versleutelde of gecodeerde reeks.

### file_name_matching_patterns
- **Betekenis**: Patronen die worden gebruikt om bestandsnamen voor import te matchen.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Patroonreeksen of `null`.

### last_mtime
- **Betekenis**: Laatste wijzigingstijd van bestanden, gebruikt voor het filteren van importen.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Reeks die een tijdstempel vertegenwoordigt of `null`.

### auth_failed_count
- **Betekenis**: Teller voor mislukte authenticatiepogingen.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Integer, bijv. `0` of `5`.

### auth_message
- **Betekenis**: Bericht dat het resultaat van de laatste authenticatiepoging beschrijft.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Tekstbericht of `null`.

### ignore_certificate
- **Betekenis**: Geeft aan of de validatie van het SSL-certificaat moet worden genegeerd.
- **Rol**: Statusvlag.
- **Typische Inhoud**: `True` of `False`.

### move_after_import
- **Betekenis**: Geeft aan of bestanden moeten worden verplaatst nadat de import is voltooid.
- **Rol**: Statusvlag.
- **Typische Inhoud**: `True` of `False`.

### destination_directory
- **Betekenis**: Mappad waarnaar bestanden na import moeten worden verplaatst.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Reeks met mappad of `null`.

### import_directory
- **Betekenis**: Mappad van waaruit bestanden worden geïmporteerd.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Reeks met mappad of `null`.

### include_subfolder_content
- **Betekenis**: Geeft aan of de inhoud van submappen moet worden opgenomen in de import.
- **Rol**: Statusvlag.
- **Typische Inhoud**: `True` of `False`.
```

Deze documentatie biedt een uitgebreid begrip van elke kolom in de tabel `public.ftp_import_configurations`, met uitleg over het doel, de rol en de typische inhoud, gebaseerd op de verstrekte gegevens en kolomnamen.
