# TASK: Implement phase-specific context budgets

## Metadados

| Campo | Valor |
|---|---|
| ID | TASK-002-01 |
| Status | In review |
| Responsável | Implementation Agent |
| SPEC | SPEC-002 |
| Critérios | AC-001, AC-002, AC-003, AC-004 |
| Dependências | Markdown repository structure only |

## Objetivo

Converter o estado monolítico do projeto em um índice curto e módulos de
conhecimento recuperáveis seletivamente, com regras verificáveis de contexto
para cada fase de entrega.

## Escopo

### Incluído

- Criar o guia de orçamento de contexto por fase e a política em `AGENTS.md`.
- Limitar `PROJECT.md` a 75 linhas ou menos e preservar seu papel de índice
  canônico.
- Criar `knowledge/INDEX.md` e módulos que cubram todas as categorias antes
  presentes em `PROJECT.md`.
- Alinhar a documentação da Knowledge Base à nova composição do estado canônico.
- Adicionar verificações estruturais reutilizáveis para os critérios documentais.

### Não incluído

- Alterar requisitos, workflows, quality gates, roles ou conteúdo normativo de
  standards e ADRs.
- Criar automação de busca semântica, embeddings ou contagem de tokens.

## Abordagem e impacto

- Arquivos ou componentes prováveis: `PROJECT.md`, `AGENTS.md`,
  `docs/context-budget.md`, `docs/knowledge-base.md`, `knowledge/INDEX.md`,
  `knowledge/modules/` e testes em `tests/`.
- Dados, contratos ou migrações: módulos são aditivos; o índice e o guia
  documentam a transição sem remover caminhos existentes.
- Riscos e precauções: conferir cada categoria do PROJECT anterior; módulos
  apontam para documentos normativos em vez de duplicar regras.
- ADRs e padrões aplicáveis: `standards/quality-gates.md` e
  `standards/testing.md`.

## Passos

- [ ] Criar a política e o orçamento de contexto por fase.
- [ ] Modularizar as categorias de estado atual e criar índices de recuperação.
- [ ] Reduzir `PROJECT.md` a um índice canônico de até 75 linhas.
- [ ] Atualizar orientação de Knowledge Base e validar estrutura e links.

## Validação

| Critério/risco | Teste, comando ou revisão | Evidência esperada |
|---|---|---|
| AC-001 | Teste estrutural do guia | Todas as cinco fases têm entradas obrigatórias, permitidas e proibidas |
| AC-002 | Teste de índice e módulos | Cada módulo indexado existe e preserva uma categoria anterior |
| AC-003 | Inspeção do `AGENTS.md` e teste textual | Regra restringe a SPEC ativa, TASK e módulos referenciados |
| AC-004 | Revisão da seção de migração | Caminhos anteriores permanecem e a adoção incremental é documentada |

## Condição de conclusão

- [x] Escopo implementado sem expansão.
- [x] Testes e validações aplicáveis passam.
- [x] Documentação e rastreabilidade foram atualizadas.
- [x] Limitações e desvios estão registrados.

## Resultado

- Mudanças realizadas: guia por fase, índice curto de projeto, módulos de
  conhecimento, índice de recuperação, política de agentes e testes estruturais.
- Evidências: em 2026-09-15, `python3 -m unittest discover -s tests -v` passou
  com 5 testes; `python3 scripts/generate_traceability.py` gerou a matriz e
  `git diff --check` não reportou erros.
- Pendências ou bloqueios: QA e review independentes permanecem pendentes.
