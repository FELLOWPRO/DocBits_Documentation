# Faktura

## Exibir atributo em cada item de linha

Se você deseja exibir um atributo específico (como o número do Pedido de Compra) em cada item de linha, siga as etapas abaixo. A abordagem será diferente dependendo se você precisa do atributo na extração JSON ou na saída XSL.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.33.16.png" alt=""><figcaption></figcaption></figure>

### Método 1: Exibir Atributo na Extração JSON (configuração DocBits)

1. Vá para **Configurações**
2. Vá para **Tipos de Documento**
3. Selecione **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt=""><figcaption></figcaption></figure>

4. Abra a aba **"FATTURAPA"**
5. Clique em **JSON**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.01.13.png" alt=""><figcaption></figcaption></figure>

6. Para criar um rascunho, clique no ícone do **lápis**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt=""><figcaption></figcaption></figure>

7. Dentro do array `"tables"`, adicione a coluna específica que deseja exibir fornecendo um nome e um caminho:

```
{ 
"name": "PURCHASE_ORDER",    
"path":"path_to_source" 
}
```

**NOTA:** Os e-documentos sempre terão a origem definida como **Grã-Bretanha**, portanto, os valores serão salvos no formato internacional, usando um **ponto (.)** como separador decimal.

8. Salve o rascunho

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt=""><figcaption></figcaption></figure>

9. Certifique-se de que seu rascunho seja o **ativo**.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt=""><figcaption></figcaption></figure>

### Método 2: Exibir Atributo na Saída XSL (visualização HTML/PDF)

1. Vá para **Configurações**
2. Vá para **Tipos de Documento**
3. Selecione **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt=""><figcaption></figcaption></figure>

4. Abra a aba **"FATTURAPA"**
5. **Clique em XLST**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.23.06.png" alt=""><figcaption></figcaption></figure>

6. Para criar um rascunho, clique no ícone do **lápis**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt=""><figcaption></figcaption></figure>

7. No bloco `<xsl:for-each select="path">` que gera as linhas da tabela, adicione um trecho como este onde você deseja que o atributo apareça (por exemplo, em sua própria coluna):

```
<tr>
    <!-- Outras colunas ... -->

    <td>
        <!-- PO number -->
        <xsl:variable name="variable_name" select="value" />
        <xsl:value-of 
            select="path_to_attribute" 
        />
    </td>
</tr>
```

**NOTA:** Os e-documentos sempre terão a origem definida como **Grã-Bretanha**, portanto, os valores serão salvos no formato internacional, usando um **ponto (.)** como separador decimal.

8. Salve o rascunho

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt=""><figcaption></figcaption></figure>

9. Certifique-se de que seu rascunho seja o **ativo**.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt=""><figcaption></figcaption></figure>
