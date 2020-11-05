from datetime import datetime
from typing import Dict

from flpy_bank.objects import Record
from flpy_bank.parser import CsvDataParser


def parse_sparkasse_time(input: str) -> datetime:
    return datetime.strptime(input, '%d.%m.%y')


def parse_sparkasse_amount(input: str) -> float:
    return float(input.replace(',', '.'))


class SparkasseDataParser(CsvDataParser):
    def __init__(self):
        super().__init__(delimiter=';')

    def parse_to_record(self, parsed_item: Dict[str, str]) -> Record:
        return Record(account=parsed_item['Auftragskonto'],
                      date=parse_sparkasse_time(parsed_item['Buchungstag']),
                      interest_date=parse_sparkasse_time(parsed_item['Valutadatum']),
                      description=parsed_item['Verwendungszweck'],
                      counterparty=parsed_item['Kontonummer/IBAN'],
                      counterparty_name=parsed_item['Beguenstigter/Zahlungspflichtiger'],
                      amount=parse_sparkasse_amount(parsed_item['Betrag']),
                      other_info='Kundenref: {}'.format(parsed_item['Kundenreferenz (End-to-End)']) \
                          if parsed_item['Kundenreferenz (End-to-End)'] \
                          else None,
                      source='Sparkasse')
