def search4letters(phrase: str, letters: str = 'ATCG') -> set:
    """
    Return the set of target letters found in the supplied phrase.

    phrase  -> DNA sequence to search
    letters -> target letters to look for
                Default value is 'ATCG'
    """

    
    target_letters = set(letters)

    
    dna_letters = set(phrase)

    
    return target_letters.intersection(dna_letters)
print("========== TASK 1: search4letters ==========")
print()

result1 = search4letters('TGGACC', 'GC')
print("1. Positional arguments:")
print("search4letters('TGGACC', 'GC') =", result1)
print()

result2 = search4letters(letters='CG', phrase='TGGACC')
print("2. Keyword arguments:")
print("search4letters(letters='CG', phrase='TGGACC') =", result2)
print()

result3 = search4letters('TGGACC')
print("3. Default argument:")
print("search4letters('TGGACC') =", result3)
print()

def analyze_sequence(sequence_list, marker):
    """
    Append marker to sequence_list and display object IDs
    before and after the mutation.
    """

    
    print(
        f"Inside Function (Start) - ID: {id(sequence_list)} "
        f"| Data: {sequence_list}"
    )

    
    sequence_list.append(marker)

   
    print(
        f"Inside Function (End) - ID: {id(sequence_list)} "
        f"| Data: {sequence_list}"
    )

print("========== TASK 2: Memory Reference Demonstration ==========")
print()

dna_database = ['AATCCG', 'TGGCTA']

print(
    f"Global Scope (Before) - ID: {id(dna_database)} "
    f"| Data: {dna_database}"
)

print()

analyze_sequence(dna_database, 'CGAT')

print()

print(
    f"Global Scope (After) - ID: {id(dna_database)} "
    f"| Data: {dna_database}"
)

print()

print("========== SLICE EXPERIMENT ==========")
print()


dna_database = ['AATCCG', 'TGGCTA']

print(
    f"Global Scope (Before) - ID: {id(dna_database)} "
    f"| Data: {dna_database}"
)

print()


analyze_sequence(dna_database[:], 'CGAT')

print()

print(
    f"Global Scope (After) - ID: {id(dna_database)} "
    f"| Data: {dna_database}"
)

print()

print("========== EDGE CASE 1: Empty Phrase ==========")
print()

empty_result = search4letters('')

print("search4letters('') =", empty_result)
print()

print("========== EDGE CASE 2: Mixed Arguments ==========")
print()

mixed_result = search4letters('TGGACC', letters='GC')

print("search4letters('TGGACC', letters='GC') =", mixed_result)
print()

print("========== EDGE CASE 3: Repeated Slice Calls ==========")
print()

dna_database = ['AATCCG', 'TGGCTA']

print("Original list before repeated calls:")
print(dna_database)
print()

analyze_sequence(dna_database[:], 'CGAT')

print()

analyze_sequence(dna_database[:], 'AAAA')

print()

print("Original list after repeated slice calls:")
print(dna_database)
print()

def analyze_sequence_rebind(sequence_list, marker):
    """
    Demonstrates reassignment instead of mutation.
    """

    print(
        f"Inside (Start) - ID: {id(sequence_list)} "
        f"| Data: {sequence_list}"
    )

    sequence_list = sequence_list + [marker]

    print(
        f"Inside (End) - ID: {id(sequence_list)} "
        f"| Data: {sequence_list}"
    )


print("========== BONUS: Mutation vs Reassignment ==========")
print()

dna_database = ['AATCCG', 'TGGCTA']

print(
    f"Global Scope (Before) - ID: {id(dna_database)} "
    f"| Data: {dna_database}"
)

print()

analyze_sequence_rebind(dna_database, 'CGAT')

print()

print(
    f"Global Scope (After) - ID: {id(dna_database)} "
    f"| Data: {dna_database}"
)

print()

