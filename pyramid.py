def get_bricks(rows):

    if rows <= 0:
        return 0
    return rows + get_bricks(rows - 1)

    print(rows)

get_bricks(10)