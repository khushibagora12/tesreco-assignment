from flask import Flask, render_template, request, jsonify
from DB import add_intern, update_intern, delete_data, get_all, assign_mentor ,get_mentors, delete_mentor
from attendenceFile import mark_attendence 

app = Flask(__name__)

'''
This is the default route
display -> home page
'''
@app.route("/")
def display():
    return render_template('home.html')

'''
Contains details about TESRECO
display -> about page
'''
@app.route('/about')
def about():
    return render_template('about.html')

'''
Allow us to move to different routes
display -> dashboard page
'''
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

'''
Allow interns to registered
display -> 
    GET - intern registration form 
    POST - redirect to the interns page
'''
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

'''
Allow updation in intern's information
display -> 
    GET - intern updation form 
    POST - redirect to the interns page
'''
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

'''
Delete an intern with given id
return -> message intern deleted
'''
@app.route('/delete/<int:id>', methods=["DELETE"])
def delete(id):
    delete_data(id)
    return {"message" : "intern deleted"}

'''
return -> all interns information in json format
'''
@app.route("/interns")
def get_interns():
    data = get_all()

    return jsonify(data)

'''
show details of all interns
display -> interns page
'''
@app.route('/view_interns')
def view_interns():
    return render_template('interns.html')

'''
Takes name and status and marks the attendance
display -> 
    GET - mark_attendance page
    POST - redirects to the dashboard
'''
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

'''
Assign some domain to the given mentor
display -> 
    GET - mentor assignment form
    POST - redirect to the view_mentors page
'''
@app.route("/assign_mentors", methods=["POST", "GET"])
def assign_mentors():
    if request.method == "POST":
        domain = request.form['domain']
        mentor = request.form['mentor']
        assign_mentor(domain, mentor)
        return app.redirect('/view_mentors')
    return render_template('mentors.html')

'''
return -> all mentors information in json format
'''
@app.route("/getMentors")
def get_all_mentors():
    data = get_mentors()
    return jsonify(data)

'''
show details of all mentors
display -> view_mentors page
'''
@app.route("/view_mentors")
def view_mentors():
    return render_template('view_mentors.html')

'''
deletes a mentor with the given id
'''
@app.route("/delete_mentor/<int:id>", methods=["DELETE"])
def delete_mentor_id(id):
    delete_mentor(id)
    return {"message" : "mentor deleted"}

if __name__ == "__main__":
    app.run(debug=True)
