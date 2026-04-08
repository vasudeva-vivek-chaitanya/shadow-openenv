FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

ENV API_BASE_URL=https://api.openai.com/v1
ENV PORT=7860

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]