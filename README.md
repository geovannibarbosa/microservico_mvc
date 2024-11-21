# microservico_mvc

Grupo - 15
Geovanni Barbosa
Silvana Araujo
Lucivanio Junior

-----------------------------------------------

O sistema de atividades está implementado, e agora é necessário implementar algumas funcionalidade para permitir que os usuários (professores) possam realizar operações de criação, atualização e exclusão de atividades. 
Deve-se implementar os endpoints de POST, PUT  e DELETE, respeitando a arquitetura já definida do microsserviço.

A tarefa é adicionar as funcionalidades de criação, atualização e exclusão de atividades no serviço de atividades, mantendo a arquitetura e o padrão de código já fornecidos.

A atividade deve ter os seguintes campos (já definidos):
id_atividade: Identificador único da atividade (número inteiro).
id_disciplina: Identificador da disciplina à qual a atividade pertence (número inteiro).
enunciado: Descrição da atividade (texto).
respostas: Lista de respostas fornecidas pelos alunos (lista de objetos com id_aluno, resposta e nota).
Criar as rotas: POST (/atividades/): Cria uma nova atividade.
Requer um corpo de solicitação com os campos id_disciplina, enunciado e respostas (campo respostas pode ser uma lista vazia inicialmente).

PUT (/atividades/<int:id_atividade>/): Atualiza uma atividade existente.
Requer um corpo de solicitação com os campos id_disciplina, enunciado e respostas (os campos podem ser alterados).

DELETE (/atividades/<int:id_atividade>/): Exclui uma atividade existente.
Exclui a atividade com o id_atividade especificado.

Além disse, enviar alguns prints de TODAS as rotas sendo executadas no Postman + código fonte

Recomendação: Clone o repositório do projeto, faça as implementações, crie uma pasta "imagens" inserindo as imagens solicitadas e suba em seu github.

Projeto deve ser realizado com o mesmo grupo da AP2 e entregue via github.
