# Estado do Projeto Universal SDD

## Estado atual

| Campo | Valor |
|---|---|
| Produto | Universal SDD Framework (USF) |
| Versão e status | Rascunho de desenvolvimento pré-1.0; em desenvolvimento ativo |
| Runtime e dependências | Apenas documentação em Markdown; sem runtime ou dependências |
| Resultado principal | Requisitos aprovados tornam-se implementação rastreável e evidências de qualidade reprodutíveis |

## Hierarquia canônica

1. Uma SPEC aprovada é a linha de base de aceitação para uma mudança ativa.
2. Este índice e seus módulos de estado do projeto vinculados registram o estado atual canônico.
3. O conteúdo do repositório e as evidências de QA demonstram o comportamento entregue.
4. Resolva divergências como defeito, mudança de escopo ou dívida de documentação.

## Índice de contexto

Use `knowledge/INDEX.md` para selecionar um módulo. Não carregue todos os módulos; siga o pacote de fases em `docs/context-budget.md` e as referências (`Refs:`) da SPEC ativa.

| Módulo | Cobertura do estado atual |
|---|---|
| `knowledge/modules/framework-overview.md` | Domínio, usuários, resultado, versão, runtime, dependências, tecnologias excluídas |
| `knowledge/modules/governance-and-structure.md` | Responsabilidades do repositório e arquitetura modular de documentos |
| `knowledge/modules/delivery-and-quality.md` | UX, acessibilidade, QA, segurança, entrega e limitações conhecidas |

## Documentos autoritativos do framework

| Necessidade | Fonte |
|---|---|
| Definição do framework | `UNIVERSAL_SDD_FRAMEWORK.md` |
| Protocolo de sessão | `AGENTS.md` e arquivos de entrada de IA |
| Papéis e fluxo de trabalho | `agents/` e `workflows/` |
| Práticas normativas | `standards/` |
| Registros de mudança | `specs/`, `tasks/`, `reviews/`, `adr/` |
| Artefatos reutilizáveis | `templates/`, `knowledge/`, `profiles/`, `docs/` |

## Migração

Adotantes existentes podem manter um `PROJECT.md` monolítico enquanto criam módulos e um índice incrementalmente. Nenhum caminho de arquivo existente é removido ou renomeado.
