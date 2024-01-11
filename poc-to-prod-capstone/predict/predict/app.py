from flask import Flask, request, render_template_string
from predict.predict.run import TextPredictionModel

app = Flask(__name__)
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>StackOverflow Tags Prediction</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 20px;
        }

        h2 {
            color: #007bff;
        }

        form {
            margin-top: 20px;
        }

        textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            box-sizing: border-box;
        }

        button {
            padding: 10px;
            background-color: #007bff;
            color: #fff;
            border: none;
            cursor: pointer;
        }

        div {
            margin-top: 20px;
            padding: 10px;
            background-color: #dff0d8;
            border: 1px solid #3c763d;
            color: #3c763d;
        }
    </style>
</head>
<body>
    <h2>StackOverflow Tag Prediction</h2>
    <form action="/" method="post">
        <textarea name="text" rows="4" placeholder="Type your StackOverflow title here..."></textarea>
        <button type="submit">Predict</button>
    </form>
    {% if predictions %}
    <div>
        <strong>Predictions:</strong> {{ predictions }}
    </div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    predictions = None
    if request.method == 'POST':
        text_list = [request.form['text']]
        model = TextPredictionModel.from_artefacts('train/data/artefacts/2024-01-06-12-46-21')
        predictions = model.predict(text_list)
    return render_template_string(HTML_TEMPLATE, predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)