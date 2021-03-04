def num1words(num):
    nums_20_90 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    nums_0_19 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    nums_dict = {100: "hundred", 1000:"thousand", 1000000:"million", 1000000000:"billion"}

    if num < 20:
        return nums_0_19[num]

    if num < 100:
        return nums_20_90[num // 10 - 2] + ("" if num % 10 == 0 else " " + nums_0_19[num % 10])

    maxkey = max([key for key in nums_dict.keys() if key <= num])
    return num1words(num // maxkey) + " " + nums_dict[maxkey] + ("" if num % maxkey == 0 else " " + num1words(num % maxkey))

def num2words(num):
    nums_0_9 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return nums_0_9[num]


if __name__ == "__main__":
    w = input()
    if "." not in w:
        print(num1words(int(w)))
    else:
        p = w.index(".")
        print(num1words(int(w[0:p])), end = "")
        print(" point ", end = "")
        for i in range(p+1, len(w)-1):
            print(num2words(int(w[i])), end = " ")
        print(num2words(int(w[-1])))
