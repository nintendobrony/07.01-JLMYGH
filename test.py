import pytest
import System
import json

username = 'calyam'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
password3 = 'imoutofpasswordnames'
course = 'cloud_computing'
assignment = 'assignment1'
profUser = 'saab'
profPass = 'boomr345'

#(1) Tests if the program can handle a successful login, pass
def test_login(grading_system):
    grading_system.login(username,password)
    if grading_system.usr.name != 'calyam':
        assert False
    if grading_system.usr.password != '#yeet':
        assert False

#(2) Tests if the program can handle a login, pass
def test_check_password(grading_system):
    test = grading_system.check_password(username,password)
    test2 = grading_system.check_password(username,'#yeet')
    test3 = grading_system.check_password(username,'#YEET')
    if test == test3 or test2 == test3:
        assert False
    if test != test2:
        assert False

#(3) Tests if a grade can be changed, fail
def test_change_grade(grading_system):
    grading_system.login(username,password)
    grading_system.usr.change_grade(username3,course,assignment,100)
    assert grading_system.users[username3]['courses'][course][assignment]['grade'] == 100

#(4) test staff assignment creation, pass
def test_create_assignment(grading_system):
    grading_system.login(username,password)
    grading_system.usr.create_assignment('testAssignment', "11/11/20",course)
    f = open('Data/courses.json', "r") #read the json to see if the method correctly added assignment
    courses_doc = f.readline()
    f.close()
    assert -1 != courses_doc.rfind('"cloud_computing": {"assignments": {"assignment1": {"due_date": "1/3/20"}, "assignment2": {"due_date": "2/3/20"}, "testAssignment": {"due_date": "11/11/20"}}')
    
#(5) test add student by professor, fail
def test_add_student(grading_system):
    grading_system.login(profUser,profPass)
    grading_system.usr.add_student(username,"comp_sci")
    f = open('Data/users.json', "r") #read the json to see if the method correctly added class
    users_doc = f.readline()
    f.close()
    assert -1 != users_doc.rfind('"yted91": {"courses": {"cloud_computing": {"assignment1": {"grade": 0, "submission_date": "1/7/20", "submission": "Blah Blah Blah", "ontime": false}, "assignment2": {"Grade": 5, "Submission Data": "2/7/20", "Submission": "Blah2 Blah2 Blah2", "ontime": false}}, "software_engineering": {"assignment1": {"grade": 43, "submission_date": "1/5/20", "submission": "Blah Blah Blah", "ontime": false}, "assignment2": {"grade": 22, "submission_date": "2/5/20", "submission": "Blah2 Blah2 Blah2", "ontime": false}},"comp_sci"')


#(6) test drop student by professor, pass
def test_drop_student(grading_system):
    grading_system.login(username,password)
    grading_system.usr.drop_student(username3,course)
    f = open('Data/users.json', "r") #read the json to see if the method correctly dropped student
    users_doc = f.readline()
    f.close()
    assert -1 != users_doc.rfind('"yted91": {"courses": {"software_engineering": {"assignment1": {"grade": 43, "submission_date": "1/5/20", "submission": "Blah Blah Blah", "ontime": false}, "assignment2": {"grade": 22, "submission_date": "2/5/20", "submission": "Blah2 Blah2 Blah2", "ontime": false}}}, "password": "imoutofpasswordnames"')

#(7) test submit assignment for student, fail
def test_student_submit_assignment(grading_system):
    grading_system.login(username3,password3)
    grading_system.usr.submit_assignment(course,'assignment1','hi','12/12/20')

#(8) test check if assignment is on time for student, fail
def test_student_on_time(grading_system):
    grading_system.login(username3,password3)
    assert False == grading_system.usr.check_ontime("1/1/1999","1/1/2000")
    assert True == grading_system.usr.check_ontime("1/1/2000","1/1/1999")
    assert True == grading_system.usr.check_ontime("1/1/2000","1/1/2000")

#(9) test check grades for student, fail 
def test_check_grade(grading_system):
    grading_system.login(username3,password3)
    grades = grading_system.usr.check_grades(course)
    assert ['assignment2',5] in grades #done this way so that order doesnt matter
    assert ['assignment1',0] in grades 

#(10) test view assignments for student

#(11) test ability for student to directly message professor

#(12) test for student ability to drop a class

#(13) test for staff ability to email professor

#(14) test for student ability to delete submission

#(15) test for student ability to comment on submission

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem