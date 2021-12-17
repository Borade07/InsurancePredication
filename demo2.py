import pandas as pd
import seaborn as sns
insurance = pd.read_csv("insurance.csv")
insurance.head()


# Replacing string values to numbers
insurance['sex'] = insurance['sex'].apply({'male':0,      'female':1}.get)
insurance['smoker'] = insurance['smoker'].apply({'yes':1, 'no':0}.get)
insurance['region'] = insurance['region'].apply({'southwest':1, 'southeast':2, 'northwest':3, 'northeast':4}.get)


# Correlation betweeen 'charges' and 'age'
sns.jointplot(x=insurance['age'],y=insurance['charges'])

# Correlation betweeen 'charges' and 'smoker'
sns.jointplot(x=insurance['age'],y=insurance['charges'])

# features
X = insurance[['age', 'sex', 'bmi', 'children','smoker','region']]
# predicted variable
y = insurance['charges']

# importing train_test_split model
from sklearn.model_selection import train_test_split
# splitting train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

len(X_test) # 402
len(X_train) # 936
len(insurance) # 1338

# importing the model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
# Fit linear model by passing training dataset
model.fit(X_train,y_train)

# Predicting the target variable for test datset
predictions = model.predict(X_test)

acc = model.score(X,y)
print("accuracy is ",acc)

# Predict charges for new customer : Name- Frank
data = {'age' : 33,
        'sex' : 0,
        'bmi' : 24.60,
        'children' : 2,
        'smoker' : 0,
        'region' : 3}
index = [1]
frank_df = pd.DataFrame(data,index)
frank_df


prediction_frank = model.predict(frank_df)
print("Medical Insurance cost for Frank is : ",prediction_frank)
