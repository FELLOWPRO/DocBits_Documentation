# OAuth Office365

{% embed url="https://youtu.be/Vvy38N_5g3Y" %}

Tutaj wystarczy wpisać swoją podorganizację i nacisnąć **Uwierzytelniać**

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-authenticate-pl-20261009.png" alt="Okno »Konfiguracja serwera poczty e-mail« z protokołem OAuth Office365, trasowaniem dokumentów i przyciskiem »Uwierzytelniać«."><figcaption><p>Wybierz trasowanie i naciśnij Uwierzytelniać.</p></figcaption></figure>

Zostaniesz przeniesiony na tę stronę Microsoft i będziesz musiał wprowadzić kod.

![](https://lh7-us.googleusercontent.com/Q76mIMXr5bWCrcu_6TOKDrh6yQIMESIrFvEcfvqg7mJp-K_4ES2e5ekPY4Ghhwxym-uRKz_QVCHyqk2u5onyoCCmg7fMbt3mnIUyCrc8XT4jBGn9ueEYij3DRg1-oODWHd-vDfM9FfbU3omF6RJJKsE)

Ten kod znajdziesz, wracając do DocBits — kod zostanie tam wyświetlony tak jak poniżej. Skopiuj kod i wprowadź go na stronie Microsoft. Następnie musisz podać własne dane logowania Microsoft.

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-code-pl-20261009.png" alt="Okno »Konfiguracja serwera poczty e-mail« z kodem uwierzytelniania firmy Microsoft, przyciskiem »Kopia« i przyciskiem »Zakończ uwierzytelnianie«."><figcaption><p>Kod Microsoft jest wyświetlany w DocBits.</p></figcaption></figure>

Naciśnij przycisk **Zakończ uwierzytelnianie**, a zostaniesz przeniesiony do tego menu

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-options-pl-20261009.png" alt="Okno »Konfiguracja serwera poczty e-mail« po uwierzytelnieniu z przełącznikami »Użyj folderu«, »Użyj udostępnionej skrzynki pocztowej« i »Przenieś wiadomości e-mail do innego folderu«."><figcaption><p>Opcje po zakończeniu uwierzytelniania.</p></figcaption></figure>

**Użyj folderu**

Jeśli używasz folderu innego niż skrzynka odbiorcza, wpisz nazwę folderu po włączeniu przełącznika.

**Użyj udostępnionej skrzynki pocztowej**

Jeśli chcesz, aby import e-maili miał dostęp do skrzynki odbiorczej lub folderu udostępnionej skrzynki pocztowej, wpisz tutaj adres e-mail po włączeniu przełącznika.

**Przenieś zaimportowane e-maile do kosza**

(W oknie przełącznik nazywa się **Przenieś wiadomości e-mail do innego folderu**.)

Jeśli chcesz zaimportować wszystkie e-maile, a nie tylko nieprzeczytane, i przenieść je do innego folderu (na przykład do kosza), włącz tę opcję. W przeciwnym razie sprawdzane będą tylko nieprzeczytane e-maile: dokumenty zostaną zaimportowane, e-mail oznaczony jako przeczytany i pozostawiony na swoim miejscu. Ta sama opcja jest opisana na stronie [Importowanie](../../../../administration-and-setup/settings/document-processing/import.md).

W przypadku otrzymania komunikatu o błędzie wskazującego, że nie masz uprawnień do ustanowienia takiego połączenia, ktoś z uprawnieniami administratora w Azure musi autoryzować to połączenie. Aby uzyskać więcej informacji, odwiedź następującą stronę: [https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps)
