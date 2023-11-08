from string_processor import StringProcessor
sp = StringProcessor()


def test_process_string():
    """Test for process_string function"""
    assert sp.process_string("ab") == ""
    assert sp.process_string("ab*") == "b"
    assert sp.process_string("ab^") == "ba"
    assert sp.process_string("^") == ""


test_process_string()
