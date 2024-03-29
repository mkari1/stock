from polygon.rest.models import Exchange
from base import BaseTest


class ExchangesTest(BaseTest):
    def test_get_exchanges(self):
        exchanges = self.c.get_exchanges("stocks")
        expected = [
            Exchange(
                acronym="AMEX",
                asset_class="stocks",
                id=1,
                locale="us",
                mic="XASE",
                name="NYSE American, LLC",
                operating_mic="XNYS",
                participant_id="A",
                type="exchange",
                url="https://www.nyse.com/markets/nyse-american",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=2,
                locale="us",
                mic="XBOS",
                name="Nasdaq OMX BX, Inc.",
                operating_mic="XNAS",
                participant_id="B",
                type="exchange",
                url="https://www.nasdaq.com/solutions/nasdaq-bx-stock-market",
            ),
            Exchange(
                acronym="NSX",
                asset_class="stocks",
                id=3,
                locale="us",
                mic="XCIS",
                name="NYSE National, Inc.",
                operating_mic="XNYS",
                participant_id="C",
                type="exchange",
                url="https://www.nyse.com/markets/nyse-national",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=4,
                locale="us",
                mic="FINY",
                name="FINRA NYSE TRF",
                operating_mic="XNYS",
                participant_id="D",
                type="TRF",
                url="https://www.finra.org",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=4,
                locale="us",
                mic="FINN",
                name="FINRA Nasdaq TRF Carteret",
                operating_mic="FINR",
                participant_id="D",
                type="TRF",
                url="https://www.finra.org",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=4,
                locale="us",
                mic="FINC",
                name="FINRA Nasdaq TRF Chicago",
                operating_mic="FINR",
                participant_id="D",
                type="TRF",
                url="https://www.finra.org",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=4,
                locale="us",
                mic="XADF",
                name="FINRA Alternative Display Facility",
                operating_mic="FINR",
                participant_id="D",
                type="TRF",
                url="https://www.finra.org",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=5,
                locale="us",
                mic=None,
                name="Unlisted Trading Privileges",
                operating_mic="XNAS",
                participant_id="E",
                type="SIP",
                url="https://www.utpplan.com",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=6,
                locale="us",
                mic="XISE",
                name="International Securities Exchange, LLC - Stocks",
                operating_mic="XNAS",
                participant_id="I",
                type="TRF",
                url="https://nasdaq.com/solutions/nasdaq-ise",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=7,
                locale="us",
                mic="EDGA",
                name="Cboe EDGA",
                operating_mic="XCBO",
                participant_id="J",
                type="exchange",
                url="https://www.cboe.com/us/equities",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=8,
                locale="us",
                mic="EDGX",
                name="Cboe EDGX",
                operating_mic="XCBO",
                participant_id="K",
                type="exchange",
                url="https://www.cboe.com/us/equities",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=9,
                locale="us",
                mic="XCHI",
                name="NYSE Chicago, Inc.",
                operating_mic="XNYS",
                participant_id="M",
                type="exchange",
                url="https://www.nyse.com/markets/nyse-chicago",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=10,
                locale="us",
                mic="XNYS",
                name="New York Stock Exchange",
                operating_mic="XNYS",
                participant_id="N",
                type="exchange",
                url="https://www.nyse.com",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=11,
                locale="us",
                mic="ARCX",
                name="NYSE Arca, Inc.",
                operating_mic="XNYS",
                participant_id="P",
                type="exchange",
                url="https://www.nyse.com/markets/nyse-arca",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=12,
                locale="us",
                mic="XNAS",
                name="Nasdaq",
                operating_mic="XNAS",
                participant_id="T",
                type="exchange",
                url="https://www.nasdaq.com",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=13,
                locale="us",
                mic=None,
                name="Consolidated Tape Association",
                operating_mic="XNYS",
                participant_id="S",
                type="SIP",
                url="https://www.nyse.com/data/cta",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=14,
                locale="us",
                mic="LTSE",
                name="Long-Term Stock Exchange",
                operating_mic="LTSE",
                participant_id="L",
                type="exchange",
                url="https://www.ltse.com",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=15,
                locale="us",
                mic="IEXG",
                name="Investors Exchange",
                operating_mic="IEXG",
                participant_id="V",
                type="exchange",
                url="https://www.iextrading.com",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=16,
                locale="us",
                mic="CBSX",
                name="Cboe Stock Exchange",
                operating_mic="XCBO",
                participant_id="W",
                type="TRF",
                url="https://www.cboe.com",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=17,
                locale="us",
                mic="XPHL",
                name="Nasdaq Philadelphia Exchange LLC",
                operating_mic="XNAS",
                participant_id="X",
                type="exchange",
                url="https://www.nasdaq.com/solutions/nasdaq-phlx",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=18,
                locale="us",
                mic="BATY",
                name="Cboe BYX",
                operating_mic="XCBO",
                participant_id="Y",
                type="exchange",
                url="https://www.cboe.com/us/equities",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=19,
                locale="us",
                mic="BATS",
                name="Cboe BZX",
                operating_mic="XCBO",
                participant_id="Z",
                type="exchange",
                url="https://www.cboe.com/us/equities",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=20,
                locale="us",
                mic="EPRL",
                name="MIAX Pearl",
                operating_mic="MIHI",
                participant_id="H",
                type="exchange",
                url="https://www.miaxoptions.com/alerts/pearl-equities",
            ),
            Exchange(
                acronym=None,
                asset_class="stocks",
                id=21,
                locale="us",
                mic="MEMX",
                name="Members Exchange",
                operating_mic="MEMX",
                participant_id="U",
                type="exchange",
                url="https://www.memx.com",
            ),
        ]
        self.assertEqual(exchanges, expected)
