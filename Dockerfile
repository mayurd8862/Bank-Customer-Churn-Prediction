FROM python:3.11.4

# Set working directory
WORKDIR /app

# Copy application code
COPY . /app

# Install awscli using apt
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        awscli \
        ffmpeg \
        libsm6 \
        libxext6 \
        unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python3", "app.py"]
