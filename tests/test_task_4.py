import pytest

import app


@pytest.fixture
def good_events_data():
    class MockedSoupElement:
        def __init__(self, data):
            self.data = data

        @property
        def text(self):
            return self.data

    events_list = [MockedSoupElement("1914 World War 1 starts"), MockedSoupElement("1990 First appearance of python")]
    return events_list


def test_format_events_exists():
    assert "format_events" in dir(app), \
        "The format_events function has not been created in app.py, please create."


def test_format_events_none_input():
    actual_result = app.format_events(None)
    expected_result = []
    assert isinstance(actual_result, list), "The format events function does not return a list, " \
                                            "ensure format_events returns a list irregardless of if its argument " \
                                            "is None or not"
    assert actual_result == expected_result, "The list returned when the argument to format_events is None " \
                                             "is not an empty list. Ensure an  empty list is been returned " \
                                             "when the argument is None"


def test_format_events_empty_events():
    actual_result = app.format_events([])
    expected_result = []
    assert isinstance(actual_result, list), "The format events function does not return a list, " \
                                            "ensure format_events returns a list irregardless of if its argument " \
                                            "is None or not"

    assert actual_result == expected_result, "The list returned when the argument to format_events is an empty " \
                                             "is not an empty list. Ensure you are not appending an item" \
                                             " outside of the for loop"


def test_format_events(good_events_data):
    actual_result = app.format_events(good_events_data)
    excepted_result = [{'year': '1914', 'details': "World War 1 starts"},
                       {'year': '1990', 'details': "First appearance of python"}
                       ]

    assert isinstance(actual_result, list), "The format events function does not return a list, " \
                                            "ensure format_events returns a list irregardless of if its argument " \
                                            "is None or not"

    first_event = actual_result[0]
    assert isinstance(first_event, dict), "Elements in the list returned by format_events " \
                                          f" are {type(first_event)} instead of dictionaries"

    try:
        event_year = first_event['year']
    except KeyError:
        pytest.fail("The dictionaries in the list returned from the format_events function do not have a 'year' key")
    else:
        assert isinstance(event_year, str), "The 'year' key of the returned dictionaries do not map to a string"

    try:
        event_details = first_event['details']
    except KeyError:
        pytest.fail("The dictionaries in the list returned from the format_events "
                    "function do not have a 'details' key")
    else:
        assert isinstance(event_details, str), "The 'details' key of the returned dictionaries do not map to a string"

    assert excepted_result == actual_result, "Something is wrong with the returned list. Check that: \n " \
                                             "i. The dictionaries you are appending to the list have only two keys\n" \
                                             "ii. You did not mistakenly change the variable order of the tuple gotten" \
                                             " from the line event.text.split(" ", 1); year of the event is the " \
                                             "first element of the tuple and details of the event is the second element"
