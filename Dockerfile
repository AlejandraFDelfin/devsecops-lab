# Imagen base moderna y actualizada
FROM python:3.12-slim-bookworm

WORKDIR /app

# Crear usuario no privilegiado
RUN useradd -m appuser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app/

USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s \
CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/buscar')" || exit 1

CMD ["python", "app.py"]