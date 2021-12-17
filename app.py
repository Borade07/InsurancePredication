from flask import Flask,render_template,request
# import demo as d
import FInalModel as FM

app =Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello():
    print("hello welcome to app .py ")
    mm = [0]
    if request.method == 'POST':
        age = request.form["age"]
        sex = request.form["sex"]
        bmi = request.form["bmi"]
        children = request.form["children"]
        smoker = request.form["smoker"]
        region = request.form["region"]

        print("SEX OF PERSON IS ",sex)
        s=[1]
        if sex=="male":
            # s.append(0)
            s[0] = 0
        elif sex=="female":
            # s.append(1)
            s[0] = 1
        print("value of s")
        print(s)

        print("THE PRESONS SAY SMOKER",smoker)
        sm = [1]
        if smoker == "Yes":
            # sm.append(0)
            sm[0] = 1
        elif smoker == "No":
            # sm.append(1)
            sm[0] =0
        print("value of sm")
        print(sm)

        print("THE REGION OF THE PERSON IS",region)
        re = [0]
        if region=="southeast":
            re[0] = 2
        elif region == "southwest":
            re[0] = 1
        elif region == "northeast":
            re[0] = 4
        elif region == "northwest":
            re[0] = 3

        print(re)

        # data = {'age': age,
        #         'sex': s[0],
        #         'bmi': bmi,
        #         'children': children,
        #         'smoker': sm[0],
        #         'region': re[0]}
        # data = {'age': 44,
        #         'sex' : 1,
        #         'bmi' : 27.5,
        #         'children' : 1,
        #         'smoker' : 0,
        #         'region' : 1}
        # print(data)
        # asd = (age,s[0],bmi,children,sm[0],re[0])
        # print(asd)

        # prd = d.InsuranceCost(age,s[0],bmi,children,sm[0],re[0])
        prd = FM.InsuranceCost(age,s[0],bmi,children,sm[0],re[0])
        print(prd)
        # mm.append(prd)
        mm[0] = prd

    return render_template("index.html",amey= mm[0])

if __name__ == '__main__':
    app.run()