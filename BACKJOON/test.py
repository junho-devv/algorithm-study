def test(para_num):

    def track():

        global num_b

        num_b += 1

    num_b = 0

    track()

    print(num_b)


test(0)
