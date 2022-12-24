# Base image
FROM python:3.10-slim

ENV LANG="C.UTF-8"

# Set working directory
WORKDIR /

# Copy files
COPY ./app /app
COPY ./requirements.txt /

RUN python3 -m pip install -U pip \
      && pip install --no-cache-dir -r requirements.txt


# Run the application
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
