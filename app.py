from flask import *
from crud_operation import *
app = Flask(__name__)
@app.route("/")
def openhomepage():
    students=StudentCRUD.get_all_students()
    print(students)
    return render_template("index.html",students=students)
@app.route('/addstudentlink')
def addstudentpage():
    return render_template("student_home.html")
@app.route('/savestudenttodb', methods=['POST','GET'])
def insertstudenttodb():
    if request.method == 'POST':
        try:
            print("i am here")
            id = request.form['id']
            name = request.form['name']
            location = request.form['location']
            print("Location")
            msg = StudentCRUD.create_student(id, name, location)
        except:
            msg="Not inserted successfully"
        finally:
            return render_template('success.html',msg=msg)
@app.route('/sdelete/<id>')
def deletestudent(id):
    try:
        msg=StudentCRUD.delete_student(id)
    except:
        msg="not deleted successfully"
    finally:
        return render_template('success.html',msg=msg)
@app.route('/sedit/<id>')
def seditstudent(id):
    studentdata=StudentCRUD.get_student_by_id(id)
    print(studentdata)
    print("from")
    return render_template("student_edit.html",studentdata=studentdata)

@app.route('/updatestudenttodb', methods=['POST','GET'])
def updatestudenttodb():
    if request.method == 'POST':
        try:
            print("i am here")
            id = request.form['id']
            name = request.form['name']
            location = request.form['location']
            print("Location")
            msg = StudentCRUD.update_student(id, name, location)
        except:
            msg="Not updated successfully"
        finally:
            return render_template('success.html',msg=msg)

if __name__ == '__main__':
    app.run(port=8985)