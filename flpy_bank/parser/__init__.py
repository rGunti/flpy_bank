import csv
from typing import List, Dict

from flpy_bank.objects import Record


class DataParser(object):
    def parse_file(self, file: str) -> List[Record]:
        raise NotImplementedError()


class CsvDataParser(DataParser):
    def __init__(self,
                 delimiter=',',
                 quote='"'):
        self.delimiter = delimiter
        self.quote = quote

    def parse_file(self, file: str) -> List[Record]:
        records: List[Record] = []
        with open(file, 'r') as f:
            reader = csv.reader(f,
                                delimiter=self.delimiter,
                                quotechar=self.quote)

            first_row: List[str] = None
            for row in reader:
                if not first_row:
                    first_row = row
                    continue

                # Parse CSV line to Dict
                item: Dict[str, str] = {}
                for i in range(0, len(first_row)):
                    k = first_row[i]
                    item[k] = row[i]

                # Parse Dict to Record object
                records.append(self.parse_to_record(item))

        return records

    def parse_to_record(self, parsed_item: Dict[str, str]) -> Record:
        raise NotImplementedError()
