# Mobile-Price-Classification
Project for university.


## Download dataset

Our dataset is from kaggle. First, install kaggle package.
```
  $ pip install kaggle
```
Then download data to folder *dataset*
```
  $ kaggle datasets download -d iabhishekofficial/mobile-price-classification
  
  $ unzip mobile-price-classification.zip dataset/
```

## Insight data and Train model

Please found in folder notebook

## Application

A interface is provided to try our AI-Applications.

To run this application, we use [Docker](https://docs.docker.com/) and [Docker Compose](https://docs.docker.com/compose/). Install them via official website.

```
  $ docker compose up --build
```

Then open http://localhost:8000/docs to enjoy it.

