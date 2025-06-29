# Python Kata-Machine Dockerfile
# Provides a consistent development environment for algorithm practice

FROM python:3.11-slim

# Set working directory
WORKDIR /kata-machine

# Install system dependencies for development
RUN apt-get update && apt-get install -y \
    git \
    vim \
    nano \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set up environment
ENV PYTHONPATH=/kata-machine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user for security
RUN useradd -m -s /bin/bash kata-user

# Create a custom bashrc that shows welcome message with helpful commands, and add global commands
RUN echo 'python /kata-machine/scripts/welcome.py' >> /home/kata-user/.bashrc && \
    echo '' >> /home/kata-user/.bashrc && \
    echo '# Global kata-machine commands' >> /home/kata-user/.bashrc && \
    echo 'alias daily="python /kata-machine/kata.py daily"' >> /home/kata-user/.bashrc && \
    echo 'alias test="python /kata-machine/kata.py test"' >> /home/kata-user/.bashrc && \
    echo 'alias complete="python /kata-machine/kata.py complete"' >> /home/kata-user/.bashrc && \
    echo 'alias progress="python /kata-machine/kata.py progress"' >> /home/kata-user/.bashrc && \
    echo 'alias kata="python /kata-machine/kata.py"' >> /home/kata-user/.bashrc

# Switch to safe user
USER kata-user

# Default command starts an interactive bash session
CMD ["/bin/bash"]
