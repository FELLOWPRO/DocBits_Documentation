# Cookies and Browser Storage

Reviewed on **16 October 2026** for questionnaire item **4.15**. The public website, the DocBits application, and this documentation have different cookies and services.

## Policy and purposes

The [DocBits Privacy Policy](https://docbits.com/en/privacy-policy/) contains the website's **Cookies** and **Consent with Borlabs Cookie** sections. It describes consent storage, essential functions, bot protection, Google Analytics, advertising and Leadfeeder. Analytics can produce reports on visits, pages, interactions and performance, but collection is not limited to anonymous aggregate data. The website policy does not by itself establish the application's cookie inventory.

## Cookie inventory

**Observed** means a fresh visit without signing in or selecting optional consent. **Source** means reviewed application code or infrastructure settings; it does not confirm the attributes of every deployed response.

| Cookie / scope | Purpose and retention | Evidence and security attributes |
| --- | --- | --- |
| `__cf_bm` / website and app | Cloudflare bot protection; 30 minutes of inactivity | Observed: `Secure`, `HttpOnly`, `SameSite=None`. [Cloudflare](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/) encrypts the bot information except time information. |
| `pll_language` / website | Language preference; about one year | Observed: `Secure`, JavaScript-readable, `SameSite=Lax`. |
| `_lfa` / website | Leadfeeder visitor/company analytics; about one year | Observed: JavaScript-readable, `SameSite=Lax`, **no `Secure` flag** in this visit. |
| Borlabs consent cookie / website | Saves consent choices and withdrawals | Declared in the privacy policy; name, deployed attributes and lifetime were not verified in this visit. |
| `session` / authentication service | Session state for authentication flows | Source default: `Secure`, `HttpOnly`, `SameSite=None`; signed Flask session data, not encrypted. Deployment settings can override defaults. |
| `dbx_td` / authentication service | Remembers a trusted device after successful MFA when selected; 30 days | Source: `Secure`, `HttpOnly`, `SameSite=None`; random token, with a hash stored server-side. |
| `prod-sticky` / production load balancing | Routes requests to the same backend; configured lifetime 300 seconds | Infrastructure setting verified; browser attributes not verified. |
| `dontAsk` / app | Remembers a prompt preference; no explicit expiry in the reviewed setter | Source: JavaScript-readable; no explicit `Secure` or `SameSite` option in this setter. |

No cookies were observed on a fresh documentation visit. This is a dated snapshot, not an exhaustive inventory of authenticated flows, optional features or third-party embeds. The policy names additional analytics/advertising services whose cookies were not confirmed by this visit. Consent enforcement and a complete inventory require checking those flows separately.

## Security and analytics

`Secure` limits transmission to HTTPS. `HttpOnly` prevents JavaScript from reading a cookie. `SameSite` controls cross-site sending. These flags do not encrypt a cookie's contents. A blanket statement that every cookie is encrypted or has identical security flags would be inaccurate. Public application endpoints support TLS 1.2 and 1.3; see [Secure Storage of Credentials](secure-storage-of-credentials.md).

Browser storage is also used independently of cookies. The application's Grafana Faro configuration supports persistent session tracking, errors, performance measurements and traces, with user and organization identifiers when available. Collection depends on the deployed collector configuration. It must not be described as anonymous aggregate cookie analytics. Language preferences also use local storage.

You can delete cookies and browser storage in your browser. This can remove preferences and remembered-device state. For a current inventory or privacy questions, contact **compliance@fellowpro.com**.
