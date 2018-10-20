class TDDKata:

    def string_calc(self, input):
        intArray = input.split(',')
        total = 0

        if self.array_has_ints(intArray):
            for integer in intArray:
                total += int(integer)
        else:
            intArray = input.split('\n')
            if self.array_has_ints(intArray):
                for integer in intArray:
                    total += int(integer)
        return total

    def array_has_ints(self, array):
        try:
            int(array[0])
        except:
            return False
        return True


    def main(self):
        self.string_calc("1,2")

if __name__ == '__main__':
    kata = TDDKata()
    kata.main()