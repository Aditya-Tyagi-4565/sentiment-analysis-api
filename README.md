# End-to-End Customer Sentiment and Topic Analysis API

This project is a complete, end-to-end machine learning application that analyzes customer reviews to predict sentiment and identify key topics. The final product is a containerized REST API built with FastAPI and Docker.

## Project Overview

The system takes raw customer review text as input and returns a sentiment prediction (Positive/Negative). It was built progressively, starting from a baseline model and advancing to a deep learning solution. The project also includes an unsupervised learning component for topic modeling to extract business insights. The entire application is containerized with Docker for easy deployment and scalability.

## Features

-   **Sentiment Analysis:** Predicts if a review is positive or negative using a trained LSTM model.
-   **Topic Modeling:** Identifies 7 key topics from the review data using LDA.
-   **REST API:** A robust API built with FastAPI to serve the sentiment model.
-   **Dockerized:** The entire application is containerized for portability and reproducible builds.
-   **Interactive Docs:** The API includes automatically generated, interactive documentation via Swagger UI.

## Technologies & Skills Demonstrated

-   **Programming:** Python
-   **Data Science:** Pandas, NumPy, NLTK, Scikit-learn, Matplotlib, Seaborn
-   **Machine Learning:**
    -   Feature Engineering (TF-IDF, Word2Vec)
    -   Supervised Learning (Logistic Regression)
    -   Deep Learning (TensorFlow/Keras, LSTMs)
    -   Unsupervised Learning (LDA for Topic Modeling)
-   **Backend & API:** FastAPI, Uvicorn
-   **MLOps & Deployment:** Docker, REST API principles

## Project Structure

```
complaint_analysis/
│
├── artifacts/              # Saved model and tokenizer
│   ├── tokenizer.pkl
│   └── sentiment_model.h5
├── data/                   # Raw and processed data
├── notebooks/              # Jupyter notebooks for EDA and modeling
├── main.py                 # The FastAPI application script
├── Dockerfile              # Recipe for building the Docker image
├── .dockerignore           # Specifies files to ignore in the Docker build
└── requirements.txt        # Production dependencies
```

## Setup & Installation

The easiest way to run this application is by using Docker.

### 1. Prerequisites
- Docker must be installed and running on your machine.

### 2. Build the Docker Image
Navigate to the project's root directory in your terminal and run:
```bash
docker build -t sentiment-api .
```

### 3. Run the Docker Container
Once the image is built, run the following command to start the API server:
```bash
docker run -p 8000:8000 sentiment-api
```

## How to Use the API

Once the container is running, the API is accessible on your local machine.

### Interactive Documentation (Swagger UI)
The easiest way to test the API is through the interactive docs.
1.  Open your browser and go to **`http://127.0.0.1:8000/docs`**.
2.  Click on the `/predict` endpoint, then "Try it out."
3.  Enter a review in the request body and execute.

### Using cURL
You can also send a request from your terminal using `cURL`:
```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "The quality of this sweater is fantastic and it feels very durable."
}'
```

## Model Performance

The final LSTM model achieved an **F1-score of 92%** on the held-out test set, outperforming the baseline Logistic Regression models.

## Future Improvements

-   Deploy the Docker container to a cloud service (e.g., AWS ECS, Google Cloud Run).
-   Experiment with more advanced Transformer models like BERT for sentiment analysis.
-   Create a database to store incoming requests and predictions.
