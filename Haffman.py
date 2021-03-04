def main(x):
    # x is not alpahbet but number.
    num = [x.count(str(k)) for k in range(10)]
    huffman = {k: "null" for k in range(10)}
    for i in range(10):
        t = max(num)
        if t <= 0:
            if i > 1:
                huffman[p] = "1" * (i - 1)
            break
        p = num.index(t)
        huffman[p] = "1" * i + "0"
        num[p] = -1
    for i in range(10):
        print("{} {}".format(i, huffman[i]))
    """ This program has fatal weakness.
        It is length is too long, and average length is not shortest."""

    
if __name__ == '__main__':
    x = input()
    main(x)
