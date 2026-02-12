from checkmate import checkmate


def main():
    board = """\
....
....
.P..
..K."""

    result = checkmate(board)
    print(result)


if __name__ == "__main__":
    main()

#R...
#.K..
#..P.
#...."""