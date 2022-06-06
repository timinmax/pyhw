import re


def get_ip(log_line):
    remote_addr = re.findall("[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}", log_line)
    if remote_addr:
        return remote_addr[0].strip()
    return ""


def get_request_type(log_line):
    request_type = re.findall('\"([A-Z]+)\s', log_line)
    if request_type:
        return request_type[0].strip()
    return ""


def get_resource(log_line):
    resource = re.findall('\"[A-Z]+\s(/[a-zA-Z0-9_.+-]+/[a-zA-Z0-9_.+-]+)\s', log_line)
    if resource:
        return resource[0].strip()
    return ""


data_tuples = []
spam_rating = {}
spamer_rating = 0
spamer_ip = None

with open("nginx_logs.txt", "r") as log_file:
    for line in log_file:
        remote_ip = get_ip(line)
        data_tuples.append((remote_ip, get_request_type(line), get_resource(line)))
        spam_rating.setdefault(remote_ip, 0)
        spam_rating[remote_ip] += 1
        if spamer_rating < spam_rating[remote_ip]:
            spamer_rating = spam_rating[remote_ip]
            spamer_ip = remote_ip

# task 1 - parsed data
print(data_tuples)

# task 2 - the most spamer detected
print(f"The most spamer is {spamer_ip} with {spamer_rating} requests")
