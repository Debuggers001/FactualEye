from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from bardapi import BardCookies
import re

EXPLAIN_TEMPLATE_LOADING = True
app = Flask(__name__)
else_conditon="Page Not Found"
Cookies_dict={
    "__Secure-1PSID" :"bwjWW4lImVa4JheO3fMi9U0Yc4euhNToIdUzUPuAoiCtztREaK4YdS5GcCPxRUDrC_CYGw.",
    # "__Secure-1PSIDTS":"sidts-CjEB3e41hQSLaG27796sEVIR-DJH2b14tpmSva2r_d6zZomLLE-OElFNRM2Wsj6zixiIEAA",
    "__Secure-1PSIDCC" :"ACA-OxM-xStJEBH2UsJvHfIMBi7pF4Whak6j0CvqjLF7cOxpVcQ-a1_-Iwvc6KKqeyuQakAkP-e4"}

@app.route("/", methods=["GET", "POST"])
def index():
    Reply = ""
    if request.method == "POST":
        names = request.form["names"]        
        with open("data.txt", "w", encoding="utf-8") as f:
            f.writelines("""tell me if the following news or information is fake or real. Give the answer in either 'FAKE' or 'REAL'. Not only tell if the news is real or not but also tell the what is the real news if the news / information is 'FAKE'. Here is the News: """+ str(names))
        with open("data.txt", "r", encoding="utf-8") as f:
            R=f.read()
        R_variable=R

        Bard = BardCookies(cookie_dict=Cookies_dict)
        Reply = Bard.get_answer(R_variable)['content']
        with open("data2.txt", "w", encoding="utf-8") as f:
            f.writelines(Reply)

        def remove_bold(text):
            return re.sub(r'\**', '', text)

        def main():
        
            with open('data2.txt', 'r') as f:
                text = f.read()

            text = remove_bold(text)

            with open('data3.txt', 'w') as f:
                f.write(text)
        main()
        with open("data3.txt", "r", encoding="utf-8") as f:
            read=f.read()
        
        
        return render_template("bard.html", reply=read)    
    else:
        return render_template("index.html", reply=Reply)
    
@app.route('/custom', methods=['GET'])
def index1():
    with open("data3.txt", "r", encoding="utf-8") as f:
        read=f.read()
    with open("custom.html", "w", encoding="utf-8") as f:
        f.writelines(read)

    return render_template("custom.html", reply=read)


@app.route('/update', methods=['POST'])
def update():
    update = request.form["updatedDraft"]

    with open("data3.txt", "w", encoding="utf-8") as f:
        f.writelines(update)
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)

