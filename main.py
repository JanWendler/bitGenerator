# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import sys;


# Press the green button in the gutter to run the script.
def generateBitEnum(numberOfBits):
    output = "enum { \n"
    padding = math.ceil(numberOfBits / 4)
    for number in range(0, numberOfBits):
        value = 2 ** number
        hexValue = f"0x{value:0{padding}X}"
        if number == numberOfBits - 1:
            output += "\tbit" + str(number) + " = " + hexValue + "\n"
        else:
            output += "\tbit" + str(number) + " = " + hexValue + ",\n"
    output += "};\n"
    return output


if __name__ == '__main__':
    numberOfBits = 32  # sys.argv[0]
    outputFilePath = "C:/Users/jan.wendler/PycharmProjects/bitGenerator/output.txt"  # sys.argv[1]
    output = generateBitEnum(numberOfBits)
    with open(outputFilePath, "w") as file:
        file.write(output)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
