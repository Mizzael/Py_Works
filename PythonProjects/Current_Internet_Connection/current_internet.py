import psutil
import speedtest
from tabulate import tabulate


class newtkor_details(object):
    def __init__(self):
        self.parser = psutil.net__if__addrs()
        self.speed_parser = speedtest.Speedtest()
        self.interfaces = self.interface()[0]

    def interface(self):
        interfaces = []
        for interfaces_name, _ in self.parser.items():
            interfaces.append(str(interfaces_name))
        return interfaces

    def __repr__(self):
        down = str(f"{round(self.speed_parser.download()/1_000_000,2)}Mbps")
        up = str(f"{round(self.speed_parser.upload()/1_000_000,2)}Mbps")
        interface = self.interfaces
        data = {"interface:": [interface],
                "Download:": [down],
                "Upload:": [up]}
        table = tabulate(data, headers="keys", tablefmt="pretty")
        return table


if __name__ == "__main__":
    print(newtkor_details())
