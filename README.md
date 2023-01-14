Streamlit Cloud deployment link: https://inuwamobarak-employee-attrition-xgboost-web-app-9uh06g.streamlit.app/

# ABOUT THE PROJECT

## Employee-attrition Prediction
Employee attrition prediction using machine learning models

**Problem:** Replacing a departing employee often costs an organization $4,000 or more. The average cost to hire an employee, according to a different research by the Society for Human Resource Management, is $4,129, and it often takes 42 days to fill a post. The typical American company spends $4,000 to hire a new employee, and it might take up to 52 days to fill a post, according to Glassdoor.

**Approach:** The project utilizes a public dataset available online in Kagle dataset repository to build a proto-type machine learning pipeline.
* In practice, the XGBoost algorithm is selected for model building due to its ability in handling imbalanced data.
* We do not need to always balance data before using when we have the flexibility of utilizing powerful models like XGBoost. Resampling would have been the alternative if we didnt have XGBoost algorithms.

Any comapny could re-create a personalized dataset and utilize this prototype.

### The Dataset
This is a fictional data set created by IBM data scientists.

Education
1 'Below College'
2 'College'
3 'Bachelor'
4 'Master'
5 'Doctor'

EnvironmentSatisfaction
1 'Low'
2 'Medium'
3 'High'
4 'Very High'

JobInvolvement
1 'Low'
2 'Medium'
3 'High'
4 'Very High'

JobSatisfaction
1 'Low'
2 'Medium'
3 'High'
4 'Very High'

PerformanceRating
1 'Low'
2 'Good'
3 'Excellent'
4 'Outstanding'

RelationshipSatisfaction
1 'Low'
2 'Medium'
3 'High'
4 'Very High'

WorkLifeBalance
1 'Bad'
2 'Good'
3 'Better'
4 'Best'


* Dataset license: https://opendatacommons.org/licenses/dbcl/1-0/
* Dataset: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
