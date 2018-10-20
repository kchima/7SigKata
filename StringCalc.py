class TDDKata:

    def string_calc(self, input):
        if input == "":
            return 0
        return int(input)


    def main(self):
        self.string_calc("1,2")

if __name__ == '__main__':
    kata = TDDKata()
    kata.main()