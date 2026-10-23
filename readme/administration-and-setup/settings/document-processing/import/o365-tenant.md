# O365 Tenant

## Registrare un'App su Azure AD

<mark style="color:red;">**Nota**</mark>: Le autorizzazioni potrebbero richiedere l'autorizzazione di un amministratore.

1. Accedere al [Portale Azure](https://portal.azure.com/) utilizzando le proprie credenziali.
2. Dai servizi Azure, individuare e aprire Azure Active Directory (noto anche come Azure AD).

![Pagina del portale di Azure con la voce Azure Active Directory e la barra di ricerca dei servizi](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. Nella sezione **Manage**, selezionare **App registrations**.

![Pagina di panoramica di Azure Active Directory con il menu Manage a sinistra aperto e App registrations evidenziato](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. Nella schermata App registrations, fare clic su **+ New registration**.

![Schermata App registrations in Azure con il pulsante New registration nella barra degli strumenti e l'elenco delle app registrate](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. Viene visualizzata la schermata **Register an application**. Inserire il nome visualizzato rivolto all'utente per l'App in **Name**.

![Schermata Register an application nel portale di Azure con il campo Name vuoto per la nuova app](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Selezionare uno dei seguenti tipi di account a seconda delle proprie esigenze:

* **Account in qualsiasi directory organizzativa (qualsiasi directory Azure AD Multitenant) e account Microsoft personali (ad esempio Skype, Xbox)**
* **Account in qualsiasi directory organizzativa (qualsiasi directory Azure AD multitenant)**

![Schermata Register an application con le opzioni del pulsante di opzione per il tipo di account supportato per directory organizzative e account Microsoft personali](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Lasciare l'opzione **Redirect URI (optional)** così com'è.

![Schermata Register an application con la sezione Redirect URI (optional) lasciata invariata in basso](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Fare clic su **Register** per completare la registrazione dell'App. Questo ti riporterà alla schermata della nuova App.
9. Nella schermata dell'App, individuare l'**Application (client) ID**. Copiarlo per utilizzarlo durante la configurazione dell'importazione delle email per **DocBits**.

![Pagina panoramica dell'app registrata che mostra il Display name Ephesoft OAuth2 App e l'Application client ID](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. Dal pannello di sinistra, selezionare **Certificates & secrets**:

![Pagina di panoramica dell'app registrata con Certificates and secrets selezionato nella sezione Manage del pannello sinistro](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. Nella schermata **Certificates & secrets**, fare clic sul pulsante **+ New client secret** nella sezione **Client secrets**:

![Schermata Certificates & secrets con la sezione Client secrets e il pulsante + New client secret](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. Nella finestra di dialogo **Add a client secret**, fare clic sul pulsante **Add**:

![Finestra di dialogo Add a client secret con i campi Description ed Expires e il pulsante Add](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

Si consiglia di compilare una descrizione per identificare questo segreto tra molti (al momento il limite è di 2 segreti per App).

![Elenco dei client secret che mostra il nuovo secret con le colonne descrizione, Value ed Expires](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Nota**</mark>: Selezionare questa data di scadenza in base alla politica aziendale. Una volta scaduto, sarà necessario creare un nuovo client secret e specificarlo per ogni configurazione email in cui è stato utilizzato in precedenza.

13. Il client secret appena generato sarà visibile. Copiare questo client secret per utilizzarlo durante la configurazione dell'importazione delle email per DocBits.

![Sezione Client secrets di Certificates & secrets con il valore del segreto generato pronto da copiare](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Importante:** Assicurarsi di aver copiato il client secret poiché il client secret non verrà più visualizzato una volta chiuso.

14. Selezionare **Authentication** nel pannello di sinistra. Questo mostrerà la schermata **Authentication** sul lato destro.

![Schermata di autenticazione della registrazione dell'app aperta dal pannello sinistro con le impostazioni della piattaforma a destra](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. Nella sezione **Advanced settings**, fare clic su **Yes** per **Default client type**.

![Sezione Advanced settings della schermata di Authentication con l'opzione Default client type impostata su Yes](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Fare clic su **Save** per confermare le modifiche.

![Barra superiore della registrazione dell'app con il pulsante Save evidenziato dopo l'abilitazione del tipo di client predefinito](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Selezionare **API permissions** nel pannello di sinistra. Questo mostrerà la schermata delle autorizzazioni API.

![Schermata API permissions aperta dal pannello sinistro che mostra le autorizzazioni configurate per l'app](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Per impostazione predefinita, l'autorizzazione **User.Read** da **Microsoft Graph** è presente, lasciarla così com'è.

![Elenco delle autorizzazioni configurate con l'autorizzazione delegata predefinita User.Read per Microsoft Graph](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Nota**</mark>: Questa è un'autorizzazione obbligatoria. Se questa autorizzazione non è disponibile, aggiungere l'autorizzazione con i passaggi menzionati di seguito per l'autorizzazione **Mail.ReadWrite**.

19. Fare clic su **+ Add a permission**. Questo aprirà il pannello **Request API permissions**.

![Pannello Request API permissions con Microsoft APIs, APIs my organization uses e il flusso di + Add a permission](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Fare clic su **Microsoft Graph**.

![Pannello Request API permissions con Microsoft Graph evidenziato tra le API Microsoft più utilizzate](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. Dalle due sottocategorie, selezionare **App Permissions**.

![Pannello Request API permissions per Microsoft Graph con le opzioni Delegated permissions e Application permissions](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Digitare **Mail.ReadWrite** nella casella di ricerca. Selezionare la casella di controllo **Mail.ReadWrite** per l'autorizzazione.

![Casella di ricerca delle autorizzazioni dell'applicazione con Mail.ReadWrite digitato e la casella di controllo dell'autorizzazione Mail.ReadWrite selezionata](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Questo abiliterà il pulsante **Add permissions** nella parte inferiore del pannello. Fare clic su **Add permissions**.

![Pannello Request API permissions con l'autorizzazione Mail.ReadWrite selezionata e il pulsante Add permissions in basso](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Questo aggiungerà l'autorizzazione **Mail.ReadWrite** all'elenco delle **Configured permissions** per l'App.

<mark style="color:red;">**Nota**</mark>: Potrebbero essere necessarie autorizzazioni di amministratore. L'amministratore dovrà autorizzare l'App per l'utilizzo di queste autorizzazioni. Una volta autorizzato, lo stato concesso sarà indicato come segue:

![Elenco delle autorizzazioni configurate con l'autorizzazione dell'applicazione Mail.ReadWrite aggiunta e il relativo stato concesso mostrato](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)
