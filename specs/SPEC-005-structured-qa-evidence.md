# SPEC: Esquema e contrato de evidência de QA estruturado (Structured QA evidence schema and contract)

## Metadados

| Campo | Valor |
|---|---|
| ID | SPEC-005 |
| Status | Implementada |
| Responsável | Agente de Especificação |
| Revisores | QA / Engenharia |
| Criado | 2026-09-15 |
| Atualizado | 2026-09-15 |
| Liberação Alvo | Não programado |
| Refs: | Discovery: N/A — alteração interna do framework; Design: N/A — nenhuma interface voltada para o usuário; ADRs: N/A — apenas documentação de fluxo de trabalho de qualidade |

## Problema e resultado

Os critérios de aceitação no SPEC-004 tornaram-se legíveis por máquina, e o fluxo de trabalho do QA-Verifier foi definido para comparar os critérios com as evidências. No entanto, sem um contrato e um template de evidências estruturadas de QA, a verificação não pôde ser realizada de forma determinística, deixando o QA-Verifier em um estado bloqueado e não operacional.

O resultado é um esquema e um template de evidência estruturada de QA (`templates/QA_EVIDENCE_TEMPLATE.md`), um template de relatório de verificação estruturado (`templates/VERIFICATION_REPORT_TEMPLATE.md`) e padrões de teste e fluxo de trabalho atualizados que tornam o QA-Verifier operacional para mudanças ativas.

## Escopo

### No escopo

- Criar `templates/QA_EVIDENCE_TEMPLATE.md` com blocos YAML estruturados por resultado de critério de aceitação.
- Criar `templates/VERIFICATION_REPORT_TEMPLATE.md` com saídas de comparação reproduzíveis do Portão 3.
- Atualizar `workflows/verification.md` para referenciar o template de evidência estruturada e declarar a etapa de verificação operacional.
- Atualizar `standards/testing.md` para exigir evidências estruturadas de QA para a validação dos critérios de aceitação.
- Adicionar testes estruturais em `tests/test_structured_qa_evidence.py`.

### Fora do escopo

- Implementar scripts de analisador (parser) automatizado ou executáveis ​​de CI runner.
- Retrofit (adaptar) SPECs concluídas passadas com arquivos de evidências estruturados.
- Alterar IDs de tarefas, trailers de commit ou autoridades de aprovação.

## Comportamento funcional

- Cada mudança que requer validação de QA registra evidências em um documento estruturado com base em `templates/QA_EVIDENCE_TEMPLATE.md`.
- Cada critério aplicável `AC-NNN` da SPEC deve ter uma entrada contendo: `criterion_id`, `status` (`passed` [aprovado], `failed` [falhou] ou `exception` [exceção]), `execution_type` (tipo de execução), `execution_date` (data de execução), `verified_by` (verificado por) e `reproducible_evidence` (evidência reprodutível).
- A etapa do fluxo de trabalho do QA-Verifier em `workflows/verification.md` compara os critérios estruturados da SPEC com a evidência estruturada de QA.
- O QA-Verifier produz um relatório usando `templates/VERIFICATION_REPORT_TEMPLATE.md` classificando quaisquer discrepâncias como `missing` (ausente), `unmapped` (não mapeado), `failed` (falhou) ou `ambiguous` (ambíguo).
- A revisão de código (Code Review) não pode prosseguir enquanto houver descobertas aplicáveis do QA-Verifier em aberto.

## Critérios de aceitação

### AC-001: O template canônico de evidências de QA possui resultados de critérios consumíveis por máquina

```yaml
id: AC-001
title: O template canônico de evidências de QA contém os campos de contrato YAML exigidos
preconditions:
  - Um autor cria um artefato de evidência de QA usando templates/QA_EVIDENCE_TEMPLATE.md
action: Inspecionar as entradas de evidência de critérios
expected_result: Cada entrada de critério contém os campos criterion_id, status, execution_type, execution_date, verified_by, e reproducible_evidence
evidence_type: automated
```

### AC-002: O template de relatório de verificação estrutura o relatório de divergência do QA-Verifier

```yaml
id: AC-002
title: O template de relatório de verificação estrutura a comparação e as descobertas do Portão 3
preconditions:
  - QA-Verifier produz um relatório de verificação usando templates/VERIFICATION_REPORT_TEMPLATE.md
action: Inspecionar a estrutura do relatório
expected_result: O template define referências de SPEC/TASK, status critério por critério, classificação de divergência (missing, unmapped, failed, ambiguous), e a decisão de pass/block (aprovado/bloqueado) do Portão 3
evidence_type: automated
```

### AC-003: O fluxo de trabalho de verificação e o padrão de teste operacionalizam as evidências estruturadas

```yaml
id: AC-003
title: O fluxo de trabalho de verificação e o padrão de teste referenciam evidências estruturadas de QA
preconditions:
  - Inspecionar workflows/verification.md e standards/testing.md
action: Verificar referências ao contrato de evidências de QA
expected_result: workflows/verification.md faz referência a templates/QA_EVIDENCE_TEMPLATE.md como operacional, e standards/testing.md exige evidências estruturadas para os critérios de aceitação
evidence_type: automated
```

## Abordagem técnica

Fornecer templates canônicos em maiúsculas (uppercase) em `templates/` usando blocos YAML claros para extração por máquina e legibilidade humana. Atualizar as referências em `workflows/verification.md` e `standards/testing.md` para vincular os contratos. Testes unitários automatizados em `tests/test_structured_qa_evidence.py` confirmam a presença dos campos obrigatórios e referências cruzadas.

## Riscos e dependências

| Risco ou dependência | Impacto | Probabilidade | Mitigação | Responsável |
|---|---|---|---|---|
| Registros de evidência incompletos | Falsas verificações aprovadas | Média | Exigir command, log/artifact e verified_by em evidência reprodutível | Agente de QA |
| Critérios não mapeados ou extras na evidência | Teste obsoleto ou não documentado | Baixa | O QA-Verifier sinaliza os critérios não mapeados como descobertas de bloqueio do Portão 3 | QA-Verifier |
| Expectativas de ferramentas sem código de parser | Confusão sobre CI automatizado vs. contrato portátil | Baixa | Documentar claramente o formato markdown/YAML como portátil e verificável por humanos/IA | Agente de Especificação |

## Questões abertas

| Questão | Responsável | Data limite | Resolução |
|---|---|---|---|
| Scripts de parser automatizados serão adicionados em uma especificação futura? | Engenharia | Lançamento futuro | Adiado; esta spec define os contratos autoritativos do documento. |

## Aprovação

| Papel | Nome | Decisão | Data | Notas |
|---|---|---|---|---|
| Engenharia | | Pendente | | |
| QA | | Pendente | | |
| Patrocinador Humano | Usuário | Aprovado | 2026-09-15 | Aprovação registrada na conversa do CLI. |
