import json
import threading
import re
import pandas as pd
from bson import json_util
from flask import make_response, jsonify

dbEmpDataLock = threading.Lock()

def parse_json(data):
    return json.loads(json_util.dumps(data))

def serverResponse(data, status_code, msg):
    packet = {
        "data": data,
        "description": msg
    }
    r = make_response(jsonify(parse_json(packet)))
    r.status_code = status_code
    return r

def readEmpCSVData(fileObj) -> pd.DataFrame:
    df = pd.read_csv(fileObj,
            sep=',',     
            comment='#',
            header=0,
            skipinitialspace=True,
            skip_blank_lines=True,
            error_bad_lines=True,
            warn_bad_lines=True,
            encoding="utf-8"
            ).sort_index()
    df.dropna(how="all", inplace=True)

    return df