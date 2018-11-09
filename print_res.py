def print_tbl(rs):
    import prettytable
    from numpy import around

    x = prettytable.PrettyTable()

    x.field_names = ['k', "x_k", "x_k+1", "x_k+1 - x_k",
                     "y_k", "y_k+1", "y_k+1 - y_k",
                     "z_k", "z_k+1", "z_k+1 - z_k"]

    for i in range(len(rs)):
        around(rs[i], decimals=3)
    for i in range(1, len(rs)):
        x.add_row([i, rs[i-1][0][0], rs[i][0][0], (rs[i][0][0] - rs[i-1][0][0]),
                      rs[i-1][1][0], rs[i][1][0], (rs[i][1][0] - rs[i-1][1][0]),
                      rs[i-1][2][0], rs[i][2][0], (rs[i][2][0] - rs[i-1][2][0])])

    print(x)


