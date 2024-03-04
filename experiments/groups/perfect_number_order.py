"""Young fused-row group orders for perfect numbers and partitions of factors"""

import functools
import operator

from sympy.combinatorics import DihedralGroup, SymmetricGroup
from sympy.ntheory import factor_ as factor

from maths.comb.young import YoungTableau
from maths.groups import young, iso


def generate_perfect_partitions(max_n: int):
    """Generate partitions of perfect numbers"""
    data = []
    for n in range(max_n):
        if factor.is_perfect(n):
            print(f"Perfect number: {n}")
            p = list(sorted(factor.divisors(n)[:-1], reverse=True))
            yt_p = YoungTableau(p)

            data.append([
                p,
                young.group(yt_p).order(),
                young.group(yt_p, include_fused_rows=True, include_cols=False).order(),
                young.group(yt_p, include_fused_rows=False, include_cols=False).order(),
                DihedralGroup(n).order(),  # 2 * n
                SymmetricGroup(n).order(),  # n!
            ])

    return data


def generate_square_tableaus(max_n: int):
    """Generate partitions of perfect numbers"""
    data = [('Partition', 'Group', 'Group (fused rows)', 'Group (no fused rows)', 'Dihedral', 'Symmetric')]
    for n in range(2, max_n):
        p = n * [n]
        N = sum(p)
        yt_p = YoungTableau(p)

        data.append([
            p,
            young.group(yt_p, include_fused_rows=False, include_cols=False).order(),
            young.group(yt_p, include_fused_rows=True, include_cols=False).order(),
            young.group(yt_p).order(),
            DihedralGroup(N).order(),  # 2 * n
            SymmetricGroup(N).order(),  # n!
        ])

    return data


def generate_rlen_2_tableaus(max_n: int):
    """Generate partitions of perfect numbers"""
    data = [('Partition', 'Group', 'Group (fused rows)', 'Group (no fused rows)', 'Dihedral', 'Symmetric')]
    for n in range(2, max_n):
        p = n * [2]
        K = functools.reduce(operator.mul, p, 1)
        yt_p = YoungTableau(p)

        yg = young.group(yt_p, include_fused_rows=False, include_cols=False)
        dg = DihedralGroup(K // 2)

        data.append([
            p,
            yg.order(),
            dg.order(),
            iso.is_iso_possible(yg, dg),
        ])

    return data


def main():
    """Main function"""
    data = generate_rlen_2_tableaus(9)
    for d in data:
        print(d)


if __name__ == '__main__':
    main()
