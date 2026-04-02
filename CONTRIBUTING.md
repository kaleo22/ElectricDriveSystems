# Contributing to Electric Drive Systems

Thank you for contributing to this project. Please read this guide before opening issues or pull requests.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
3. [Branching Model](#branching-model)
4. [Commit Messages](#commit-messages)
5. [Pull Request Process](#pull-request-process)
6. [Documentation Standards](#documentation-standards)
7. [Pre-commit Hooks](#pre-commit-hooks)

---

## Code of Conduct

Be respectful, constructive, and professional in all interactions.
This is a university project — we are here to learn and build something together.

---

## How to Contribute

1. Check the [issue tracker](../../issues) for open tasks or report a new one.
2. Assign the issue to yourself or discuss in the issue thread before starting work.
3. Create a branch from `dev` — **never** from `main`.
4. Make your changes in small, logical commits.
5. Open a Pull Request against `dev` using the template.
6. Request a review from at least one team member.
7. Address all review comments.
8. A maintainer will merge once the PR is approved and all checks pass.

---

## Branching Model

| Branch prefix | When to use |
|---------------|-------------|
| `feature/<description>` | New feature or work package |
| `fix/<description>` | Bug fix or correction |
| `docs/<description>` | Documentation-only changes |

Branch names must be lowercase and use hyphens as separators.

```sh
# Good
git checkout -b feature/pwm-generation
git checkout -b fix/overcurrent-threshold
git checkout -b docs/adr-motor-driver-selection

# Bad
git checkout -b Feature_PWM
git checkout -b mychanges
```

---

## Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```markdown
<type>(<scope>): <short description>

[optional body]

[optional footer: closes #<issue-number>]
```

**Types:**

| Type | Use for |
|------|---------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation changes only |
| `chore` | Maintenance tasks (deps, CI config, etc.) |
| `test` | Adding or updating tests |
| `refactor` | Code restructuring without changing behaviour |
| `style` | Formatting, whitespace (no logic change) |

**Examples:**

```markdown
feat(firmware): add PWM duty-cycle control stub
fix(hardware): correct gate driver footprint reference
docs(adr): add ADR-0002 for motor driver selection
chore(ci): add markdown lint workflow
```

---

## Pull Request Process

1. Fill in the PR template completely.
2. Reference the related issue with `Closes #<number>`.
3. Keep PRs focused — one logical change per PR.
4. Ensure no trailing whitespace and all files end with a newline.
5. Update relevant documentation alongside code changes.
6. Add a `CHANGELOG.md` entry under `[Unreleased]`.

---

## Documentation Standards

- All documentation is written in **Markdown**.
- Files live under `docs/` unless they are repository meta-files (CONTRIBUTING, README, etc.).
- Significant technical decisions must be recorded as an **ADR** in `docs/decisions/`.
- Keep the **glossary** (`docs/glossary/GLOSSARY.md`) up to date when introducing new terms.

---

## Pre-commit Hooks

This repository uses [pre-commit](https://pre-commit.com/) for lightweight automated checks.

```sh
./scripts/setup-pre-commit.sh
```

Hooks include: trailing whitespace, end-of-file newline, YAML/JSON syntax, and Markdown lint.
Run manually on all files with:

```sh
.venv/bin/pre-commit run --all-files
```

Using the project-local virtual environment avoids distro-specific `nodeenv` issues and is only needed for pre-commit hooks.
