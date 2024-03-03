"""Utilities for permutation groups, mostly algorithms for seeking isomorphisms
"""

import enum
import itertools
from typing import Dict, Callable

from sympy.combinatorics import Permutation, PermutationGroup


class IsoMethod(str, enum.Enum):
	"""Enumeration of methods for finding isomorphisms between permutation groups
	"""
	BruteForce = "brute_force"
	ElementOrders = "element_orders"


def is_iso_possible(A: PermutationGroup, B: PermutationGroup) -> bool:
	"""Check if isomorphism between permutation groups A and B is possible.

	Args:
		A:
			PermutationGroup
		B:
			PermutationGroup

	Returns:
		bool: True if isomorphism is possible, False otherwise
	"""
	# Check if the groups have the same order
	if A.order() != B.order():
		return False

	# Check if the groups have the same degree
	if A.degree != B.degree:
		return False

	# Check if the group elements have the same orders and order-multiplicities
	a_elem_orders = list(sorted(a.order() for a in A.elements))
	b_elem_orders = list(sorted(b.order() for b in B.elements))
	if a_elem_orders != b_elem_orders:
		return False

	# Check if groups are alike in commutativity
	if A.is_abelian != B.is_abelian:
		return False

	return True


def is_iso(f: Callable, A: PermutationGroup, B: PermutationGroup) -> bool:
	"""Check if f is an isomorphism between permutation groups A and B.

	Args:
		f:
			Callable, function to check
		A:
			PermutationGroup
		B:
			PermutationGroup

	Returns:
		bool: True if f is an isomorphism, False otherwise
	"""
	# Check f is onto
	f_range = set(f(a) for a in A.elements)
	if f_range != B.elements:
		return False

	# Check f is one-to-one
	f_domain = set(a for a in A.elements)
	if len(f_domain) != len(f_range):
		return False

	# Check f preserves group operation
	for a, b in itertools.product(A.elements, A.elements):
		if f(a * b) != f(a) * f(b):
			return False

	return True


def find_iso_by_element_orders(A: PermutationGroup, B: PermutationGroup) -> Dict[Permutation, Permutation]:
	"""Find an isomorphism between permutation groups A and B.

	Args:
		A:
			PermutationGroup
		B:
			PermutationGroup
	"""
	# Get all element orders
	a_elem_orders = {a: a.order() for a in A.elements}
	b_elem_orders = {b: b.order() for b in B.elements}

	# Partition the elements of A and B by their orders
	a_elem_orders = {order: [a for a, a_order in a_elem_orders.items() if a_order == order] for order in set(a_elem_orders.values())}
	b_elem_orders = {order: [b for b, b_order in b_elem_orders.items() if b_order == order] for order in set(b_elem_orders.values())}

	# Construct permutations for each order equivalence-class
	order_perms = {order: itertools.permutations(b_elem_orders[order]) for order in b_elem_orders.keys()}
	domain = list(itertools.chain(*[a_elem_orders[order] for order in sorted(a_elem_orders.keys())]))

	# Iterate over product of permutations restricted to equivalence-classes
	for perm in itertools.product(*[order_perms[order] for order in sorted(b_elem_orders.keys())]):
		# Assemble candidate isomorphism by matching order equivalence-classes

		iso = dict(zip(domain, itertools.chain(*perm)))
		if is_iso(iso.get, A, B):
			return iso


def find_iso_by_brute_force(A: PermutationGroup, B: PermutationGroup) -> Dict[Permutation, Permutation]:
	"""Find an isomorphism between permutation groups A and B.

	Args:
		A:
			PermutationGroup
		B:
			PermutationGroup

	Returns:
		Dict[Permutation, Permutation] or None: isomorphism or None if not found
	"""
	a_elements = list(A.elements)
	b_elements = list(B.elements)

	# Brute force search for isomorphism
	for perm in itertools.permutations(b_elements):
		iso = dict(zip(a_elements, perm))
		if is_iso(iso.get, A, B):
			return iso


def find_iso(A: PermutationGroup, B: PermutationGroup, method: IsoMethod) -> Dict[Permutation, Permutation]:
	"""Find an isomorphism between permutation groups A and B.

	Args:
		A:
			PermutationGroup
		B:
			PermutationGroup
		method:
			IsoMethod, method to use for finding isomorphism

	Returns:
		Dict[Permutation, Permutation]: isomorphism
	"""
	if not is_iso_possible(A, B):
		raise ValueError("Isomorphism is not possible")

	method_func = {
		IsoMethod.BruteForce: find_iso_by_brute_force,
		IsoMethod.ElementOrders: find_iso_by_element_orders
	}.get(method, None)

	if method_func is None:
		raise ValueError(f"Invalid method: {method}, options are: {', '.join(IsoMethod.__members__)}")

	return method_func(A, B)
