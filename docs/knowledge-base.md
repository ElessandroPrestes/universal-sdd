# Base de conhecimento

A Knowledge Base preserva contexto reutilizável que ajuda decisões futuras sem
substituir fontes normativas.

## O que registrar

- glossário e linguagem do domínio;
- convenções recorrentes e exemplos aprovados;
- mapas de sistemas, integrações e responsáveis;
- armadilhas conhecidas e diagnóstico operacional;
- lições verificadas e referências duráveis.

Use `templates/knowledge-entry.md` e armazene a entrada em `knowledge/`.

## O que pertence a outro lugar

| Informação | Local correto |
|---|---|
| Estado atual do projeto | `PROJECT.md` |
| Requisito de uma mudança | `specs/` |
| Decisão arquitetural | `adr/` |
| Trabalho executável | `tasks/` |
| Regra obrigatória | `standards/` |
| Resultado de validação | `reviews/` ou evidência de teste |

## Qualidade de uma entrada

Toda entrada deve declarar origem, responsável, data de revisão, aplicabilidade
e links para fontes. Hipóteses devem ser identificadas. Conteúdo obsoleto deve
ser atualizado ou marcado como superseded; não deve desaparecer sem histórico.
