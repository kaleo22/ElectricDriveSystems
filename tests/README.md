# Tests

> **Status:** Not started — placeholder only

This folder will contain system-level test plans, test procedures, and measurement logs.

## Structure (Planned)

```text
tests/
├── plans/          # Test plans and specifications
├── procedures/     # Step-by-step test procedures
├── logs/           # Raw measurement data and captures (gitignored by default)
└── reports/        # Processed test reports
```

## Test Categories (Planned)

| Category | Description |
|----------|-------------|
| Unit tests | Firmware module tests (see `firmware/tests/`) |
| Hardware tests | Electrical verification of assembled PCBs |
| Integration tests | End-to-end system behaviour |
| Performance tests | Speed response, accuracy, settling time |

## Notes

- Raw measurement data (CSV, binary scope captures) is listed in `.gitignore`.
  Processed reports and summaries should be committed.
