import sys


def parse_number(s, mapping):
    digits = ""
    for i in range(0, len(s), 3):
        triplet = s[i:i + 3]
        digits += str(mapping[triplet])
    return int(digits)


def to_triplets(num, reverse_mapping):
    if num == 0:
        return "ZER"
    result = ""
    for digit in str(num):
        result += reverse_mapping[int(digit)]
    return result


def main():
    s = sys.stdin.readline().strip()

    mapping = {
        "ONE": 1, "TWO": 2, "THR": 3, "FOU": 4, "FIV": 5,
        "SIX": 6, "SEV": 7, "EIG": 8, "NIN": 9, "ZER": 0
    }

    reverse_mapping = {v: k for k, v in mapping.items()}

    for op in ['+', '-', '*']:
        if op in s:
            operator = op
            left, right = s.split(op)
            break

    num1 = parse_number(left, mapping)
    num2 = parse_number(right, mapping)

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    print(to_triplets(result, reverse_mapping))


if __name__ == "__main__":
    main()