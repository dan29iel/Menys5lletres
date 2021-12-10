def main():
    state = "Practica els problemes de list comprehnsion sper a ser Pythonic!"

    consonants = [i for i in state.split() if len(i) < 6]

    print(consonants)

if __name__ == '__main__':
    main()

