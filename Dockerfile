# Using lightweight python image
FROM python:3.11-slim

# Install uv
RUN pip install uv

# Set up a non-root user
RUN useradd --create-home appuser
WORKDIR /home/appuser/app

# Copy application and install dependencies
COPY . .
RUN uv pip install --system . fastapi uvicorn

# Switch to non-root user
USER appuser

# Expose port and start the application
EXPOSE 8000
CMD ["uvicorn", "kasa_fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
#harbor.freshbrewed.science/freshbrewedprivate/kasarest:2.0.0