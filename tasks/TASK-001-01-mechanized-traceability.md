# TASK: Implement mechanized traceability baseline

## Metadados

| Campo | Valor |
|---|---|
| ID | TASK-001-01 |
| Status | Done |
| Responsável | Implementation Agent |
| SPEC | SPEC-001 |
| Critérios | AC-001, AC-002, AC-003, AC-004 |
| Dependências | Git; Python 3 standard library; POSIX shell for optional hook |

## Objetivo

Entregar os artefatos reutilizáveis que tornam rastreável a cadeia SPEC → TASK
→ commit → status de QA/review, preservando os templates atuais para
compatibilidade.

## Escopo

### Incluído

- Criar o guia de IDs e rastreabilidade.
- Adicionar templates em caixa alta para SPEC e TASK com `ID` e `Refs:`.
- Documentar trailers `Spec-Ref:` e `Task-Ref:` em `AGENTS.md`.
- Criar um gerador Python sem dependências externas que emite uma matriz
  Markdown em `docs/traceability-matrix.md`.
- Criar hook `commit-msg` opcional que valida trailers quando referências são
  declaradas no commit.
- Adicionar testes de unidade para o gerador e o hook, quando a infraestrutura
  leve necessária puder ser incluída sem dependências externas.

### Não incluído

- Reescrever SPECs, TASKs ou commits históricos para acrescentar referências.
- Instalar hooks automaticamente.
- Verificar critérios de aceite estruturados ou produzir evidência de QA em
  formato novo.

## Abordagem e impacto

- Arquivos ou componentes prováveis: `docs/ids-and-traceability.md`,
  `templates/SPEC_TEMPLATE.md`, `templates/TASK_TEMPLATE.md`, `AGENTS.md`,
  `scripts/generate_traceability.py`, `templates/hooks/commit-msg`, testes e
  `docs/traceability-matrix.md` gerada.
- Dados, contratos ou migrações: o script lê Markdown e histórico Git; artefatos
  sem referências permanecem válidos e são reportados como lacunas.
- Riscos e precauções: não inferir elos ausentes; falhas de Git e dados malformados
  devem ser diagnósticos acionáveis; o hook permanece opt-in.
- ADRs e padrões aplicáveis: `standards/commits.md`, `standards/testing.md` e
  `standards/quality-gates.md`.

## Passos

- [ ] Definir a convenção de IDs, `Refs:`, trailers e instalação do hook.
- [ ] Criar templates adicionais compatíveis e atualizar a orientação de agentes.
- [ ] Implementar e testar o gerador de matriz Markdown.
- [ ] Implementar e testar o hook opcional.
- [ ] Gerar a matriz para os artefatos atuais e registrar evidências.

## Validação

| Critério/risco | Teste, comando ou revisão | Evidência esperada |
|---|---|---|
| AC-001 | Revisão do guia e dos formatos documentados | Formatos e relações são inequívocos e genéricos |
| AC-002 | Inspeção dos dois novos templates | Ambos têm campos `ID` e `Refs:` |
| AC-003 | Executar o hook com mensagens válidas e inválidas | Mensagens inválidas são rejeitadas com diagnóstico |
| AC-004 | Executar o gerador contra um fixture e o repositório | Matriz Markdown reproduzível com lacunas explícitas |

## Condição de conclusão

- [x] Escopo implementado sem expansão.
- [x] Testes e validações aplicáveis passam.
- [x] Documentação e rastreabilidade foram atualizadas.
- [x] Limitações e desvios estão registrados.

## Resultado

- Mudanças realizadas: guia de IDs, templates compatíveis, trailers, hook
  opcional, gerador de matriz Markdown e testes de regressão.
- Evidências: em 2026-09-15, `python3 -m unittest discover -s tests -v` passou
  com 2 testes; `python3 scripts/generate_traceability.py` gerou
  `docs/traceability-matrix.md`; `git diff --check` não reportou erros.
- Pendências ou bloqueios: QA e review independentes permanecem pendentes. A
  decisão humana foi registrada em `reviews/REVIEW-001-mechanized-traceability.md`.
  A matriz registra corretamente a ausência de commit com
  `Task-Ref: TASK-001-01`, pois estas mudanças ainda não foram commitadas.
