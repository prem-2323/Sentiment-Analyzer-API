# Sentiment Analyzer (FastAPI + Streamlit)

A full-stack machine learning web application that analyzes the sentiment of text as either **Positive** or **Negative**. 

This project uses a Deep Learning model built with TensorFlow, served through a high-performance **FastAPI** backend, and presented beautifully with a **Streamlit** frontend interface.

## 🚀 Features

- **Deep Learning Model:** Utilizes a pre-trained SimpleRNN neural network model.
- **FastAPI Backend:** Robust, fast API serving predictions via a REST endpoint.
- **Streamlit Frontend:** A beautiful, responsive, custom-styled web interface.

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, Uvicorn, TensorFlow
- **Frontend:** Streamlit, Custom CSS
- **Data Processing:** Pandas, Numpy, Pickle

## 📋 Prerequisites

Make sure you have Python 3.10+ installed on your machine.

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/prem-2323/Sentiment-Analyzer-API.git
   cd Sentiment-Analyzer-API
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Application

To run the full application, you need to start both the backend API and the frontend UI.

### 1. Start the FastAPI Backend
Open a terminal, activate your virtual environment, and run:
```bash
uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
```
*The backend API will be available at `http://localhost:8000`*
*Interactive API documentation (Swagger) is automatically generated at `http://localhost:8000/docs`*

### 2. Start the Streamlit Frontend
Open a **new** terminal window, activate your virtual environment again, and run:
```bash
streamlit run frontend.py
```
*The Streamlit web interface will open automatically in your browser at `http://localhost:8501`*

## 📡 API Endpoints

If you want to use the API programmatically without the frontend, you can send a `POST` request to the `/predict` endpoint.

**Endpoint:** `POST http://localhost:8000/predict`

**Request Body (JSON):**
```json
{
  "text": "I really love this product, it is amazing!"
}
```

**Response (JSON):**
```json
{
  "sentiment": "Positive",
  "score": 0.9854
}
```

## 📁 Project Structure

- `backend.py`: The FastAPI application server code.
- `frontend.py`: The Streamlit web interface code and custom styling.
- `model.h5`: The pre-trained TensorFlow Deep Learning model file.
- `tokenizer.pkl`: The tokenizer used to process text input into sequences.
- `requirements.txt`: Python package dependencies required to run the app.
