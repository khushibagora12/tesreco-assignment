from flask import Flask, render_template, request, jsonify
from DB import add_intern, update_intern, delete_data, get_all, assign_mentor ,get_mentors, delete_mentor
from attendenceFile import mark_attendence 

app = Flask(__name__)

@app.route("/")
def display():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/intern_registration', methods=["POST", "GET"])
def register():
    if(request.method == "POST"):
        data = {
            "name" : request.form['name'],
            "email" : request.form['email'],
            "domain" : request.form['domain']
        }
        print(data)
        add_intern(data)
        return render_template('interns.html')
    return render_template('intern_registration.html')


@app.route('/update_record/<int:id>', methods=["POST", "GET"])
def update(id):
    if request.method == "POST":
        data = {
            "name" : request.form['name'],
            "email" : request.form['email'],    
            "domain" : request.form['domain']
        }
        update_intern(id, data)
        return render_template('interns.html')
    return render_template('update_record.html')


@app.route('/delete/<int:id>', methods=["DELETE"])
def delete(id):
    delete_data(id)
    return {"message" : "intern deleted"}


@app.route("/interns")
def get_interns():
    data = get_all()

    return jsonify(data)


@app.route('/view_interns')
def view_interns():
    return render_template('interns.html')


@app.route("/attendance", methods=['POST', 'GET'])
def attendence():
    if request.method == "POST":
        data = {
            "name" : request.form['name'],
            "status" : request.form['status']
        }
        mark_attendence(data)
        return app.redirect('/dashboard')
    return render_template('attendance.html')

@app.route("/assign_mentors", methods=["POST", "GET"])
def assign_mentors():
    if request.method == "POST":
        domain = request.form['domain']
        mentor = request.form['mentor']
        assign_mentor(domain, mentor)
        return app.redirect('/view_mentors')
    return render_template('mentors.html')

@app.route("/getMentors")
def get_all_mentors():
    data = get_mentors()
    return jsonify(data)


@app.route("/view_mentors")
def view_mentors():
    return render_template('view_mentors.html')

@app.route("/delete_mentor/<int:id>", methods=["DELETE"])
def delete_mentor_id(id):
    delete_mentor(id)
    return {"message" : "mentor deleted"}

if __name__ == "__main__":
    app.run(debug=True)
