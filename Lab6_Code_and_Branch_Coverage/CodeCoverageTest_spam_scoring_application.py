
from spam_scoring import score_message, classify, filter_inbox, inbox_status


def test_plain_message_scores_zero():
    assert score_message("hello there", False, 0) == 0


def test_spam_word():
    assert score_message("free", False, 0) == 2


def test_uppercase_word():
    assert score_message("HELLO", False, 0) == 1


def test_many_links():
    assert score_message("hello", False, 4) == 4


def test_one_link():
    assert score_message("hello", False, 1) == 1


def test_known_sender():
    assert score_message("free winner", True, 0) == 1


def test_known_sender_zero_floor():
    assert score_message("hello", True, 0) == 0


def test_low_score_is_clean():
    assert classify(1) == "clean"


def test_suspicious_classification():
    assert classify(4) == "suspicious"


def test_spam_classification():
    assert classify(8) == "spam"


def test_empty_inbox():
    assert filter_inbox([]) == {
        "spam": 0, "suspicious": 0, "clean": 0
    }


def test_filter_inbox_messages():
    messages = [
        ("free winner urgent cash", False, 0),
        ("free winner", False, 0),
        ("hello", False, 0),
    ]
    assert filter_inbox(messages) == {
        "spam": 1, "suspicious": 1, "clean": 1
    }


def test_empty_inbox_status():
    assert inbox_status({
        "spam": 0, "suspicious": 0, "clean": 0
    }) == "empty"


def test_flooded_inbox():
    assert inbox_status({
        "spam": 6, "suspicious": 2, "clean": 2
    }) == "flooded"


def test_noisy_inbox():
    assert inbox_status({
        "spam": 3, "suspicious": 2, "clean": 5
    }) == "noisy"


def test_healthy_inbox():
    assert inbox_status({
        "spam": 1, "suspicious": 2, "clean": 7
    }) == "healthy"
