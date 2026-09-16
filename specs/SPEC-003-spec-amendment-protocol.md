# SPEC: Protocolo de alteração de SPEC (SPEC amendment protocol)

## Metadados

| Campo | Valor |
|---|---|
| ID | SPEC-003 |
| Status | Implementada |
| Responsável | Agente de Especificação |
| Revisores | Produto / Engenharia / QA |
| Criado | 2026-09-15 |
| Atualizado | 2026-09-15 |
| Liberação Alvo | Não programado |
| Refs: | Discovery: N/A — alteração interna do framework; Design: N/A — nenhuma interface voltada para o usuário; ADRs: N/A — apenas documentação de fluxo de trabalho |

## Problema e resultado

Descobertas na implementação atualmente não têm um caminho leve e auditável para esclarecer uma SPEC aprovada. As equipes podem ignorar o registro de aprovação ou repetir um ciclo completo de aprovação para um texto que não altera o comportamento observável.

O resultado é um registro reutilizável de solicitação de mudança e critérios objetivos de portão (gate criteria) que distinguem um esclarecimento de uma mudança de escopo, preservam as versões da SPEC e garantem que qualquer mudança material de comportamento retorne à aprovação humana.

## Escopo

### No escopo

- Estender o guia de ID e rastreabilidade com o ciclo de vida de alteração da SPEC e as regras de referência `SPEC-NNN-vN`.
- Adicionar `templates/CHANGE_REQUEST_TEMPLATE.md` com fluxos distintos para esclarecimentos leves (lightweight clarification) e alterações de escopo.
- Adicionar requisitos objetivos de classificação e aprovação a `standards/quality-gates.md`.

### Fora do escopo

- Alterar a atual autoridade de aprovação, sequência de portões de qualidade, esquema de ID de tarefa ou gerador de rastreabilidade.
- Aprovar, mesclar ou aplicar automaticamente uma solicitação de alteração.
- Definir ferramentas de issue-tracker (rastreamento de problemas), notificação ou aprovação assíncrona.

## Comportamento funcional

- Um esclarecimento leve (lightweight clarification) registra a pergunta, resolução, justificativa e aprovação assíncrona; não pode modificar o comportamento observável ou os critérios de aceitação.
- Uma mudança de escopo registra o impacto e cria uma versão de SPEC alterada, exigindo o ciclo completo de aprovação humana aplicável antes de a implementação continuar.
- Os portões de qualidade classificam uma solicitação usando testes explícitos de comportamento observável e critérios de aceitação; incertezas são tratadas como mudança de escopo.

## Critérios de aceitação

### AC-001: Alterações de SPEC preservam a rastreabilidade versionada

```gherkin
Dado que uma SPEC aprovada requer uma mudança de escopo
Quando uma alteração é registrada
Então o guia define seu identificador SPEC-NNN-vN, referência do predecessor e relação de aprovação sem sobrescrever a SPEC aprovada anteriormente
```

Evidência requerida: revisão de documentação.

### AC-002: Solicitações de alteração expõem os dois caminhos de decisão

```gherkin
Dado uma descoberta de implementação
Quando um autor usa o template de solicitação de mudança (change request)
Então pode-se registrar um esclarecimento leve ou uma mudança de escopo com o impacto, decisão e campos de aprovação necessários para aquele caminho
```

Evidência requerida: inspeção de template.

### AC-003: A classificação é um portão de qualidade bloqueador

```gherkin
Dado uma solicitação de alteração proposta
Quando o seu comportamento observável ou impacto nos critérios de aceitação é incerto ou foi alterado
Então o padrão de portões de qualidade classifica-a como uma mudança de escopo e bloqueia a implementação até que a aprovação humana seja registrada
```

Evidência requerida: revisão de padrões.

## Abordagem técnica

Usar apenas documentação Markdown e um template reutilizável. Preservar `SPEC-NNN` como o identificador base e adicionar `-vN` apenas para alterações de escopo aprovadas. A implementação registrará explicitamente que um esclarecimento não é uma nova versão de SPEC, enquanto uma mudança de escopo nunca substitui o predecessor aprovado.

## Riscos e dependências

| Risco ou dependência | Impacto | Probabilidade | Mitigação | Responsável |
|---|---|---|---|---|
| Esclarecimentos rotulados erroneamente para burlar a aprovação | Expansão de escopo não documentada | Média | Usar perguntas objetivas de portão e classificar incertezas como mudança de escopo | Agente de QA |
| Conflitos de versionamento de tarefa ou de commit | Rastreabilidade quebrada | Baixa | Documentar referências exatas e preservar artefatos anteriores | Agente de Implementação |
| A aprovação assíncrona carece de evidência durável | Decisão não verificável | Média | Requerir aprovador, timestamp e referência de aprovação estável | Agente de Especificação |

## Questões abertas

| Questão | Responsável | Data limite | Resolução |
|---|---|---|---|
| Quais funções humanas podem dar aprovação assíncrona a esclarecimentos? | Product owner | 2026-09-15 | Resolvido: a mesma autoridade humana que aprovou a SPEC base. |

## Aprovação

| Papel | Nome | Decisão | Data | Notas |
|---|---|---|---|---|
| Produto | | Pendente | | |
| Engenharia | | Pendente | | |
| QA | | Pendente | | |
| Patrocinador Humano | Usuário | Aprovado | 2026-09-15 | Aprovação registrada na conversa do CLI. |
