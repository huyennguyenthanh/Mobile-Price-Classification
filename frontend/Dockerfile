# Base image
FROM python:3.10-slim

ENV LANG="C.UTF-8"


WORKDIR /

# Copy files
COPY ./app /app
COPY ./requirements.txt /

# Install
RUN python3 -m pip install -U pip \
      && pip install --no-cache-dir -r requirements.txt

# Run the application
EXPOSE 8501
CMD ["streamlit", "run", "app/main.py","--server.port=8501", "--server.address=0.0.0.0"]
