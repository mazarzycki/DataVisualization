# app.py

from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Read the uploaded CSV file
            df = pd.read_csv(file)

            # Perform data processing and generate visualizations
            columns = df.columns
            x_column = columns[0]
            y_column = columns[1]

            plt.figure()
            plt.bar(df[x_column], df[y_column])
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.title('Data Visualization')
            plt.savefig('static/chart.png')
            plt.close()

            # Render the visualizations template
            with app.app_context():
                return render_template('visualizations.html')
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
