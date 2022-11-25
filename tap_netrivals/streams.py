"""Stream type classes for tap_netrivals."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_netrivals.client import netrivalsStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


# class UsersStream(netrivalsStream):
class PrivateStoresStream(netrivalsStream):
    """Define custom stream."""
    # name = "users"
    name = "private_stores"
    # path = "/users"
    path = r"/bi/v1/private/stores"
    # path = r"https://endpoint.netrivals.com/bi/v1/private/stores"
    # path = "/bi/v1/private/stores?api_key=$2y$10$y6Uy4TVSC.g0lfHNt8iJMeEBlIorP5R1Otq4P6uXpzbvEwaW86NEm"
    # primary_keys = ["id"]
    primary_keys = ["private_store_id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property(
            # "id",
            "private_store_id",
            # th.StringType,
            th.IntegerType,
            # description="The user's system ID"
            description="private_store_id"
        ),
        th.Property(
            "domain",
            th.StringType,
            description="domain"
        ),
        th.Property(
            "domain_alias",
            th.StringType,
            description="domain_alias"
        ),
        th.Property(
            "country_code",
            th.StringType,
            description="country_code"
        )
        # th.Property(
        #     "age",
        #     th.IntegerType,
        #     description="The user's age in years"
        # ),
        # th.Property(
        #     "email",
        #     th.StringType,
        #     description="The user's email address"
        # ),
        # th.Property("street", th.StringType),
        # th.Property("city", th.StringType),
        # th.Property(
        #     "state",
        #     th.StringType,
        #     description="State name in ISO 3166-2 format"
        # ),
        # th.Property("zip", th.StringType),
    ).to_dict()


# class UsersStream(netrivalsStream):
#     """Define custom stream."""
#     name = "users"
#     path = "/users"
#     primary_keys = ["id"]
#     replication_key = None
#     # Optionally, you may also use `schema_filepath` in place of `schema`:
#     # schema_filepath = SCHEMAS_DIR / "users.json"
#     schema = th.PropertiesList(
#         th.Property("name", th.StringType),
#         th.Property(
#             "id",
#             th.StringType,
#             description="The user's system ID"
#         ),
#         th.Property(
#             "age",
#             th.IntegerType,
#             description="The user's age in years"
#         ),
#         th.Property(
#             "email",
#             th.StringType,
#             description="The user's email address"
#         ),
#         th.Property("street", th.StringType),
#         th.Property("city", th.StringType),
#         th.Property(
#             "state",
#             th.StringType,
#             description="State name in ISO 3166-2 format"
#         ),
#         th.Property("zip", th.StringType),
#     ).to_dict()


# class GroupsStream(netrivalsStream):
#     """Define custom stream."""
#     name = "groups"
#     path = "/groups"
#     primary_keys = ["id"]
#     replication_key = "modified"
#     schema = th.PropertiesList(
#         th.Property("name", th.StringType),
#         th.Property("id", th.StringType),
#         th.Property("modified", th.DateTimeType),
#     ).to_dict()
