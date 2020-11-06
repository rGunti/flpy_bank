# flpy_bank
`flpy_bank` aims to convert bank statements from different formats to a common
object format for further analysis.

`flpy_bank` is written in Python 3.9 and currently doesn't have a lot of dependencies.

## Command Line Arguments
```
usage: __main__.py [-h] -i INPUT -p {sparkasse,bunq} [-f {json,yaml}] -o OUTPUT [-P {tag} [{tag} ...]] [--tagrules TAG_RULES]

BankStatementParser

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT              A file to process
  -p {sparkasse,bunq}   The name for a supported file parser
  -f {json,yaml}        The name of a supported output format
  -o OUTPUT             A path to the output file
  -P {tag} [{tag} ...]  One or more processors to run before exporting the data
  --tagrules TAG_RULES  A YAML file containing tagging rules

```

## Supported input files
This project currently support exports from the following institutes:

| Name | Institute (Country) | Format |
|:----:|:----:|:----:|
| `sparkasse` | Sparkasse (Germany)     | CSV-CAMT |
| `bunq`      | bunq B.V. (Netherlands) | Auto Export Statement (CSV, `;` delimiter) |

_More input formats are not planned but can be easily added via Pull Request._

## Supported output files
`flpy_bank` generally outputs data using its own object structure which contains
the following properties:

| Name                | Type       | Description |
|:-------------------:|:----------:|:-----------:|
| `date`              | `date`     | Date of record |
| `interest_date`     | `date`     | Booking date |
| `account`           | `string`   | Account (IBAN) |
| `counterparty`      | `string`   | Counterparty of booking (IBAN) |
| `counterparty_name` | `string`   | Name of counterparty |
| `description`       | `string`   | Usually also known as "Reference" |
| `amount`            | `number`   | Amount |
| `tags`              | `string[]` | an optional list of tags for the record |
| `other_info`        | `string`   | additional, unstructured information |
| `source`            | `string`   | Data source identifier |

This object can then be exported to one of the following formats:
- JSON
- YAML
- ~~CSV~~ (not yet implemented)

## Processing
`flpy_bank` is also intended for post-processing of these bank records.
By implementing data processors, the produced data can be enhanced as needed.
Currently, the following processors exist:

- `tag`: Adds tags to records based on given conditions.
  These conditions can be provided in a YAML file. See below for reference.

### `tag` processor
Adds tags to records based on given conditions. These conditions can be provided 
in a YAML file. The YAML file can either be provided via command line arguments
or will automatically be picked up when placed in the current working directory
and named `rules.yaml`.

```yaml
# When source = "Sparkasse", add a tag "Sparkasse"
- property: source
  condition: eq
  value: Sparkasse
  tags:
    - Sparkasse

# When counterparty_name contains "RCI" and description contains "renault"
# add a tag "Renault Leasing"
- condition: and
  sub_rules:
    - property: counterparty_name
      condition: contains
      value: RCI
    - property: description
      condition: contains
      value: renault
  tags:
    - Renault Leasing
```

## Planned features
- [ ] CSV export
- [ ] multi-file input (load multiple files and collect in a single output file)

## License
This project is licensed under the **MIT license**. See [LICENSE.md](LICENSE.md) for
more information.
