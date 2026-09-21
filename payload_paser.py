def parse_payload(raw_packet: list, delimiter: str, /, *,
                  correction_offset: int = 0) -> tuple:

    status_tokens = raw_packet[2].split(delimiter)

    corrected_sensors = [
        value if "ERROR" in status_tokens else value + correction_offset
        for value in raw_packet[1][:]
    ]

    return raw_packet[0], corrected_sensors



raw_packet_1 = [
    501,
    [12.5, 13.0, 11.8],
    "NOMINAL|CALIBRATED"
]

original_sensors_1 = raw_packet_1[1][:]

result_1 = parse_payload(
    raw_packet_1,
    "|",
    correction_offset=2
)

print("Test 1 ->", result_1[0], result_1[1])

assert raw_packet_1[1] == original_sensors_1
assert id(result_1[1]) != id(raw_packet_1[1])

print("Test 1 side-effect assertions passed.")



raw_packet_2 = [
    502,
    [9.0, 8.5],
    "ERROR|SENSOR FAULT"
]

original_sensors_2 = raw_packet_2[1][:]

result_2 = parse_payload(
    raw_packet_2,
    "|",
    correction_offset=5
)

print("Test 2 ->", result_2[0], result_2[1])

assert raw_packet_2[1] == original_sensors_2
assert id(result_2[1]) != id(raw_packet_2[1])

print("Test 2 side-effect assertions passed.")



raw_packet_3 = [
    503,
    [1.0, 2.0],
    "NOMINAL"
]

result_3 = parse_payload(
    raw_packet_3,
    "|"
)

print("Test 3 (default offset) ->", result_3[0], result_3[1])

assert result_3[1] == [1.0, 2.0]
assert id(result_3[1]) != id(raw_packet_3[1])



raw_packet_4 = [
    504,
    [5.0, 6.0, 7.0],
    "NOMINAL|CALIBRATED|LOW POWER"
]

result_4 = parse_payload(
    raw_packet_4,
    "|",
    correction_offset=3
)

print("Test 4 ->", result_4[0], result_4[1])

assert result_4[1] == [8.0, 9.0, 10.0]
assert id(result_4[1]) != id(raw_packet_4[1])

raw_packet_5 = [
    505,
    [],
    "NOMINAL"
]

result_5 = parse_payload(
    raw_packet_5,
    "|",
    correction_offset=10
)

print("Test 5 (empty sensors) ->", result_5[0], result_5[1])

assert result_5[1] == []
assert id(result_5[1]) != id(raw_packet_5[1])


raw_packet_6 = [
    506,
    [10.0, 20.0],
    "NOMINAL"
]

result_6a = parse_payload(
    raw_packet_6,
    "|"
)

result_6b = parse_payload(
    raw_packet_6,
    "|",
    correction_offset=0
)

print("Test 6 -> omitted:", result_6a)
print("Test 6 -> explicit 0:", result_6b)

assert result_6a == result_6b


try:
    parse_payload(
        raw_packet=raw_packet_1,
        delimiter="|"
    )
except TypeError as error:
    print("Test 7 passed. TypeError raised as expected:", error)


try:
    parse_payload(
        raw_packet_1,
        "|",
        2
    )
except TypeError as error:
    print("Test 8 passed. TypeError raised as expected:", error)
