import argparse
import json


# convert a zap report to this format:
# {
#     "vulnerabilities": [
#         {
#             "name": "Name of first vulnerability",
#             "count": 2
#         },
#         {
#             "name": "Name of second vulnerability",
#             "count": 4
#         }
#     ]
# }
def convert_report(filename_in: str, filename_out: str) -> None:
    with open(filename_in, mode='r') as f:
        report_in = json.load(f)

    report_out = {
        'vulnerabilities': []
    }

    alerts = report_in['site'][0]['alerts']
    for vuln in alerts:
        report_out['vulnerabilities'].append(
            {
                'name': vuln['name'],
                'count': int(vuln['count'])
            }
        )

    with open(filename_out, mode='w') as f:
        json.dump(report_out, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a zap report to the desired report format')

    parser.add_argument(
        '-i', '--input', dest='input', type=str, help='path to input zap report', required=True)
    parser.add_argument(
        '-o', '--output', dest='output', type=str, help='path to output result report', required=True)

    args = parser.parse_args()

    convert_report(args.input, args.output)
