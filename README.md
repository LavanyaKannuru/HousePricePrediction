House Price Prediction Project
This project is a machine learning-based web application built with Streamlit to predict house prices using the California housing dataset. The model predicts prices based on various input features, including location, number of bedrooms, and household median income.

Project Structure
.
├── data/                     # Dataset folder (California housing data)
├── app/                      # Application files
│   ├── model.py              # ML model code
│   ├── app.py                # Streamlit application
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation

Features:
Machine Learning Model - Trained on the California housing dataset.
Web Application - User-friendly interface created with Streamlit.

Installation and Setup:
Prerequisites:
Python 3.7 or above
Pip
Virtual environment tool (optional but recommended)

Setup Instructions
Clone the repository:
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction

Create a virtual environment:
python -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`

Install dependencies:
pip install -r requirements.txt

Run the application locally:
streamlit run app/app.py
After running this command, open your browser and go to http://localhost:8501 to view the application.

Model and Assumptions:
Dataset: The model is trained on the California housing dataset.
Assumptions:
Features Used: The model uses features like median income (MedInc), number of bedrooms, and location for predictions.
Target Variable: Median house price in a block group.
Data Preprocessing: Standard scaling is applied to features, and any missing values are handled by filling with the median.
License
This project is licensed under the MIT License.




