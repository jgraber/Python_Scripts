#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: test_example
.. moduleauthor:: Johnny Graber <JG@JGraber.ch>

This is a sample test module.
"""

import pytest

"""
This is just an example test suite.  It will check the current project version
numbers against the original version numbers and will start failing as soon as
the current version numbers change.
"""


def test_import_getVersions_originalVersions():
    """
    Arrange: Load the primary module.
    Act: Retrieve the versions.
    Assert: Versions match the version numbers at the time of project creation.
    """
    assert (
        # fmt: off
        # '0.0.1' == gpsinfo.__version__,
        # fmt: on
        "This test is expected to fail when the version increments. "
        "It is here only as an example and you can remove it."
    )
