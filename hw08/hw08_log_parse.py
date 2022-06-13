import re

re_ip = re.compile(r'((?:\d{1,3}\.){3}\d{1,3})\s')
re_date_time = re.compile(r'\s\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4})\]\s')
re_request_type = re.compile(r'\s\"([A-Z]{3,})\s')
re_requested_resource = re.compile(r'\s((?:/[a-zA-Z0-9_.+-]+)+)\s')
re_response_code = re.compile(r'\"\s(\d{3})\s\d+')
re_response_size = re.compile(r'\"\s\d{3}\s(\d+)\s\"-')


def parse_line(textline):
    remote_addr = re_ip.findall(textline)
    remote_addr = remote_addr[0] if remote_addr else None

    request_datetime = re_date_time.findall(line)
    request_datetime = request_datetime[0] if request_datetime else None

    request_type = re_request_type.findall(line)
    request_type = request_type[0] if request_type else None

    requested_resource = re_requested_resource.findall(line)
    requested_resource = requested_resource[0] if requested_resource else None

    response_code = re_response_code.findall(line)
    response_code = response_code[0] if response_code else None

    response_size = re_response_size.findall(line)
    response_size = response_size[0] if response_size else None

    return (remote_addr, request_datetime, request_type, requested_resource, response_code, response_size)


parse_result = []
with open("nginx_logs.txt", "r") as log_file:
    for line in log_file:
        parse_result.append(parse_line(line))

print(parse_result)