from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Record(object):
    date: datetime
    interest_date: datetime
    account: str
    counterparty: str
    counterparty_name: str
    description: str
    amount: float
    tags: List[str]
    other_info: str
    source: str

    def __init__(self,
                 date: datetime,
                 interest_date: datetime,
                 account: str,
                 counterparty: str,
                 counterparty_name: str,
                 description: str,
                 amount: float,
                 tags: List[str] = None,
                 other_info: str = None,
                 source: str = None):
        self.date = date
        self.interest_date = interest_date
        self.account = account
        self.counterparty = counterparty
        self.counterparty_name = counterparty_name
        self.description = description
        self.amount = amount
        self.tags = tags
        self.other_info = other_info
        self.source = source

    def __str__(self):
        return '{}: {:.2f} to {}'.format(self.date,
                                         self.amount,
                                         self.counterparty)
