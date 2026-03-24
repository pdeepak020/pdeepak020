from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd

# Load the model
my_model = pickle.load(open('full_pipeline', 'rb'))

# Initialize the FastAPI app
app = FastAPI()

# Define a request model for input validation
class InputData(BaseModel):
    Married: str
    Education: str
    ApplicantIncome: float
    LoanAmount: float
    Credit_History: float

# Define the prediction endpoint
@app.post("/predict")# API call
def predict(input_data: InputData):
    try:
        # Convert input data to DataFrame
        test = pd.DataFrame([[input_data.Married, input_data.Education, input_data.ApplicantIncome,
                              input_data.LoanAmount, input_data.Credit_History]],
                             columns=['Married', 'Education', 'ApplicantIncome', 'LoanAmount', 'Credit_History'],
                             index=['input'])

        # Get the model's prediction
        prediction = my_model.predict(test)[0]

        # Return the prediction result
        return {"prediction": prediction}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

# Run the app (use `uvicorn` to start the server in development)
# Example: uvicorn script_name:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("appnew:app", host="127.0.0.1", port=8000, reload=True)