#!/usr/bin/env python3
import argparse
import json
import sys

def validate_datalayer(page_dl_path, schema_path):
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    with open(page_dl_path, "r", encoding="utf-8") as f:
        dl = json.load(f)

    issues = []
    events = dl if isinstance(dl, list) else [dl]

    for ev in events:
        ename = ev.get("event")
        if ename in schema:
            req_fields = schema[ename].get("required", [])
            for rf in req_fields:
                if rf not in ev:
                    issues.append(f"Event '{ename}' missing required property: '{rf}'")

    return len(issues) == 0, issues

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--datalayer", required=True)
    p.add_argument("--schema", default="schema/ecommerce_datalayer_schema.json")
    args = p.parse_args()

    ok, issues = validate_datalayer(args.datalayer, args.schema)
    print(f"Data Layer Status: {'PASS' if ok else 'FAIL'}")
    for i in issues:
        print(f"- {i}")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
