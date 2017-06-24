from pyping.core import ping
from multiprocessing import Pool
from common.config_reader import read_config
from process_results import process_results

config = read_config("../configuration/config.json")
hosts = config["hosts"]


def ping_host(host):
    try:
        response = ping(host["value"], config["maxTimeout"], config["packetCount"])
        return response
    except Exception as e:
        return e.message


if __name__ == '__main__':
    nicknames = [(obj["nickname"], obj["value"]) for obj in hosts]

    pool = Pool(min(len(hosts), 4))
    responses = pool.map(ping_host, hosts)

    process_results(nicknames, responses)
