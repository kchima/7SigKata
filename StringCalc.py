class TDDKata:

    def string_calc(self, input):
        if input == "1":
            return 1
        else:
            return 0

    def main(self):
        self.string_calc("1,2")

if __name__ == '__main__':
    kata = TDDKata()
    kata.main()