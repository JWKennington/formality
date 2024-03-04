"""Young fused-row group orders"""
from sympy.combinatorics import PermutationGroup, DihedralGroup, SymmetricGroup

from mathtools.comb import partition
from mathtools.comb.young import YoungTableau
from mathtools.groups import young


def check_effect_of_row_fusing_on_orders(n: int):
    """Check the effect of fusing rows on the orders of the resulting groups"""
    data = []

    for p in partition.generate_partitions(n):
        # Create the Young Tableau
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


def main():
    """Main function"""
    data = check_effect_of_row_fusing_on_orders(8)
    for d in data:
        print(d)


if __name__ == '__main__':
    main()
