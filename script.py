#!/usr/bin/env python

import json
import urllib
import time
import winsound

desired_servers = ['143casys11', '143casys10', '143casys13', '161casys4']
desired_zones = ['bhs', 'rbx']

server_names = {
    '161casys4': 'E3-SSD-5',
    '143casys11': 'E3-SSD-3',
    '143casys10': 'E3-SSD-2',
    '143casys13': 'E3-SSD-1'
}

while True:
    raw_data = urllib.urlopen("https://ws.ovh.ca/dedicated/r2/ws.dispatcher/getAvailability2")
    parsed_data = json.loads(raw_data.read())

    available_servers = []

    for server in parsed_data["answer"]["availability"]:
        if server["reference"] in desired_servers:
            name = "{0}: ".format(server_names[server["reference"]])
            info = ""
            for zone in server["zones"]:
                if zone["zone"] in desired_zones:
                    if zone["availability"] != "unknown" and zone["availability"] != "unavailable":
                        info = info + "AVAILABLE ({0}) @ {1}".format(zone["availability"], zone["zone"])
            if info:
                available_servers.append(name + info)

    if available_servers:
        print(available_servers)
        winsound.Beep(440, 2500)

    time.sleep(30)
