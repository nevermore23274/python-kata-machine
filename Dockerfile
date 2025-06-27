FROM python:3.11-slim

# Set working directory
WORKDIR /kata-machine

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    vim \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies for development
RUN pip install --no-cache-dir \
    pytest \
    pytest-watch \
    black \
    flake8 \
    mypy \
    pyyaml \
    rich

# Create the kata-machine directory structure
RUN mkdir -p /kata-machine/scripts \
    && mkdir -p /kata-machine/templates \
    && mkdir -p /kata-machine/tests \
    && mkdir -p /kata-machine/src

# Set environment variables
ENV PYTHONPATH=/kata-machine
ENV PYTEST_CURRENT_TEST=""

# Create a non-root user
RUN useradd -m -s /bin/bash kata-user
RUN chown -R kata-user:kata-user /kata-machine
USER kata-user

# Default command
CMD ["/bin/bash"]

