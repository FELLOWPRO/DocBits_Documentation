# Vigilante

<figure><img src="../../../.gitbook/assets/watchdog-infographic-pt.png" alt="WatchDog Infographic"><figcaption></figcaption></figure>

**Instalação e Configurações**

Após baixar o arquivo WatchDog.exe, procure por Prompt de Comando → Executar como administrador em seu dispositivo Windows.

![](https://lh7-us.googleusercontent.com/a2kmyk7eD7HqZfPiLWmvSGFnpzg9oHejHe5TpE6gFwErFyJYYBB5BZjqopwr-cEqmlMvaW8-PgARZUGI9KMKHSkz-lU\_C\_w6aHrVA4Wqhwo8WBSqnBfVvCpSckqLu4PwUriGs1MxbKHBBkuQ2pPaVRM)

Assim que isso for aberto, chame o arquivo digitando o caminho onde o arquivo WatchDog.exe está armazenado em seu dispositivo como abaixo

![](https://lh7-us.googleusercontent.com/W\_jDgPVTtpEW96jR0w\_ibnZGY2CVwF2nAN0nEjMW3liw10bgPGlADiVR\_lWyEAlfGYRD--gSQMdEqboRlMW5TAEP6Ao3GOW-hP3tQimA58K9Uh-WNZf7i06YYNqk5\_EgKERYkjMzPx1Xd56qH2Pw8wA)

Digite install após o caminho do arquivo e pressione ENTER em seu teclado

![](https://lh7-us.googleusercontent.com/vZQxNIh\_wY2SFTznxNTboFOSePmEMqXQMWbhsSoO45B\_mIh\_6C-yjfJ4SPleBIIV4p943XBN1E-3HJBgFXRRABVfDX9Ey-dnb9c5KYaNleOmE5x1ocK32zLQ4luc71rmcbv7V\_dQ8pEtH\_WoWZkN0fg)

Você deverá receber a seguinte mensagem de erro, pois iniciará o aplicativo no modo de interface do usuário e ainda não há configuração presente.

![](https://lh7-us.googleusercontent.com/HmudHszeaiAj3xIlb1Oz1IXPh3Kz1JovUvPjkr9UI7EwSGbGWRK7xVhUNwc9LGlt3t1RRVR0l7DFLfG\_Ob2b8Yxd4DffLb27Hv3z22tzf9LqDVTn577CFV-4Bzs2P\_vTsGDJvtNzf8XW0wPiaWLDj2o)

O aplicativo abrirá automaticamente após a instalação. No topo, navegue até Einstellungen (Configurações) e aqui você verá 2 seções separadas.

**Configurações de pasta (Ordner Einstellungen)**

![](https://lh7-us.googleusercontent.com/8uSWIY8EJKPrKj9Zk5buY\_ByE9fu2oE7mJ-shG1VB2n7QWyVLAfDfUFdj-Jv3hBq2ncf2Ls1Wh3Lm7Kf-TFqet7yFso2S6srnZev-yzVdKjUxtCMTt2IUtWvUwUU0LMGktA8ioBfIkkZGqG4f53yYHM)

Aqui você configurará os caminhos dos arquivos onde os documentos serão lidos e processados. O caminho de leitura será para os documentos que você deseja que o WatchDog extraia e processe, enquanto o caminho processado será usado para indicar quais documentos da pasta de leitura foram extraídos e processados.

**Configurações gerais (Allgemeine Einstellungen)**

![](https://lh7-us.googleusercontent.com/mTUxSXPBZi\_TTtVEQbGQXyXNonkIuganpTjqaamkB7C7zZ7Qaodvf9Sl8nXjnp6ZpYNf8XOwvuk-MYYEyGkFcKB-SqC9lklBXehC-3jMI7G12tXqfa6ROWywPBFE4fy-p-DcuLo3QdZXy-1rjSzlu9s)

Aqui você configurará seu aplicativo DocBits com o WatchDog. Você precisará inserir seu ambiente DocBits, chave de API e o tipo de documento (conforme indicado acima). Para adicionar mais de um tipo de documento, separe os nomes dos tipos de documento com uma vírgula (INVOICE,DELIVERY-NOTE,PURCHASE-ORDER, etc.)

Se uma configuração inválida for inserida para qualquer um dos campos, você receberá uma mensagem de erro como a abaixo.

![](https://lh7-us.googleusercontent.com/BIOMuVCPUojfwPVr-cJukzvoBdWdtxzj5XCXocWlZwbaXwkTpb4u5Gk84vKu-\_Z5UxvZ2cq0asHs4aFRLklBrUOKA19d2R4nqsxyZjd3iJlh3y97f07OfzEyv6jl7JpnorANzdPIgyZfqwmCEYZOlek)

Após isso estar completo, volte para a área do Prompt de Comando e execute novamente o arquivo WatchDog.exe e desta vez ele será instalado corretamente devido às configurações agora estarem presentes

![](https://lh7-us.googleusercontent.com/GqtwbyvQjjNb1u9DY\_Eww2woOdK1nYMm0oRMFxEGWSP9oSYN51eu1kkWiDzenz1rHGLvYG-ocwosOK2bTM6ruXTI5co05kjV2HPGI-8TgEIBTVCPpTrvs37SKMk9eBWY0KEj9vCCyPeqXYgCVD0DDXw)

Para iniciar o aplicativo no modo de interface do usuário, execute o seguinte comando

![](https://lh7-us.googleusercontent.com/LELZuaiuL8ukiKPE-pbezsOZAICffXxAomx6gSe0vOvYaIdkr8Sr7X2znc\_Lb3G76bh11X6kGPizWzoA05L-nBwUcJV8NNLUgQuGOf0TyICmhyL4syhnZFGu82JP0a3dORlQXz9MnTA\_f-8b6oy8v6g)

Se você apenas deseja iniciar o aplicativo, execute este comando em vez disso.

![](https://lh7-us.googleusercontent.com/yHiO-x4CPGIjC9hRx6o-Wr5lAYiwjGi0vNBp3faB91OYIqm8TTZcz3SVDgjSmq\_7TN11aVCsNHoHV5sR0FHsA5DJqxJ74z3lAmXoaDkkMutl7yXj4fCoabX-9SwfsWJwOaooiVZhCvOKFXvJOCBicEA)

**Início Automático**

Para configurar o aplicativo WatchDog de forma que ele inicie automaticamente quando você ligar seu sistema.

Basta abrir “Serviços” nas configurações de sua máquina Windows.

![](https://lh7-us.googleusercontent.com/IEqq96LGZ9lBz2E0ApDrTz5huYutY7G1DecXLwhkdIF0pS235RN9HIqcehuJvXv5tyLdOnobhM\_VNeMFA7tnMhwvWCnFRU5G14cHWN1swA4ZYF1rjvKzZtFMaCK2MDsPebvIz3MejDwjiYEiQ-\_BQyg)

Procure por WatchDog nos serviços locais e abra o serviço (clique duas vezes na entrada)

![](https://lh7-us.googleusercontent.com/qOtVCqR-zytJw2zifnjHmW\_s5Hl6ijJt72d3PRI\_euZU0H3wA-QD69mSFOnyDEnCVJXblEeA\_Zbh5iQsyPa8gPJ85TY8wz-Ir0aMd2SWoKizKw1G4yi9jOmtxZG7-9EZbOvborv45OASD6zSa6lLbAk)

No menu acima, você terá as seguintes opções para iniciar automaticamente:

* Selecione Automático, o serviço iniciará na inicialização
* Automático (Início Atrasado), isso aguardará 2 minutos após a inicialização para iniciar o serviço
