# SSO-Konfiguration

## Voraussetzungen

| Erforderliche Informationen    | Beschreibung                                                                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anmeldedaten für die Cloud     | Anmeldedaten sind zwingend erforderlich, um auf die Infor-Cloud-Umgebung zuzugreifen. Der Benutzer sollte die Rollen „Infor-SystemAdministrator" und „UserAdmin" haben. |
| Config-Admin-Daten (DocBits)   | Sie sollten von der FellowPro AG eine E-Mail mit den Anmeldedaten für die Seite „DocBits SSO Settings" erhalten haben. Sie benötigen einen Login und ein Passwort. |
| Zertifikat                     | Sie können das Zertifikat in DocBits unter „SSO Service Provider Settings" herunterladen.                                                          |

## Zugriff auf die Cloud erhalten und Ihren Zugriff prüfen

Die URL beginnt mit https://mingle-portal.eu1.inforcloudsuite.com/\<TENANT\_NAME>, gefolgt von Ihrer persönlichen Erweiterung

![](https://lh7-us.googleusercontent.com/bLBEM2KCtSiztzy3htdtA8hpnR9J616ecGXPVYZIn-r\_m1tHkLeC8SJZJobl8Hu-Xju4WR7BanVq6NClf9hvbp5qXpjLVHaO9thfmE6-2ITJrlIZzv6OyG93KVhmOsdt6xiEoNrfJO8PwUFRDBblMT4)

Wählen Sie die Option „Cloud Identities" und verwenden Sie Ihre Anmeldedaten

![](https://lh7-us.googleusercontent.com/aF9VyjY-cuTx5NZ9GdnyOQjZmegW9Hp5r7-8AY8SJb1Lj-\_saFTwju49KKqltxXt3ZevQ1Yr47MRQA0UdXkXeb2TnactKpxC5YV3eqkyZiYJVx-cVkolYfwuJElPEgiYMrRQSeSb5fALoUQehxQUh\_0)

Nach der Anmeldung haben Sie Zugriff auf die Infor Cloud. In diesem Fall öffnen wir diese Seite, aber über das Burger-Menü finden Sie Zugriff auf alle Anwendungen.

![](https://lh7-us.googleusercontent.com/rUfjNI7DIYDw\_sm-KWcGaU\_xGWRZesRkyoYB\_00gOe6OUVAeFXL4UvlKWdtuz771fElXi4fC9NWahRQVLGAxAL6alR5K8edHcOdpdxu-PPfGO7O9exx61NyL4KTqNrt2AofIcnkbWyjf2EGeytPKTdA)

![](https://lh7-us.googleusercontent.com/low1Mq1NxL-Fzo72m-Wy8RPaooMuuQHBdA7rMFVcl7Ps\_G284L2Ze-BjEGy2bM7gcbeWBNeMm6yU8taNCUXgSzb9OcRWRFhQACzsg90XxmxhIfXanKz\_y8tqB4qv8I3W6HIj7SB84NzqK0IJ6UAcYbs)

## Benutzerverwaltung öffnen, um einen neuen Service Provider hinzuzufügen

Auf der rechten Seite der Menüleiste finden Sie das Benutzermenü, über das Sie auf die Benutzerverwaltung zugreifen können

![](https://lh7-us.googleusercontent.com/4SvG9pBCyZxBc-kUzwGarIdJkL4S-3bbFnxdfEQoAczOY7abTN72-MYDZ7TtIMqpvAkgsrpM\_Fz2sud5M84r8PrAXkEZHJuhIAAHCCpxqKwkmmfFVnCxiU-iLLBeAlEANp05j\_3kznyOGYqOgs1e1fo)

Anschließend müssen Sie im Menü auf der linken Seite die Option „Security Administration" und „Service Provider" auswählen.

![](https://lh7-us.googleusercontent.com/F2dwiMbEqSF8XkZz5JvuOOOjs6MoxIqUAyj3gU6QasaGEUPuPiR\_ANQuJ6wrZjnl1LWNRh2aBBvLvXNp85yfpTjnJP6cLbNoEfcjTbbDyrGfEciYu39jXwcBral6Q70IKkIvzANbJN1WjIonpDzPZQ0)

Sie sehen dieses Fenster mit den Service Providern.

![](https://lh7-us.googleusercontent.com/BBANp\_qDLF8qBKXErAc65893Ya954hqNzg2U8xK-oZCXiSqr\_pboGzuLLW7cCeDjjpCzJn1Zkzc5B4IAI-NOCA\_E5EVW47AWixVGRDUkJ4NGuqAAXYM2UDmIWgi2DggfPkE2CaX0Da7CPGBNrDbe9Yo)

Klicken Sie nun auf das „+"-Zeichen und fügen Sie unser DocBits als Service Provider hinzu.&#x20;

![](https://lh7-us.googleusercontent.com/Ksq7zDLEy0AZ3CfobBG8ua2QXsec10nJ3UAed-LXsziZs4VVzxdydmWzP4lBgIOkfQmiCSQo4Q-773wRbsGLyvk2UG4Mj34HeyiSyRAAET7Ojr8mJFZENfAszSViM-QPpcC3AIEFOQuKWYfN0-jOsHY)

## Zugriff auf die SSO SERVICE PROVIDER SETTINGS in DocBits

* Melden Sie sich unter der URL https://app.docbits.com/ mit den von uns erhaltenen Anmeldedaten an.
* Gehen Sie zu EINSTELLUNGEN (in der oberen Leiste) und wählen Sie INTEGRATION; unter „SSO Service Provider Settings" finden Sie alle Informationen, die Sie für die folgenden Schritte benötigen.
* Laden Sie das Zertifikat herunter

![](https://lh7-us.googleusercontent.com/R9VSArrCuGWySeSTYBCLHXybVdvbx37TiviLKFvgNZVfaGXITpxoNkIY4JUMuaROZ1f9BYmqfhhq5YYdRbIz5aJaLGAt7oOxZ5m47MAzgUacP-STjdEHzcy1zjgq22YUh4UrqiTrzC969upxt1qDFxs)

Befüllen des Service Providers mithilfe der „SSO Service Provider Settings" in DocBits&#x20;

![](https://lh7-us.googleusercontent.com/ATCza1efYWKWr7MfDZfa3WbK1r88L9U91fKs319lTh\_QZxyJEp5WLjjCuOqwqnA6Li-h3\_KmRzaxVujbhqTn4Xq6eHAaeAt3K5Whg4KuLPlgTHAuCU02YXaOqhPNBAWSERRwCCmuXQDknoTPosNlDgA)

| Feld                       | Wert                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| Application Type           | DEFAULT\_SAML                                                                              |
| Display Name               | DocBits                                                                                    |
| Entity ID                  | Siehe Entity ID unter SSO SERVICE SETTINGS                                                 |
| SSO Endpoint               | Kopieren Sie die SSO-URL aus SSO SERVICE SETTINGS und fügen Sie sie in das Feld „SSO Endpoint" ein. |
| Signing Certificate        | Laden Sie die passende .cer-Datei hoch, die Sie in Schritt 3c) aus SSO SERVICE SETTINGS heruntergeladen haben |
| Name ID Format and Mapping | E-Mail-Adresse                                                                             |

![](https://lh7-us.googleusercontent.com/YfEUu3X34cjKrPKTLybMvRn-6rKS5aSWGoJLria08yYFZYyidnnVQKRJgzVgudPVPk8k9xWwUpzQyGi2peHFxY8UsQvXV-2twH9G-8IiFSRfoCk5eQUnoplNrttNYNYKUDjs7ckFw0BVYpzGz26Htxs)

* Wenn Sie alles ausgefüllt haben, denken Sie daran, es mit dem Disketten-Symbol über „Application Type" zu speichern
* Öffnen Sie den Service Provider DocBits erneut.
* Klicken Sie darunter auf „view the Identity Provider Information".

![](https://lh7-us.googleusercontent.com/ajA6zmOcJCNOHJM\_2fUMaObnOGzTLmjUHhOm5QfR7inIfhavc0YywcyUHalVY22ay5rG\_JtcTbUVUX7ZIn7GOPecylljFLdhrQg-JzOZ3Vcav8FM0ZdjT82otfdNYMFyPT3W3ZZuXpKJ1gUcvyx70jU)

![](https://lh7-us.googleusercontent.com/7VPP4izI8E5idcQOA3zRhCOCB5L9uZuylVcMhToiHUI3qk\_fCE4n30D-ccYO3OAvAjIrrhJ-AApNMJ7tQO3DmtP3TS5n5r15YUgf\_FzBCdL77a\_wcAIE0zS2VjKLPB2iPaxOokPHk9G5NW86MV6sZUI)

## Exportieren Sie die SAML-METADATEN.

Die Datei sieht so aus: ServiceProviderSAMLMetadata\_10\_20\_2021.xml

Importieren Sie die SAML-METADATEN in den SSO-Einstellungen.

Gehen Sie zu IDENTITY SERVICE PROVIDER SETTINGS, das sich unter INTEGRATIONS in den EINSTELLUNGEN befindet. Geben Sie Ihre Tenant ID ein (z. B. FELLOWPRO\_DEV); unterhalb dieser Zeile sehen Sie die Schaltfläche „Upload file" und die Schaltfläche IMPORT, über die Sie die zuvor exportierte SAML-METADATEN-Datei hochladen müssen.

* Klicken Sie auf IMPORT und wählen Sie dann die METADATEN-Datei aus, die Sie bereits aus den SSO SERVICE PROVIDER SETTINGS heruntergeladen haben
* Klicken Sie auf CONFIGURE

![](https://lh7-us.googleusercontent.com/7-v\_YNgl\_29WrK2lE62nEfIRQ3R5KVmOL\_PeR8\_ZxS8LNxHSVpHuKcNwDAmaSGTNepi0Izg64T3l3FY6XUSMZCVB-kyV3cbf0DtI-9GnspkrSibmRW3Dx2ESxZeyrkseRYRKdnmUn-GR4fmh8gUx\_Rg)

## Neue Anwendung in INFOR Ming.le hinzufügen

Gehen Sie zu den Admin-Einstellungen

![](https://lh7-us.googleusercontent.com/D5shQ6CN5YAbGM\_0Gr6Hf7-nOlAkTXMyOSr1DntZv8NMSg-mxT5ckp2uIxpHkt4WRQGwCcpIBip9D4Q7\_Z590oRQOlg36lu9Y\_gq0VxHojNu8ma\_3tvtYzrBlZVJJdrXPoib9cvizawCBxGaQlvZ4x8)

Klicken Sie oben rechts auf ADD APPLICATION

![](https://lh7-us.googleusercontent.com/l1JjP7c7Y9Echd\_xx9gEoG7zD-U9wLv-0DNpHtdycXco--1urpcmObRhW4mYngaS8U0OcSv3vA\_wSvg3diSMmsC50BcSTbcMD47hsS7q3QwssdS7cY8rpNQHF7v\_20\_tBpZRuUhTLZ5bY6QnD53T0Lw)

Füllen Sie alle Felder wie auf dem folgenden Bild aus, jedoch mit Ihrer eigenen SSO-URL, vergessen Sie nicht, ein Symbol auszuwählen, und klicken Sie auf SAVE.

![](https://lh7-us.googleusercontent.com/\_ToZv0\_KzrnCJtTprJU7FJirxGC9Vn7c632BaLbIQH8aSJCAeOaw6XxpJ3nzUKs4yI4MtEX5QxuLwf\_ywjiAP\_cEdVEV8fIueOGh10A46pBIEnK5cDu4PS-q2La8tbqOWQb3nkKPyfgfEYxRDlWf7bI)

**Letzter Schritt**

* Melden Sie sich von DocBits ab.
* Gehen Sie zurück zum Burger-Menü in Infor und wählen Sie das soeben erstellte Symbol aus.
* Sie gelangen daraufhin zum Dashboard von DocBits.
