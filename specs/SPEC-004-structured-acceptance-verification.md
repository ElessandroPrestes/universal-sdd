# SPEC: Critérios de aceitação estruturados e portão de verificação de QA (Structured acceptance criteria and QA verification gate)

## Metadados

| Campo | Valor |
|---|---|
| ID | SPEC-004 |
| Status | Implementada |
| Responsável | Agente de Especificação |
| Revisores | Engenharia / QA |
| Criado | 2026-09-15 |
| Atualizado | 2026-09-15 |
| Liberação Alvo | Não programado |
| Refs: | Discovery: N/A — alteração interna do framework; Design: N/A — nenhuma interface voltada para o usuário; ADRs: N/A — apenas documentação de fluxo de trabalho de qualidade |

## Problema e resultado

Os critérios de aceitação atualmente permitem texto livre (prosa) e não definem um contrato consumível para comparar o comportamento aprovado com as evidências de QA. A regra contra divergência silenciosa, portanto, depende de interpretação manual.

O resultado é um formato de critério de aceitação estruturado no template canônico de SPEC e uma etapa bloqueadora de fluxo de trabalho (workflow) QA-Verifier (Verificador de QA) que reporta cada critério ausente, não mapeado, falho ou ambíguo antes da revisão de código (code review).

## Escopo

### No escopo

- Atualizar `templates/SPEC_TEMPLATE.md` com um formato de critério de aceitação estruturado e estável.
- Adicionar `workflows/verification.md` definindo entradas do QA-Verifier, comparação, saída, relatórios de divergência e sua posição antes do Code Review.
- Adicionar o QA-Verifier como uma condição de bloqueio em `standards/quality-gates.md`.

### Fora do escopo

- Definir o arquivo de evidências estruturadas de QA em si; isso pertence à Melhoria 6.
- Implementar um analisador (parser) automatizado, integração de CI, ou alterar SPECs existentes.
- Alterar IDs de tarefas, trailers de commit, autoridades de aprovação ou estratégia de teste.

## Comportamento funcional

- Cada novo critério no template canônico de SPEC tem um ID estável `AC-NNN`, pré-condições, ação, resultado observável esperado e tipo de evidência requerida em YAML estruturado.
- O QA-Verifier compara cada critério estruturado com a evidência estruturada de QA; ele emite uma lista reprodutível de itens não mapeados, ausentes, falhos ou ambíguos em vez de inferir o cumprimento.
- Até que o contrato de evidência de QA da Melhoria 6 exista, o portão (gate) QA-Verifier está documentado, mas não pode passar para mudanças que exigem evidências de QA.
- O Code Review não pode começar enquanto houver descobertas aplicáveis do QA-Verifier em aberto.

## Critérios de aceitação

### AC-001: O template canônico de SPEC tem critérios legíveis por máquina

```gherkin
Dado que um autor usa o template canônico de SPEC
Quando ele define um critério de aceitação
Então o critério tem os campos estruturados ID, pré-condição, ação, resultado esperado e tipo de evidência sem depender de texto livre (prosa)
```

Evidência requerida: inspeção de template.

### AC-002: O QA-Verifier relata divergências antes da revisão

```gherkin
Dado uma SPEC aprovada e sua evidência de QA
Quando o QA-Verifier compara IDs de critérios e resultados
Então ele lista cada critério ausente, não mapeado, falho ou ambíguo antes que o Code Review possa começar
```

Evidência requerida: revisão de fluxo de trabalho (workflow) e de portão (gate).

### AC-003: A verificação é um portão de qualidade bloqueador

```gherkin
Dado que o QA-Verifier tem descobertas aplicáveis não resolvidas
Quando a mudança solicita Code Review
Então o padrão de portões de qualidade bloqueia a transição até que as descobertas sejam resolvidas ou tenham uma exceção autorizada
```

Evidência requerida: revisão de padrões.

## Abordagem técnica

Use um bloco de código YAML por critério de aceitação no template canônico em letras maiúsculas. O fluxo de trabalho (workflow) especifica um contrato de comparação agnóstico de tecnologia e nomeia o futuro esquema de evidência de QA como uma dependência. Isso preserva o template legado em minúsculas e evita adicionar um analisador (parser) antes que seus esquemas de entrada e de evidência estejam ambos definidos.

## Riscos e dependências

| Risco ou dependência | Impacto | Probabilidade | Mitigação | Responsável |
|---|---|---|---|---|
| O esquema de evidência de QA ainda não está disponível | O portão não pode produzir um resultado de aprovação | Alta | Marcar a Melhoria 6 como um pré-requisito explícito para uso operacional | Agente de QA |
| SPECs existentes usam critérios em prosa | Ônus de migração | Alta | Preservar templates legados e exigir o novo formato apenas para novas SPECs canônicas | Agente de Documentação |
| Os critérios são estruturalmente completos, mas vagos | Falsa confiança | Média | Exigir resultados esperados observáveis e sinalizar a ambiguidade como uma descoberta | QA-Verifier |

## Questões abertas

| Questão | Responsável | Data limite | Resolução |
|---|---|---|---|
| O QA-Verifier deve ser automatizado após a Melhoria 6? | Revisor de Engenharia | Após Melhoria 6 | Adiado; esta alteração define apenas o contrato portátil e o portão. |

## Aprovação

| Papel | Nome | Decisão | Data | Notas |
|---|---|---|---|---|
| Engenharia | | Pendente | | |
| QA | | Pendente | | |
| Patrocinador Humano | Usuário | Aprovado | 2026-09-15 | Aprovação registrada na conversa do CLI. |
