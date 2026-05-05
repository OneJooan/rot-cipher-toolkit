from rot_toolkit.core import rot_process

def test_rot13():
    assert rot_process("Hello", 13) == "Uryyb"

def test_lowercase():
    assert rot_process("abc", 1) == "bcd"

def test_uppercase():
    assert rot_process("ABC", 1) == "BCD"

def test_symbols():
    assert rot_process("Hello!", 13) == "Uryyb!"

def test_negative_shift():
    assert rot_process("Uryyb", -13) == "Hello"

def test_analysis_detects_rot13():
    from rot_toolkit.analysis import analyze_text
    results = analyze_text("Uryyb")
    assert results[0][0] == 13

def test_analysis_detects_symbols():
    from rot_toolkit.analysis import analyze_text
    results = analyze_text("Uryyb!")
    assert results[0][0] == 13
