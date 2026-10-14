# Resolução de Problemas de Controle de Acesso e Permissões

Se os usuários estiverem enfrentando restrições de acesso inesperadas, como documentos ausentes, incapacidade de editar campos ou ações negadas, use a seguinte lista de verificação para identificar e resolver o problema com base na configuração das permissões no DocBits.

### 1. Verificar Se o Controle de Acesso Está Habilitado

As configurações de Controle de Acesso se aplicam apenas se o recurso estiver **habilitado**.

* Navegue até: `Configurações` > `Processamento de Documentos` > `Módulo`.
* Certifique-se de que a chave de **Controle de Acesso** esteja ligada.
* Se desativado, todos os usuários geralmente têm acesso irrestrito, independentemente das permissões de grupo ou campo.

### 2. Verificar Atribuições de Grupo

Certifique-se de que o usuário esteja corretamente atribuído ao(s) grupo(s) apropriado(s):

* Navegue até: `Configurações` > `Configurações Globais` > `Grupos, Usuários e Permissões`.
* Selecione **Grupos e Permissões**.
* Confirme se o usuário está listado sob o grupo esperado.
* Se o grupo usar controle de acesso específico, a falta de atribuição de grupo bloqueará o acesso a documentos e ações.

### 3. Revisar Permissões de Acesso do Grupo

O acesso é concedido por tipo de documento e por ação:

* Na tela de **Controle de Acesso** do grupo, verifique o tipo de documento (por exemplo, Fatura, Ordem de Compra).
* Valide permissões como:
  * **Listar**, **Visualizar**, **Editar**, **Excluir**, **Atualização em Massa**
  * **Níveis de Aprovação** (1º, 2º), **Desbloquear Documento**
* Certifique-se de que o nível de acesso não esteja limitado a **Proprietário** ou **Administrador**, a menos que seja apropriado.

### 4. Confirmar Permissões de Nível de Campo

O acesso também pode ser restrito no **nível de campo**, o que pode bloquear a edição ou visibilidade:

* Na configuração de Controle de Acesso do grupo, navegue até o tipo de documento e verifique as configurações de nível de campo.
* Confirme se os campos estão definidos como:
  * **Ler/Escrever**, **Somente Leitura**, **Escrita do Proprietário**, **Nenhum**
* Ajuste, se necessário, com base na função do usuário.

### 5. Verificar a Configuração "Apenas Documentos Atribuídos"

Essa configuração global limita a visibilidade do documento:

* Navegue até: `Configurações` > `Configurações Globais` > `Grupos, Usuários e Permissões`.
* Se **Apenas Documentos Atribuídos** estiver **habilitado**, os usuários só podem ver documentos atribuídos explicitamente a eles ou ao seu grupo.
* Se os usuários não puderem ver os documentos esperados:
  * Verifique as atribuições de documentos.
  * Desative temporariamente a configuração para testar se é a causa raiz.

### 6. Testar com um Usuário ou Grupo com Funcionamento Conhecido

Para isolar o problema:

* Faça login com um usuário de um grupo que tenha acesso confirmado.
* Compare a visibilidade do documento e as ações disponíveis.
* Isso ajuda a determinar se o problema é específico do usuário, do grupo ou do sistema.

### 7. Revisar Atribuições de Documentos

Se "Apenas Documentos Atribuídos" estiver **habilitado**, certifique-se de que:

* O documento esteja **atribuído** ao usuário ou a um dos seus grupos.
* Use os controles de atribuição na visualização detalhada do documento para fazer ou revisar as atribuições.

### 8. Redefinir ou Reconfigurar Permissões

Se as permissões foram alteradas recentemente ou os usuários foram movidos entre grupos:

* Confirme se as configurações de Controle de Acesso refletem as novas configurações de grupo.
* Ajuste as permissões de campo e documento conforme necessário.
* Se estiver inseguro, crie um grupo de teste com permissões amplas e teste o comportamento de acesso antes de aplicar alterações aos grupos ativos.
