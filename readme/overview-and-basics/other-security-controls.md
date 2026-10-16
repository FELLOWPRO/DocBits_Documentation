# Otros controles de seguridad

Revisado el **16 de octubre de 2026** para la pregunta **4.17**. Se distinguen los informes de auditoría publicados del inventario actual de infraestructura.

| Control | Alcance documentado |
| --- | --- |
| Firewalls de red | El informe SOC 2 describe filtros VPC/security groups de DigitalOcean y la supervisión de cambios por Seguridad TI. Las comprobaciones actuales de solo lectura confirmaron firewalls activos, incluidas reglas asociadas a recursos Kubernetes. |
| Firewall de aplicaciones web (WAF) | La auditoría del RGPD documenta una WAF que protege el producto. No se verificaron independientemente las reglas gestionadas actuales, exclusiones ni cobertura de cada hostname. Se observaron cookies de protección contra bots de Cloudflare en el sitio y la aplicación; esto por sí solo no acredita las reglas WAF. |
| Balanceadores de carga | El inventario actual de DigitalOcean confirmó balanceadores de producción activos en Frankfurt con comprobaciones de estado configuradas. El enrutamiento y la afinidad de sesión son funciones de infraestructura. Consulte [Cookies y almacenamiento del navegador](cookies-and-browser-storage.md). |
| Listas de IP permitidas | Las reglas de infraestructura permiten filtrar por origen. No se confirmó una lista de IP por cliente configurable por el propio cliente, su cobertura ni excepciones. Acuerde la restricción requerida con FELLOWPRO para su despliegue. |
| Pruebas locales y sandbox | La [Estrategia del ciclo de versiones](docbits-release-lifecycle-strategy.md) documenta desarrollo, QA/UAT y evaluación en sandbox antes de producción. Las pruebas locales de integración requieren un entorno definido y datos adecuados. El acceso a sandbox no autoriza por sí mismo pruebas de penetración. |
| Máquinas virtuales y Kubernetes | El informe SOC describe estándares de endurecimiento, controles de acceso, puertos restringidos y gestión de parches de sistemas y red. El inventario actual confirmó clústeres Kubernetes gestionados. Esto no garantiza una configuración idéntica para todas las cargas. |
| Dispositivos y móviles | El informe SOC describe antimalware, análisis automáticos, actualización de firmas y supervisión de parches. El informe ISO identifica MDM como oportunidad de mejora. Deben confirmarse actualmente la cobertura universal de MDM, el borrado remoto y las reglas de móviles/BYOD. Los clientes gestionan la seguridad de sus propios dispositivos de navegación. |
| Políticas y procedimientos | El informe SOC describe políticas formales de seguridad, evaluación de riesgos, acceso, gestión de cambios, incidentes y formación. Solicite las políticas vigentes y su alcance al contacto de cumplimiento. |

## Evidencias y más información

[Certificaciones](architecture/certifications.md) contiene los informes y sus periodos. Las auditorías históricas respaldan los controles para el alcance evaluado; el inventario confirma recursos presentes en la fecha de revisión y no es una auditoría completa de configuración.

Consulte [Almacenamiento seguro de credenciales](secure-storage-of-credentials.md), [Cifrado en reposo](encryption-at-rest.md) y [Gestión de vulnerabilidades](vulnerability-management.md).

Para restricciones del despliegue, requisitos de móviles o políticas actualizadas: **compliance@fellowpro.com**.
