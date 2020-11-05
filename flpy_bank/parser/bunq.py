from datetime import datetime
from typing import List, Dict

from flpy_bank.objects import Record
from flpy_bank.parser import CsvDataParser


def parse_bunq_date(input: str) -> datetime:
    return datetime.strptime(input, '%Y-%m-%d')


class BunqDataParser(CsvDataParser):
    def __init__(self):
        super().__init__(';')

    def parse_to_record(self, parsed_item: Dict[str, str]) -> Record:
        return Record(date=parse_bunq_date(parsed_item['Date']),
                      interest_date=parse_bunq_date(parsed_item['Interest Date']),
                      amount=float(parsed_item['Amount']),
                      account=parsed_item['Account'],
                      counterparty=parsed_item['Counterparty'],
                      counterparty_name=parsed_item['Name'],
                      description=parsed_item['Description'],
                      source='bunq')
