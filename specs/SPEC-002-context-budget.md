# SPEC: Orçamento de contexto por fase de entrega (Context budget by delivery phase)

## Metadados

| Campo | Valor |
|---|---|
| ID | SPEC-002 |
| Status | Implementada |
| Responsável | Agente de Especificação |
| Revisores | Engenharia / QA / Documentação |
| Criado | 2026-09-15 |
| Atualizado | 2026-09-15 |
| Liberação Alvo | Não programado |
| Refs: | Discovery: N/A — alteração interna do framework; Design: N/A — nenhuma interface voltada para o usuário; ADRs: N/A — apenas estrutura de documentação e recuperação |

## Problema e resultado

O `PROJECT.md` atualmente combina todo o estado do framework em um documento e os agentes não recebem nenhum pacote de contexto exato específico para a fase em que estão. À medida que a base de conhecimento (knowledge base) cresce, os agentes ou carregam contexto demais, ou omitem informações de forma inconsistente.

O resultado é um índice curto e canônico para o projeto, registros de conhecimento modulares onde as descobertas são baseadas apenas em metadados, e um orçamento (budget) explícito de contexto para Descoberta (Discovery), Arquitetura, Implementação, QA e Revisão. Desse modo, um agente pode recuperar apenas a SPEC ativa, a TAREFA (TASK) designada quando aplicável e os módulos de conhecimento explicitamente relevantes para sua fase.

## Escopo

### No escopo

- Adicionar `docs/context-budget.md` com os arquivos requeridos exatos e as seções permitidas para as fases de Discovery, Architecture, Implementation, QA, e Review.
- Reduzir o `PROJECT.md` a um índice canônico curto que vincula o contexto modular.
- Criar o `knowledge/INDEX.md` com metadados e orientações de recuperação em vez de manter o conteúdo copiado de seus módulos.
- Mover o atual conteúdo do estado do projeto para os módulos de domínio reutilizáveis sob `knowledge/modules/` sem perder as informações canônicas.
- Adicionar uma regra explícita no arquivo `AGENTS.md` proibindo agentes de carregar toda a base de conhecimento quando a SPEC referenciar módulos selecionados.
- Preservar caminhos existentes onde for possível e documentar um plano de migração para adotantes que usam um arquivo monolítico `PROJECT.md`.

### Fora do escopo

- Mudar a ordem de workflow, portões de qualidade (quality gates), IDs, referências de tarefas ou papéis dos agentes.
- Construir sistema de busca semântica, embeddings (incorporações), um banco de dados vetorial, um contador de tokens, ou um carregador de contexto (context loader) em runtime.
- Alterar o conteúdo do conhecimento do projeto que adota o framework além de guias de migração e templates reutilizáveis.

## Comportamento funcional

- Cada orçamento da fase diz o nome dos documentos obrigatórios, os opcionais e as leituras amplas que estão proibidas. Uma fase pode apenas carregar módulos de conhecimento que foram nomeados por sua SPEC ativa, ou módulos expressamente justificados devido a riscos anotados.
- `PROJECT.md` permanece como o ponto de entrada canônico, mas seus detalhes são dispostos como links para os módulos, ao invés de prosa duplicada.
- O `knowledge/INDEX.md` suporta recuperação seletiva usando títulos dos módulos, o seu domínio, quem os criou, data de atualização, resumo (summary metadata) e status da origem da fonte da verdade.
- Uma nota de migração (migration note) torna o acréscimo de novos módulos algo de fácil agregação àqueles usuários que desejam conservar seus sistemas baseados em arquivos únicos.

## Critérios de aceitação

### AC-001: Toda a fase de entrega tem um pacote de contexto executável

```gherkin
Dado um agente inicializa Discovery, Architecture, Implementation, QA ou Review
Quando consulta o manual de orçamento de contexto (context budget)
Então este pode identificar perfeitamente a exatidão dos arquivos necessários, a escolha permitida aos módulos e ler amplamente a política para aquela fase
```

Evidência requerida: revisão de documentação.

### AC-002: O contexto de projeto suporta recuperação seletiva

```gherkin
Dado que o agente abre o PROJECT.md e knowledge/INDEX.md
Quando necessita de contexto referente a alterações correntes
Então encontra perfeitamente todos os seus dados relevantes dentre os meta e sem carregar todas as funções existentes, não comprometendo de nenhuma forma os estados prévios canônicos do projeto
```

Evidência requerida: migração e auditoria de link.

### AC-003: Os processos ativos usam apenas funções precisas (relevant knowledge)

```gherkin
Dado que a SPEC em andamento menciona algumas dependências específicas (knowledge modules)
Quando algum agente orienta-se por AGENTS.md
Então ele executa a SPEC junto aos seus recursos essenciais se existir algo correspondente; somente se requisitado formalmente os recursos extraordinários farão parte dos cálculos ou do pacote final
```

Evidência requerida: inspeção de política.

### AC-004: Compatível retroativamente e propício à fácil adoção

```gherkin
Dado um formato antiquado centrado sobre um único arquivo PROJECT.md
Quando uma equipe transita ao plano de inovação
Então dispõe livremente e ininterruptamente da progressão orientada e com migração em andamento gradual
```

Evidência requerida: revisão de documentação.

## Abordagem técnica

A solução usará apenas Markdown. O plano fará as averiguações em categorias isoladas antes de dividi-las aos conjuntos de conhecimentos e em seguida direcionará tudo aos canais apropriados em conformidade e sem perdas de especificações primárias já adotadas pelo software em vigor.

## Riscos e dependências

| Risco ou dependência | Impacto | Probabilidade | Mitigação | Responsável |
|---|---|---|---|---|
| O orçamento de contexto omite uma fonte material | Decisão de entrega incorreta | Média | Exigir uma exceção documentada baseada em risco e validar cada pacote de fase | Agente de QA |
| O detalhe é perdido ao modularizar o PROJECT.md | Divergência de documentação | Média | Auditar cada seção atual em relação ao novo índice e aos módulos | Agente de Documentação |
| Os módulos reproduzem políticas normativas | Fontes de verdade conflitantes | Média | Link para padrões e workflows com autoridade em vez de copiá-los | Agente de Implementação |

## Questões abertas

| Questão | Responsável | Data limite | Resolução |
|---|---|---|---|
| Que tamanho (extensão) deve ser base pra julgar se o índice de PROJECT.md já está suficientemente minúsculo ou enxuto? | Revisor de Engenharia | 2026-09-15 | Resolvido: foco sobre algo que possua no máximo 75 linhas de abrangência (sem somar caracteres brancos ou separadores ao cômputo). |

## Aprovação

| Papel | Nome | Decisão | Data | Notas |
|---|---|---|---|---|
| Engenharia | | Pendente | | |
| QA | | Pendente | | |
| Documentação | | Pendente | | |
| Patrocinador Humano | Usuário | Aprovado | 2026-09-15 | Aprovação registrada pela instrução de execução. |
