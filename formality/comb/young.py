"""Utilities for working with Young Tableaus and partitions
"""

from typing import Union, List

from sympy.combinatorics import IntegerPartition

from maths.comb import partition


class YoungTableau:
    """Class for Young Tableau"""

    def __init__(self, p: Union[str, List[int]], zero_indexed: bool = False):
        """Create a Young Tableau

        Args:
            p:
                str or List[int], partition notation or list of partition segment sizes
            zero_indexed:
                bool, if True, the values are zero-indexed
        """
        if isinstance(p, str):
            self._p = partition.from_str(p)
        elif isinstance(p, list):
            self._p = IntegerPartition(p)
        else:
            raise ValueError("Invalid input type")
        self.zero_indexed = zero_indexed

    def __str__(self):
        """String representation"""
        return f'YT({partition.to_str(self._p)})'

    def rows(self) -> List[List[int]]:
        """Get the rows of the Young Tableau

        Returns:
            List[List[int]]: list of rows
        """
        return partition.values(self._p, zero_indexed=self.zero_indexed)

    def columns(self) -> List[List[int]]:
        """Get the columns of the Young Tableau

        Returns:
            List[List[int]]: list of columns
        """
        rows = self.rows()
        cols = []
        for i in range(len(rows[0])):
            col = []
            for row in rows:
                if i < len(row):
                    col.append(row[i])
            cols.append(col)
        return cols
