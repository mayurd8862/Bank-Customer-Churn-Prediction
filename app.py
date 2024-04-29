

from flask import Flask, request, render_template
from src.mlproject.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Route for predicting data
@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    
    if request.method == 'GET':
        # return render_template('result.html')
        return render_template('test.html')
    else:

        data = CustomData(
            CreditScore=float(request.form.get('CreditScore')),
            Geography=request.form.get('Geography'),
            Gender=request.form.get('Gender'),
            Age=int(request.form.get('Age')),
            Tenure=int(request.form.get('Tenure')) if request.form.get('Tenure') else None,
            Balance=float(request.form.get('Balance')) if request.form.get('Balance') else None,
            # NumOfProducts=int(request.form.get('NumOfProducts')) if request.form.get('NumOfProducts') else None,
            HasCrCard=int(request.form.get('HasCrCard')),
            IsActiveMember=int(request.form.get('IsActiveMember')),
            EstimatedSalary=float(request.form.get('EstimatedSalary')) if request.form.get('EstimatedSalary') else None
        )
        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        if results[0]==1:
            otpt = "Customer will LEAVE the bank"
        else:
            otpt = "Customer will NOT LEAVE the bank"

        # Include the form values in the rendered template
        # return render_template('result.html', results=(results[0]), **request.form)
        return render_template('test.html', results=otpt, **request.form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

# http://127.0.0.1:5000/