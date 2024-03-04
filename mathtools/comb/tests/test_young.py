"""Tests for the mathexp.comb.young module."""
from mathtools.comb.young import YoungTableau


class TestYoung:
	"""Test group"""

	def test_create(self):
		"""Test YoungTableau creation"""
		# Proper case
		yt = YoungTableau("5 + 3 + 1")
		assert isinstance(yt, YoungTableau)

	def test_str(self):
		"""Test YoungTableau string representation"""
		# Proper case
		yt = YoungTableau("5 + 3 + 1")
		assert str(yt) == "YT(5 + 3 + 1)"

	def test_rows(self):
		"""Test YoungTableau rows"""
		# Proper case
		yt = YoungTableau("5 + 3 + 1")
		rows = yt.rows()
		assert rows == [
			[1, 2, 3, 4, 5],
			[6, 7, 8],
			[9],
		]

	def test_columns(self):
		"""Test YoungTableau columns"""
		# Proper case
		yt = YoungTableau("5 + 3 + 1")
		cols = yt.columns()
		assert cols == [
			[1, 6, 9],
			[2, 7],
			[3, 8],
			[4],
			[5],
		]