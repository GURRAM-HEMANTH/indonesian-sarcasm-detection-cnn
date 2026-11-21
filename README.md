# Indonesian Sarcasm Detection using CNN

An NLP-based project that detects sarcastic expressions in Indonesian text using a Convolutional Neural Network (CNN) and a Flask web application.

## Project Overview

Sarcasm detection is a challenging Natural Language Processing (NLP) task because sarcastic statements often express meanings different from their literal interpretation.

This project uses a CNN-based deep learning model to classify Indonesian text into two categories:

- Sarcastic
- Non-Sarcastic

The trained model is integrated into a Flask web application that allows users to submit text and receive predictions.

## Objectives

- Detect sarcasm in Indonesian textual content.
- Apply Natural Language Processing techniques for text processing.
- Use CNN for automatic feature extraction and classification.
- Integrate the trained model into a Flask web application.
- Provide an interactive interface for text prediction.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| TensorFlow / Keras | Deep learning model |
| CNN | Text classification |
| Flask | Web application |
| NumPy | Numerical operations |
| Joblib | Tokenizer loading |
| HTML | Frontend |
| Jupyter Notebook | Model development |

## Project Structure

```text
indonesian-sarcasm-detection-cnn/
│
├── Model/
│   ├── cnn.ipynb
│   ├── lstm_model.h5
│   ├── LSTM_MODEL.ipynb
│   ├── LSTM_MODEL_train.ipynb
│   └── tokenizer.pkl
│
├── static/
│   └── Application assets
│
├── templates/
│   ├── home.html
│   ├── input.html
│   ├── login.html
│   ├── result.html
│   ├── abstract.html
│   └── chart.html
│
├── app.py
├── cnn_model.h5
├── cnn_tokenizer.pkl
├── requirements.txt
└── test_data.xlsx
```

## How It Works

1. The user enters Indonesian text into the web application.
2. The text is converted into numerical sequences using the trained tokenizer.
3. The sequences are padded to a fixed length of 100.
4. The trained CNN model processes the input.
5. The model predicts whether the text is sarcastic or non-sarcastic.
6. The prediction is displayed on the web interface.

## Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/GURRAM-HEMANTH/indonesian-sarcasm-detection-cnn.git
```

### 2. Navigate to the project directory

```bash
cd indonesian-sarcasm-detection-cnn
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app.py
```

### 5. Open the application

Visit:

```text
http://127.0.0.1:5000/
```

## Model Information

The primary Flask application loads:

- `cnn_model.h5` – Trained CNN model.
- `cnn_tokenizer.pkl` – Fitted text tokenizer.

The repository also includes supplementary LSTM model files and Jupyter notebooks.

## Dataset

The original training dataset is not included in this repository because of its large file size.

The dataset used for training should be placed in the appropriate project directory before running the training notebooks.

## Future Enhancements

- Improve model performance through additional experiments.
- Explore advanced NLP architectures such as LSTM and Transformer models.
- Support additional languages.
- Improve the user interface.
- Deploy the application online.

## Author

**Gurram Hemanth**

B.Tech – Computer Science and Engineering

GitHub: [GURRAM-HEMANTH](https://github.com/GURRAM-HEMANTH)

## Disclaimer

This project was developed as an academic major project. Model performance should be independently evaluated before using the application in real-world systems.
