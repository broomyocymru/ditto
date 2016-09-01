#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from ditto.core import util


def test_version():
    assert util.ditto_version() == "0.0.1"


def test_ditto_dir():
    path = util.ditto_dir()
    assert path.endswith("ditto")


def test_today_string():
    pattern = re.compile("^[0-9]{4}-[0-1][0-9]-[0-3][0-9]$")
    assert pattern.match(util.today_string())


def test_timestamp():
    pattern = re.compile("^[0-9]{4}-[0-1][0-9]-[0-3][0-9] [0-2][0-9]:[0-6][0-9]:[0-6][0-9]$")
    assert pattern.match(util.timestamp())


def test_remove_ascii_chars_none():
    s = util.remove_non_ascii("xyz")
    assert s == "xyz"


def test_remove_ascii_chars():
    s = util.remove_non_ascii("€xyz€")
    assert s == "xyz"


def test_unique_with_duplicates():
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "monday", "wednesday"]
    unique_days = util.unique(days)
    assert len(list(unique_days)) == 5


def test_unique_without_duplicates():
    days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    unique_days = util.unique(days)
    assert len(list(unique_days)) == 5


def test_unique_without_duplicates_num():
    days = [1, 2, 3, 4, 5]
    unique_days = util.unique(days)
    assert len(list(unique_days)) == 5


def test_unique_with_duplicates_num():
    days = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    unique_days = util.unique(days)
    assert len(list(unique_days)) == 5


def test_read_json_str_valid():
    obj = util.read_json_str("{\"test\":\"pass\"}")
    if "test" in obj:
        if obj["test"] == "pass":
            assert True
            return
    assert False








