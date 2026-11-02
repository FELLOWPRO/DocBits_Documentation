# Teste de importação de ficheiros 1

## Finalidade

Estes testes verificam o funcionamento da importação de ficheiros PDF e TIFF, confirmando que são processados e guardados com êxito no sistema.

#### Preparação e limpeza dos testes

* **Preparação:**
  * Antes de cada teste, é registada uma mensagem de preparação.
  * **Limpeza:** após cada teste, os documentos criados pelo utilizador de teste são eliminados da base de dados para evitar que dados residuais afetem os testes seguintes.

#### Cenários de teste

1. **Importar um ficheiro PDF:**
   * **Teste de importação de PDF (`test_import_pdf`):**
     * Importar um ficheiro PDF (`FellowBananaInvoice.pdf`) para o sistema.
     * **Resultado esperado:** o ficheiro é importado com êxito e é devolvido um identificador de documento.
2. **Importar um ficheiro TIFF:**
   * **Teste de importação de TIFF (`test_import_tiff`):**
     * Importar um ficheiro TIFF (`TIFF_FILE.TIF`) para o sistema.
     * **Resultado esperado:** o ficheiro é importado com êxito e é devolvido um identificador de documento.

## Explicação detalhada de cada teste

* **Preparação e limpeza:**
  * **Registo:** são registadas mensagens de preparação e limpeza para cada teste.
  * **Limpeza da base de dados (`clean_documents`):** elimina da base de dados os documentos criados pelo utilizador de teste para manter um estado limpo.
*   **Testes de importação de ficheiros:**

    **Importar um ficheiro PDF:**

    * **Carregar o utilizador:** carregar o utilizador de teste.
    * **Caminho do ficheiro:** indicar o caminho do ficheiro PDF (`tests/files/pdfs/FellowBananaInvoice.pdf`).
    * **Importar o ficheiro:** utilizar a classe `FileImporter` para importar o PDF.
    * **Verificar a resposta:** confirmar que é uma lista com uma mensagem de sucesso e um identificador de documento.

    **Importar um ficheiro TIFF:**

    * **Carregar o utilizador:** carregar o utilizador de teste.
    * **Caminho do ficheiro:** indicar o caminho do ficheiro TIFF (`tests/files/pdfs/TIFF_FILE.TIF`).
    * **Importar o ficheiro:** utilizar a classe `FileImporter` para importar o TIFF.
    * **Verificar a resposta:** confirmar que é uma lista com uma mensagem de sucesso e um identificador de documento.

## Estrutura do código

* **Registo de eventos:** regista mensagens de depuração durante a preparação, a limpeza e a execução dos testes.
* **Auxiliar de base de dados:** executa consultas sem devolver resultados para efetuar a limpeza.
* **Importador de ficheiros:** gere a importação de ficheiros para o sistema.
* **Fixtures:** a fixture `set_up` gere a preparação e a limpeza dos testes.
* **Testes:**
  * `test_import_pdf`: testa a importação de um ficheiro PDF.
  * `test_import_tiff`: testa a importação de um ficheiro TIFF.

#### Resumo

Estes testes verificam se a importação de PDF e TIFF funciona como esperado, confirmando a importação correta dos ficheiros e o tratamento de diferentes tipos de ficheiro.


