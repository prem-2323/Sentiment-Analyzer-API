# Project Report: Sentiment Analyzer

## 1. Introduction
The Sentiment Analyzer is a full-stack machine learning web application designed to evaluate the emotional tone of user-provided text. It determines whether the sentiment of a given sentence is **Positive** or **Negative**. 

## 2. Objectives
- To deploy a pre-trained Deep Learning model for natural language processing (NLP).
- To create a robust, high-performance REST API to serve model predictions securely.
- To build an intuitive, beautiful, and responsive user interface for seamless user interaction.

## 3. Technology Stack
- **Machine Learning**: TensorFlow, Keras (SimpleRNN model)
- **Backend API**: Python, FastAPI, Uvicorn, Pydantic
- **Frontend UI**: Streamlit, HTML/CSS (Custom Styling)
- **Data Processing**: Numpy, Pandas, Pickle
- **Version Control**: Git & GitHub

## 4. System Architecture
The application follows a modern, decoupled client-server architecture:
- **Client (Frontend)**: Built with Streamlit, it captures user input and sends it to the backend via an HTTP POST request using the `requests` library. It features a custom-styled, modern UI utilizing raw CSS injection.
- **Server (Backend)**: Built with FastAPI. It receives the text, tokenizes it using a pre-trained `tokenizer.pkl`, pads the sequences to a fixed length, and feeds it into the `model.h5` neural network.
- **Model**: A Simple Recurrent Neural Network (RNN) trained on a large dataset of Twitter sentiment data.

## 5. Implementation Details
### 5.1 The Backend (FastAPI)
The backend exposes a single REST endpoint (`/predict`) which accepts a JSON payload containing the text string. 
- **Performance:** Fast and asynchronous request handling.
- **Validation:** Automatic data validation using Pydantic models.
- **Documentation:** Generates automatic interactive API documentation (Swagger UI) accessible at `/docs`.

### 5.2 The Frontend (Streamlit)
- **Custom CSS**: Overrides Streamlit's default components to render floating cards, vibrant gradients, and custom buttons.
- **Dynamic Results**: Conditionally renders UI elements (Emerald Green for Positive, Red for Negative) based on the API response, ensuring an engaging user experience.
- **Error Handling**: Gracefully handles API connection errors or empty text submissions.

## 6. Project Setup & Execution
The project is containerized within a Python virtual environment (`venv`). Dependencies are strictly managed via `requirements.txt`. The backend runs on a lightweight Uvicorn ASGI server on port 8000, while the Streamlit frontend runs parallelly on port 8501.

## 7. Conclusion
The project successfully bridges the gap between a raw machine learning model and end-user accessibility. By utilizing FastAPI for backend logic and Streamlit for rapid UI development, the application achieves both high backend performance and a highly polished frontend experience.
