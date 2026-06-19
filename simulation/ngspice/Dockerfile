FROM debian:bookworm-slim

LABEL maintainer="kaleo22"
LABEL description="Hybrid Simulation Environment: AVR-GCC & Ngspice"

# Install core components
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    # Toolchain for Arduino Nano (ATmega328P)
    gcc-avr \
    avr-libc \
    binutils-avr \
    avrdude \
    # # Simulation & analysis
    ngspice \
    python3 \
    python3-pip \
    python3-matplotlib \
    python3-scipy \
    libelf-dev \
    libsimavr-dev \
    simavr \
    # Cleanup
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages PySpice

# Working directory
WORKDIR /simulation
