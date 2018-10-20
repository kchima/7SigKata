import re

class TDDKata:

    def string_calc(self, input):
        # take in a string representing a string of integers separated by some delimeter, return the sum of those ints
        if input == "":
            return 0
        if len(input.split('-')) > 1:
            raise Exception("negatives not allowed")
        total = 0

        if len(input) > 5 and input[0] == '/' and input[1] == '/':

            endIndex = input.find('\n')
            delimString = input[2:endIndex]
            intString = input[endIndex+1:]
            intArray = []
            if input[2] == '[':
                # get multiple delimeters, each of indeterminate length
                delimeters = re.findall(r'\[(.*?)\]', delimString)

                regex = ""
                for delim in delimeters:
                    regex += re.escape(delim) + '|'
                regex = regex[:len(regex)-1]

                # divide the input by my regex to get an array of integers
                intArray = re.split(regex, intString)
            else:
                # if we only have one delim, we can just use the function
                intArray = self.get_valid_array_for_delim(intString, delimString)

            total = self.string_calc_for_delimeter(intArray)
        else:
            intArray = self.get_valid_array_for_delim(input, ',')
            if intArray:
                total = self.string_calc_for_delimeter(intArray)
            else:
                intArray = self.get_valid_array_for_delim(input, '\n')
                total = self.string_calc_for_delimeter(intArray)
        return total

    def string_calc_for_delimeter(self, intArray):
        # takes in an array of ints and returns their sum (only including ints <= 1000)
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

if __name__ == '__main__':
    kata = TDDKata()
    kata.main()