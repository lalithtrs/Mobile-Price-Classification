from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get values from form
        features = [
            float(request.form['battery_power']),
            float(request.form['int_memory']),
            float(request.form['mobile_wt']),
            float(request.form['pc']),
            float(request.form['px_height']),
            float(request.form['px_width']),
            float(request.form['ram']),
            float(request.form['sc_h']),
            float(request.form['sc_w']),
            float(request.form['talk_time'])
        ]
        f = features
        print(features)
        # Make prediction
        prediction = model.predict([features])[0]
        
        return render_template('index.html', prediction=prediction)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)