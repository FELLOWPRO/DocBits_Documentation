# Grupos, usuarios y permisos

## Crear un grupo y probar el acceso a documentos

Con los permisos de grupo ya activados, cree un grupo de revisión y añada un usuario de prueba sin permisos de administrador. Permita listar, ver y editar facturas asignadas; mantenga desactivadas la eliminación, los cambios masivos y las aprobaciones. Guarde y vuelva a abrir los ajustes. Después inicie sesión como usuario normal: la factura asignada aparece y el documento de control no asignado no aparece.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/groups-permissions-admin/v1/es.mp4" %}

[Ver con subtítulos](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/groups-permissions-admin/v1/es.html)

Estos ajustes responden a tres preguntas distintas: quién puede iniciar sesión, en qué suborganización trabaja y qué puede hacer su grupo.

| Si necesita… | Abra… |
| --- | --- |
| Añadir o editar la cuenta de una persona | **Ajustes** → **Usuarios**; después lea [Users](users/README.md). |
| Organizar el acceso entre unidades de la empresa | **Ajustes** → **Suborganizaciones**; después lea [Sub-Organizations](sub-organizations/README.md). |
| Controlar el acceso por grupo | **Ajustes** → **Grupos y Permisos**; después lea [Groups and Permissions](groups-and-permissions/README.md). |

<figure><img src="../../../../.gitbook/assets/prior-t008-es.png" alt="Panel de selección de grupos."><figcaption><p>Panel de selección de grupos.</p></figcaption></figure>

Si un usuario no puede ver un documento o una acción, compruebe primero su cuenta y su organización. Después compruebe los permisos del grupo correspondiente. Utilice una cuenta de prueba sin privilegios de administrador para confirmar el acceso que tendrá realmente un usuario normal antes de modificar una organización en producción.
