"""Partition utilities for combinatorics.

References:
	[1] https://docs.sympy.org/latest/modules/combinatorics/partitions.html#sympy.combinatorics.partitions.IntegerPartition
"""

import re
from typing import List, Generator

from sympy.combinatorics import IntegerPartition

# The pattern below is used to match a valid partition notation
# A valid partition notation is a string of the form "a1 + a2 + ... + an"
# where a1, a2, ..., an are integers in decreasing order
# e.g. "5 + 4 + 3 + 2 + 1"
PATTERN_PARTITION_NOTATION = re.compile(r'^(\d+)(\s*\+\s*\d+)*$')


def is_valid_partition(p: str) -> bool:
	"""Determine if a string is a valid partition notation. A valid partition
	notation is a string of the form "a1 + a2 + ... + an" where a1, a2, ..., an
	are integers in decreasing order.

	Args:
		p:
			str, partition notation

	Returns:
		bool: True if the string is a valid partition notation, False otherwise
	"""
	# Check that string matches the regex pattern
	if not PATTERN_PARTITION_NOTATION.match(p):
		return False

	# Check that the partition is in decreasing order
	parts = p.split("+")
	for i in range(1, len(parts)):
		if parts[i] > parts[i - 1]:
			return False

	return True


def from_str(p: str) -> IntegerPartition:
	"""Convert a string notation partition, e.g. a1 + a2 + ... + an into
	an Integer Partition object

	Args:
		p:

	Returns:

	"""
	if not is_valid_partition(p):
		raise ValueError(f"Invalid partition notation: {p}")

	# Convert the string to a list of integers
	parts = p.split("+")
	parts = [int(part.strip()) for part in parts]

	# Create the IntegerPartition object
	return IntegerPartition(parts)


def to_str(p: IntegerPartition) -> str:
	"""Convert an Integer Partition object into a string notation partition,
	e.g. a1 + a2 + ... + an

	Args:
		p:

	Returns:

	"""
	return " + ".join(str(part) for part in p.partition)


def values(p: IntegerPartition, zero_indexed: bool = False) -> List[List[int]]:
	"""Get the values of the partition (the integers 1 to n where n is the
	sum of parts in the partition) in a list of lists where each list
	represents an equivalence class of the partition.

	Args:
		p:
			IntegerPartition
		zero_indexed:
			bool, if True, the values are zero-indexed

	Returns:
		list: list of lists of integers
	"""
	equiv_classes = []
	prev_class_max = -1 if zero_indexed else 0

	for part in p.partition:
		ec = list(range(prev_class_max + 1, prev_class_max + part + 1))
		equiv_classes.append(ec)
		prev_class_max = ec[-1]

	return equiv_classes


def generate_partitions(n: int) -> Generator[List[int], None, None]:
	"""Generate all partitions of n

	Args:
		n:
			int, number to partition
		max_parts:
			int, maximum number of parts in the partition

	Returns:
		list: list of IntegerPartition
	"""
	# base case of recursion: zero is the sum of the empty list
	if n == 0:
		yield []
		return

	# modify partitions of n-1 to form partitions of n
	for p in generate_partitions(n - 1):
		yield p + [1]
		if p and (len(p) < 2 or p[-2] > p[-1]):
			yield p[:-1] + [p[-1] + 1]

