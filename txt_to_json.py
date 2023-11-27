#!/usr/local/bin/python3

import json
import sys

def convert_key_value_sets_to_json(output):
    data_list = []
    
    sets = output.strip().split('\n\n')

    for set_str in sets:
        key_value_pairs = set_str.strip().split('\n')
        data = {}

        for pair in key_value_pairs:
            if ':' in pair:
                key, value = pair.split(':', 1)
                data[key.strip()] = value.strip()

        data_list.append(data)

    return json.dumps(data_list, indent=2)

if __name__ == "__main__":
    script_output = sys.stdin.read()
    json_output = convert_key_value_sets_to_json(script_output)
    print(json_output)
