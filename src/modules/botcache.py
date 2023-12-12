import json
from dataconstructor import data_constructor

def log_profit(profit: int | float, _index: str, total: int | float):
    f = open("/botdata/profit-log.json")
    data = json.load(f)
    
    data[_index] = data_constructor.new_profit_index(profit, total)