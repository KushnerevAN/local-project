class NewInt(int):
    pass

    def repeat(self, n=2):
        res = ''
        for i in range(n):
            res += str(self)
        return int(res)

    def to_bin(self):
        return int(bin(self)[2:])


c1 = NewInt(9)
assert isinstance(c1, NewInt)
assert issubclass(NewInt, int)
assert c1 + 9 == 18
assert c1 * 9 == 81

c2 = NewInt(31)
assert c2.repeat() == 3131
assert c2.repeat(4) == 31313131
assert NewInt(16).to_bin() == 10000
assert NewInt(14).to_bin() == 1110

print('Good')
