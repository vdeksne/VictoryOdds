import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    DB = []
    field_names = []
    with open(sys.argv[1], "r", newline="\n") as file:
        reader = csv.DictReader(file)
        field_names = reader.fieldnames
        DB = list(reader)

    # TODO: Read DNA sequence file into a variable
    # sequence = ""
    with open(sys.argv[2], "r", newline="\n") as file:
        reader = csv.DictReader(file, fieldnames=["seq"])
        for row in reader:
            sequence = row["seq"]

    # TODO: Find longest match of each STR in DNA sequence
    possible_sequences = field_names[1:]
    person = {}
    for sequence_to_find in possible_sequences:
        person[sequence_to_find] = str(longest_match(sequence, sequence_to_find))

    # TODO: Check database for matching profiles
    found = False
    name = ""
    for row in DB:
        r = list(row.values())
        p = list(person.values())
        if r[1:] == p:
            found = True
            name = r[0]
    if found:
        print(name)
    else:
        print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
