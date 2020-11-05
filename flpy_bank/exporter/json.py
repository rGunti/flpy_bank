import datetime
import json
from dataclasses import asdict
from typing import List, Any

from flpy_bank.exporter import DataExporter
from flpy_bank.objects import Record


class DateEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()


class JsonExporter(DataExporter):
    def __init__(self,
                 file: str):
        self.file = file

    def export_data(self, data: List[Record]):
        dict_data = [asdict(i) for i in data]

        with open(self.file, 'w') as f:
            f.write(json.dumps(dict_data,
                               cls=DateEncoder,
                               indent=2))
