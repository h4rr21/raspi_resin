from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/google")
def printFileG():
    with open("google.txt", "r") as f:
        content = f.read()
    return render_template("template.html", content=content)

@app.route("/facebook")
def printFileF():
    with open("facebook.txt", "r") as f:
        content = f.read()
    return render_template("template.html", content=content)    
 
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)