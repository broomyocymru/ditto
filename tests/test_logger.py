from ditto.core import logger as l


def test_log_setup():
    test_log = l.setup()
    assert test_log is not None
    assert test_log.mask_values == []


def test_mask_add():
    l.mask("my_password")
    msg = l.log("Test my_password is hidden")
    assert msg.endswith("Test **** is hidden")


def test_mask_add_multiple():
    l.mask("my_username")
    l.mask("my_password")
    msg = l.log("Test my_username and my_password is hidden")
    assert msg.endswith("Test **** and **** is hidden")

