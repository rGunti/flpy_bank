from typing import List

from flpy_bank.objects import Record


class DataExporter(object):
    def export_data(self,
                    data: List[Record]):
        raise NotImplementedError()
