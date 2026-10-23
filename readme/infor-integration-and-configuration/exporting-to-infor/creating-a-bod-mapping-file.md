# Criar um ficheiro de mapeamento BOD

Descarregue um ficheiro de mapeamento BOD e abra-o no editor de ficheiros que preferir. Neste guia, é utilizado o VSCode.

## Editar o ficheiro de mapeamento

Defina a empresa correta em SFV\_AccountingEntityID e altere o identificador da localização, se necessário.

![Ficheiro de mapeamento BOD aberto no VSCode com SFV_AccountingEntityID e outros mapeamentos chave-valor de SyncCaptureDocumentType](https://lh7-us.googleusercontent.com/eJQI1CKlxEkS\_Pwp0VH2hgS220b-q8NSFG5iJKpLOL457qTN3CbUB8IHTw1lRinbB\_kP00UUNgepWNsbh3\_Ko-SExObePjqmxP7ee\_lQnADTtDmxEtRM\_S7AONMbcpjwtnHTakYd1Q06GVm2G0o-UDA)

Verifique o código do tipo de documento nas respetivas configurações de campos. O código aparece no URL da página de campos do tipo de documento no DocBits, como no exemplo abaixo.

![Página de configurações de campos do DocBits para o tipo de documento de fatura no navegador com o URL que mostra o código do documento](https://lh7-us.googleusercontent.com/AhU3i27qFS7BMCgpNQnmLWAjcIWHXHOlxMKqd2Yob5RQKa8qysQQsSsacr6zao4cnAh3DISPgYu1GnjubIJpgtAdiBR\_0vy3WJZXPY-HeEfVQkWnlRI9UEJWMPQ7DbWYLQhz339BOlbd4KgxU9B\_CPE)

Por fim, altere SFV\_LogicalID. Em INFOR ION DESK → Connect → Connection points, selecione o ponto DocBits\_Export, ou equivalente, e copie o Logical ID apresentado.

![Página Connect no ION Desk com a lista de Connection Points e DocBits-Prod-Export selecionado](https://lh7-us.googleusercontent.com/f50i7pzRuZULJ6shehba0lWIWFBTsPZyip-LQxAYJpYDXK66SlzdGOpdEG-wqLQfqXMgMMhm5SAvj57UOCvF6xf2OMCXtFiEEKr9yiQr4xtv8vbV-NGcLuJwuQ9zHMBBKfTktAp1nSfBJhdPeAu3RWc)

![Página Connection Point DocBits-Prod-Export no ION Desk com API Client Id e Logical ID infor.ims.docbits-prod-export](https://lh7-us.googleusercontent.com/qyEt4iYRIjOZCCrVbImeK6EdZGun2YrAy8li8u3tulcD8bwzl\_sl1TiEXKqbik-4MxnbV\_MCwltvuA2WAgzzvDpTVd7W52he9QD9IK0qijoz3ZihUYcWJlqlD5kbcsRTj3SfP1CDqcyhoFfBeiE1Xfo)

## Criar o Logical ID (ponto de ligação)

Se o ponto de ligação ainda não existir, crie-o.

Abra ION Desk → Connect → Connection Points e clique em «+ Add».

![Menu Connect do ION Desk com a navegação Connection Points, Mappings e File Templates aberta](https://lh7-us.googleusercontent.com/fQPmV8KgffyWhM0i0cQlyh7fyQe37p8uR6C\_pVD5SboEx2emIJX2212GXqk\_KT71DfYMKSjkfYFFTARqgLLxoOPNQFXHxUOo9vMXH2pmDN469VgbQkV-JjRtCevZJsbvS8vbfUtasN83xN25tX6\_S5U)

Selecione «IMS via API Gateway».

![Lista de Connection Points no ION Desk com a opção IMS via API Gateway destacada entre os tipos de pontos de conexão disponíveis](https://lh7-us.googleusercontent.com/uPLiiLHp6Z3jPCzYBOzHVuI8sGY5XQuUfv66fZYH0HndSBL7yvzFHh3lJjEMxteJfXsVMhUe3U\_38xZHDRFSn0jeiMZUQBJJLzZ2oaIQAixY7wUPd6D0PJwg7wvC8XBeZxPmjNoiUvP3ImoG\_aOhFmY)

![Diálogo Infor Application Connection Point para IMS via API Gateway com as secções Authorization e IMS Endpoint](https://lh7-us.googleusercontent.com/VhyMDEuglPfxeX-3cATu6ZFB\_Mz2Y7C-yJ99EvBvrhD8IoVzGd4ksjrWAE0mIPub2PX5\_Zua10ZHQeWI82QbJ8ZgJKN-tVpVrYGvMdfQOj3Uco5efsPT6JYkDyPu\_lkeR9aTGhh5-q2bzZztXuTUixM)

Preencha os dados necessários no ecrã acima. Utilize um nome como «DocBits\_export».

Em «ION API Client ID», introduza o Client ID obtido anteriormente para o ficheiro de mapeamento ION.

Abra o separador Document da criação do ponto de ligação e adicione os documentos seguintes com o ícone «+». Estes serão utilizados posteriormente.

![Página Infor Application Connection Point DocBits-Sandbox-Export com o ID lógico infor.ims.docbits-sandbox-export](https://lh7-us.googleusercontent.com/GtHlTliePV-JIDLP9YNGlXELKuWIU2VSlUt4mvWO4q\_XM54MSL9zTmtxPMdeOl24VFtNC0pQ-nbXyHb9PaeMkKvgzpCOo5kLdL3A8Bw54ILniwIdTyfxFhPuzRUGKs2hRi5ioKvfkdsPMgq4x6EHOtM)

Depois de guardar o ponto de ligação, obterá o Logical ID, como no exemplo abaixo.

![Página de criação de Connection Point com o nome DocBits-Sandbox e o campo Logical ID Type](https://lh7-us.googleusercontent.com/P7cihsQT2Qcq\_XGL08dTV2jHMUK7YCMQyXsJudkVDXDh73GZ-hS61IoAKSHptPyX4C5e\_xPKP0yZGzpQOwCFw6BppPlzZuFWZ\_VGIrOUmJH2egxaCEXMoVBHBM6lkZeb3gPYWYdMYpuNqFFPC-4Qol0)

Introduza esse Logical ID na secção correspondente do ficheiro de mapeamento BOD e guarde o ficheiro.

## Carregar o ficheiro no DocBits

Arraste o ficheiro para a configuração de exportação do DocBits, em Configurações → Exportação.

![Página Export Settings do DocBits com as colunas Title, Document Type, Sub-Organizations, Export Method e Actions](https://lh7-us.googleusercontent.com/AqCo7QgC-kaAxbaIJD8MYeKGLBXbwGVJPGx9\_2yfUp3R2MYxJPowVAjnO80uxQ9qMDxNoXy1eY3WH-mEpaeWwatwi91edm\_0lS9Hg93FSAjQGtDAR5y7Ptce-ARfetSiXIBJKiGwujSggVXXHUhG77U)
