from core.tools import get_time_date, get_file_data, get_folder_data
from unittest.mock import Mock, patch
from core.client import ask_llm
import shutil
import tempfile
from pathlib import Path


@patch("core.client.client")
def test_ask_llm_returns_reply(mock_client):
    fake_response = Mock()
    fake_response.choices = [Mock()]
    fake_response.choices[0].message.content = "fake reply text"
    fake_response.choices[0].message.tool_calls = None

    mock_client.chat.completions.create.return_value = fake_response

    result = ask_llm("hello")
    assert result == "fake reply text"


def test_get_time_date():
    date = get_time_date()
    assert isinstance(date, str)
    assert "at" in date


def test_get_file_data():
    home_temp_dir = Path(tempfile.mkdtemp(dir=Path.home()))
    try:
        test_file = home_temp_dir / "sample.txt"
        test_file.write_text("hello world")
        result = get_file_data(str(test_file))
        assert result == "hello world"
    finally:
        shutil.rmtree(home_temp_dir)


def test_get_file_data_false():
    test_file = get_file_data('core/acame.py')
    assert "Out of Bounds" in test_file


def test_get_folder_data_false():
    test_file = get_folder_data('settings/')
    assert "Out of Bounds" in test_file


def test_get_folder_data():
    test_file = get_folder_data('core/')
    assert "client.py" in test_file
