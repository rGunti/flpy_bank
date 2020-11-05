from dataclasses import asdict
from typing import List, Any, Dict

import yaml

from flpy_bank import env
from flpy_bank.objects import Record
from flpy_bank.objects.tagging import TagRule, CONDITION_EXISTS, CONDITION_EQ, CONDITION_NEQ, CONDITION_CONTAINS, \
    CONDITION_NOT_CONTAINS, CONDITION_AND, CONDITION_OR
from flpy_bank.processor import RecordProcessor


def read_tag_rules_from_file(path: str) -> List[TagRule]:
    try:
        with open(path, 'r') as f:
            r: List[Dict[str, Any]] = yaml.safe_load(f)
            return [TagRule(**i) for i in r]
    except FileNotFoundError:
        raise RuntimeError('Couldn\'t find tag rule file at {}'.format(path))


class TagProcessor(RecordProcessor):
    def __init__(self):
        self.rules = read_tag_rules_from_file(env.RUNTIME_ARGS.tag_rules)

    def _process_record(self, record: Record):
        record_dict = asdict(record)
        for rule in self.rules:
            if TagProcessor._record_matches_rule(record_dict, rule):
                if not record.tags:
                    record.tags = []
                for tag in rule.tags:
                    if tag not in record.tags:
                        record.tags.append(tag)

    @staticmethod
    def _record_matches_rule(record_dict: Dict[str, Any], rule: TagRule) -> bool:
        if rule.condition == CONDITION_EXISTS:
            return rule.property in record_dict and record_dict[rule.property]
        if rule.condition == CONDITION_EQ:
            return rule.property in record_dict \
                   and record_dict[rule.property] == rule.value
        if rule.condition == CONDITION_NEQ:
            return rule.property not in record_dict \
                   or record_dict[rule.property] != rule.value
        if rule.condition == CONDITION_CONTAINS:
            return rule.property in record_dict \
                   and str(rule.value).lower() in str(record_dict[rule.property]).lower()
        if rule.condition == CONDITION_NOT_CONTAINS:
            return rule.property not in record_dict \
                or str(rule.value).lower() not in str(record_dict[rule.property]).lower()
        if rule.condition == CONDITION_AND:
            for sub_rule in rule.sub_rules:
                if not TagProcessor._record_matches_rule(record_dict, sub_rule):
                    return False
            return True
        if rule.condition == CONDITION_OR:
            for sub_rule in rule.sub_rules:
                if TagProcessor._record_matches_rule(record_dict, sub_rule):
                    return True
            return False
