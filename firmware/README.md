# Firmware

**Status:** Not started — placeholder only

This folder will contain the bare-metal firmware for the brushed DC motor controller.

## Planned Structure

```text
firmware/
├── src/            # C/C++ source files
├── include/        # Header files
├── tests/          # Unit and integration tests for firmware
├── CMakeLists.txt  # (placeholder — build system TBD)
└── README.md
```

## Toolchain (TBD)

- Microcontroller family: _to be decided (see ADRs)_
- Build system: CMake / Makefile / vendor IDE
- Compiler: GCC ARM / LLVM
- Debugger: JTAG / SWD via OpenOCD or vendor tool

## Getting Started (TBD)

_Build and flash instructions will be added once the toolchain is selected._

## References

- [`docs/architecture/ARCHITECTURE.md`](../docs/architecture/ARCHITECTURE.md)
- [`docs/requirements/REQUIREMENTS.md`](../docs/requirements/REQUIREMENTS.md)
