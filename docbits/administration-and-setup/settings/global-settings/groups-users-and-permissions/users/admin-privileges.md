# Admin Privileges

The role of an administrator is crucial for managing IT systems, networks and digital platforms in an organization. An administrator has advanced permissions and responsibilities that allow them to control various aspects of the technical infrastructure and ensure that it is operated efficiently and securely. Here are some of the main responsibilities of an administrator:

* **User management:** Administrators manage user accounts, access rights and permissions. They create new user accounts, assign them the necessary permissions and manage access control to ensure that only authorized users can access certain resources.
* **Security:** Administrators are responsible for the security of IT systems to protect against data loss and unauthorized access.
* **Troubleshooting and support:** The administrator is often the first point of contact for technical issues. They help users troubleshoot and resolve problems and ensure that the system is running smoothly.

In addition to these responsibilities, administrators are also tasked with managing sensitive settings and ensuring that systems meet compliance requirements and information security best practices. This includes managing sensitive data, configuring access controls and permissions, and monitoring and analyzing system logs to identify and address potential security risks.

## Admin vs System Admin

DocBits has two administrator roles: **Admin** and **System Admin**. They sound similar, but they do different jobs. Here is the simple version.

### Admin — a person who manages your organization

An **Admin** is a real person on your team who is allowed to manage DocBits. Admins can:

* Open all areas of **Settings** and change how your organization works.
* Add new users, edit them, switch them on or off, and decide who else becomes an Admin.
* Set up groups, permissions, integrations, and workflows.

You can have **as many Admins as you need**, and you can give or take away the Admin role from any user at any time. Most administrators on your team are this type.

### System Admin — the account DocBits uses to work on its own

A **System Admin** is **one special account per organization** that DocBits uses for actions that happen **automatically, without anyone clicking a button** — for example when documents are imported from email, exported to another system, or passed along by a connected service in the background.

Think of it as the organization's "robot" account. When the system does something on its own, it does it **as the System Admin**, so that automatic activity is easy to recognize and is not mixed up with the work of your real team members.

A System Admin is special in three ways:

* **It is always an Admin too.** Choosing System Admin automatically gives that account full Admin rights as well.
* **There is only one per organization.** Once a System Admin exists, you cannot mark another user as System Admin.
* **It is set only when the user is created.** You decide this at the moment you add the user. It **cannot be turned on or off later**.

> **Recommendation:** Create a dedicated account for this purpose — for example `system@your-company.com` — and mark it as the System Admin. That way, anything DocBits does automatically clearly shows up as the **System Admin** in your logs and document history, separate from your real users.

### At a glance

| | Admin | System Admin |
|---|---|---|
| Full access to manage the organization | Yes | Yes |
| How many you can have | As many as you need | Only one |
| Can be changed after the user is created | Yes, anytime | No, only set at creation |
| Used for automatic, behind-the-scenes actions | No | Yes |
| Always has Admin rights | — | Yes |

## Security Best Practice

Security is an essential aspect of any organization, especially when it comes to managing user accounts and access rights. Here are some best practices to maintain a secure user management protocol:

* **Regular password updates:** Encourage users to update their passwords regularly to keep their accounts secure. Establish password complexity policies and require the use of strong passwords that include a combination of letters, numbers, and special characters.
* **Monitor administrator actions:** Implement mechanisms to monitor administrator activities to detect suspicious or unusual activity. Log all administrator actions, including access to sensitive data or settings, to ensure accountability and identify potential security breaches.
* **Limit the number of administrators:** Reduce the number of administrators to a minimum and grant administrative privileges only to those who really need them. By limiting the number of administrators, you minimize the risk of security breaches and make it easier to manage and monitor user accounts.
* **Zwei-Faktor-Authentifizierung (2FA):** Implementieren Sie eine Zwei-Faktor-Authentifizierung für Administratorkonten, um die Sicherheit zusätzlich zu erhöhen. Dadurch wird ein zusätzlicher Sicherheitsschritt eingeführt, der sicherstellt, dass selbst bei Kompromittierung eines Kennworts ein Angreifer keinen unbefugten Zugriff auf das Konto erhält.
* **Regelmäßige Sicherheitsüberprüfungen:** Führen Sie regelmäßige Sicherheitsüberprüfungen und Audits durch, um potenzielle Sicherheitslücken oder Schwachstellen zu identifizieren und zu beheben. Überprüfen Sie die Zugriffsrechte und Berechtigungen von Benutzerkonten, um sicherzustellen, dass sie den aktuellen Anforderungen und Best Practices entsprechen.
* **Training and awareness:** Regularly train employees and administrators on security best practices and awareness of phishing attacks and other cyber threats. Make them aware of the importance of security and encourage them to report suspicious activity.

By implementing these best practices, organizations can improve the security of their user management protocol and minimize the risk of security breaches and data loss. It is important to view security as an ongoing process and make regular updates and adjustments to keep up with ever-changing threats and security requirements.



