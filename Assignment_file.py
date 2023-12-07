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
#from the input data received by the server as JSON, the relevant data is extracted and converted to a datatype and format suitable for getting the predictions from the model
    user_number = np.array(user_sent_this_data).reshape(1, -1)
    model_predictions = my_lr_model.predict(user_number)
    return Response(str(model_predictions))
#the model has been wrapped in a Flask server and both POST and GET have been enabled for this server. To get prediction, user can send input data using requests.post and will get back the prediction or the output through response
if __name__ == '__main__':
    app.run(debug=True, port=5005)