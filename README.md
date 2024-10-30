House Price Prediction App
This project is a web application built using Streamlit that predicts house prices based on various features such as location, number of bedrooms, and square footage. The application utilizes a machine learning model trained on the California housing dataset.

Features
User-friendly interface for inputting house features.
Real-time price predictions based on user inputs.
Visualization of predicted prices.
Technologies Used
Python: Programming language for application development.
Streamlit: Framework for building interactive web applications.
Pandas: Library for data manipulation and analysis.
NumPy: Library for numerical operations.
scikit-learn: Library for machine learning model training and evaluation.
Installation
To run this project locally, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/LavanyaKannuru/HousePricePrediction.git
cd HousePricePrediction
Set Up a Virtual Environment (optional but recommended):

Windows:
bash
Copy code
python -m venv venv
venv\Scripts\activate
macOS/Linux:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install Required Packages:

bash
Copy code
pip install -r requirements.txt
Usage
To run the app locally, execute the following command:

bash
Copy code
streamlit run app.py
Open your browser and navigate to http://localhost:8501 to access the app.

API Endpoints
The Streamlit app operates through a user interface rather than traditional API endpoints. Users can interact with the app through input forms, and predictions are displayed directly in the interface.

Input Fields:
Location: Dropdown menu for selecting the location.
Number of Bedrooms: Numeric input for the number of bedrooms.
Square Footage: Numeric input for the size of the house in square feet.
Additional Features: Other relevant features can be added as necessary.
Output:
Predicted Price: Displays the estimated price of the house based on the provided inputs.
Model Building Assumptions
The model assumes that the provided features are significant predictors of house prices.
The dataset used for training is specific to California and may not be applicable to other regions.
It is assumed that the dataset is preprocessed and cleaned prior to training.
License
This project is licensed under the MIT License - see the LICENSE file for details.







