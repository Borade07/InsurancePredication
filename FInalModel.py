import pickle
import pandas as pd
import os.path
insurance = pd.read_csv("insurance.csv")
insurance.head()

if os.path.exists("TrainedModel.pickle"):
    print("load model in FinalModel ")

    model = pickle.load(open("TrainedModel.pickle","rb"))


else:
    print(" creating a model ...................................")
    print("*"*20)

    # def InsuranceCost(age, sex, bmi, children, smoker, region):
    # def InsuranceCost():
    print("in demo")
    # print("age", age, "sex", sex, bmi, children, smoker, region)
    # Replacing string values to numbers
    insurance['sex'] = insurance['sex'].apply({'male': 0, 'female': 1}.get)
    insurance['smoker'] = insurance['smoker'].apply({'yes': 1, 'no': 0}.get)
    insurance['region'] = insurance['region'].apply(
        {'southwest': 1, 'southeast': 2, 'northwest': 3, 'northeast': 4}.get)

    # features
    X = insurance[['age', 'sex', 'bmi', 'children', 'smoker', 'region']]
    # predicted variable
    y = insurance['charges']

    # importing train_test_split model
    from sklearn.model_selection import train_test_split

    # splitting train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

    # importing the model
    from sklearn.linear_model import LinearRegression

    model = LinearRegression()
    # Fit linear model by passing training dataset
    model.fit(X_train, y_train)

    # Predicting the target variable for test datset
    predictions = model.predict(X_test)

    with open("TrainedModel.pickle","wb") as file:
        pickle.dump(model,file)

# Predict charges for new customer : Name- Frank


def InsuranceCost(age, sex, bmi, children, smoker, region):
    # data = {'age' : 44,
    #             'sex' : 1,
    #             'bmi' : 27.5,
    #             'children' : 1,
    #             'smoker' : 0,
    #             'region' : 1}
    # accuracy = model.score(X, y)
    # print(accuracy)
    data = {'age': age,
            'sex': sex,
            'bmi': bmi,
            'children': children,
            'smoker': smoker,
            'region': region}
    index = [1]
    frank_df = pd.DataFrame(data, index)
    frank_df

    prediction_frank = model.predict(frank_df)
    print("Medical Insurance cost for Frank is : ", prediction_frank[0])

    return prediction_frank[0]

InsuranceCost(44,1,27.5,1,0,1)