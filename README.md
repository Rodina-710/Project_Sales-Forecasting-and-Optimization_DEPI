# Project_Sales-Forecasting-and-Optimization_Team4
📈 Sales Forecasting and Optimization
Overview
Sales Forecasting and Optimization is a data-driven application designed to assist agricultural retailers and farm managers in making informed business decisions by forecasting product sales and estimating revenue. Leveraging machine learning techniques, the project enables users to enter key product and farm information and receive predictive insights instantly via an interactive web interface.

The application is particularly useful for retail operations involving dairy and similar products where accurate demand forecasting and inventory control are essential.

📦 Model File Notice
Important:
The required machine learning model file sales_multi_model.pkl is included in a compressed archive named Models.zip.

Please make sure to:

Download the Models.zip file from the project repository.

Extract the contents.

Move the sales_multi_model.pkl file into the project’s root directory (same folder as server2.py).

The application will not run without this model file properly placed.
🔧 Features
🌾 Input-Based Prediction: Predicts sales quantity and expected revenue based on customizable inputs like land size, number of cows, farm size, product ID, and pricing.

🧠 Machine Learning Model: Uses a trained regression model to generate real-time predictions.

📊 Interactive Web Interface: Built with Streamlit for a clean, responsive user experience.

⚙️ Inventory Optimization: Helps determine stock requirements and reorder levels.

💼 Business Intelligence Tool: Ideal for small to medium-scale retailers and farm owners seeking actionable insights.

🛠️ Installation Guide
Follow the steps below to set up and run the application locally:

1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/sales-forecasting-optimization.git
cd sales-forecasting-optimization
2. Set Up a Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt

Note: If requirements.txt is not present, install manually:

bash
Copy
Edit
pip install streamlit pandas scikit-learn joblib
4. Add the Model File
Ensure the trained model file [ sales_multi_model.pkl ] is placed in the root directory of the project. This file is essential for making predictions.

🚀 How to Run the App
Launch the Streamlit web application with the following command:

bash
Copy
Edit
streamlit run server2.py
The app will start in your browser at https://projectsales-forecasting-and-optimizationdepi-mvmydjupao3fdvuk.streamlit.app/

📘 Usage Instructions
Start the App and wait for the interface to load.

Fill in the Product and Farm Details in the provided form:

Total Land Area (acres)

Number of Cows

Farm Size (Small / Medium / Large)

Product ID (1–10)

Quantity (liters/kg)

Price per Unit

Quantity in Stock

Minimum Stock Threshold

Reorder Quantity

Select the Target Prediction Output:

Quantity Sold

Approximate Revenue (INR)

Both

Click Predict.

View the prediction results on the screen.

📂 File Structure
bash
Copy
Edit
├── server2.py               # Streamlit app script
├── sales_multi_model.pkl    # Pretrained machine learning model (you must add this)
├── requirements.txt         # List of dependencies
├── Sales Forecasting and Optimization - DEPI_DRAFT.ipynb  # Notebook for model training and analysis
📌 Requirements
Python 3.7+

Streamlit

pandas

scikit-learn

joblib


