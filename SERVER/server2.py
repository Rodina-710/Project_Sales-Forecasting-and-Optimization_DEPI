import streamlit as st
import pandas as pd
import joblib

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Retail Sales Prediction App",
    page_icon=":bar_chart:",
    layout="centered",
    initial_sidebar_state="auto",
)

# ---- HEADER IMAGE ----
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <img src="https://static.vecteezy.com/system/resources/previews/033/291/417/non_2x/sales-process-illustration-with-steps-of-communication-for-attracting-new-customers-and-making-profit-in-business-strategy-flat-background-vector.jpg"
             alt="Analytics Illustration"
             style="width:350px; margin-bottom: 20px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.07);"
        />
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Retail Sales Prediction App")
st.caption("Predict Quantity Sold and Revenue for Retail Products")

st.markdown("---")

# ---- LOAD MODEL ----
model = joblib.load('sales_multi_model.pkl')

# ---- INPUT FORM ----
with st.form("prediction_form"):
    st.header("Enter Product and Farm Details")
    col1, col2 = st.columns(2)

    with col1:
        total_land_area = st.number_input('Total Land Area (acres)', min_value=0.0, value=100.0)
        number_of_cows = st.number_input('Number of Cows', min_value=0, value=10)
        farm_size = st.selectbox('Farm Size', ['Small', 'Medium', 'Large'])
        product_id = st.number_input('Product ID', min_value=1, max_value=10, value=1)
        quantity = st.number_input('Quantity (liters/kg)', min_value=0.0, value=100.0)

    with col2:
        price_per_unit = st.number_input('Price per Unit', min_value=0.0, value=10.0)
        quantity_in_stock = st.number_input('Quantity in Stock (liters/kg)', min_value=0.0, value=50.0)
        min_stock_threshold = st.number_input('Minimum Stock Threshold (liters/kg)', min_value=0.0, value=10.0)
        reorder_quantity = st.number_input('Reorder Quantity (liters/kg)', min_value=0.0, value=20.0)

    target = st.radio(
        "Select the target to predict:",
        ('Quantity Sold (liters/kg)', 'Approx. Total Revenue(INR)', 'Both')
    )

    submitted = st.form_submit_button("Predict")

# ---- PREDICTION ----
if submitted:
    farm_size_map = {'Small': 0, 'Medium': 1, 'Large': 2}
    farm_size_num = farm_size_map[farm_size]

    input_df = pd.DataFrame([{
        'Total Land Area (acres)': total_land_area,
        'Number of Cows': number_of_cows,
        'Farm Size': farm_size_num,
        'Product ID': product_id,
        'Quantity (liters/kg)': quantity,
        'Price per Unit': price_per_unit,
        'Quantity in Stock (liters/kg)': quantity_in_stock,
        'Minimum Stock Threshold (liters/kg)': min_stock_threshold,
        'Reorder Quantity (liters/kg)': reorder_quantity
    }])

    prediction = model.predict(input_df)[0]
    st.markdown("---")
    st.subheader("Prediction Results")
    if target == 'Quantity Sold (liters/kg)':
        st.success(f"Predicted Quantity Sold (liters/kg): **{prediction[0]:.2f}**")
    elif target == 'Approx. Total Revenue(INR)':
        st.success(f"Predicted Approx. Total Revenue (INR): **{prediction[1]:.2f}**")
    else:
        st.success(f"Predicted Quantity Sold (liters/kg): **{prediction[0]:.2f}**")
        st.success(f"Predicted Approx. Total Revenue (INR): **{prediction[1]:.2f}**")

# ---- FOOTER ----
st.markdown("---")
st.caption("© 2025 Retail Sales Prediction App | Powered by Streamlit")
