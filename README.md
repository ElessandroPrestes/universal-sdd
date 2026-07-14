# Universal SDD

> 🚧 **Status:** Em desenvolvimento ativo. O framework evolui continuamente até a versão **1.0**.

> **Framework universal para aplicar Spec-Driven Development (SDD) em qualquer projeto de software, utilizando pessoas e agentes de IA de forma organizada, previsível e auditável.**

---

## O que é o Universal SDD?

O **Universal SDD (USF)** é um framework open source para desenvolvimento orientado por especificações (**Spec-Driven Development**).

Seu objetivo é transformar a especificação em **fonte única de verdade**, criando um processo reutilizável para qualquer linguagem, arquitetura ou ferramenta de IA.

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
Discovery
   ↓
Arquitetura
   ↓
SPEC
   ↓
Aprovação Humana
   ↓
TASK
   ↓
Implementação
   ↓
Testes
   ↓
Review
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
| `PROJECT.md` | Fonte única da verdade do projeto |
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

---

# Princípios

- O código é a fonte da verdade.
- Toda implementação começa por uma SPEC.
- Toda SPEC precisa de aprovação humana.
- A IA implementa apenas o escopo aprovado.
- Toda implementação deve ser revisada.
- Mudanças arquiteturais geram ADRs.
- A documentação evolui junto com o código.

---

# Primeiros Passos

1. Copie a estrutura do Universal SDD para seu projeto.
2. Solicite à IA que analise todo o repositório.
3. Gere automaticamente o `PROJECT.md`.
4. Identifique arquitetura, stack e padrões.
5. Preencha a Base de Conhecimento.
6. Aguarde a primeira SPEC antes de implementar qualquer funcionalidade.

---

# Roadmap

## v1.0
- Framework base
- Agents
- Workflows
- Templates
- Knowledge Base

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
