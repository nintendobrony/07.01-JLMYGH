import pytest
import System

username = 'calyam'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
password3 = 'imoutofpasswordnames'
course = 'cloud_computing'
assignment = 'assignment1'
profUser = 'goggins'
profPass = 'augurrox'

#(1) Tests if the program can handle a successful login
def test_login(grading_system):
    grading_system.login(username,password)
    if grading_system.usr.name != 'calyam':
        assert False
    if grading_system.usr.password != '#yeet':
        assert False

#(2) Tests if the program can handle a correct username, pass
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

#(4) test staff assignment creation

#(5) test add student by professor

#(6) test drop student by professor

#(7) test submit assignment for student

#(8) test check if assignment is on time for student

#(9) test check grades for student, fail
def test_check_grade(grading_system):
    grading_system.login(username3,password3)
    grades = grading_system.usr.check_grades(course)
    if 5 not in grades: #done this way so that order doesnt matter
        assert False
    if 3 not in grades:
        assert False

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