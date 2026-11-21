from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load the model and tokenizer once when the app starts
model = load_model('cnn_model.h5')
tokenizer = joblib.load('cnn_tokenizer.pkl')
max_len = 100  # Define the sequence length for padding

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "admin":
            return redirect(url_for('predict'))  # Redirect to predict route after successful login
        else:
            return render_template('login.html', error="Invalid credentials. Please try again.")
    
    return render_template('login.html')

@app.route('/abstract')
def abstract():
    return render_template('abstract.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        input_text = request.form['text_input']

        # Tokenize and pad the input text
        input_seq = tokenizer.texts_to_sequences([input_text])
        input_padded = pad_sequences(input_seq, maxlen=max_len)

        # Make the prediction
        prediction = model.predict(input_padded)
        predicted_class = np.argmax(prediction, axis=1)[0]

        if predicted_class == 0:
            sarcasm_result = "Found 'No sarcastic' in this text"
        else:
            sarcasm_result = "Found 'Sarcastic' in this text"

        # Pass the result to the result page
        return render_template('result.html', prediction=sarcasm_result)

    return render_template('input.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)

