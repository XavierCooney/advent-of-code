# ⚡⚡ Xavier Cooney's Slightly Dodgy and Possibly Completely Uncessary Python Template: v4 ⚡⚡

import collections
import functools
import heapq
import itertools
import math
import operator
import pprint
import queue
import random
import re
import string
import sys
import textwrap
import time
import os
from collections import defaultdict, deque

assert sys.version_info >= (3, 8), "Please evaluate with Python 3.8 or higher thanks"

ceil = math.ceil
floor = math.floor
def identity(x): return x
def log_2(x): return math.log(x) / math.log(2)

def read_input():
    match = re.search(r'(\d+)[\\\/]([\d])+\.py$', sys.argv[0])
    assert match
    with open(os.path.join(match.group(1), match.group(2) + '.in')) as f:
        return f.read().strip()

def read_input_lines():
    return read_input().split('\n')

old_map = map
def map(*args, **kwargs):
    return list(old_map(*args, **kwargs))

old_filter = filter
def filter(*args, **kwargs):
    return list(old_filter(*args, **kwargs))

def splitlines(s): return [l.strip() for l in s.strip().split('\n')]

def dp_cache(func):
    mapping = {}
    @functools.wraps(func)
    def wrapper_dp_cache(*args):
        # assert type(args) == tuple
        if args not in mapping:
            mapping[args] = func(*args)
        return mapping[args]
    return wrapper_dp_cache

inf = float('inf')

def range_middle_idx(start, end, rounding_func=floor):
    # Middle index of [start, end)
    return rounding_func((start + end) / 2)

def bin_search_increasing(start, end, f):
    """ Returns first integer i for which f(i) returns True, where
        i is in the range (start, end], f(end) is True,
        and f is a boolean non-decreasing pure function """
    # invariant: f(start) is False, f(end) is True
    while end > start + 1:
        mid = range_middle_idx(start, end)
        if f(mid):
            end = mid
        else:
            start = mid
    return end

def arg_max(l):
    return max(
        enumerate(l),
        key=lambda x: x[1]
    )

def tuple_range(ranges):
    return list(itertools.product(
        *[(range(*r) if type(r) == tuple else range(r)) for r in ranges]
    ))

def apply_alternating(f, cap, m, k=0):
    """ Run a function f with every integer i
        in the range [0, cap) such that i % m == k """
    # assume k < m
    while k < cap:
        f(k)
        k += m

def mismatch(seq_1, seq_2, p=operator.eq):
    # like std::match
    i = 0
    while i < len(seq_1) and i < len(seq_2) and p(seq_1[i], seq_2[i]):
        i += 1
    return i

progress_char = '.'
progress_char_index = 0
progress_chars_list = ['|', '/', '-', '\\']
progress_last_update = 0 # time.time()

def needs_progress_update():
    global progress_char, progress_last_update, progress_char_index

    if time.time() - progress_last_update > 0.25:
        progress_last_update = time.time()
        progress_char = progress_chars_list[progress_char_index]
        progress_char_index = (progress_char_index + 1) % len(progress_chars_list)

        return True

    return False


def iter_track_with_len(l, msg):
    global is_iter_tracking
    iterable_len = len(l)
    re_print_every = ceil(iterable_len / 1000)
    i = 0
    try:
        for x in l:
            if i % re_print_every == 0:
                needs_progress_update()
                print('\r{} [{}]: {:04.1f}% [{:59}]'.format(
                    progress_char,
                    msg, i / iterable_len * 100,
                    '#' * floor(i / iterable_len * 60)
                ), end='')
            yield x
            i += 1
    finally:
        print('')
        is_iter_tracking = False

def iter_track_no_len(l, msg):
    global is_iter_tracking
    i = 1
    for x in l:
        if needs_progress_update():
            print('\r{} [{}]: {:8d} [{:30}]'.format(
                progress_char,
                msg, i,
                '#' * ceil(log_2(i))
            ), end='')
        yield x
        i += 1
    print('')
    is_iter_tracking = False

is_iter_tracking = False

def iter_track(l, msg='iter'):
    global is_iter_tracking
    # should have a lock or something
    if is_iter_tracking: return l
    is_iter_tracking = True
    try:
        len(l)
    except TypeError:
        return iter_track_no_len(l, msg)
    else:
        return iter_track_with_len(l, msg)


def get_bit(i, n):
    return i & (1 << n)

def set_bit(i, n, v):
    if v:
        return i | (1 << n)
    else:
        return i & ~(1 << n)

ADJACENT_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ADJACENT_8 = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def is_digits(s):
    return re.match("^[0-9]+$", s)

def is_letters(s):
    return re.match("^[a-zA-Z]+$", s)


def detect_cycles(initial, mapping):
    i = initial
    seq = []
    seen = set()
    while i is not None and i not in seen:
        seen.add(i)
        seq.append(i)
        i = mapping[i]
    if i not in seen: # diverges, or whatever :(
        return None
    first_place_in_cycle = seq.index(i)
    return seq[first_place_in_cycle:]

def constant_value_default_dict(val):
    return defaultdict(lambda: val)

def int_to_base_b_digits(n, b):
    digits = []
    while n:
        digits.append(n % b)
        n //= b
    return digits[::-1]

def base_b_digits_to_int(digits, b):
    total = 0
    for place, val in enumerate(digits[::-1]):
        total += val * b ** place
    return total

def graph_function(x_values, y_values):
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        print("You gotta install pyplot and numpy to see the graph...")
        return

    fix, ax = plt.subplots()
    ax.set_title('A graph of something probably')
    ax.plot(x_values, y_values)
    plt.show()

def bfs(start, edge_function, done_predicate, should_iter_track=True):
    q = deque([(start, ())])
    seen = {start}
    # edge_function = dp_cache(edge_function)

    total_iterations = 0

    while q:
        top_node, top_path = q.popleft()

        if done_predicate(top_node):
            if should_iter_track:
                print()

            path_flat_reversed = []
            while top_path:
                path_flat_reversed.append(top_path[0])
                top_path = top_path[1]

            return top_node, path_flat_reversed[::-1]

        for next_move, neighbour in edge_function(top_node):
            # print(neighbour)
            if neighbour in seen:
                continue
            seen.add(neighbour)
            q.append((neighbour, (next_move, top_path)))

        total_iterations += 1
        if should_iter_track and needs_progress_update():
            print(f'\r{progress_char} BFSing... {total_iterations} it, len of {len(q)}   ', end='')

    if should_iter_track:
        print()

    return None

def inverse_dictionary(old_dict, error_on_non_one_to_one=True):
    new_dict = {}
    for key, value in old_dict.items():
        if error_on_non_one_to_one:
            assert value not in new_dict
        new_dict[value] = key
    return new_dict

def find_all_factors_improper(p):
    # return all factors from 1 to p inclusive
    factors = []
    for i in range(1, p + 1):
        if p % i == 0:
            factors.append(i)
    return factors

def make_symmetric_assignment(num_slots, n):
    # i have no idea whether this is actually a thing
    # and i can't describe it well, but i've come come up with
    # solutions which use this kind of idea a couple of times.
    # fills slots with labels 0 to n (incl, excl), but there's
    # symmetry
    all_possibilities = [(0, [])]
    for slot in range(num_slots):
        next_round = []
        for next_max, current_vals in all_possibilities:
            next_next_max = next_max if next_max == n - 1 else next_max + 1
            for next_val in range(1 + next_max):
                next_round.append((
                    next_next_max if next_val == next_max else next_max,
                    current_vals + [next_val]
                ))
        all_possibilities = next_round
    return all_possibilities

VOWELS = 'aeiouAEIOU'
CONSONANTS = ''.join(c for c in string.ascii_letters if c not in VOWELS)

def powerlist(ls):
    # like a powerset, but for a list (possibly has duplicates if duplicates in original)
    result = []
    for assignment in tuple_range([(2,)] * len(ls)):
        this_set = []
        for i, x in enumerate(ls):
            if assignment[i]:
                this_set.append(x)
        result.append(this_set)
    return result

def fully_flatten(ls):
    res = []
    for el in ls:
        if type(el) in (list, tuple):
            res += fully_flatten(el)
        else:
            res.append(el)
    return res

# END XAV TEMPLATE