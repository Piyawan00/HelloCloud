from tkinter.tix import INTEGER
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, CHAR, VARCHAR, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///user.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()

class Students(Base):
    __tablename__ = 'Student'
    student_id = Column(CHAR(13), primary_key=True, nullable=False)
    f_name = Column(VARCHAR(30), nullable=False)
    l_name = Column(VARCHAR(30), nullable=False)
    e_mail = Column(VARCHAR(50), nullable=False)

class Registrations(Base):
    __tablename__ = 'Registration'
    student_id = Column(CHAR(13), primary_key=True, nullable=False)
    subject_id = Column(VARCHAR(15),primary_key=True,nullable=False)
    year = Column(CHAR(4), nullable=False)
    semester = Column(CHAR(1), nullable=False)
    grade = Column(CHAR(2), nullable=False)

class Teachers(Base):
    __tablename__ = 'Teacher'
    teacher_id = Column(CHAR(3), primary_key=True, nullable=False)
    f_name = Column(VARCHAR(30), nullable=False)
    l_name = Column(VARCHAR(30), nullable=False)
    e_mail = Column(VARCHAR(50), nullable=False)

class Subjects(Base):
    __tablename__ = 'Subject'
    subject_id = Column(VARCHAR(15), primary_key=True, nullable=False)
    subject_name = Column(VARCHAR(50), nullable=False)
    creadit = Column(Integer(), nullable=False)
    teacher_id = Column(VARCHAR(50), nullable=False)


P1 = Students(student_id='6406022610058',f_name='Piyawan',l_name='Nimpraprut',e_mail='s6406022610058@email.kmutnb.ac.th')
Rg1   = Registrations(student_id='6406022610058',subject_id='060233113', year='2565', semester='1', grade='C')
Rg11  = Registrations(student_id='6406022610058',subject_id='060233201', year='2565', semester='1', grade='B')
Rg111 = Registrations(student_id='6406022610058',subject_id='060233112', year='2565', semester='1', grade='A')

M2    = Students(student_id='6406022620061',f_name='Mathawee',l_name='Robkhob',e_mail='s6406022620061@email.kmutnb.ac.th')
Rg2   = Registrations(student_id='6406022620061', subject_id='060233113', year='2565', semester='1', grade='A')
Rg22  = Registrations(student_id='6406022620061', subject_id='060233201', year='2565', semester='1', grade='C')
Rg222  = Registrations(student_id='6406022620061',subject_id='060233112', year='2565', semester='1', grade='B')

K3    = Students(student_id='6406022630016',f_name='Kamonwan',l_name='Janmanee',e_mail='s6406022630016@email.kmutnb.ac.th')
Rg3   = Registrations(student_id='6406022630016',subject_id='060233113', year='2565', semester='1', grade='B')
Rg33  = Registrations(student_id='6406022630016',subject_id='060233201', year='2565', semester='1', grade='A')
Rg333 = Registrations(student_id='6406022630016',subject_id='060233112', year='2565', semester='1', grade='C')

Tc1 = Teachers(teacher_id='AMK',f_name='Anirach',     l_name= 'Mingkwan',         e_mail='Anirach@email.kmutnb.ac.th')
Tc2 = Teachers(teacher_id='WKN',f_name='Watcharachai',l_name= 'Kongsiriwattana',  e_mail='Watcharachai@email.kmutnb.ac.th')
Tc3 = Teachers(teacher_id='STS',f_name='Sarayoot',    l_name= 'Tanessakulwattana',e_mail='Sarayoot@email.kmutnb.ac.th')


Sj1 = Subjects(subject_id='060233113',subject_name='ADVANCED COMPUTER PROGRAMMIN', creadit=3, teacher_id='AMK')
Sj2 = Subjects(subject_id='060233201',subject_name='NETWORK ENGINEERING LABORATO', creadit=3, teacher_id='WKN')
Sj3 = Subjects(subject_id='060233112',subject_name='DATA ENGINEERING',             creadit=3,teacher_id='STS')


Base.metadata.create_all(engine)

list = [P1,Rg1,Rg11,Rg111, M2,Rg2,Rg22,Rg222, K3,Rg3,Rg33,Rg333, Tc1,Tc2,Tc3, Sj1,Sj2,Sj3]
for x in list: 
    session.add(x)
session.commit()


