from flask import Flask, render_template, request
app = Flask(__name__)

import marks

@app.route("/")
def marks():
    #print(marks.predt)
    
    return render_template("indes.html")

if __name__ == "__main__":
    app.run(debug=True)