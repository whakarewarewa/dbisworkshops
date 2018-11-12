
"""словники що описують сутності HOMEWORK(ENGLISH) та USER(TEACHER1)""""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

user_dictionary = {
     "pass_id": "PA330871",
     "user_name": "Teacher1",
     "user_role": "teacher",
}

hw_dictionary = {
     "hw_discipline_name": "English",
     "hw_date": "01/11/2018",
     "hw_description": "Write a motivation letter",
}


@app.route('/api/<action>', methods=['GET'])
def apiget(action):

    if action == "user":
        return render_template("user.html", user=user_dictionary)

    elif action == "homework":
        return render_template("homework.html", homework=hw_dictionary)

    elif action == "all":
        return render_template("all.html", user=user_dictionary, homework=hw_dictionary)

    else:
        return render_template("404.html", action_value=action, link=["user","homework"])

@app.route('/api', methods=['POST'])

def apipost():
    if request.form["action"] == "user_update":
        user_dictionary["pass_id"] = request.form["pass_id"]
        user_dictionary["user_name"] = request.form["first_name"]
        user_dictionary["user_role"] = request.form["role"]
    if request.form["action"] == "hw_update":
        hw_dictionary["hw_discipline_name"] = request.form["hw_discipline_name"]
        hw_dictionary["hw_date"] = request.form["hw_date"]
        hw_dictionary["hw_description"] = request.form["hw_description"]

    return redirect(url_for('apiget', action="all"))



if __name__ == '__main__':
    app.run()
