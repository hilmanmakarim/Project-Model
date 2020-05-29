from flask import Flask, render_template, url_for, request, send_from_directory
import numpy as np
import pandas as pd
import folium
import joblib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("predict.html")

@app.route("/about")
def stats():
    return render_template("about.html")

@app.route('/gallery/<path:x>')
def gal(x):
    return send_from_directory("gallery", x)

@app.route('/visualisation')
def vis():
    return render_template('visualisation.html')

@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        input = request.form
        #Age
        Age = int(input['Age'])

        # Balance
        Balance = int(input['Balance'])

        # Duration
        Duration = int(input['Duration'])
        
        # Campaign
        Campaign = int(input['Campaign'])
        
        # Job
        Job = input['Job']
        strJob = ''
        if Job == 'Admin':
            job1 = 1
            job2 = 0
            job3 = 0
            job4 = 0
            job5 = 0
            job6 = 0
            job7 = 0 
            job8 = 0 
            job9 = 0; 
            job10 = 0; 
            job11 = 0; 
            job12 = 0; 
            strJob = 'Admin'
        if Job == 'Blue-Collar':
            job1 = 0
            job2 = 1
            job3 = 0
            job4 = 0
            job5 = 0
            job6 = 0
            job7 = 0
            job8 = 0
            job9 = 0
            job10 = 0
            job11 = 0
            job12 = 0
            strJob = 'Blue-Collar'
        if Job == 'Entrepreneur':
            job1 = 0
            job2 = 0
            job3 = 1
            job4 = 0
            job5 = 0
            job6 = 0
            job7 = 0
            job8 = 0
            job9 = 0
            job10 = 0
            job11 = 0
            job12 = 0
            strJob = 'Entrepreneur'
        if Job == 'Housemaid':
            job1 = 0
            job2 = 0
            job3 = 0
            job4 = 1
            job5 = 0
            job6 = 0
            job7 = 0
            job8 = 0
            job9 = 0
            job10 = 0
            job11 = 0
            job12 = 0
            strJob = 'Housemaid'
        if Job == 'Management':
            job1 = 0
            job2 = 0
            job3 = 0
            job4 = 0
            job5 = 1
            job6 = 0
            job7 = 0
            job8 = 0
            job9 = 0
            job10 = 0
            job11 = 0
            job12 = 0
            strJob = 'Management'
        if Job == 'Retired':
            job1 = 0
            job2 = 0
            job3 = 0
            job4 = 0
            job5 = 0
            job6 = 1
            job7 = 0
            job8 = 0
            job9 = 0
            job10 = 0
            job11 = 0
            job12 = 0
            strJob = 'Retired'
        if Job == 'Self Employed':
            job1 = 0
            job2 = 0
            job3 = 0
            job4 = 0
            job5 = 0
            job6 = 0
            job7 = 1
            job8 = 0
            job9 = 0
            job10 = 0
            job11 = 0
            job12 = 0
            strJob = 'Self-Employed'
        if Job == 'Services':
            job1 = 0
            job2 = 0
            job3 = 0
            job4 = 0
            job5 = 0
            job6 = 0
            job7 = 0
            job8 = 1
            job9 = 0
            job10 = 0
            job11 = 0
            job12 = 0
            strJob = 'Services'
        if Job == 'Student':
            job1 = 0
            job2 = 0
            job3 = 0
            job4 = 0
            job5 = 0
            job6 = 0
            job7 = 0
            job8 = 0
            job9 = 1
            job10 = 0
            job11 = 0
            job12 = 0
            strJob = 'Student'
        if Job == 'Technician':
            job1 = 0
            job2 = 0
            job3 = 0
            job4 = 0
            job5 = 0
            job6 = 0
            job7 = 0
            job8 = 0
            job9 = 0
            job10 = 1
            job11 = 0
            job12 = 0
            strJob = 'Technician'
        if Job == 'Unemployed':
            job1 = 0
            job2 = 0
            job3 = 0
            job4 = 0
            job5 = 0
            job6 = 0
            job7 = 0
            job8 = 0
            job9 = 0
            job10 = 0
            job11 = 1
            job12 = 0
            strJob = 'Unemployed'
        if Job == 'Other':
            job1 = 0
            job2 = 0
            job3 = 0
            job4 = 0
            job5 = 0
            job6 = 0
            job7 = 0
            job8 = 0
            job9 = 0
            job10 = 0
            job11 = 0
            job12 = 1
            strJob = 'Other'
        
        # Marital
        Marital = input['Marital']
        strMar = ''
        if Marital == 'Divorced':
            div = 1
            mar = 0
            sgl = 0
            strMar = 'Divorced'
        elif Marital == 'Married':
            div = 0
            mar = 1
            sgl = 0
            strMar = 'Married'
        else :
            div = 0
            mar = 0
            sgl = 1
            strMar = 'Single'
        
        # Education
        Education = input['Education']
        strEdu = ''
        if Education == 'Primary':
            pri = 1
            sec = 0
            ter = 0
            unkEdu = 0
            strEdu = 'Primary'
        if Education == 'Secondary':
            pri = 0
            sec = 1
            ter = 0
            unkEdu = 0
            strEdu = 'Secondary'
        if Education == 'Tertiary':
            pri = 0
            sec = 0
            ter = 1
            unkEdu = 0
            strEdu = 'Tertiary'
        if Education == 'Other':
            pri = 0
            sec = 0
            ter = 0
            unkEdu = 1
            strEdu = 'Other'
        
        # Default
        Default = input['Default']
        strDft = ''
        if Default == 'No':
            dftNo = 1
            dftYes = 0
            strDft = 'No'
        else:
            dftNo = 0
            dftYes = 1
            strDft = 'Yes'
                
        # Housing
        Housing = input['Housing']
        strHous = ''
        if Housing == 'No':
            housingNo = 1
            housingYes = 0
            strHous = 'No'
        else:
            housingNo = 0
            housingYes = 1
            strHous = 'Yes'
        
        # Loan
        Loan = input['Loan']
        strLoan = ''
        if Loan == 'No':
            loanNo = 1
            loanYes = 0
            strLoan = 'No'
        else:
            loanNo = 0
            loanYes = 1
            strLoan = 'Yes'
        
        # Contact
        Contact = input['Contact']
        strCon = ''
        if Contact == 'Cellular':
            cel = 1
            tel = 0
            unkCon = 0
            strCon = 'Cellular'
        elif Contact == 'Telephone':
            cel = 0
            tel = 1
            unkCon = 0; strCon = 'Telephone'
        else :
            cel = 0
            tel = 0
            unkCon = 1
            strCon = 'Other'
                
        # Month
        Month = input['Month']
        strMon = ''
        if Month == 'January':
            jan = 1
            feb = 0
            mar = 0
            apr = 0
            may = 0
            jun = 0
            jul = 0
            aug = 0
            sep = 0
            okt = 0
            nov = 0
            dec = 0
            strMon = 'January'
        if Month == 'February':
            jan = 0
            feb = 1
            mar = 0
            apr = 0
            may = 0
            jun = 0
            jul = 0
            aug = 0
            sep = 0
            okt = 0
            nov = 0
            dec = 0
            strMon = 'February'
        if Month == 'March':
            jan = 0
            feb = 0
            mar = 1
            apr = 0
            may = 0
            jun = 0
            jul = 0
            aug = 0
            sep = 0
            okt = 0
            nov = 0
            dec = 0
            strMon = 'March'
        if Month == 'April':
            jan = 0
            feb = 0
            mar = 0
            apr = 1
            may = 0
            jun = 0
            jul = 0
            aug = 0
            sep = 0
            okt = 0
            nov = 0
            dec = 0
            strMon = 'April'
        if Month == 'May':
            jan = 0
            feb = 0
            mar = 0
            apr = 0
            may = 1
            jun = 0
            jul = 0
            aug = 0
            sep = 0
            okt = 0
            nov = 0
            dec = 0
            strMon = 'May'
        if Month == 'June':
            jan = 0
            feb = 0
            mar = 0
            apr = 0
            may = 0
            jun = 1
            jul = 0
            aug = 0
            sep = 0
            okt = 0
            nov = 0
            dec = 0
            strMon = 'June'
        if Month == 'July':
            jan = 0
            feb = 0
            mar = 0
            apr = 0
            may = 0
            jun = 0
            jul = 1
            aug = 0
            sep = 0
            okt = 0
            nov = 0
            dec = 0
            strMon = 'July'
        if Month == 'August':
            jan = 0
            feb = 0
            mar = 0
            apr = 0
            may = 0
            jun = 0
            jul = 0
            aug = 1
            sep = 0
            okt = 0
            nov = 0
            dec = 0
            strMon = 'August'
        if Month == 'September':
            jan = 0
            feb = 0
            mar = 0
            apr = 0
            may = 0
            jun = 0
            jul = 0
            aug = 0
            sep = 1
            okt = 0
            nov = 0
            dec = 0
            strMon = 'September'
        if Month == 'October':
            jan = 0
            feb = 0
            mar = 0
            apr = 0
            may = 0
            jun = 0
            jul = 0
            aug = 0
            sep = 0
            okt = 1
            nov = 0
            dec = 0
            strMon = 'October'
        if Month == 'November':
            jan = 0
            feb = 0
            mar = 0
            apr = 0
            may = 0
            jun = 0
            jul = 0
            aug = 0
            sep = 0
            okt = 0
            nov = 1
            dec = 0
            strMon = 'November'
        if Month == 'December':
            jan = 0
            feb = 0
            mar = 0
            apr = 0
            may = 0
            jun = 0
            jul = 0
            aug = 0
            sep = 0
            okt = 0
            nov = 0
            dec = 1
            strMon = 'December'
        
        feature = [Age, Balance, Duration, Campaign, job1, job2, job3, job4, job5, job6, job7, job8, job9, job10, job11, job12, div, mar, sgl, pri, sec, ter, unkEdu, dftNo, dftYes, housingNo, housingYes, loanNo, loanYes, cel, tel, unkCon, apr, aug, dec, feb, jan, jul, jun, mar, may, nov, okt, sep]
        
        pred= modelrf.predict([feature])
        pred_proba = modelrf.predict_proba([feature])
        
        if pred == 0:
            endresult = f"{round(pred_proba.max()*100)}% {'NOT Accept the Offer'}"
            col = 'red'
        else:
            endresult = f"{round(pred_proba.max()*100)}% {'Customer will Accept the Offer'}"
            col = 'green'
        
        return render_template('result.html', 
            data=input, pred=endresult, Age = Age, Balance = Balance, Duration = Duration, Campaign = Campaign, Job = strJob,
            Marital = strMar, Education = strEdu, Default = strDft, Housing = strHous, Loan = strLoan,
            Contact = strCon, Month = strMon, color = col
        )



if __name__ == "__main__":
    modelrf = joblib.load("modelFix")
    app.run(debug=True, port=4000)