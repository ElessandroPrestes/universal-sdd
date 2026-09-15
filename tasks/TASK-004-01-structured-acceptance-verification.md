# TASK: Implement structured acceptance verification

## Metadados

| Campo | Valor |
|---|---|
| ID | TASK-004-01 |
| Status | Done |
| Responsável | Implementation Agent |
| SPEC | SPEC-004 |
| Critérios | AC-001, AC-002, AC-003 |
| Dependências | Melhoria 6 for operational structured QA evidence |

## Objetivo

Definir critérios de aceite estruturados no template canônico e um QA-Verifier
bloqueante, sem introduzir parser ou esquema de evidência antes da Melhoria 6.

## Escopo

### Incluído

- Atualizar o template canônico com YAML por critério `AC-NNN`.
- Criar o workflow QA-Verifier e sua saída de divergências.
- Integrar a verificação como pré-condição bloqueante antes do Code Review.
- Adicionar testes estruturais aos novos contratos documentais.

### Não incluído

- Alterar template legado, SPECs existentes, CI ou executar QA-Verifier com
  evidência não estruturada.
- Criar o arquivo de evidência estruturada da Melhoria 6.

## Abordagem e impacto

- Arquivos ou componentes prováveis: `templates/SPEC_TEMPLATE.md`,
  `workflows/verification.md`, `standards/quality-gates.md` e testes em `tests/`.
- Dados, contratos ou migrações: o YAML é o formato canônico futuro; o template
  minúsculo existente continua disponível para adoção compatível.
- Riscos e precauções: não declarar o gate operacional sem a evidência da
  Melhoria 6; toda divergência deve ser listada em vez de inferida.
- ADRs e padrões aplicáveis: `standards/quality-gates.md` e
  `standards/testing.md`.

## Passos

- [x] Padronizar o bloco YAML de critérios no template canônico.
- [x] Definir entradas, comparação e saída do QA-Verifier.
- [x] Inserir o gate bloqueante antes do Code Review.
- [x] Executar testes estruturais e atualizar a matriz.

## Validação

| Critério/risco | Teste, comando ou revisão | Evidência esperada |
|---|---|---|
| AC-001 | Teste do template | Campos YAML obrigatórios por critério presentes |
| AC-002 | Teste do workflow | Entradas, lista de divergências e ordem antes de review presentes |
| AC-003 | Teste dos gates | Findings abertos bloqueiam Code Review |

## Condição de conclusão

- [x] Escopo implementado sem expansão.
- [x] Testes e validações aplicáveis passam.
- [x] Documentação e rastreabilidade foram atualizadas.
- [x] Limitações e desvios estão registrados.

## Resultado

- Mudanças realizadas: critérios YAML, workflow QA-Verifier, gate antes de
  Code Review, integração ao workflow principal e testes estruturais.
- Evidências: em 2026-09-15, `python3 -m unittest discover -s tests -v` passou
  com 11 testes; `python3 scripts/generate_traceability.py` gerou a matriz e
  `git diff --check` não reportou erros.
- Pendências ou bloqueios: decisão humana registrada em
  `reviews/REVIEW-004-structured-acceptance-verification.md`; a Melhoria 6
  precisa fornecer o formato de evidência estruturada para operação em produção.
