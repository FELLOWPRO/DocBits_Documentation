# Criando um Arquivo de Mapeamento IDM

Uma vez obtido, abra o arquivo no editor de arquivos aplicável de sua escolha. Para este passo a passo, o VSCode será usado.

## Editar Arquivo de Mapeamento

Verifique se o código do tipo de documento está como está no DocBits (como no Arquivo de Mapeamento BOD, deve corresponder ao nome do tipo de documento na URL das configurações de campo) e também verifique o nome do tipo de documento conforme deve estar no Gerenciador de Documentos (IDM) na Infor.

![](https://lh7-us.googleusercontent.com/WHO0vg2W36yVFBq0ay0wBMFVzMfT6pNvHklt0o8N4tqUpM03jXJm2fykuYjyZh0z4wFTO4Eaeh39-D03re3a9utegrdVdsjHBfucmALA3B7YBWd92-9bcYr543G4MWftv0RosvTgFP3J6NNmLZAz5Dc)

**FYI**: Afirma que o nome do tipo de documento no IDM é M3\_SupplierInvoice, isso ocorre devido a este ser um exemplo de uma instância M3. Isso pode mudar dependendo se você usa LN ou M3, bem como sua configuração específica do IDM.

Verifique o ID da empresa e verifique o ID da Entidade (SF\_MDS\_EntityType), este valor deve ser o mesmo que estava no Arquivo de Mapeamento BOD.

Certifique-se de que IndexFieldFromDocBits=IDMAttributeID (verifique se o DocBits à esquerda nas configurações de campo corresponde ao IDM à direita em Tipo de Documento → Atributos).

### Gerenciador de Documentos na Infor

Vá para o Gerenciador de Documentos e selecione o nome do tipo de documento atual que você está tentando exportar, por exemplo, Fatura de Fornecedor.

![](https://lh7-us.googleusercontent.com/EV3uw3R1L6\_RRANB7FRLwtUFMbv\_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Clique no ícone acima e em seguida clique em Administração → Tipo de Documento e depois encontre o tipo de documento que você precisa na lista

![](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j\_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

Como mostrado abaixo, você verá então o nome do tipo de documento conforme está na INFOR

![](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj\_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW\_dpRfw\_5BXm0WvAnw4HOALmw)

Certifique-se de que este é o modo como o nome é exibido no Arquivo de Mapeamento IDM

## Carregar Arquivo para DocBits

Uma vez que o arquivo estiver preparado, faça o upload para sua configuração de exportação no DocBits. Isso está disponível em Configurações → Exportar.

![](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F\_i5mZ42YDnjqZUYKYSJu1Cetc\_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)
