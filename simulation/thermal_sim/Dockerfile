FROM quay.io/jupyter/minimal-notebook:latest

# Switch to root for system packages
USER root

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    curl \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set workspace
WORKDIR /workspace

# Python environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt

# Give jovyan access to workspace
RUN mkdir -p /workspace \
    && chown -R jovyan:users /workspace

# Switch back to default non-root Jupyter user
USER jovyan

# Default shell
CMD ["bash"]