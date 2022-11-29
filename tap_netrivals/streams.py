"""Stream type classes for tap_netrivals."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_netrivals.client import netrivalsStream
from tap_netrivals.client import netrivalsStandardStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class PrivateStoresStream(netrivalsStream):
    name = "private_stores"
    path = r"/bi/v1/private/stores"
    primary_keys = ["private_store_id"]
    replication_key = None

    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("private_store_id", th.IntegerType, description="private_store_id"),
        th.Property("domain", th.StringType, description="domain"),
        th.Property("domain_alias", th.StringType, description="domain_alias"),
        th.Property("country_code", th.StringType, description="country_code")
    ).to_dict()


class PrivateProductsStream(netrivalsStream):
    name = "private_products"
    path = r"/bi/v1/private/products"
    primary_keys = ["private_product_id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("private_product_id", th.StringType),
        th.Property("store_id", th.IntegerType),
        th.Property("product_id", th.StringType),
        th.Property("country_code", th.StringType),
        th.Property("currency", th.StringType),
        th.Property("title", th.StringType),
        th.Property("brand", th.StringType),
        # th.Property("price", th.IntegerType),
        th.Property("price", th.NumberType),
        # th.Property("price_difference", th.IntegerType),
        th.Property("price_difference", th.NumberType),
        # th.Property("shipping", th.IntegerType),
        th.Property("shipping", th.NumberType),
        # th.Property("stock", th.IntegerType),
        th.Property("stock", th.NumberType),
        # th.Property("stock_quantity", th.IntegerType),
        th.Property("stock_quantity", th.NumberType),
        th.Property("url", th.StringType),
        th.Property("detection_date", th.StringType),
        th.Property("detection_timestamp", th.IntegerType),
        th.Property("updated_date", th.StringType),
        th.Property("updated_timestamp", th.StringType),
        # th.Property("public_product_amount", th.IntegerType),
        th.Property("public_product_amount", th.IntegerType),
        # th.Property("public_product_min_price", th.IntegerType),
        th.Property("public_product_min_price", th.NumberType),
        # th.Property("public_product_max_price", th.IntegerType)
        th.Property("public_product_max_price", th.NumberType)
    ).to_dict()


class PublicProductsStream(netrivalsStream):
    name = "public_products"
    path = r"/bi/v1/public/products"
    primary_keys = ["public_product_id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("public_product_id", th.StringType),
        th.Property("store_id", th.IntegerType),
        th.Property("code", th.StringType),
        th.Property("subcode", th.StringType),
        th.Property("country_code", th.StringType),
        th.Property("currency", th.StringType),
        th.Property("title", th.StringType),
        th.Property("product_variant", th.StringType),
        th.Property("price", th.NumberType),
        th.Property("shipping", th.NumberType),
        th.Property("stock", th.NumberType),
        th.Property("stock_quantity", th.NumberType),
        th.Property("url", th.StringType),
        th.Property("image", th.StringType),
        th.Property("detection_date", th.StringType),
        th.Property("detection_timestamp", th.IntegerType),
        th.Property("update_date", th.StringType),
        th.Property("update_timestamp", th.IntegerType),
        th.Property("last_failure_date", th.StringType),
        th.Property("last_failure_timestamp", th.IntegerType)
    ).to_dict()


class ConnectionsStream(netrivalsStream):
    name = "connections"
    path = r"/bi/v1/connections"
    primary_keys = ["private_product_id", "public_product_id", "connection_timestamp"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("private_product_id", th.StringType),
        th.Property("public_product_id", th.StringType),
        th.Property("connection_date", th.StringType),
        th.Property("connection_timestamp", th.StringType)
    ).to_dict()


class PrivateHistoryProductsPriceStream(netrivalsStream):
    name = "private_history_products_price"
    path = r"/bi/v1/private/history/products-price"
    primary_keys = ["public_product_id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("public_product_id", th.StringType),
        th.Property("date", th.StringType),
        th.Property("price", th.IntegerType),
        th.Property("stock", th.IntegerType),
        th.Property("promotion", th.StringType)
    ).to_dict()


class PublicHistoryProductsPriceStream(netrivalsStream):
    name = "public_history_products_price"
    path = r"/bi/v1/public/history/products-price" # bad API
    primary_keys = ["public_product_id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("public_product_id", th.StringType),
        th.Property("date", th.StringType),
        th.Property("price", th.IntegerType),
        th.Property("stock", th.IntegerType),
        th.Property("promotion", th.StringType),
        th.Property("private_product_id", th.StringType)
    ).to_dict()


class PublicHistoryMarketplaceOffersPriceStream(netrivalsStream):
    name = "public_history_marketplace_offers_price"
    path = r"/bi/v1/public/history/marketplace-offers-price" # bad API
    primary_keys = ["public_product_id", "seller_name", "date"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("public_product_id", th.StringType),
        th.Property("seller_name", th.StringType),
        th.Property("date", th.StringType),
        th.Property("price", th.IntegerType),
        th.Property("stock", th.IntegerType),
        th.Property("offer_num", th.IntegerType),
        th.Property("product_status", th.StringType)
    ).to_dict()


class PublicHistoryProductsScoreStream(netrivalsStream):
    name = "public_history_products_score"
    path = r"/bi/v1/public/history/products-score" # bad API
    primary_keys = ["public_product_id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("public_product_id", th.StringType),
        th.Property("score", th.StringType),
        th.Property("date", th.StringType)
    ).to_dict()


class PublicHistoryProductsCommentsStream(netrivalsStream):
    name = "public_history_products_comments"
    path = r"/bi/v1/public/history/products-comments" # bad API
    primary_keys = ["public_product_id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("public_product_id", th.StringType),
        th.Property("comments", th.StringType),
        th.Property("date", th.StringType)
    ).to_dict()


class PublicProductsMarketplaceOffersStream(netrivalsStream):
    name = "public_products_marketplace_offers"
    path = r"/bi/v1/public/products-marketplace-offers" # bad API
    primary_keys = ["public_product_id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("public_product_id", th.StringType),
        th.Property("position", th.IntegerType),
        th.Property("offer_num", th.IntegerType),
        th.Property("seller_id", th.StringType),
        th.Property("seller_name", th.StringType),
        th.Property("product_status", th.StringType),
        th.Property("price", th.IntegerType),
        th.Property("url", th.StringType),
        th.Property("detection_date", th.StringType),
        th.Property("detection_timestamp", th.IntegerType),
        th.Property("update_date", th.StringType),
        th.Property("update_timestamp", th.IntegerType),
        th.Property("active", th.IntegerType)
    ).to_dict()


class StoresStream(netrivalsStandardStream):
    name = "stores"
    path = r"/v1/stores"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("country", th.StringType),
        th.Property("total_products", th.IntegerType)
    ).to_dict()
