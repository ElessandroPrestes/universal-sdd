# SPEC: Rastreabilidade mecanizada (Mechanized traceability)

## Metadados

| Campo | Valor |
|---|---|
| ID | SPEC-001 |
| Status | Implementada |
| Responsável | Agente de Especificação |
| Revisores | Engenharia / QA |
| Criado | 2026-09-15 |
| Atualizado | 2026-09-15 |
| Liberação Alvo | Não programado |
| Relacionado a UX brief | N/A — documentação interna do framework e alteração de ferramentas |
| Relacionado a design spec | N/A — nenhuma interface voltada para o usuário |
| Relacionado a ADRs | Nenhum identificado; a mudança não altera a arquitetura do framework |

## Problema e resultado

O framework requer rastreabilidade entre requisitos aprovados, trabalhos executáveis, commits e evidências de QA, mas atualmente não fornece nenhum esquema estável de identificadores, matriz legível por máquina (machine-readable matrix) ou validação no momento do commit. Isso faz com que a auditoria dependa de revisão manual de documentos.

O resultado são artefatos de framework reutilizáveis e com poucas dependências que estabelecem e validam uma cadeia auditável desde a SPEC até a TAREFA (TASK), commit e status de QA.

## Escopo

### No escopo

- Documentar identificadores estáveis `SPEC-NNN`, `TASK-NNN-XX` e `ADR-NNN` e os seus relacionamentos de referência.
- Adicionar os campos ID e `Refs:` (Referências) a templates reutilizáveis de SPEC e TASK sem remover os templates minúsculos (lowercase) existentes.
- Documentar os trailers de commit necessários `Spec-Ref:` e `Task-Ref:` no arquivo `AGENTS.md`.
- Adicionar um script reutilizável e com poucas dependências que varre (scans) as pastas `specs/`, `tasks/`, `reviews/` e o histórico do Git para gerar uma matriz de rastreabilidade em `docs/`.
- Adicionar um template de hook `commit-msg` opcional que valida os trailers requeridos.

### Fora do escopo

- Verificação automática de critérios de aceitação ou de evidências estruturadas de QA.
- Reestruturação de limites de contexto (context-budget), alterações de SPEC, contratos de transferência (handoff) de agentes, higienização de conteúdo externo e métricas do framework.
- Instalar hooks automaticamente, mudar o histórico do Git, ou requerer uma linguagem de programação específica, provedor de CI ou rastreador de problemas (issue tracker).

## Comportamento funcional

- O guia de identificadores especifica os formatos, as expectativas de singularidade (uniqueness) e como os artefatos são vinculados a seu predecessor na cadeia de entrega.
- Os novos templates tornam os campos `ID` e `Refs:` explícitos para uso futuro, mantendo os caminhos de templates existentes de forma compatível retroativamente.
- O gerador de matriz reporta, para cada SPEC descoberta, as tarefas (TASKs) vinculadas, os commits correspondentes do Git e os status disponíveis de QA/revisão sem modificar os artefatos originais ou o histórico do Git.
- O hook opcional rejeita mensagens de commit que não contenham os trailers necessários estipulados pela convenção documentada, enquanto os projetos continuam livres para aderir copiando o hook para o diretório de hooks do Git.

## Critérios de aceitação

### AC-001: A convenção de identificadores e links é reutilizável

```gherkin
Dado um projeto que adota o framework
Quando criar uma SPEC, TAREFA (TASK) ou ADR
Então o guia de identificadores define o formato e as relações de vinculação do identificador sem depender de exemplos específicos do projeto
```

Evidência requerida: revisão de documentação.

### AC-002: Templates capturam as referências exigidas

```gherkin
Dado que um autor cria uma SPEC ou TAREFA (TASK) usando o novo template
Quando preencher a seção de metadados
Então este tem os campos explícitos ID e Refs para registro da rastreabilidade
```

Evidência requerida: inspeção de template.

### AC-003: Referências de commit são documentadas e validadas opcionalmente

```gherkin
Dado um projeto que opte por usar o hook fornecido commit-msg
Quando uma mensagem de commit omitir um trailer de referência exigido documentado
Então o hook rejeita a mensagem de commit com um erro acionável
```

Evidência requerida: teste local do hook.

### AC-004: A matriz de rastreabilidade é reprodutível

```gherkin
Dado um repositório que contém SPECs, TAREFAS (TASKs), revisões e commits do Git
Quando o gerador de matriz for executado
Então ele escreve uma matriz consultável que mapeia as SPECs descobertas para TAREFAS vinculadas, commits correspondentes e status de QA ou de revisão
```

Evidência requerida: teste do gerador usando artefatos do repositório.

## Abordagem técnica

Usar documentação Markdown e templates mais um script usando apenas a biblioteca padrão (standard-library-only), escolhido durante a implementação. O script deve tolerar diretórios opcionais ausentes e referências sem correspondência, reportando-os como lacunas (gaps) em vez de inventar links. O formato gerado para a matriz será Markdown ou JSON, escolhido na TAREFA de implementação baseando-se em testabilidade e em ser passível de revisão.

## Entrega e operações

- Plano de rollout: publicar novos artefatos juntamente com os templates existentes.
- Plano de migração: projetos existentes podem manter artefatos atuais; os novos IDs e referências são adotados gradualmente.
- Plano de rollback: remover o uso opcional do novo script e do hook; nenhuma migração de dados ou histórico do Git é realizada.
- Monitoramento e alertas: N/A — este framework atualmente não possui runtime (tempo de execução).

## Riscos e dependências

| Risco ou dependência | Impacto | Probabilidade | Mitigação | Responsável |
|---|---|---|---|---|
| Artefatos históricos sem IDs ou trailers | Linhas de matriz incompletas | Alta | Relatar lacunas explicitamente; não exigir reescrita retroativa | Agente de Implementação |
| O Git está indisponível para o script | Dados de commit não podem ser coletados | Baixa | Sair do script com um diagnóstico prático preservando os artefatos | Agente de Implementação |
| Convenção do hook entra em conflito com a política do adotante | Atrito na adoção | Média | Manter o hook opcional e documentar expectativas de instalação/sobrescrita | Agente de Documentação |

## Questões abertas

| Questão | Responsável | Data limite | Resolução |
|---|---|---|---|
| A matriz gerada deve ser Markdown, JSON, ou ambos? | Revisor de Engenharia | Antes da aprovação da TAREFA (TASK) | Aberta |

## Aprovação

| Papel | Nome | Decisão | Data | Notas |
|---|---|---|---|---|
| Engenharia | | Pendente | | |
| QA | | Pendente | | |
| Patrocinador Humano | Usuário | Aprovado | 2026-09-15 | Aprovação registrada na conversa do CLI. |
