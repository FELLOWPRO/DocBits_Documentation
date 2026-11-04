# Configuración e instalación

Conectar un asistente de IA a DocBits MCP requiere un solo comando y un inicio de sesión único. La forma recomendada de iniciar sesión es **OAuth**: el mismo inicio de sesión de DocBits que ya utiliza, en su navegador. Para la automatización puede conectarse con una clave de API en su lugar.

## 1. Elija su endpoint

El servidor MCP se encuentra en el host de la API de DocBits. Utilice el host de **su región (UE o EE. UU.)**:

| Entorno | Endpoint UE | Endpoint EE. UU. |
|-------------|-------------|-------------|
| Producción | `https://eu.api.docbits.com/v3/mcp` | `https://us.api.docbits.com/v3/mcp` |
| Sandbox | `https://eu.sandbox.api.docbits.com/v3/mcp` | `https://us.sandbox.api.docbits.com/v3/mcp` |

{% hint style="info" %}
`api.docbits.com` es el único endpoint que utilizan los clientes. Elija siempre la **región en la que se encuentra su organización** (UE o EE. UU.): el MCP dirige automáticamente el inicio de sesión al servidor de autenticación correspondiente, por lo que no tiene que configurarlo por separado. Los ejemplos siguientes utilizan el host de producción de la UE; sustitúyalo por el suyo.
{% endhint %}

## 2. Inicie sesión con OAuth (recomendado)

OAuth es el camino más sencillo: no hay que copiar secretos. Después de añadir el servidor, la **primera conexión abre el inicio de sesión de DocBits en su navegador**, usted aprueba una pantalla de consentimiento y el cliente queda conectado.

**Lo que verá, con cualquier cliente:**

1. El cliente abre la página de inicio de sesión de DocBits en su navegador.
2. Usted inicia sesión con su cuenta de DocBits (si ya ha iniciado sesión en la aplicación web de DocBits, se reutiliza la sesión y no es necesario volver a iniciarla).
3. Usted aprueba la pantalla de consentimiento ("Authorize access").
4. El navegador entrega un token al cliente y la conexión queda activa.

OAuth emite un token de acceso de corta duración (8 h) y un token de actualización (30 días), por lo que el cliente se actualiza automáticamente y permanece conectado: **solo tiene que iniciar sesión una vez.**

{% hint style="success" %}
**Debe haber iniciado sesión en DocBits: se reutiliza su sesión existente.** El inicio de sesión de MCP no le pide que vuelva a iniciar sesión si su navegador ya tiene una sesión de DocBits. Si ya ha iniciado sesión en la aplicación web de DocBits, pasará **directamente a la pantalla de consentimiento**. Si no ha iniciado sesión, aparece primero la página de inicio de sesión de DocBits; tras iniciar sesión una vez, la sesión se traspasa automáticamente al MCP.
{% endhint %}

<figure><img src="../../.gitbook/assets/docbits-mcp-login.png" alt="Página de inicio de sesión de DocBits"><figcaption><p>Aún sin sesión iniciada: la página de inicio de sesión de DocBits con la marca corporativa (solo la verá si su navegador no tiene una sesión de DocBits)</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/docbits-mcp-consent.png" alt="Pantalla de autorización de acceso / consentimiento de DocBits"><figcaption><p>Sesión ya iniciada: se reutiliza la sesión y pasa directamente a la pantalla de consentimiento. Apruebe para conectar; se muestra lo que solicita el cliente (ámbito y redirección).</p></figcaption></figure>

{% tabs %}
{% tab title="Claude Code" %}
```bash
# 1) add the server
claude mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp

# 2) sign in (opens browser → DocBits login + consent → connected)
claude mcp login docbits
```

`claude mcp login docbits` es el paso de OAuth. Cuando termine correctamente, confírmelo pidiéndole a Claude: *"comprueba el estado de la API de DocBits"*.
{% endtab %}

{% tab title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp
```

Gemini CLI detecta automáticamente el servidor OAuth. La **primera vez** que utiliza el servidor, abre el inicio de sesión de DocBits en su navegador (el registro dinámico de clientes y la gestión de tokens se realizan por usted). Apruebe el consentimiento y quedará conectado. Si es necesario, puede volver a iniciar el inicio de sesión desde el menú `/mcp` de Gemini.
{% endtab %}

{% tab title="OpenAI Codex" %}
```bash
codex mcp add docbits \
  --url https://eu.api.docbits.com/v3/mcp \
  --oauth-resource https://eu.api.docbits.com/v3/mcp
```

El indicador `--oauth-resource` le indica a Codex que ejecute el inicio de sesión OAuth para este servidor. En el primer uso, Codex abre el inicio de sesión de DocBits en su navegador; apruebe el consentimiento y quedará conectado.
{% endtab %}
{% endtabs %}

## 3. Conéctese con una clave de API (automatización)

Para agentes sin interfaz, CI o cualquier entorno sin navegador, omita OAuth y envíe la clave de API de su organización en la cabecera `X-API-KEY`.

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp \
  --header "X-API-KEY: <your-api-key>"
```
{% endtab %}

{% tab title="Gemini CLI" %}
Añada a `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "docbits": {
      "httpUrl": "https://eu.api.docbits.com/v3/mcp",
      "headers": { "X-API-KEY": "<your-api-key>" }
    }
  }
}
```
{% endtab %}

{% tab title="OpenAI Codex" %}
Añada a `~/.codex/config.toml`:

```toml
[mcp_servers.docbits]
url = "https://eu.api.docbits.com/v3/mcp"
http_headers = { "X-API-KEY" = "<your-api-key>" }
```

O bien mantenga la clave fuera del archivo y léala desde el entorno:

```toml
[mcp_servers.docbits]
url = "https://eu.api.docbits.com/v3/mcp"
env_http_headers = { "X-API-KEY" = "DOCBITS_API_KEY" }
```
{% endtab %}
{% endtabs %}

## Cómo funciona el inicio de sesión OAuth (por dentro)

DocBits implementa el flujo estándar **MCP OAuth 2.1**, por lo que cualquier cliente compatible se conecta sin configuración manual:

1. El cliente llama al endpoint MCP y recibe un `401` con una cabecera `WWW-Authenticate` que apunta a los metadatos del recurso protegido.
2. Lee `/.well-known/oauth-protected-resource`, que nombra al servidor de autenticación de DocBits.
3. Lee los metadatos del servidor de autenticación y **se registra a sí mismo** dinámicamente (RFC 7591); no se necesita ningún secreto de cliente.
4. Su navegador abre el inicio de sesión y el consentimiento de DocBits. Si ya ha iniciado sesión en la aplicación web, se reutiliza la sesión.
5. El cliente intercambia el código de autorización (PKCE) por un token de acceso y un token de actualización, y llama al MCP.

{% hint style="warning" %}
Cerrar sesión en la **aplicación web de DocBits no desconecta el MCP**: el MCP conserva sus propios tokens y sigue funcionando hasta que caduca el token de actualización (30 días) o usted elimina el servidor de su cliente.
{% endhint %}

## Solución de problemas

| Síntoma | Causa / solución |
|---------|-------------|
| La página de inicio de sesión nunca se abre | Confirme que el host y la región del endpoint son correctos y accesibles; algunos entornos sin interfaz no pueden abrir un navegador: utilice una clave de API en su lugar. |
| `401` tras conectar | El token ha caducado y no hay token de actualización (el modo de clave de API nunca se actualiza): vuelva a conectar / inicie sesión de nuevo. |
| Faltan herramientas | Es posible que su usuario o clave de API no tenga permiso para esas funciones; compruebe su rol en DocBits. |
| Datos / región incorrectos | Asegúrese de haber utilizado el endpoint de **su** región (UE o EE. UU.). |
