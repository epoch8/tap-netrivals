"""netrivals tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_netrivals.streams import (
    netrivalsStream, # -
    PrivateStoresStream, # -
    PrivateProductsStream,
    PublicProductsStream,
    ConnectionsStream,
    PrivateHistoryProductsPriceStream,
    PublicHistoryProductsPriceStream,
    PublicHistoryMarketplaceOffersPriceStream,
    PublicHistoryProductsScoreStream,
    PublicHistoryProductsCommentsStream,
    PublicProductsMarketplaceOffersStream,
    StoresStream,
    ListOfProductsStream,
    ListOfRivalsStream,
    RivalsMarketplacesStream
)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    PrivateStoresStream, # -
    PrivateProductsStream,
    PublicProductsStream,
    ConnectionsStream,
    PrivateHistoryProductsPriceStream,
    PublicHistoryProductsPriceStream,
    PublicHistoryMarketplaceOffersPriceStream,
    PublicHistoryProductsScoreStream, # -
    PublicHistoryProductsCommentsStream, # -
    PublicProductsMarketplaceOffersStream,
    StoresStream,
    ListOfProductsStream,
    ListOfRivalsStream,
    RivalsMarketplacesStream
]


class Tapnetrivals(Tap):
    """netrivals tap class."""
    name = "tap_netrivals"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service"
        ),
        th.Property(
            "username",
            th.StringType,
            required=True,
            description="Username for Standard API"
        ),
        th.Property(
            "password",
            th.StringType,
            required=True,
            description="Password for Standard API"
        ),
        th.Property(
            "api_url",
            th.StringType,
            default=r"https://endpoint.netrivals.com",
            description="The url for the API service"
        ),
        th.Property(
            "date_from",
            th.StringType,
            default=None,
            description="Filter from date (Format Y-m-d)"
        ),
        th.Property(
            "date_to",
            th.StringType,
            default=None,
            description="Filter to date (Format Y-m-d)"
        )
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
