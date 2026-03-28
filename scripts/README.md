# Scripts & Tools

> **Status:** Placeholder only

This folder will contain utility scripts and tooling used by the team.

## Planned Contents

| Script / File | Purpose |
|---------------|---------|
| `setup-pre-commit.sh` | Create project `.venv`, install pinned pre-commit tooling, and install hooks |
| _(TBD)_ | Flash firmware to target |
| _(TBD)_ | Export KiCad Gerbers |
| _(TBD)_ | Parse and plot measurement data |
| _(TBD)_ | Generate BOM from schematic |

## Guidelines

- The programming language for the controller software is freely selectable (C, C++).
- PCB design software is freely selectable.
- Any helper scripts for documentation, analysis, or tooling should be documented clearly.
- Do not hardcode absolute paths.
- Keep the repository structure cleanly separated into hardware, firmware, documentation, and project files.
