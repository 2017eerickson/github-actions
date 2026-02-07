"""
    Include 
        -test fir correctness 
        -term output
        -and arg using monkey patch
    
 """
 
import calculator 

def test_add():
    assert calculator.calculate(1,2,"add") == 3
def test_subtract():
    assert calculator.calculate(4,2,"subtract") == 2
def test_multiply():
    assert calculator.calculate(2,4,"multiply") == 8
def test_divide():
    assert calculator.calculate(8,2,"divide") == 4

def test_output(capsys):
    calculator.calculate(10,2,"multiply") 
    captured = capsys.readouterr()
    # this above line is to restore original stream of information after interruption
    assert captured.out == "Result: 20\n"

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv",[calculator,"6","2","divide"]) == 3.0 

    