caliberation_feed = [
    [201, 6.0 ,9.5, "IGNORE", 4.0],
    [],
    [202, 11.2, "FAULT", 7.8, 5.5],
    [203, 14.0, 3.5, 8.25],
    [204, 2.75, "HALT", 6.0]
]
total_valid_readings = 0
global_max = None
global_min = None
total_checksum = 0.0
emergency_stop = False

feed_cursor = 0

while (current_slice := caliberation_feed[feed_cursor:feed_cursor + 1]):
    batch = current_slice[0]

    if not batch:
        print("Batch", feed_cursor, "is EMPTY. Proceeding.")

        feed_cursor += 1
        continue

    caliberation_id = batch[0]
    batch_sum = 0.0
    print("Evaluating Batch",
        feed_cursor,
        "(ID:",
        caliberation_id,
        ")..."
    )
    batch_length = 0
    for _ in batch:
        batch_length += 1

    for i in range(1, batch_length):
        target_index = batch_length - i
        reading = batch[target_index]

        if reading == "IGNORE":
            print("Signal FAULT detected. Suppressing batch", caliberation_id)
            continue

        if reading == "FAULT":
            print("Signal FAULT detected. Suppressing batch",
                caliberation_id
            )

        if reading == "HALT":
            print("Signal HALT detected. Executing emergency protocol.")
            emergency_stop = True
            break

        if isinstance(reading, str):

            print(
                "Unexpected text reading:",
                reading,
                "in Batch",
                caliberation_id
            )

            continue


        if global_max is None or reading > global_max:
            global_max = reading
        if global_min is None or reading < global_min:
            global_min = reading

    else:
        if caliberation_id % 2 ==0:
            adjusted_sum = batch_sum*1.5
        else:
            adjusted_sum = batch_sum*0.8
        total_checksum += adjusted_sum

    if emergency_stop:
        break

    feed_cursor += 1
print()
print("========================================")
print("CALIBRATION COMPLETE :", end=" ")

if emergency_stop:
    print("EMERGENCY TERMINATION")
else:
    print("NORMAL TERMINATION")

print("========================================")
print("Total Valid Readings Processed :",
    total_valid_readings
)
print("Global Calibration Checksum :", total_checksum)
print("Maximum Reading Encountered :", global_max)
print("Minimum Reading Encountered :", global_min)
    
        
    
