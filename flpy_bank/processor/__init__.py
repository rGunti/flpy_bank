from typing import List

from flpy_bank.objects import Record


class RecordProcessor(object):
    def process(self,
                records: List[Record]):
        for record in records:
            self._process_record(record)

    def _process_record(self,
                        record: Record):
        raise NotImplementedError()
