"""Tests for the mathexp.perm_groups module."""

import enum

from sympy.combinatorics import SymmetricGroup, DihedralGroup

from mathexp import perm_groups
from mathexp.perm_groups import IsoMethod


class TestIsomorphismMethods:
	"""Test group for isomorphism methods"""

	def test_isomethod_enum(self):
		"""Test isomethod enum, mostly here for coverage"""
		assert issubclass(IsoMethod, enum.Enum)
		assert IsoMethod.BruteForce.value == "brute_force"
		assert IsoMethod.ElementOrders.value == "element_orders"

	def test_is_iso_case_pos(self):
		"""Test is_iso method, known case where iso exists"""
		A = SymmetricGroup(3)
		B = DihedralGroup(3)
		assert perm_groups.is_iso_possible(A, B)

	def test_is_iso_case_neg_order(self):
		"""Test is_iso method, known case where iso does not exist due to order"""
		A = SymmetricGroup(3)
		B = DihedralGroup(4)
		assert not perm_groups.is_iso_possible(A, B)

	def test_find_iso_by_element_orders(self):
		"""Test find iso by element orders method"""
		A = SymmetricGroup(3)
		B = DihedralGroup(3)
		iso = perm_groups.find_iso_by_element_orders(A, B)
		assert iso is not None

	def test_find_iso_by_brute_force(self):
		"""Test find iso by brute force method"""
		A = SymmetricGroup(3)
		B = DihedralGroup(3)
		iso = perm_groups.find_iso_by_brute_force(A, B)
		assert iso is not None

	def test_find_iso(self):
		"""Test find_iso method, higher level interface to multiple methods"""
		A = SymmetricGroup(3)
		B = DihedralGroup(3)
		iso = perm_groups.find_iso(A, B, IsoMethod.ElementOrders)
		assert iso is not None
