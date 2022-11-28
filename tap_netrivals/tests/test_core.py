"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_standard_tap_tests

from tap_netrivals.tap import Tapnetrivals

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    # TODO: Initialize minimal tap config
    # "auth_token": r"$2y$10$y6Uy4TVSC.g0lfHNt8iJMeEBlIorP5R1Otq4P6uXpzbvEwaW86NEm",
    "api_key": r"$2y$10$y6Uy4TVSC.g0lfHNt8iJMeEBlIorP5R1Otq4P6uXpzbvEwaW86NEm",
    "project_ids": ['motul_netrival']
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        Tapnetrivals,
        config=SAMPLE_CONFIG
    )
    for test in tests:
        test()


# TODO: Create additional tests as appropriate for your tap.
