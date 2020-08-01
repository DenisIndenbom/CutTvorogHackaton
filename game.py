from flask import Flask, request, redirect, url_for, make_response
from flask import render_template


app = Flask( __name__ )

app.config['SECRET_KEY'] = "EalTCIxT2UpQBkX6z5u4"


@app.route("/")
def main():
    if  not request.cookies.get("longhair"):
        res = make_response("Setting a cookie")
        res.set_cookie('longhair', "0", max_age=60 * 60 * 24 * 365 * 100)
    with open('longhair.txt', "r") as file:
        maxlonghair = int(file.read())

    meters = request.cookies.get("longhairf")
    if meters != None:
        meters = int(meters)
    else:
        meters=0
        res = make_response("Setting a cookie")
        res.set_cookie('Cut', str(meters), max_age=60 * 60 * 24)
    return render_template("CutTvorog.html",longhair=meters,maxlonghair=maxlonghair)


@app.route("/cut")
def cut():
    maxlonghair = 0
    longhair = 0
    if request.cookies.get("longhair") != None:
        longhair = request.cookies.get("longhair")
    else:
        res = make_response("Setting a cookie")
        res.set_cookie('longhair', str(0), max_age=60 * 60 * 24)
    with open('longhair.txt', "r") as file:
        maxlonghair = int(file.read())
    if longhair >= maxlonghair:
        with open('longhair.txt', "w") as file:
            file.write(str(longhair))

    res = make_response("Setting a cookie")
    res.set_cookie('longhair', str(longhair), max_age=60 * 60 * 24)

    return redirect("/")


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True,port=5000)