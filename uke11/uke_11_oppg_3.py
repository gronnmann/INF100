def select_pass(id_col, pass_fail_col):
    return [x[0] for x in zip(id_col, pass_fail_col) if x[1] == 1]
