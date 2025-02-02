FROM python:3.9-slim

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install plotly

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "fast_gaebabja_api.main:app", "--host", "0.0.0.0", "--port", "3100"]
