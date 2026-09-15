# TASK: Implement SPEC amendment protocol

## Metadados

| Campo | Valor |
|---|---|
| ID | TASK-003-01 |
| Status | Done |
| Responsável | Implementation Agent |
| SPEC | SPEC-003 |
| Critérios | AC-001, AC-002, AC-003 |
| Dependências | Markdown repository structure only |

## Objetivo

Disponibilizar um protocolo reutilizável e bloqueante para distinguir
clarificações leves de mudanças de escopo, preservando a cadeia de versões da
SPEC.

## Escopo

### Incluído

- Detalhar ciclo, predecessora, referência e aprovação de `SPEC-NNN-vN`.
- Criar template de change request com os dois fluxos mutuamente exclusivos.
- Incluir classificação objetiva e gate bloqueante nos quality gates.
- Adicionar testes estruturais dos três artefatos.

### Não incluído

- Alterar etapas gerais do workflow ou automatizar aprovação.
- Criar IDs adicionais, integração com tickets ou notificação assíncrona.

## Abordagem e impacto

- Arquivos ou componentes prováveis: `docs/ids-and-traceability.md`,
  `templates/CHANGE_REQUEST_TEMPLATE.md`, `standards/quality-gates.md` e
  testes em `tests/`.
- Dados, contratos ou migrações: SPECs existentes permanecem válidas; a versão
  só é criada para alteração de escopo aprovada.
- Riscos e precauções: incerteza sempre bloqueia como mudança de escopo; o
  template exige evidência durável da aprovação assíncrona.
- ADRs e padrões aplicáveis: `standards/quality-gates.md`,
  `standards/commits.md` e `docs/ids-and-traceability.md`.

## Passos

- [ ] Documentar o ciclo completo de emenda e referências de versão.
- [ ] Criar o template de change request com os dois fluxos.
- [ ] Adicionar gate de classificação e bloqueio.
- [ ] Executar testes estruturais e atualizar a matriz.

## Validação

| Critério/risco | Teste, comando ou revisão | Evidência esperada |
|---|---|---|
| AC-001 | Teste do guia de IDs | Versão, predecessora e aprovação são exigidas |
| AC-002 | Teste do template | Ambos os fluxos e seus registros obrigatórios existem |
| AC-003 | Teste dos quality gates | Dúvida ou mudança observável bloqueia a implementação |

## Condição de conclusão

- [x] Escopo implementado sem expansão.
- [x] Testes e validações aplicáveis passam.
- [x] Documentação e rastreabilidade foram atualizadas.
- [x] Limitações e desvios estão registrados.

## Resultado

- Mudanças realizadas: ciclo de versão documentado, template bifurcado, gate
  bloqueante e testes estruturais.
- Evidências: em 2026-09-15, `python3 -m unittest discover -s tests -v` passou
  com 8 testes; `python3 scripts/generate_traceability.py` gerou a matriz e
  `git diff --check` não reportou erros.
- Pendências ou bloqueios: decisão humana registrada em
  `reviews/REVIEW-003-spec-amendment-protocol.md`; não há bloqueios conhecidos.
