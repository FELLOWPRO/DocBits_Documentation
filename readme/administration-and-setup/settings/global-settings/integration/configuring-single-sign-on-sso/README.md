# Single Sign-On (SSO) konfigurieren

Richten Sie DocBits als SAML-Service-Provider (SP) ein und verbinden Sie Ihren Identitätsanbieter (IdP). Sie benötigen Administratorzugriff auf die entsprechenden Einstellungen beider Systeme.

## SSO-Einstellungen öffnen

Melden Sie sich als Administrator bei DocBits an und öffnen Sie Single Sign-On in den Integrationseinstellungen.

<figure><img src="../../../../../.gitbook/assets/s50-dbdc-182-infor-v2-sso-settings-de.png" alt="SSO-Einstellungen mit Zertifikat und Metadaten in der deutschen Oberfläche. Organisationskennungen und Eingabewerte sind ausgeblendet."><figcaption><p>SSO-Einstellungen mit Zertifikat und Metadaten in der deutschen Oberfläche. Organisationskennungen und Eingabewerte sind ausgeblendet.</p></figcaption></figure>

## Werte des DocBits-Service-Providers ablesen



DocBits zeigt Entity ID, SSO URL und SLO URL schreibgeschützt an. Kopieren Sie diese Werte oder verwenden Sie die SP-Metadaten, um die DocBits-Anwendung beim IdP einzurichten. Tragen Sie in diesen DocBits-Feldern keine Ersatzwerte ein. Die Entity ID identifiziert den Service-Provider. Verwenden Sie die angezeigten Endpunkte entsprechend den SAML-Anforderungen Ihres IdP.

## SP-Zertifikat und Metadaten herunterladen



Verwenden Sie Download Certificate und den Metadaten-Download in den Service-Provider-Einstellungen von DocBits. Diese Downloads beschreiben DocBits als SP. Stellen Sie dem IdP die SP-Metadaten und bei Bedarf das heruntergeladene SP-Zertifikat bereit. Dieses Zertifikat ist von den IdP-Metadaten zu unterscheiden, die Sie später in DocBits hochladen.

## Identitätsanbieter konfigurieren



1. Konfigurieren Sie DocBits beim IdP anhand der in DocBits angezeigten SP-Werte oder der heruntergeladenen SP-Metadaten.
2. Verwenden Sie die DocBits Tenant ID, falls Ihr Anbieter sie benötigt. Prüfen Sie den Mandanten- und Anbieterkontext in den Identitätsanbieter-Einstellungen von DocBits.
3. Beziehen Sie die SAML-XML-Metadaten der eingerichteten Anwendung vom IdP und laden Sie diese IdP-XML-Datei in DocBits hoch. Verwenden Sie dafür nicht die zuvor heruntergeladenen DocBits-SP-Metadaten.
4. Speichern Sie die Konfiguration über die Aktion Configure/Save in den Identitätsanbieter-Einstellungen von DocBits.

## Anmeldung und unterstützte Abmeldung testen

Prüfen Sie, ob sich ein Benutzer über den eingerichteten IdP bei DocBits anmelden kann. Testen Sie Single Log-Out nur, wenn DocBits und der IdP es unterstützen und es auf beiden Seiten eingerichtet ist. Eine Abmeldung von DocBits garantiert allein keine Abmeldung von allen anderen verbundenen Anwendungen.
