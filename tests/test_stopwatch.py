#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ditto.core import stopwatch


def test_duration():
    watch = stopwatch.DittoStopwatch()
    watch.start()
    assert watch.start_time is not None
    watch.stop()
    assert watch.end_time is not None
    duration = watch.duration()
    assert duration is not None


def test_split():
    watch = stopwatch.DittoStopwatch()
    watch.start()
    assert watch.start_time is not None
    split = watch.split()
    assert split is not None




