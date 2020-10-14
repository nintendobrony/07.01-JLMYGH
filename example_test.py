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

#(4) 

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem