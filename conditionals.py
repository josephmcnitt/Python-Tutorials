#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 1000, 1000
    lt = 'x is less than y'
    eq = 'x is the same as y'
    gt = 'x is greater than y'

    # # conditional flow uses if, elif, else
    # if x < y:
    #     result = lt
    # elif x==y:
    #     result = eq
    # else:
    #     result = gt

    # print(result)

    # # conditional statements let you use "a if C else b"
    # result = lt if x < y else gt
    # print(result)

    # match-case makes it easy to compare multiple values
    value = "one"
    match value:
        case "one":
            result = 1
        case 'two':
            result = 2
        case 'three'|'four':
            result = (3,4)
        case _:
            result = -1
    print(result)

if __name__ == "__main__":
    main()
