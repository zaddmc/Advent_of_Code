"""Day3 of AoC in python"""

# pylint: disable-msg=C0103
with open("../../input/day3.txt", "r", encoding="utf-8") as data:
    prev_letters = ""
    comma_flag = False
    val1 = ""
    val2 = ""
    product_sum = 0
    product_sum_enb = 0
    enabled_flag = True
    for letter in data.read():
        if prev_letters == "do(" and letter == ")":
            enabled_flag = True
            print("Enabled")
            prev_letters = ""
            continue
        if prev_letters == "don't(" and letter == ")":
            enabled_flag = False
            print("Disabled")
            prev_letters = ""
            continue

        if prev_letters[0:4] == "mul(":
            if letter.isdigit():
                prev_letters += letter
                if comma_flag:
                    val2 += letter
                else:
                    val1 += letter
                continue
            if letter == ",":
                prev_letters += letter
                comma_flag = True
                continue
            if letter == ")":
                prev_letters += letter
                if val2 == "":
                    continue
                print(f"{prev_letters}, val1 = {val1}, val2 = {val2}", end="")
                product = int(val1) * int(val2)
                print(f", product = {product}")
                product_sum += product
                if enabled_flag:
                    product_sum_enb += product

            prev_letters = ""
            comma_flag = False
            val1 = ""
            val2 = ""
            continue

        prev_letters += letter
        try:
            if "mul(".index(prev_letters, 0, 100) == 0:
                continue
        except:
            pass
        try:
            if "do()".index(prev_letters, 0, 100) == 0:
                continue
        except:
            pass
        try:
            if "don't()".index(prev_letters, 0, 100) == 0:
                continue
        except:
            pass

        prev_letters = ""
    print(product_sum)
    print(product_sum_enb)
