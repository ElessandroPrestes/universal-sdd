# TASK: Implement structured QA evidence schema and contract

## Metadados

| Campo | Valor |
|---|---|
| ID | TASK-005-01 |
| Status | Done |
| Responsável | Implementation Agent |
| SPEC | SPEC-005 |
| Critérios | AC-001, AC-002, AC-003 |
| Dependências | Structured acceptance criteria baseline |

## Objetivo

Disponibilizar o contrato e os templates estruturados de evidência de QA e de
relatório de verificação, atualizando os fluxos para tornar o QA-Verifier operacional.

## Escopo

### Incluído

- Criar `templates/QA_EVIDENCE_TEMPLATE.md` com YAML estruturado por critério `AC-NNN`.
- Criar `templates/VERIFICATION_REPORT_TEMPLATE.md` para saída do QA-Verifier.
- Atualizar `workflows/verification.md` e `standards/testing.md`.
- Adicionar testes estruturais em `tests/test_structured_qa_evidence.py`.

### Não incluído

- Criar executáveis de CI ou parsers automatizados em código de produção.
- Alterar evidências ou formatos de SPECs já finalizadas.

## Abordagem e impacto

- Arquivos ou componentes prováveis: `templates/QA_EVIDENCE_TEMPLATE.md`,
  `templates/VERIFICATION_REPORT_TEMPLATE.md`, `workflows/verification.md`,
  `standards/testing.md` e testes em `tests/`.
- Dados, contratos ou migrações: define os templates canônicos uppercase para
  evidências de QA e relatórios de verificação sem remover templates legados.
- Riscos e precauções: assegurar que todos os campos exigidos por `workflows/verification.md`
  estejam no YAML de evidência; garantir que os testes validem o contrato.
- ADRs e padrões aplicáveis: `standards/quality-gates.md` e `standards/testing.md`.

## Passos

- [x] Criar o template canônico de evidência de QA com campos estruturados em YAML.
- [x] Criar o template de relatório de verificação do QA-Verifier.
- [x] Atualizar workflows/verification.md e standards/testing.md para operacionalizar o contrato.
- [x] Adicionar testes estruturais e atualizar a matriz de rastreabilidade.

## Validação

| Critério/risco | Teste, comando ou revisão | Evidência esperada |
|---|---|---|
| AC-001 | Teste do template de evidência | Campos YAML obrigatórios (criterion_id, status, execution_type, execution_date, verified_by, reproducible_evidence) presentes |
| AC-002 | Teste do template de verificação | Estrutura de divergências (missing, unmapped, failed, ambiguous) e decisão do Gate 3 presentes |
| AC-003 | Teste de workflow e standards | workflows/verification.md e standards/testing.md referenciam o novo contrato operacional |

## Condição de conclusão

- [x] Escopo implementado sem expansão.
- [x] Testes e validações aplicáveis passam.
- [x] Documentação e rastreabilidade foram atualizadas.
- [x] Limitações e desvios estão registrados.

## Resultado

- Mudanças realizadas: criação de `templates/QA_EVIDENCE_TEMPLATE.md` e
  `templates/VERIFICATION_REPORT_TEMPLATE.md`, atualização de
  `workflows/verification.md` e `standards/testing.md`, e criação de testes em
  `tests/test_structured_qa_evidence.py`.
- Evidências: em 2026-09-15, `python3 -m unittest discover -s tests -v` passou
  com 14 testes; `git diff --check` não reportou erros.
- Pendências ou bloqueios: decisão humana registrada em
  `reviews/REVIEW-005-structured-qa-evidence.md`; não há bloqueios conhecidos.
