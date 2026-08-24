Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============= RESTART: C:/Users/DELL/Documents/packet_scrambler.py =============
--- Stage 1: Input Validation ---
Validation passed. Processing packet...
Original packet: [5, 12, 0, 8, 21, 34, 7, 19, 0, 3]

================================================================= RESTART: C:/Users/DELL/Documents/packet_scrambler.py =================================================================
--- Stage 1: Input Validation ---
Validation passed. Processing packet...
Original packet: [5, 12, 0, 8, 21, 34, 7, 19, 0, 3]

--- Stage 2: Middle-Out Swap ---
Front half: [5, 12, 0, 8, 21]
Back half: [34, 7, 19, 0, 3]
Scrambled: [3, 0, 19, 7, 34, 5, 12, 0, 8, 21]
Is packet same as front_half? False

================================================================= RESTART: C:/Users/DELL/Documents/packet_scrambler.py =================================================================
--- Stage 1: Input Validation ---
Validation passed. Processing packet...
Original packet: [5, 12, 0, 8, 21, 34, 7, 19, 0, 3]

--- Stage 2: Middle-Out Swap ---
Front half: [5, 12, 0, 8, 21]
Back half: [34, 7, 19, 0, 3]
Scrambled: [3, 0, 19, 7, 34, 5, 12, 0, 8, 21]
Is packet same as front_half? False

--- Stage 3: In-Place Correction ---
After SYNC-BIT insertion: [3, 0, 19, 7, 34, 5, 'SYNC-BIT', 12, 0, 8, 21]
After removing zeros: [3, 19, 7, 34, 5, 'SYNC-BIT', 12, 8, 21]

--- Stage 4: Memory Integrity Check ---
Original packet: [5, 12, 0, 8, 21, 34, 7, 19, 0, 3]
Final scrambled packet: [3, 19, 7, 34, 5, 'SYNC-BIT', 12, 8, 21]
Header: 3
Footer: 21
Body length: 7

packet = [5, 12, 0, 8, 21, 34, 7, 19, 0, 3]
print("Stage 1:Input Validation")
Stage 1:Input Validation
if packet and len(packet) >= 10:
    print("Validation passed. Processing packet")
else:
    print("Validation failed: packet is empty or too short.")
    
print("Original packet:", packet)
SyntaxError: invalid syntax
if packet and len(packet) >= 10:
    print("Validation passed. Processing packet")
else:
    print("Validation failed: packet is empty or too short.")
print("Original packet:", packet)
SyntaxError: invalid syntax
if packet and len(packet) >= 10:
    print("Validation passed. Processing packet")
else:
    print("Valudation failed: packet is empty or too short.")

    
Validation passed. Processing packet
print("Original packet:", packet)
Original packet: [5, 12, 0, 8, 21, 34, 7, 19, 0, 3]
print("\n--- Stage 2: Middle-Out Swap ---")

--- Stage 2: Middle-Out Swap ---
midpo-int = len(packet) // 2
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

midpoint = len(packet) // 2

front_half = packet[:midpoint]
back_half = packet[midpoint:]

scrambled = back_half[::-1] + front_half

print("Front half:", front_half)
Front half: [5, 12, 0, 8, 21]
print("Back_half:", back_half)
Back_half: [34, 7, 19, 0, 3]
print("Scrambled:", scrambled)
Scrambled: [3, 0, 19, 7, 34, 5, 12, 0, 8, 21]

print("Is packet same as front_half?",
      id(packet) == id(front_half))
Is packet same as front_half? False
>>> 
>>> print("\n-- Stage 3: In-Place Correction --")

-- Stage 3: In-Place Correction --
>>> 
>>> middle_index = len(scrampled) // 2
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    middle_index = len(scrampled) // 2
NameError: name 'scrampled' is not defined. Did you mean: 'scrambled'?
>>> middle_index = len(scrambled) // 2
>>> 
...  
>>> if type(scrambled[middle_index]) is int:
...     scrambled.insert(middle_index + 1, "SYNC-BIT")
... 
...     
>>> print("After SYNC-BIT insertion:", scrambled)
After SYNC-BIT insertion: [3, 0, 19, 7, 34, 5, 'SYNC-BIT', 12, 0, 8, 21]
>>> 
>>> while 0 in scrambled:
...     scrambled.remove(0)
... 
...     
>>> print("After removing zeros:", scrambled)
After removing zeros: [3, 19, 7, 34, 5, 'SYNC-BIT', 12, 8, 21]
>>> 
...  
>>> print("\n--- Stage 4: Memory Integrity Check ---")

--- Stage 4: Memory Integrity Check ---
>>> 
>>> first, *middle, last = scrambled
>>> 
>>> print("Original packet:", packet)
Original packet: [5, 12, 0, 8, 21, 34, 7, 19, 0, 3]
>>> print("Final scrambled packet:", scrambled)
Final scrambled packet: [3, 19, 7, 34, 5, 'SYNC-BIT', 12, 8, 21]
>>> 
>>> print("Header:", first)
Header: 3
>>> print("Footer:", last)
Footer: 21
>>> print("Body Length:", len(middle))
Body Length: 7
