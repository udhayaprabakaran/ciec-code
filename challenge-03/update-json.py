import json
import pandas as pd
import argparse

parse = argparse.ArgumentParser()

parse.add_argument("--env", "-e")
parse.add_argument("--json", "-j")
parse.add_argument("--csv", "-c")

args = parse.parse_args()

envir = args.env
in_json = args.json
in_csv = args.csv

inp_csv = pd.read_csv(in_csv)

with open(in_json,'r') as fp:
    js = json.load(fp)

ind = lambda i : 1 if(envir=='DEV') else 0

for j in js[envir]:
    if j == 'port':
        js[envir][j] = int(inp_csv[j][ind])
    else:
        js[envir][j] = inp_csv[j][ind]

with open(in_json,'w') as fp:
    json.dump(js, fp, indent=4)            