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

* mobile_price.ipynb: feature extraction
* insight_and_training.ipynb: preprocess data and training model.

To run notebook, please install environment first.
```
conda create -n <environment-name> --file requirements.txt
```


## Detail documentation

Found File PDF: Báo cáo phân tích và định giá điện thoại.pdf

## Application

A interface is provided to try our AI-Applications.

To run this application, we use [Docker](https://docs.docker.com/) and [Docker Compose](https://docs.docker.com/compose/). Install them via official website.

```
  $ docker compose up --build
```

Then open http://localhost:8000/docs to enjoy our api, or open http://localhost:8501/ with an interface provided by Streamlit.

