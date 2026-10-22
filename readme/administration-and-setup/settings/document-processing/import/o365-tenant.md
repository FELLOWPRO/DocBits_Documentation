# O365 Tenant

## Registrare un'App su Azure AD

<mark style="color:red;">**Nota**</mark>: Le autorizzazioni potrebbero richiedere l'autorizzazione di un amministratore.

1. Accedere al [Portale Azure](https://portal.azure.com/) utilizzando le proprie credenziali.
2. Dai servizi Azure, individuare e aprire Azure Active Directory (noto anche come Azure AD).

![Voce Azure Active Directory nella ricerca e nell'elenco dei servizi del portale Azure](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. Nella sezione **Manage**, selezionare **App registrations**.

![Pagina di panoramica di Azure Active Directory con la sezione Manage e la voce App registrations nel menu a sinistra](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. Nella schermata App registrations, fare clic su **+ New registration**.

![Pagina App registrations con il pulsante + New registration nella barra degli strumenti](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. Viene visualizzata la schermata **Register an application**. Inserire il nome visualizzato rivolto all'utente per l'App in **Name**.

![Modulo Register an application con il campo Name e il testo di aiuto per il nome visualizzato](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Selezionare uno dei seguenti tipi di account a seconda delle proprie esigenze:

* **Account in qualsiasi directory organizzativa (qualsiasi directory Azure AD Multitenant) e account Microsoft personali (ad esempio Skype, Xbox)**
* **Account in qualsiasi directory organizzativa (qualsiasi directory Azure AD multitenant)**

![Elenco Supported account types con le opzioni per tenant singolo, multi-tenant e account Microsoft personali](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Lasciare l'opzione **Redirect URI (optional)** così com'è.

![Modulo Register an application con i tipi di account supportati e l'opzione multi-tenant selezionata](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Fare clic su **Register** per completare la registrazione dell'App. Questo ti riporterà alla schermata della nuova App.
9. Nella schermata dell'App, individuare l'**Application (client) ID**. Copiarlo per utilizzarlo durante la configurazione dell'importazione delle email per **DocBits**.

![Sezione Redirect URI (optional) del modulo di registrazione e il pulsante Register sotto](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. Dal pannello di sinistra, selezionare **Certificates & secrets**:

![Pagina di panoramica dell'applicazione registrata con Display name, Application (client) ID e i pulsanti Delete ed Endpoints](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. Nella schermata **Certificates & secrets**, fare clic sul pulsante **+ New client secret** nella sezione **Client secrets**:

![Voce Certificates & secrets nel menu a sinistra dell'applicazione registrata](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. Nella finestra di dialogo **Add a client secret**, fare clic sul pulsante **Add**:

![Sezione Client secrets con la sua descrizione e la nota che non è stato creato alcun segreto client](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

Si consiglia di compilare una descrizione per identificare questo segreto tra molti (al momento il limite è di 2 segreti per App).

![Finestra Add a client secret con il campo Description e le opzioni di scadenza 1 anno, 2 anni e mai](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Nota**</mark>: Selezionare questa data di scadenza in base alla politica aziendale. Una volta scaduto, sarà necessario creare un nuovo client secret e specificarlo per ogni configurazione email in cui è stato utilizzato in precedenza.

13. Il client secret appena generato sarà visibile. Copiare questo client secret per utilizzarlo durante la configurazione dell'importazione delle email per DocBits.

![Tabella Client secrets con il segreto creato, la data di scadenza e l'icona di copia accanto al valore](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Importante:** Assicurarsi di aver copiato il client secret poiché il client secret non verrà più visualizzato una volta chiuso.

14. Selezionare **Authentication** nel pannello di sinistra. Questo mostrerà la schermata **Authentication** sul lato destro.

![Voce Authentication nel menu a sinistra dell'applicazione registrata](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. Nella sezione **Advanced settings**, fare clic su **Yes** per **Default client type**.

![Pagina Authentication, sezione Advanced settings, con Default client type impostato su Yes per client pubblico](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Fare clic su **Save** per confermare le modifiche.

![Pagina Authentication con i pulsanti Save e Discard nella barra degli strumenti](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Selezionare **API permissions** nel pannello di sinistra. Questo mostrerà la schermata delle autorizzazioni API.

![Voce API permissions nel menu a sinistra dell'applicazione registrata](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Per impostazione predefinita, l'autorizzazione **User.Read** da **Microsoft Graph** è presente, lasciarla così com'è.

![Tabella API permissions con l'autorizzazione delegata User.Read di Microsoft Graph](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Nota**</mark>: Questa è un'autorizzazione obbligatoria. Se questa autorizzazione non è disponibile, aggiungere l'autorizzazione con i passaggi menzionati di seguito per l'autorizzazione **Mail.ReadWrite**.

19. Fare clic su **+ Add a permission**. Questo aprirà il pannello **Request API permissions**.

![Pannello Configured permissions con il pulsante + Add a permission e un elenco di autorizzazioni vuoto](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Fare clic su **Microsoft Graph**.

![Pannello Request API permissions con la voce Microsoft Graph tra le API Microsoft più usate](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. Dalle due sottocategorie, selezionare **App Permissions**.

![Pannello delle autorizzazioni Microsoft Graph con la scelta tra Delegated permissions e Application permissions](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Digitare **Mail.ReadWrite** nella casella di ricerca. Selezionare la casella di controllo **Mail.ReadWrite** per l'autorizzazione.

![Pannello Request API permissions con Mail.ReadWrite nella ricerca delle autorizzazioni e l'autorizzazione Mail corrispondente](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Questo abiliterà il pulsante **Add permissions** nella parte inferiore del pannello. Fare clic su **Add permissions**.

![Pannello Request API permissions con la casella Mail.ReadWrite selezionata e il pulsante Add permissions attivo](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Questo aggiungerà l'autorizzazione **Mail.ReadWrite** all'elenco delle **Configured permissions** per l'App.

<mark style="color:red;">**Nota**</mark>: Potrebbero essere necessarie autorizzazioni di amministratore. L'amministratore dovrà autorizzare l'App per l'utilizzo di queste autorizzazioni. Una volta autorizzato, lo stato concesso sarà indicato come segue:

![Pannello Configured permissions con l'autorizzazione Mail.ReadWrite e il pulsante Grant admin consent per il tenant](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)
