from core.tools import get_time_date, get_file_data, get_folder_data


def test_get_time_date():
    date = get_time_date()
    assert isinstance(date, str)
    assert "at" in date


def test_get_file_data(tmp_path):
    test_file = tmp_path / "sample.txt"
    test_file.write_text("hello world")
    result = get_file_data(str(test_file))
    assert result == "hello world"


def test_get_file_data_false():
    test_file = get_file_data('core/acame.py')
    assert "Out of Bounds" in test_file


def test_get_folder_data_false():
    test_file = get_folder_data('settings/')
    assert "Out of Bounds" in test_file


def test_get_folder_data():
    test_file = get_folder_data('core/')
    assert "client.py" in test_file
