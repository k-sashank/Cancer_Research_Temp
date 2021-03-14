from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        gender = request.form['gender']
        weight = int(request.form['weight'])
        height = float(request.form['height'])
        fbgl = float(request.form['fbgl'])
        ppgbl = float(request.form['ppgbl'])
        m1 = float(request.form['m1'])
        m2 = float(request.form['m2'])
        m3 = float(request.form['m3'])
        m4 = float(request.form['m4'])
        m5 = float(request.form['m5'])
        ques1 = request.form['ques1']
        ques2 = request.form['ques2']
        ques3 = request.form['ques3']
        ques4 = request.form['ques4']
        ques5 = request.form['ques5']
        ques6 = request.form['ques6']
        ques7 = request.form['ques7']
        ques8 = request.form['ques8']
        ques9 = request.form['ques9']
        ques10 = request.form['ques10']
        ques11 = request.form['ques11']
        ques12 = request.form['ques12']
        ques13 = request.form['ques13']
        ques14 = request.form['ques14']
        ques15 = request.form['ques15']
        ques16 = request.form['ques16']
        ques17 = request.form['ques17']
        ques18 = request.form['ques18']
        ques19 = request.form['ques19']

        BMI = weight/(height*height)

        diseases = []

        if m1>150 and m2>0.707 and m3<11800000:
            if m4>=137 and m5<=301 and m5>=3647 and m5<=4799 and ques2=="Y" and ques3=="Y":
                diseases.append("Disease_1")
            if m4>=825 and m4<=949 and m5>1040000 and ques4=="Y" and ques5=="Y":
                diseases.append("Disease_2")
            if m4<287 and m5>1040000 and ques6=="Y" and ques7=="Y":
                diseases.append("Disease_3")
            if m4<287 and m5>1040000 and ques8=="Y" and ques9=="Y":
                diseases.append("Disease_4")
            if gender=="F":
                if m4>287 and m5<1040000 and ques10=="Y":
                    diseases.append("Disease_5")
            if gender=="M":
                if m1>300 and m4>287 and m5<1040000 and ques10=="Y":
                    diseases.append("Disease_5")
        if gender=="F" and m1>150 and m2>0.707 and m3>15400000 and m4>287 and m5<1040000 and ques12=="Y" and ques19=="Y":
            diseases.append("Disease_6")
        if gender=="M" and m1>300 and m2>0.707 and m3>15400000 and m4>287 and m5<1040000 and ques12=="Y" and ques19=="Y":
            diseases.append("Disease_6")
        if gender=="F" and m1>150 and m2>0.707 and m3>=17.58 and m3<=24.46 and m4>=427.9 and m4<=968.6 and m5>=2904 and m5<=3135 and ques13=="Y" and ques14=="Y":
            diseases.append("Disease_7")
        if gender=="M" and m1>300 and m2>0.707 and m3>=17.58 and m3<=24.46 and m4>=427.9 and m4<=968.6 and m5>=2904 and m5<=3135 and ques13=="Y" and ques14=="Y":
            diseases.append("Disease_7")
        if m1>300 and m2>0.707 and m3<11800000:
            if m5>1040000:
                if m4<287 and ques15=="Y" and ques16=="Y":
                    diseases.append("Disease_8")
                if m4==289 and ques17=="Y" and ques18=="Y":
                    diseases.append("Disease_9")
            if m5<1040000:
                if m4==528.93 and ques17=="Y" and ques18=="Y":
                    diseases.apeend("Disease_10")
        if m1>150 and ques1=="Y":
            diseases.append("Disease_11")

        return render_template('index.html', BMI = BMI, diseases = 'You have the following:\n {}'.format(diseases))

if __name__== '__main__':
    app.run()
