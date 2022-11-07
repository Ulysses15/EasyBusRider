import json
from itertools import combinations

# input_bus = [
#     {
#         "bus_id": 128,
#         "stop_id": 1,
#         "stop_name": "Prospekt Avenue",
#         "next_stop": 3,
#         "stop_type": "S",
#         "a_time": "08:12"
#     },
#     {
#         "bus_id": 128,
#         "stop_id": 3,
#         "stop_name": "Elm Street",
#         "next_stop": 5,
#         "stop_type": "O",
#         "a_time": "08:19"
#     },
#     {
#         "bus_id": 128,
#         "stop_id": 5,
#         "stop_name": "Fifth Avenue",
#         "next_stop": 7,
#         "stop_type": "O",
#         "a_time": "08:25"
#     },
#     {
#         "bus_id": 128,
#         "stop_id": 7,
#         "stop_name": "Sesame Street",
#         "next_stop": 0,
#         "stop_type": "F",
#         "a_time": "08:37"
#     },
#     {
#         "bus_id": 256,
#         "stop_id": 2,
#         "stop_name": "Pilotow Street",
#         "next_stop": 3,
#         "stop_type": "S",
#         "a_time": "09:20"
#     },
#     {
#         "bus_id": 256,
#         "stop_id": 3,
#         "stop_name": "Elm Street",
#         "next_stop": 6,
#         "stop_type": "",
#         "a_time": "09:45"
#     },
#     {
#         "bus_id": 256,
#         "stop_id": 6,
#         "stop_name": "Sunset Boulevard",
#         "next_stop": 7,
#         "stop_type": "O",
#         "a_time": "09:59"
#     },
#     {
#         "bus_id": 256,
#         "stop_id": 7,
#         "stop_name": "Sesame Street",
#         "next_stop": 0,
#         "stop_type": "F",
#         "a_time": "10:12"
#     },
#     {
#         "bus_id": 512,
#         "stop_id": 4,
#         "stop_name": "Bourbon Street",
#         "next_stop": 6,
#         "stop_type": "S",
#         "a_time": "08:13"
#     },
#     {
#         "bus_id": 512,
#         "stop_id": 6,
#         "stop_name": "Sunset Boulevard",
#         "next_stop": 0,
#         "stop_type": "F",
#         "a_time": "08:16"
#     }
# ]


input_bus = [{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"},
{"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "O", "a_time" : "08:19"},
{"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"},
{"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"},
{"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "09:20"},
{"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "", "a_time" : "09:45"},
{"bus_id" : 256, "stop_id" : 6, "stop_name" : "Abbey Road", "next_stop" : 7, "stop_type" : "O", "a_time" : "09:59"},
{"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"},
{"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"},
{"bus_id" : 512, "stop_id" : 6, "stop_name" : "Abbey Road", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]




def control_dict(checking_list):
    """return dict with keys as bus id's"""
    list_of_bus_id = []
    for i in checking_list:
        list_of_bus_id.append(i['bus_id'])
    return {x: [] for x in set(sorted(list_of_bus_id))}


def time_dict(checking_list):
    """return timetable with bus id and a list of tuples (stop_name, time)"""
    cd = control_dict(checking_list)
    for i in checking_list:
        cd[i["bus_id"]].append((i["stop_name"], i["a_time"], i["stop_type"]))
    return cd


def is_ascending(time_list):
    """check if list with time is ascending and return time otherwise"""
    previous = time_list[0][1]
    for number in time_list:
        if number[1] < previous:
            return number
        previous = number[1]
    return 0


def time_order_check(checking_list: "main list"):
    time_table = time_dict(checking_list)
    arrival_time_errors = {}
    for key, value in time_table.items():
        res_check = is_ascending(value)
        if not res_check:
            continue
        else:
            new_item = {key: res_check}
            arrival_time_errors.update(new_item)
    return arrival_time_errors


def check_start_final(checking_dictionary):
    wrong_start_final = []
    for key, value in checking_dictionary.items():
        if value[0][2] != 'S' or value[-1][2] != 'F':
            wrong_start_final.append(value[0][0])
    return wrong_start_final


def count_transfers(checking_list):
    """count transfers, return sorted list"""
    h = control_dict(checking_list)
    for hh in checking_list:
        h[hh["bus_id"]].append(hh["stop_name"])
    stops = []  # a set of strops for each route
    for ii in h:
        stops.append(set(h.get(ii)))
    pairs = combinations(stops, 2)
    transfer = []
    for i in pairs:
        transfer.append(i[0].intersection(i[1]))
    for b in transfer:
        transfer[0].update(b)
    return sorted(list(transfer[0]))


def check_transfers(checking_dictionary, transfer_list):
    transfer_errors = []
    for value in checking_dictionary.values():
        for jj in value:
            for k in transfer_list:
                if jj[0] == k:
                    if jj[2] == 'O':
                        transfer_errors.append(jj[0])
    return transfer_errors


def main():
    bus_data = input()
    # bus_data = json.dumps(input_bus)
    data_deser = json.loads(bus_data)  # data deserialization from json
    # print(data_deser)
    check_dict = time_dict(data_deser)
    start_final = check_start_final(check_dict)
    transfers = count_transfers(data_deser)
    transf_faults = check_transfers(check_dict, transfers)
    # print(start_final, transf_faults, sep='\n')
    total_list = sorted(start_final + transf_faults)
    print("On demand stops test:")
    if not total_list:
        print("OK")
    else:
        print(f"Wrong stop type: {total_list}")


main()
