from flpy_bank.parser import DataParser
from flpy_bank.parser.bunq import BunqDataParser
from flpy_bank.parser.sparkasse import SparkasseDataParser

PARSER_REGISTRY = {
    'sparkasse': SparkasseDataParser,
    'bunq': BunqDataParser
}


def construct_parser_from_name(name: str) -> DataParser:
    return PARSER_REGISTRY[name]()
