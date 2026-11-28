# Quick Connect

Conecta tu asistente de IA a DocBits en tres pasos: elige tu entorno, copia un comando e inicia sesión una vez. No se necesita ninguna API key.

## 1. Elige tu entorno

Usa el endpoint de la **región** (EU o US) y el **entorno** (Sandbox o Production) en el que se encuentra tu organización.

| Entorno | Región | Endpoint |
| --- | --- | --- |
| Sandbox | EU | `https://eu.sandbox.api.docbits.com/v3/mcp` |
| Sandbox | US | `https://us.sandbox.api.docbits.com/v3/mcp` |
| Production | EU | `https://eu.api.docbits.com/v3/mcp` |
| Production | US | `https://us.api.docbits.com/v3/mcp` |

{% hint style="warning" %}
El asistente trabaja con los permisos de la cuenta con la que inicias sesión y puede modificar datos. Los cambios en **Production** afectan a tus documentos reales. Prueba primero los prompts nuevos en Sandbox.
{% endhint %}

## 2. Conecta con un clic o un comando

Usa los botones para añadir el servidor a **Cursor** o **VS Code**, o copia el comando para tu cliente de terminal. Cada entorno usa su propio nombre de servidor, así puedes conectar Sandbox y Production en paralelo sin confundirlos.

{% tabs %}
{% tab title="Sandbox EU" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-sandbox-eu&config=eyJ1cmwiOiAiaHR0cHM6Ly9ldS5zYW5kYm94LmFwaS5kb2NiaXRzLmNvbS92My9tY3AifQ%3D%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-sandbox-eu&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Feu.sandbox.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-sandbox-eu https://eu.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-sandbox-eu --url https://eu.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-sandbox-eu https://eu.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}

{% tab title="Sandbox US" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-sandbox-us&config=eyJ1cmwiOiAiaHR0cHM6Ly91cy5zYW5kYm94LmFwaS5kb2NiaXRzLmNvbS92My9tY3AifQ%3D%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-sandbox-us&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fus.sandbox.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-sandbox-us https://us.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-sandbox-us --url https://us.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-sandbox-us https://us.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}

{% tab title="Production EU" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-prod-eu&config=eyJ1cmwiOiAiaHR0cHM6Ly9ldS5hcGkuZG9jYml0cy5jb20vdjMvbWNwIn0%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-prod-eu&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Feu.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-prod-eu https://eu.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-prod-eu --url https://eu.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-prod-eu https://eu.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}

{% tab title="Production US" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-prod-us&config=eyJ1cmwiOiAiaHR0cHM6Ly91cy5hcGkuZG9jYml0cy5jb20vdjMvbWNwIn0%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-prod-us&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fus.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-prod-us https://us.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-prod-us --url https://us.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-prod-us https://us.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}
{% endtabs %}

Para **Claude Desktop** y **claude.ai**, añade un conector personalizado: abre la configuración de conectores, elige **Add custom connector** y pega el endpoint de la tabla.

## 3. Inicia sesión una vez

La primera conexión abre el inicio de sesión de DocBits en tu navegador. Si ya has iniciado sesión en DocBits, pasas directamente a la pantalla de consentimiento. Apruébala y estarás conectado.

{% tabs %}
{% tab title="Claude Code" %}
Inicia Claude Code, ejecuta `/mcp`, selecciona el servidor de DocBits y elige **Authenticate**.
{% endtab %}

{% tab title="OpenAI Codex" %}
Sustituye `docbits-sandbox-eu` por el nombre del servidor que hayas añadido:

```bash
codex mcp login docbits-sandbox-eu
```
{% endtab %}

{% tab title="Gemini CLI" %}
Gemini CLI abre el inicio de sesión la primera vez que usa el servidor. Puedes volver a iniciarlo desde el menú `/mcp`.
{% endtab %}
{% endtabs %}

Solo inicias sesión una vez. El cliente renueva su acceso automáticamente durante 30 días de uso.

## 4. Comprueba la conexión

Inicia una conversación nueva y envía este prompt:

```text
Read only. Call get_api_info and get_current_user. Show the API host and my
organization name. Do not change any setting and do not process documents.
```

El host de la API de la respuesta debe coincidir con el endpoint que elegiste, por ejemplo `eu.sandbox.api.docbits.com` para Sandbox EU. Si no coincide, elimina el servidor y vuelve a añadirlo con el endpoint correcto.

## Próximos pasos

* [Ejemplos](examples.md): prompts listos para usar con documentos, búsquedas y analíticas
* [Configurar DocBits con Claude o Codex](configuration-with-claude-or-codex.md): cambia la configuración de forma segura con vista previa, confirmación y deshacer
* [Instalación y configuración](setup-and-configuration.md): inicio de sesión con API key para la automatización y cómo funciona el inicio de sesión OAuth

## Solución de problemas

| Síntoma | Solución |
| --- | --- |
| La página de inicio de sesión no se abre | Ejecuta de nuevo el paso de inicio de sesión. En un equipo sin navegador, usa una API key como se describe en [Instalación y configuración](setup-and-configuration.md). |
| `401` después de conectar | El inicio de sesión ha caducado. Vuelve a autenticar el servidor. |
| El asistente muestra datos de otra organización | Has elegido la región o el entorno equivocados. Elimina el servidor y añade el endpoint correcto. |
| Faltan herramientas | Tu rol de DocBits no permite esas funciones. Pregunta a tu administrador. |
