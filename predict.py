"""
Phishing Classifier - Command Line Prediction Script
Usage: python predict.py
"""

import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load('phishing_classifier_model.pkl')

# Feature names (26 features after VIF filtering)
FEATURES = [
    'having_IP_Address', 'URL_Length', 'Shortining_Service', 'having_At_Symbol',
    'double_slash_redirecting', 'Prefix_Suffix', 'having_Sub_Domain', 'SSLfinal_State',
    'Domain_registeration_length', 'Favicon', 'port', 'HTTPS_token',
    'Request_URL', 'URL_of_Anchor', 'Links_in_tags', 'SFH',
    'Submitting_to_email', 'Abnormal_URL', 'Redirect', 'on_mouseover',
    'RightClick', 'popUpWidnow', 'Iframe', 'age_of_domain',
    'DNSRecord', 'web_traffic'
]

def predict_phishing(features):
    """
    Predict if a website is phishing or legitimate
    
    Args:
        features: List of 26 feature values
        
    Returns:
        Prediction: 1 = Phishing, -1 = Legitimate
    """
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)
    return prediction[0]

def main():
    print("=" * 60)
    print("🔍 PHISHING CLASSIFIER - PREDICTION")
    print("=" * 60)
    
    # Example: Manual input
    print("\nEnter feature values (0 or 1 for each feature):")
    print(f"Total features needed: {len(FEATURES)}\n")
    
    features = []
    for i, feature_name in enumerate(FEATURES, 1):
        while True:
            try:
                value = int(input(f"{i}. {feature_name} (0 or 1): "))
                if value in [0, 1]:
                    features.append(value)
                    break
                else:
                    print("Please enter 0 or 1")
            except ValueError:
                print("Please enter a valid number")
    
    # Make prediction
    result = predict_phishing(features)
    
    print("\n" + "=" * 60)
    if result == 1:
        print("⚠️  RESULT: PHISHING WEBSITE DETECTED!")
    else:
        print("✅ RESULT: LEGITIMATE WEBSITE")
    print("=" * 60)

if __name__ == "__main__":
    main()
