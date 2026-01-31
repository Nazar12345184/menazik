FROM python:3.12-slim-bullseye

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 
    

WORKDIR /MENAZIK

# системні залежності для pip-пакетів, які інколи потребують компіляції
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    python3-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# копіюємо весь проєкт у контейнер
COPY . .

EXPOSE 8000

# Gunicorn стартує Django
ENTRYPOINT ["gunicorn", "menazik.wsgi:application", "-b", "0.0.0.0:8000"]
