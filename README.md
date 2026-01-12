# Subscription-Based-Customer-Churn
Built a machine learning model to predict customer churn in a subscription-based platform

# Dataset Usage
The dataset contains customer-level information such as:

-Age and Gender
-Tenure (how long the customer has been subscribed)
-Usage Frequency
-Number of Support Calls
-Payment Delay
-Total Spend
-Last Interaction
-Subscription Type and Contract Length

The target variable is Churn, which indicates whether a customer has left the service.

# Model Building Process
-The dataset was cleaned and checked for missing values
-Categorical features were converted into numerical format using one-hot encoding
-The data was split into training and testing sets
-A Random Forest Classifier was trained to predict customer churn
-Model performance was evaluated using accuracy and cross-validation
-The trained model was saved using joblib for later use
