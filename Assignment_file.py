from flask import Flask, request, Response
from joblib import load
import numpy as np

# Loading the model
my_lr_model = load("joblib/gl_project.joblib")

app = Flask(__name__)

@app.route("/predictions", methods=['POST','GET'])
def testing():
    data = request.json
    user_sent_this_data = data.get('mydata')

    user_number = np.array(user_sent_this_data).reshape(1, -1)
    model_predictions = my_lr_model.predict(user_number)
    return Response(str(model_predictions))

if __name__ == '__main__':
    app.run(debug=True, port=5005)