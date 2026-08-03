# Universal SDD

> 🚧 **Status:** Em desenvolvimento ativo. Versão documentada: **1.0.0**.

> **Framework universal para aplicar Spec-Driven Development (SDD) em qualquer projeto de software, utilizando pessoas e agentes de IA de forma organizada, previsível e auditável.**

---

## O que é o Universal SDD?

O **Universal SDD (USF)** é um framework open source para desenvolvimento orientado por especificações (**Spec-Driven Development**).

Seu objetivo é transformar requisitos aprovados em implementação rastreável, criando um processo reutilizável para qualquer linguagem, arquitetura ou ferramenta de IA.

O framework utiliza três fontes complementares:

- a **SPEC aprovada** define o comportamento desejado de uma mudança;
- o **PROJECT.md** registra o estado canônico do projeto;
- o **código e as evidências de QA** demonstram o comportamento implementado.

Qualquer divergência entre essas fontes deve ser tratada como defeito, mudança de escopo ou dívida documental — nunca resolvida silenciosamente.

O framework é independente de:

- Linguagem de programação
- Framework
- Arquitetura
- Plataforma
- Provedor de IA

---

# Por que este projeto existe?

Ferramentas de IA aceleram o desenvolvimento, mas sem um processo consistente é comum ocorrer:

- expansão de escopo;
- requisitos inventados;
- alterações fora do objetivo;
- documentação inconsistente;
- perda de contexto entre sessões;
- dificuldade para revisar decisões.

O Universal SDD organiza todo o ciclo de desenvolvimento através de especificações, tarefas, revisões e documentação versionada.

---

# Como funciona?

```text
Ideia
   ↓
Discovery de Produto e UX
   ↓
Arquitetura
   ↓
UX/UI Design
   ↓
Aprovação do Design
   ↓
SPEC técnica e funcional
   ↓
Aprovação Humana
   ↓
TASK
   ↓
Implementação
   ↓
QA automatizado e manual
   ↓
Design Review e Code Review
   ↓
Refatoração (se necessário)
   ↓
Documentação
   ↓
Release
```

---

# Compatibilidade

## Linguagens

PHP • Java • C# • Go • Python • JavaScript • TypeScript • Kotlin • Swift • Rust e outras.

## Frameworks

Laravel • Symfony • Spring • .NET • Express • NestJS • Next.js • React • Angular • Vue • Flutter • React Native e outros.

## Ferramentas de IA

ChatGPT • Codex • Claude Code • Gemini • GitHub Copilot • Cursor • Windsurf • Aider.

---

# Estrutura do Framework

```text
Universal-SDD/

README.md
PROJECT.md
AGENTS.md
CLAUDE.md
GEMINI.md
COPILOT.md

agents/
workflows/
profiles/
knowledge/
standards/
templates/
specs/
tasks/
reviews/
adr/
docs/
```

---

# Documentação

A documentação é organizada em módulos para facilitar adoção e evolução.

| Documento | Objetivo |
|-----------|----------|
| `README.md` | Visão geral do framework |
| `PROJECT.md` | Estado canônico atual do projeto |
| `docs/getting-started.md` | Primeiros passos |
| `docs/architecture.md` | Arquitetura do framework |
| `docs/agents.md` | Papéis e responsabilidades dos agentes |
| `docs/workflows.md` | Fluxos oficiais |
| `docs/knowledge-base.md` | Base de conhecimento |
| `docs/bootstrapping.md` | Inicialização de novos projetos |
| `docs/governance.md` | Regras e governança |
| `docs/best-practices.md` | Boas práticas |
| `docs/faq.md` | Perguntas frequentes |
| `CONTRIBUTING.md` | Como contribuir |
| `CHANGELOG.md` | Histórico de versões |
| `ROADMAP.md` | Evolução planejada |
| `CODE_OF_CONDUCT.md` | Código de conduta |
| `standards/ux-ui.md` | Processo e critérios de UX/UI |
| `standards/design-system.md` | Tokens, componentes e governança visual |
| `standards/accessibility.md` | Requisitos e validações de acessibilidade |
| `standards/testing.md` | Estratégia de testes e evidências |
| `standards/quality-gates.md` | Critérios de entrada, saída e release |
| `workflows/feature.md` | Fluxo completo de uma funcionalidade |
| `agents/` | Responsabilidades e limites dos papéis de UX/UI e QA |
| `templates/` | Artefatos executáveis de especificação, design, testes e revisão |

---

# Princípios

- A SPEC aprovada define o comportamento desejado da mudança.
- O `PROJECT.md` registra o estado canônico do projeto.
- Código e evidências de QA comprovam o comportamento entregue.
- Toda implementação começa por uma SPEC.
- Interfaces começam por discovery e design aprovados antes da implementação.
- Toda SPEC precisa de aprovação humana.
- A IA implementa apenas o escopo aprovado.
- Toda implementação deve passar pelos quality gates aplicáveis.
- Mudanças de interface exigem revisão de design e acessibilidade.
- Mudanças arquiteturais geram ADRs.
- A documentação evolui junto com o código.

---

# Primeiros Passos

1. Copie a estrutura do Universal SDD para seu projeto.
2. Solicite à IA que analise todo o repositório.
3. Gere automaticamente o `PROJECT.md`.
4. Identifique arquitetura, stack e padrões.
5. Preencha a Base de Conhecimento.
6. Defina os padrões de UX/UI, acessibilidade, testes e quality gates aplicáveis.
7. Aguarde discovery, design e SPEC aprovados antes de implementar uma interface.

---

# Roadmap

## v1.0
- Framework base
- Agents
- Workflows
- Templates
- Knowledge Base
- Processo de UX/UI e Design Review
- Estratégia de QA, acessibilidade e quality gates

## v2.0
- Bootstrap automático
- Perfis por tecnologia
- CLI

## v3.0
- Extensão VS Code
- Plugin JetBrains
- Integração com múltiplas IAs
- Geração automática de documentação

---

# Contribuindo

Contribuições são bem-vindas.

1. Abra uma Issue.
2. Discuta a proposta.
3. Envie um Pull Request.

---

# Licença

MIT License.

---

# Autor

**Elessandro Prestes Macedo**

Software Engineer

Criador do Universal SDD.
