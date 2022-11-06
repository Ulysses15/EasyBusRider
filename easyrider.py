import json

json_input1 = [
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:11"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:20"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:27"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:46"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]

json_input2 = [
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:27"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    }
]


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
        cd[i["bus_id"]].append((i["stop_name"], i["a_time"],))
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


def print_results(time_errors_dict: "bus_id: (stop_name, time)"):
    print("Arrival time test:")
    if not time_errors_dict:
        print("OK")
    else:
        for key, value in time_errors_dict.items():
            print(f"bus_id line {key}: wrong time on station {value[0]}")


def main():
    bus_data = input()
    # bus_data = json.dumps(json_input2)
    data_deser = json.loads(bus_data)  # data deserialization from json
    # print(data_deser)
    error_dict = time_order_check(data_deser)
    print_results(error_dict)


if __name__ == "__main__":
    main()
