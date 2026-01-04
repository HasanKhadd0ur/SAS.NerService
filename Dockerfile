# Base image with Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependencies first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python -m spacy download en_core_web_sm

# Copy source code
COPY . .

# Expose Flask port 5100
EXPOSE 5100

# Set entrypoint
CMD ["python", "src/app/main.py"]
