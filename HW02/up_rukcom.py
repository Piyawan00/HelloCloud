from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from up_rukcom import Students,Teachers,Registrations,Subjects,session

app = Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:TMQkmy54914@node36956-piyawan.proen.app.ruk-com.cloud:5432/rukcloud'
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False

db = SQLAlchemy(app)
@app.route('/')
def index():
    result = session.query(Students.student_id,Students.sf_name,Students.sl_name,Registrations.subject_id,Subjects.subject_name,Registrations.grade,Teachers.teacher_id,Teachers.tf_name,Teachers.tl_name).join(Registrations,Students.student_id == Registrations.student_id).join(Subjects,Registrations.subject_id == Subjects.subject_id).join(Teachers,Subjects.teacher_id == Teachers.teacher_id).all()
    return render_template('up_web.html',result = result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

    
