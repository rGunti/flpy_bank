from dataclasses import dataclass
from typing import List

CONDITION_EXISTS = '*'
CONDITION_EQ = 'eq'
CONDITION_NEQ = 'ne'
CONDITION_CONTAINS = 'contains'
CONDITION_NOT_CONTAINS = 'not_contain'
CONDITION_AND = 'and'
CONDITION_OR = 'or'


@dataclass
class TagRule(object):
    property: str
    condition: str
    value: any
    sub_rules: List[any]  # type: List[TagRule]

    tags: List[str]

    def __init__(self,
                 **entries):
        self.__dict__.update(entries)
        if 'sub_rules' in entries:
            self.sub_rules = [TagRule(**i) for i in entries['sub_rules']]

    def __repr__(self) -> str:
        if self.sub_rules:
            return '{} subrule(s)'.format(len(self.sub_rules))
        return '{} {} {}'.format(self.property,
                                 self.condition,
                                 self.value)
