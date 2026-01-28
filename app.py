"""
Phishing Classifier - Streamlit Web App
Run with: streamlit run app.py
"""

import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(
    page_title="Phishing Classifier",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    """Load the trained model"""
    return joblib.load('phishing_classifier_model.pkl')

model = load_model()

# Feature names
FEATURES = [
    'having_IP_Address', 'URL_Length', 'Shortining_Service', 'having_At_Symbol',
    'double_slash_redirecting', 'Prefix_Suffix', 'having_Sub_Domain', 'SSLfinal_State',
    'Domain_registeration_length', 'Favicon', 'port', 'HTTPS_token',
    'Request_URL', 'URL_of_Anchor', 'Links_in_tags', 'SFH',
    'Submitting_to_email', 'Abnormal_URL', 'Redirect', 'on_mouseover',
    'RightClick', 'popUpWidnow', 'Iframe', 'age_of_domain',
    'DNSRecord', 'web_traffic'
]

# Title
st.title("🔍 Phishing Website Classifier")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Choose Input Method:", ["Single Prediction", "Batch Prediction", "About"])

# Main content
if page == "Single Prediction":
    st.header("Single Website Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Enter Features")
        features = []
        
        # Create input fields for each feature (2 columns)
        for i, feature in enumerate(FEATURES):
            if i % 2 == 0:
                col = col1
            else:
                col = col2
            
            value = col.number_input(f"{feature}", min_value=-1, max_value=1, value=0)
            features.append(value)
    
    # Predict button
    if st.button("🔍 Predict", use_container_width=True):
        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0]
        
        st.markdown("---")
        
        if prediction == 1:
            st.error("🚨 **PHISHING DETECTED!** This website is likely to be PHISHING")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Phishing Probability", f"{probability[1]*100:.2f}%")
            with col2:
                st.metric("Legitimate Probability", f"{probability[0]*100:.2f}%")
        else:
            st.success("✅ **SAFE!** This website appears to be LEGITIMATE")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Legitimate Probability", f"{probability[0]*100:.2f}%")
            with col2:
                st.metric("Phishing Probability", f"{probability[1]*100:.2f}%")

elif page == "Batch Prediction":
    st.header("Batch Prediction from CSV")
    
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        if st.button("🔍 Predict All Rows", use_container_width=True):
            predictions = model.predict(df)
            probabilities = model.predict_proba(df)
            
            results_df = df.copy()
            results_df['Prediction'] = ['🚨 PHISHING' if p == 1 else '✅ LEGITIMATE' for p in predictions]
            results_df['Phishing_Prob'] = probabilities[:, 1]
            results_df['Legitimate_Prob'] = probabilities[:, 0]
            
            st.dataframe(results_df, use_container_width=True)
            
            # Download button
            csv = results_df.to_csv(index=False)
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name="phishing_predictions.csv",
                mime="text/csv"
            )
            
            # Summary stats
            phishing_count = sum(predictions == 1)
            legitimate_count = sum(predictions == -1)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Predictions", len(predictions))
            with col2:
                st.metric("🚨 Phishing Sites", phishing_count)
            with col3:
                st.metric("✅ Legitimate Sites", legitimate_count)

else:  # About
    st.header("About This Project")
    
    st.markdown("""
    ### 📊 Phishing Classifier
    
    This machine learning project detects phishing websites using advanced classification algorithms.
    
    **Dataset Information:**
    - Total Samples: 11,055
    - Features: 26 (after feature engineering)
    - Target: Phishing/Legitimate classification
    
    **Model Used:** Random Forest Classifier
    - Accuracy: ~98%
    - n_estimators: 200
    - max_depth: 30
    
    **Features Analyzed:**
    - URL characteristics (length, structure, symbols)
    - Domain information (age, registration length)
    - SSL/HTTPS status
    - Content features (anchors, links, redirects)
    - And 18 more indicators...
    
    **How It Works:**
    1. Extracts 26 features from website characteristics
    2. Feeds features to trained Random Forest model
    3. Model predicts probability of phishing
    4. Returns classification with confidence score
    
    **Use Cases:**
    - Email security screening
    - Web browser extensions
    - Network security systems
    - User education tools
    
    ---
    
    **⚠️ Disclaimer:** This tool is for educational purposes. Always validate results with domain experts.
    """)
