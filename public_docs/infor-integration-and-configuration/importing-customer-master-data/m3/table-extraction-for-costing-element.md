# Extração de tabela para elemento de custo

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FhfKR7nRoSOXm7ms0X7P2%252FBildschirmfoto%25202024-09-20%2520um%252013.42.20.png%3Falt%3Dmedia%26token%3Dff914785-1bd7-41c5-a6c0-413058dbe9fc\&width=768\&dpr=4\&quality=100\&sign=2616709f\&sv=2)

Para ativar a extração de tabela para elemento de custo, você precisará importar a tabela m3costingelement para o DocBits.

Na página inicial do M3, digite Command + r e procure o prompt “PPS280”.

Selecione qualquer uma das linhas exibidas para você. No próximo menu, selecione FERRAMENTAS e “Exportar para Excel”.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FI8SYWm-JwpyYRHFUp2obGtXcsa7m_blJ_lTrnhczztRIXIN5gfxCt3eRw6ZI42fH6AwnsKyv4ux5-rhaT505PsyDFFI_anUNvmACFyx_ssgxaqWq25vLt_E5s310HNoiPPLf35qJlYtstjpj5Cc4aB4\&width=768\&dpr=4\&quality=100\&sign=5aa04ccf\&sv=2)

Selecione “Exportar todas as Linhas” e depois pressione EXPORTAR.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FwtjHI9L4YUhf-yJFjcPGu218Vis_zELtCIfpmkIUKgasfrdfNW-dr_J1DqXlfD-SBrnVduDrMLAIAQh6UTlzBqEP_JPXP48elGMyGj0ByZbX7TpqlnIfRZ4ZoD0pyCo-AKigeKjlHN6cFcdpeClZ9L4\&width=768\&dpr=4\&quality=100\&sign=7cf7a274\&sv=2)

Uma vez baixado, você precisará alterar o arquivo excel antes de convertê-lo em um arquivo CSV.

Você precisará abrir o arquivo excel, que terá uma aparência semelhante ao que é mostrado abaixo.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmR6GtTDYMGf48yc3GCau%252Fimage.png%3Falt%3Dmedia%26token%3Daf52d75f-bdb9-4b18-a4b0-572b76e14309\&width=768\&dpr=4\&quality=100\&sign=57660254\&sv=2)

Desta planilha excel, você precisa das colunas A, B, H, J, K e I, altere a planilha excel para que o resultado final fique como segue.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FajTC0UO55QZRMDyhBxm1%252Fimage.png%3Falt%3Dmedia%26token%3D5b29b038-8156-4e67-8536-e0bcb65c35ff\&width=768\&dpr=4\&quality=100\&sign=5e46e6c2\&sv=2)

Uma vez feito isso, salve o arquivo como um CSV.

Uma vez que você tenha seu arquivo CSV, vá para a seguinte página da web. Isso depende de qual ambiente você está usando:

* Prod: http://api.docbits.com/
* Sandbox: http://sandbox.api.docbits.com/
* Stage: http://stage.api.docbits.com/
* Demo: http://demo.api.docbits.com/
* Dev: http://dev.api.docbits.com/

Aqui você fará o upload manual da tabela CostingElement via uma API. Clique no botão Autorizar.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FtyzOq3BR2QqTguQFKicxo0dE5j5hGsP-BhfVbS81O_mxN5bSVp40jYfgsVJcE_rBLFMDJNvbPkPIdjPqaqoNbHBBM-9hx0i-U4VAH9ISBYhpwKgqQeUEd67VV1E4izwNyxbAwwrhCmrAo1uIKhLherY\&width=768\&dpr=4\&quality=100\&sign=188f5712\&sv=2)

Aqui você precisará inserir a Chave da API do seu ambiente DocBits. Isso está localizado em Configurações sob Integração.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F4ADnevq6kq_vbxUJpyPbHNcGvRvpO-l9Gwd8ZaYf_vO4uWhSl1jmKNpddmHGc9ZHMMbXCgLOElLDYbNwB3INmBDETecPrDnpI601IUOZQlT7tc7OLSPXwkooOJFNwML2i_gvBPuE8CvfwRpX-ZIlb_g\&width=768\&dpr=4\&quality=100\&sign=dedfcaaf\&sv=2)

Uma vez completo, procure pela API chamada master\_data\_lookup/import\_data e preencha as informações necessárias. Uma vez completo, clique em EXECUTAR para acionar a API.

### data\_type precisa ser costing\_element

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F8UD4FhFv2dRB4cMjCDL4G9ndjH7laVMKWqdeMaJGgEo48-UVvucB1uOydzNdfFy0yPM5bb66mZB4k9uJR7TTiEREGFaV2EqW01gxJpTyuUfGNh5QmBjySkyhZ56gWV8sYs8WI5RnHcENtXgjTU0vg0Q\&width=768\&dpr=4\&quality=100\&sign=7c9f4dbb\&sv=2)

Se feito corretamente, a tabela M3CostingElement deve agora estar no seu ambiente DocBits. A extração de tabela para elementos de custo agora foi configurada para o seu ambiente.
