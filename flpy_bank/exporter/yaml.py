from dataclasses import asdict
from typing import List

import yaml

from flpy_bank.exporter import DataExporter
from flpy_bank.objects import Record


class YamlExporter(DataExporter):
    def __init__(self,
                 file: str):
        self.file = file

    def export_data(self, data: List[Record]):
        dict_data = [asdict(i) for i in data]
        with open(self.file, 'w') as f:
            f.write(yaml.safe_dump(dict_data))
