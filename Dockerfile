# Stage 1: install dependencies
FROM python:3.12-slim AS build
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: small final image, runs as a non-root user
FROM python:3.12-slim
WORKDIR /app
COPY --from=build /install /usr/local
COPY app/main.py .
RUN useradd -r appuser
USER appuser
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]