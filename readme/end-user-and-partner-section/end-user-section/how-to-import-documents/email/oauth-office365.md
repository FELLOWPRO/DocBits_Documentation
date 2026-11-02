# OAuth Office365



{% embed url="https://youtu.be/Vvy38N_5g3Y" %}

Here you just need to enter your desired sub organization and press ‘Authenticate’

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-authenticate-en-20261006.png" alt="Email Server Setup dialog with protocol OAuth Office365, Document Routing and the Authenticate button."><figcaption><p>Choose the routing and press Authenticate.</p></figcaption></figure>

You will be taken to this Microsoft page and you will need to enter a code.

![](https://lh7-us.googleusercontent.com/Q76mIMXr5bWCrcu_6TOKDrh6yQIMESIrFvEcfvqg7mJp-K_4ES2e5ekPY4Ghhwxym-uRKz_QVCHyqk2u5onyoCCmg7fMbt3mnIUyCrc8XT4jBGn9ueEYij3DRg1-oODWHd-vDfM9FfbU3omF6RJJKsE)

This code can be found by clicking back to DocBits and the code will be displayed there like below, simply copy the code and enter it into the Microsoft page. Thereafter you will need to enter your own Microsoft credentials.

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-code-en-20261006.png" alt="Email Server Setup dialog showing the Microsoft authentication code with a Copy button and the Finish authentication button."><figcaption><p>The Microsoft code is displayed in DocBits.</p></figcaption></figure>

Press the FINISH AUTHENTICATION button and you will be taken to this menu

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-options-en-20261006.png" alt="Email Server Setup dialog after authentication with the switches Use Folder, Use Shared Mailbox and Move Emails To Other Folder."><figcaption><p>Options after the authentication is finished.</p></figcaption></figure>

**Use Folder**

If you are using a folder other than your inbox, enter the folder name after enabling the slider.

**Use Shared Mailbox**

If you want the email import to access an inbox or a folder of a shared mailbox, input the email address here after enabling the slider.

**Move imported emails to trash**

If you want to import all emails, not just the unread ones, and have them moved to trash then activate this. If not, it will only check for unread emails, import the documents, set the email to read and leave it in its current place.

In the event of you receiving an error message indicating you do not have the rights to establish such a connection, someone with admin rights within Azure would need to authorize this connection. For more information, visit the following page: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps
