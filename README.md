# IMDb Review Sentiment Analysis

This project is a **Streamlit** web application that performs **sentiment analysis** on IMDb movie reviews. It classifies reviews as either **positive** or **negative** using **Natural Language Processing (NLP)** techniques.

## Live Demo
🔗 [IMDb Review Sentiment Analysis App](https://sentiment-analysis-using-machine-learning.streamlit.app/)

## Features
- 📌 User-friendly **Streamlit** interface
- 📌 **Real-time** IMDb review classification
- 📌 Uses **Machine Learning** for sentiment prediction
- 📌 **Pre-trained NLP model** for better accuracy
- 📌 Supports **text input** for user reviews

## Technologies Used
- **Python 3.10.16** (on Streamlit Cloud)
- **Streamlit** for web application
- **scikit-learn** for ML models
- **NLTK / SpaCy** for NLP preprocessing (if applicable)
- **Pandas & NumPy** for data manipulation

## Installation
To run this project locally, follow these steps:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/imdb-sentiment-analysis.git
cd imdb-sentiment-analysis
```

### 2️⃣ Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## Deployment
This app is deployed on **Streamlit Cloud**. To deploy it yourself:
1. Push your project to a **GitHub repository**.
2. Go to **Streamlit Cloud** → Create a new app.
3. Connect your GitHub repo and set the **main script** (e.g., `app.py`).
4. Click **Deploy**!

## Project Structure
```
├── app.py               # Main Streamlit app
├── model.pkl            # Trained sentiment analysis model (if applicable)
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
└── dataset/             # IMDb dataset (if used)
```

## Requirements.txt
Here’s a sample **requirements.txt** file:
```txt
streamlit==1.37.0
scikit-learn==1.2.1
numpy==1.23.5
pandas==2.2.2
nltk==3.8.1  # If using NLTK
spacy==3.5.3  # If using SpaCy
```

## Contributing
Feel free to **fork** this repo and make improvements. Pull requests are welcome!

## License
📜 MIT License – Free to use and modify.


