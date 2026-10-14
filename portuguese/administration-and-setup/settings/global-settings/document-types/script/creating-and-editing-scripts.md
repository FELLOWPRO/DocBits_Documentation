# Criando e Editando Scripts

{% embed url="https://youtu.be/n8NpWWIjmlA" %}
DocBits Document Scripts Explained: Automate Custom Logic in Your Document Workflow
{% endembed %}

## Para criar um novo script no DocBits, siga estas instruções detalhadas:

**Escolha a linguagem de script:**

Primeiro, você precisa escolher a linguagem de script que deseja usar. O DocBits normalmente suporta linguagens de script comuns, como Python, JavaScript ou SQL. A escolha da linguagem depende das necessidades do seu projeto e da sua própria competência.

**Abra o ambiente de desenvolvimento de script:**

Faça login no DocBits e navegue até o ambiente de desenvolvimento de script. Ele fica na área de administração.

<figure><img src="../../../../../.gitbook/assets/docbits_script_dev_environment.png" alt="Docbits Script Dev Environment"><figcaption></figcaption></figure>

**Crie un novo script:**

Clique no botão "+ Novo" para abrir um novo editor de script.

<figure><img src="../../../../../.gitbook/assets/docbits_new_script_editor.png" alt="Docbits New Script Editor"><figcaption></figcaption></figure>

**Escreva o código:**

Use o editor para escrever o código para o seu script. Comece com a sintaxe básica da linguagem de script escolhida.

Por exemplo, se você estiver usando Python, seu script pode ser assim:

## 1. Exemplo de script em Python

<figure><img src="../../../../../.gitbook/assets/docbits_script_python_example.png" alt="Docbits Script Python Example"><figcaption></figcaption></figure>

## Função para limpar nomes de pacientes

def clean_patient_name(name): cleaned_name = name.strip().title() # Remove espaços e aplica capitalização

return cleaned_name

## Programa principal

if __name__ == "__main__": patient_name = " john doe " cleaned_name = clean_patient_name(patient_name) print("Nome do paciente limpo:", cleaned_name)

## 2. Exemplo de script

<figure><img src="../../../../../.gitbook/assets/docbits_field_required_setting.png" alt="Docbits Field Required Setting"><figcaption></figcaption></figure>

**Teste o script:**

Verifique se há erros no código e teste-o em um ambiente de teste. Certifique-se de que o script produza os resultados esperados e funcione corretamente.

<figure><img src="../../../../../.gitbook/assets/docbits_field_readonly_setting.png" alt="Docbits Field Readonly Setting"><figcaption></figcaption></figure>

**Salve o script:**

Salve o script no DocBits e dê a ele um nome significativo que descreva o objetivo do script.

<figure><img src="../../../../../.gitbook/assets/docbits_field_hidden_setting.png" alt="Docbits Field Hidden Setting" width="84"><figcaption></figcaption></figure>

**Mapeamento do script para tipos de documento:**

Uma etapa importante é mapear o script para os tipos de documento apropriados. Isso determina quando e como o script é aplicado. Isso geralmente pode ser feito por meio de uma interface de configuração no DocBits, onde você pode atribuir o script a um tipo de documento específico e especificar sob quais condições ele deve ser aplicado.

<figure><img src="../../../../../.gitbook/assets/docbits_field_ocr_setting.png" alt="Docbits Field Ocr Setting"><figcaption></figcaption></figure>

**Revisão e publicação:**

Depois de criar, testar e mapear o script, verifique-o novamente em busca de erros e inconsistências. Se tudo estiver OK, você poderá publicar o script no ambiente de produção do DocBits.

<figure><img src="../../../../../.gitbook/assets/docbits_publish_script_button.png" alt="Docbits Publish Script Button"><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/docbits_field_forced_validation_setting.png" alt="Docbits Field Forced Validation Setting"><figcaption></figcaption></figure>

Por meio dessas etapas, você pode criar, testar e implementar com sucesso um novo script no DocBits para automatizar processos e melhorar a eficiência da documentação médica.
