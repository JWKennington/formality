"""Young fused-row group orders



Conclusions:

    Orders:
    - |Y(p)| = N!, where N = sum(p)
    - |Y(p)_RO| = Prod(p_i!), where p_i are the parts of the partition p
    - |Y(p)_R| = |Y(p)_RO| * Prod(q_i!), where q_i is the number of rows with length i in the partition p

"""
import pandas
from sympy.combinatorics import DihedralGroup, SymmetricGroup

from maths.comb import partition
from maths.comb.young import YoungTableau
from maths.groups import young


def check_effect_of_row_fusing_on_orders(n: int):
    """Check the effect of fusing rows on the orders of the resulting groups"""
    data = []

    for p in partition.generate_partitions(n):
        # Create the Young Tableau
        yt_p = YoungTableau(p)

        o_y = young.group(yt_p).order()
        o_yr = young.group(yt_p, include_fused_rows=True, include_cols=False).order()
        o_y_r2 = young.group(yt_p, include_fused_rows=False, include_cols=False).order()


        data.append([
            p,
            o_y,
            o_yr,
            o_y_r2,
            o_y / o_yr,
            o_y / o_y_r2,
            DihedralGroup(n).order(),  # 2 * n
            SymmetricGroup(n).order(),  # n!
        ])

    return data


def check_row_fused_subgroup_order(n: int):
    """Check the effect of fusing rows on the orders of the resulting groups"""
    data = []

    for k in range(2, n + 1):
        # Create the Young Tableau

        p = k * [2]
        yt_p = YoungTableau(p)

        o_y = young.group(yt_p).order()
        o_yr = young.group(yt_p, include_fused_rows=True, include_cols=False).order()
        o_y_r2 = young.group(yt_p, include_fused_rows=False, include_cols=False).order()


        data.append([
            p,
            o_y,
            o_yr,
            o_y_r2,
            int(o_y / o_yr),
            int(o_y / o_y_r2),
            DihedralGroup(n).order(),  # 2 * n
            SymmetricGroup(n).order(),  # n!
        ])

    return pandas.DataFrame(data, columns=[
        'Partition',
        'Yk2',
        'Yk2R',
        'Yk2RO',
        'Yk2 / Yk2R',
        'Yk2 / Yk2RO',
        'Dihedral',
        'Symmetric',
    ])



def main():
    """Main function"""
    data = check_row_fused_subgroup_order(8)
    print(data)


if __name__ == '__main__':
    main()
