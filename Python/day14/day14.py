import re
import itertools


def solve_1(data):
    nonzero = {}
    mask = ""
    for line in data:
        if "mask" in line:
            _, mask = line.split(" = ")
        else:
            address, number = re.findall(r'\d+', line)
            number_bin = '{0:036b}'.format(int(number))
            number = int(apply_number_mask(number_bin, mask), 2)
            nonzero[int(address)] = number
    return sum(nonzero[k] for k in nonzero)


def apply_number_mask(num_bin, mask):
    final_num = ""
    for bit, m_bit in zip(num_bin, mask):
        if m_bit == "X":
            final_num += bit
        else:
            final_num += m_bit
    return final_num


def solve_2(data):
    nonzero = {}
    mask = ""
    for line in data:
        if "mask" in line:
            _, mask = line.split(" = ")
        else:
            address, number = re.findall(r'\d+', line)
            address_bin = '{0:036b}'.format(int(address))
            for addr in get_addresses(address_bin, mask):
                nonzero[addr] = int(number)
    return sum(nonzero[k] for k in nonzero)


def apply_address_mask(address, mask, replace_bits):
    final_addr = ""
    for bit, m_bit in zip(address, mask):
        if m_bit == "X":
            final_addr += "{}"
        elif m_bit == "0":
            final_addr += bit
        else:
            final_addr += "1"
    return final_addr.format(*replace_bits)


def get_addresses(address, mask):
    combinations = mask.count("X")
    bit_combinations = itertools.product(*(['01']*combinations))
    return [int(apply_address_mask(address, mask, bit_comb), 2) for bit_comb in bit_combinations]


# IO
data = [line.rstrip() for line in open("input.txt").readlines()]

# 1st
print(solve_1(data))

# 2nd
print(solve_2(data))
