# Other Security Controls

Reviewed on **16 October 2026** for questionnaire item **4.17**. This page distinguishes published audit evidence from a current infrastructure inventory.

| Control | Documented scope |
| --- | --- |
| Network firewalls | The SOC 2 report describes DigitalOcean VPC/security-group filtering and IT Security oversight of configuration changes. Current read-only infrastructure checks confirmed active cloud firewalls, including rules associated with Kubernetes resources. |
| Web Application Firewall (WAF) | The GDPR audit records a WAF protecting the product. The current managed rules, exclusions and coverage of each hostname were not independently verified. Cloudflare bot-protection cookies were observed on the website and app; that observation alone does not establish the WAF rule set. |
| Load balancers | Current DigitalOcean inventory confirmed active production load balancers in Frankfurt with configured health checks. Request routing and session affinity are infrastructure functions. See [Cookies and Browser Storage](cookies-and-browser-storage.md). |
| IP allowlisting | Infrastructure firewall rules support filtering by source. A customer-configurable tenant IP allowlist, its coverage and any access exceptions were not confirmed. Agree the required restriction with FELLOWPRO for the deployment. |
| Local and sandbox testing | The [Release Lifecycle Strategy](docbits-release-lifecycle-strategy.md) documents development, QA/UAT and sandbox evaluation before production availability. Local integration tests need a defined environment and suitable test data; sandbox availability does not establish permission to run penetration tests. |
| Virtual machines and Kubernetes | The SOC report describes production hardening standards, access controls, restricted ports and OS/network patch management. Current inventory confirmed managed Kubernetes clusters. These facts do not guarantee that every workload uses identical hardening settings. |
| Endpoints and mobile devices | The SOC report describes endpoint anti-malware, automatic scanning, definition updates and patch monitoring. The ISO surveillance report lists MDM as an improvement opportunity. Universal MDM, remote wipe and mobile/BYOD rules therefore require current confirmation. Customers manage the security of their own browser devices. |
| Policies and procedures | The SOC report describes formal information-security policies, risk assessment, access controls, change management, incident handling and staff training. Request the current policies and applicable scope from the compliance contact. |

## Evidence and further information

Audit reports and their reporting periods are available on [Certifications](architecture/certifications.md). Historical audits support the controls described for their assessed scope; the infrastructure check confirms resource presence on the review date and is not a complete security configuration audit.

For encryption and authentication, see [Secure Storage of Credentials](secure-storage-of-credentials.md) and [Encryption at Rest](encryption-at-rest.md). For assessment, patching and open-CVE questions, see [Vulnerability Management](vulnerability-management.md).

For deployment-specific restrictions, mobile-device requirements or current policy evidence, contact **compliance@fellowpro.com**.
