import os
from typing import Tuple


def process_log_stream(file_path: str, chunk_size: int, /) -> Tuple[int, float]:
    """
    Reads a file in fixed-size byte chunks.
    Returns the valid record count and mean sensor value.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Target path '{file_path}' not found.")

    valid_count = 0
    total = 0.0
    found_end = False
    leftover = b""

    with open(file_path, "rb") as file_obj:

        for chunk in iter(lambda: file_obj.read(chunk_size), b""):

            leftover += chunk

            *complete_lines, leftover = leftover.split(b"\n")

            for raw_line in complete_lines:

                line = raw_line.decode("utf-8").strip()

                if line == "END OF LOG":
                    found_end = True
                    continue

                fields = line.split(",")

                if len(fields) != 3:
                    continue

                value = fields[2].strip()

                if value == "":
                    continue

                try:
                    sensor_value = float(value)
                except ValueError:
                    continue

                valid_count += 1
                total += sensor_value

    if leftover:
        line = leftover.decode("utf-8").strip()

        if line == "END OF LOG":
            found_end = True
        else:
            fields = line.split(",")

            if len(fields) == 3:
                value = fields[2].strip()

                if value != "":
                    try:
                        sensor_value = float(value)
                        valid_count += 1
                        total += sensor_value
                    except ValueError:
                        pass

    if not found_end:
        print("Warning: END OF LOG not found. File may be truncated.")

    if valid_count == 0:
        mean = 0.0
    else:
        mean = total / valid_count

    return valid_count, mean


# Driver code
if __name__ == "__main__":

    file_path = "sample_telemetry.log"

    result = process_log_stream(file_path, 1)

    print("Chunk size = 1")
    print(result)

    result = process_log_stream(file_path, 1000)

    print("Chunk size = 1000")
    print(result)
