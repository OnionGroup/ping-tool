from pyping.core import ping
from common.config_reader import read_config
from process_results import process_results

config = read_config("../configuration/config.json")

nicknames = []
for obj in config["hosts"]:
    nicknames.append((obj["nickname"], obj["value"]))

responses = []

for host in config["hosts"]:
    try:
        response = ping(host["value"], config["maxTimeout"], config["packetCount"])
        responses.append(response)
    except Exception as e:
        responses.append(e.message)

process_results(nicknames, responses)
