# Electric Drive Systems — Brushed DC Motor Controller

> **University Semester Project** | Team of 7 | Electric Drive Systems Course

---

## Project Description

This repository contains all artefacts for the semester project on controlling a **brushed DC motor**.
The system will eventually support:

- **Main switch** — motor on/off
- **Speed up** — incremental speed increase
- **Speed down** — incremental speed decrease

At the current stage the implementation has **not been started**.
This repository is being set up to establish a professional, reproducible engineering workflow.

---

## Repository Structure

```text
ElectricDriveSystems/
├── .github/                    # GitHub configuration (templates, workflows, CODEOWNERS)
│   ├── ISSUE_TEMPLATE/         # Bug, task, and feature issue templates
│   ├── workflows/              # GitHub Actions placeholder workflows
│   ├── CODEOWNERS              # Code ownership mapping
│   └── PULL_REQUEST_TEMPLATE.md
│
├── docs/                       # All project documentation
│   ├── architecture/           # System architecture placeholder
│   ├── decisions/              # Architecture Decision Records (ADRs)
│   ├── glossary/               # Project terminology and abbreviations
│   ├── meetings/               # Meeting notes
│   ├── reports/                # Reports and presentations
│   └── requirements/           # System and hardware requirements
│
├── firmware/                   # Bare-metal firmware (not started)
│   ├── src/                    # Source files (placeholder)
│   ├── include/                # Header files (placeholder)
│   └── tests/                  # Firmware unit tests (placeholder)
│
├── hardware/                   # Hardware design artefacts (not started)
│   ├── control-board/          # Microcontroller / control board design
│   ├── power-electronics/      # Motor driver / power stage design
│   └── pcb/                    # PCB layout and fabrication files
│
├── simulation/                 # Simulation models and results (not started)
├── tests/                      # System-level tests and measurement logs
├── scripts/                    # Utility scripts and tools
├── project-management/         # Labels, milestones, and process docs
│
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── SETUP_GITHUB.md             # How to configure repository protections
└── README.md
```

---

## Team Roles

| Role | Responsibility |
|------|---------------|
| Team Leader | Project coordination, milestone tracking, interface alignment |
| Hardware Specialist | Support for hardware-related work packages (Driver Electronics, Power Electronics, assembly) |
| Software Specialist | Support for Control Board software development |
| Documentation Specialist | Coordination of report structure, consistency, and glossary |
| Presentation Specialist | Coordination of milestone presentations and final presentation |

## Work Packages

| Work Package | Main Responsibility |
|-------------|---------------------|
| Control Board | Microcontroller, buttons, software |
| Driver Electronics | Driver stage for the power electronics |
| Power Electronics | Power stage for the motor |
| DC Motor | Motor selection / specification |
| Power Supply | Supply concept / source / battery option |

*Individual assignments will be documented in the project management files.*

---

## Contribution Workflow

1. **Pick an issue** from the issue tracker or create one.
2. **Create a branch** from `dev` following the naming convention (see below).
3. **Make your changes** — commit early and often with clear messages.
4. **Open a Pull Request** to `dev` using the provided PR template.
5. **Request a review** from at least one team member.
6. **Address feedback** and ensure all checks pass.
7. A team lead merges the PR once it is approved.

> Direct pushes to `main` and `dev` are **not allowed**. All changes must go through a Pull Request.

---

## Branching Model

| Branch | Purpose |
|--------|---------|
| `main` | Protected stable branch — always represents a reviewed, integrated state |
| `dev`  | Integration branch — all feature branches merge here first |
| `feature/<short-description>` | New work package or feature |
| `fix/<short-description>` | Bug fix or correction |
| `docs/<short-description>` | Documentation-only changes |

**Examples:**

```text
feature/motor-speed-control
fix/pwm-frequency-calculation
docs/update-architecture-diagram
```

---

## Coding & Documentation Expectations

- **Commit messages** follow [Conventional Commits](https://www.conventionalcommits.org/): `type(scope): short description`
  - Types: `feat`, `fix`, `docs`, `chore`, `test`, `refactor`, `style`
- **Pull Requests** must use the provided template and reference an issue.
- **Documentation** lives in `docs/` and must be kept up to date alongside code changes.
- **Architecture Decision Records (ADRs)** are created for every significant technical decision (see `docs/decisions/`).
- **Changelog** entries are added for every merged feature or fix.
- All text files must end with a newline; no trailing whitespace.

---

## Implementation Status

> ⚠️ **Implementation not started.**
>
> This repository is scaffolded for project management and workflow purposes only.
> No firmware, PCB designs, or control algorithms have been written yet.
> Placeholder files mark where future content will live.

---

## Getting Started

1. Clone the repository:

   ```sh
   git clone https://github.com/kaleo22/ElectricDriveSystems.git
   cd ElectricDriveSystems
   ```

2. Install pre-commit hooks (optional but recommended):

   ```sh
   ./scripts/setup-pre-commit.sh
   ```

3. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before making your first change.
4. Read [`SETUP_GITHUB.md`](SETUP_GITHUB.md) if you are a maintainer configuring repository protections.

---

## License

See [`LICENSE`](LICENSE) for details.
