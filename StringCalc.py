class TDDKata:

    def string_calc(self, input):
        if len(input.split('-')) > 1:
            raise Exception("negatives not allowed")
        total = 0
        if input == "":
            return 0
        if len(input) > 5 and input[0] == '/' and input [1] == '/':
            endIndex = input.find('\n')
            delim = input[2:endIndex]
            print delim
            intArray = self.get_valid_array_for_delim(input[endIndex:], delim)
            total = self.string_calc_for_delimeter(intArray, delim)
        else:
            intArray = self.get_valid_array_for_delim(input, ',')
            if intArray:
                total = self.string_calc_for_delimeter(intArray, ',')
            else:
                intArray = self.get_valid_array_for_delim(input, '\n')
                total = self.string_calc_for_delimeter(intArray, '\n')
        return total

    def string_calc_for_delimeter(self, intArray, delim):
        total = 0
        for integer in intArray:
            value = int(integer)
            if value <= 1000:
                # ignore integers > 1000
                total += value
        return total

    def get_valid_array_for_delim(self, input, delim):
        # if input is convertible to a valid int array using our delimeter, return the array. Otherwise, return False
        intArray = input.split(delim)
        try:
            int(intArray[0])
        except:
            return False
        return intArray


    def main(self):
        self.string_calc("1,2")

if __name__ == '__main__':
    kata = TDDKata()
    kata.main()