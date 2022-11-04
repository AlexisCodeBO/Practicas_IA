import argparse
import random
from colorama import Fore
from colorama import Style

# -------------------------------- ARGUMENTS

parser = argparse.ArgumentParser()
parser.add_argument('-ch', '--numberOfChromosomes', type=int, required=False)
parser.add_argument('-pm', '--mutationPropa', required=False)
parser.add_argument('-pk', '--crossingPropa', required=False)
parser.add_argument('-max', '--maximumIterations', required=False)
parser.add_argument('-f', '--listOfArgs', required=False)
args = parser.parse_args()

listOfArgss = [x.strip() for x in args.listOfArgs.split(',')]
listOfINTArgs = [int(i) for i in listOfArgss]
sizeOfGenByes = 5


# -------------------------------- METHODS
def debug(variable, helpVairiable):
    return print(f"{Fore.BLUE}@DEBUG {Fore.YELLOW}{helpVairiable}"
                 f" {Fore.YELLOW}\n>>{Style.RESET_ALL} {variable}\n")


def generateRandomGeneration(printIt):
    chromosomeArray = [[0] * sizeOfGenByes for _ in range(args.numberOfChromosomes)]
    for i in range(args.numberOfChromosomes):
        for j in range(0, sizeOfGenByes):
            chromosomeArray[i][j] = random.randint(0, 1)
        if printIt:
            debug(chromosomeArray[i])
    return chromosomeArray


def calcAdaptation(variables):
    adaptation = [None] * args.numberOfChromosomes
    j = 0
    for i in variables:
        adaptation[j] = (listOfINTArgs[0] * pow(i, 3)) + (listOfINTArgs[1] * pow(i, 2)) + (
                listOfINTArgs[2] * i) + listOfINTArgs[3]
        j += 1
    return adaptation


def fromBinaryToDecimal(variables):
    decimalForm = [None] * args.numberOfChromosomes
    j = 0
    for i in variables:
        decimalForm[j] = int("".join(str(x) for x in i), 2)
        j += 1
    return decimalForm


def fromDecimalToBinary(variable):
    binaryForm = list(bin(variable)[2:])
    return [int(i) for i in binaryForm]


def choosingWithRoulette(variables):
    precentagesFromVariables = [None] * args.numberOfChromosomes
    choosenVariables = [None] * args.numberOfChromosomes
    summOfVariables = 0

    for j in variables:
        summOfVariables += j

    for i in range(0, args.numberOfChromosomes):
        precentagesFromVariables[i] = round((variables[i] / summOfVariables * 100), 0)

    for o in range(0, args.numberOfChromosomes):
        rand = random.randint(0, 99)
        summOfPercentages = 0

        for u in range(0, args.numberOfChromosomes):
            summOfPercentages = summOfPercentages + precentagesFromVariables[u]

            if rand <= summOfPercentages:
                choosenVariables[o] = u
                break

            elif 99.0 <= rand <= 110.0:
                choosenVariables[o] = u
                break

    return choosenVariables


def crossing(variables):
    pairs_number = int(int(args.numberOfChromosomes) / 2)
    alreadyChoosen = [None] * args.numberOfChromosomes
    firsttime = True

    afterCrossing = [None] * args.numberOfChromosomes

    for i in range(0, pairs_number):
        p1 = random.randint(0, args.numberOfChromosomes - 1)
        p2 = random.randint(0, args.numberOfChromosomes - 1)

        if firsttime:
            while p2 == p1:
                p2 = random.randint(0, args.numberOfChromosomes - 1)
            alreadyChoosen[p1] = True
            alreadyChoosen[p2] = True
            firsttime = False
        else:
            while alreadyChoosen[p1]:
                p1 = random.randint(0, args.numberOfChromosomes - 1)
            alreadyChoosen[p1] = True

            while alreadyChoosen[p2]:
                p2 = random.randint(0, args.numberOfChromosomes - 1)
            alreadyChoosen[p2] = True

        p1_str = variables[p1]
        p2_str = variables[p2]

        chanceOfCrossing = random.randint(0, 100)
        if chanceOfCrossing > int(args.crossingPropa):
            afterCrossing[p1] = p1_str
            afterCrossing[p2] = p2_str
        elif chanceOfCrossing <= int(args.crossingPropa):
            crossingPlace = random.randint(0, sizeOfGenByes - 1) + 1
            cross = crossingPlace

            for c in range(0, sizeOfGenByes - crossingPlace):
                one = p1_str[cross]
                two = p2_str[cross]
                p1_str[cross] = two
                p2_str[cross] = one
                cross += 1

            afterCrossing[p1] = p1_str
            afterCrossing[p2] = p2_str
    return afterCrossing


def mutation(variables):
    result = list()

    for variable in variables:
        for j in range(0, sizeOfGenByes):
            chance = random.randint(0, 99)
            if chance <= int(args.mutationPropa):
                if variable[j] == 0:
                    variable[j] = 1
                else:
                    variable[j] = 0
        result.append(variable[:])

    return result


# -------------------------------- Tests

firstTimeGeneration = True
for i in range(0, int(args.maximumIterations)):

    print(f"{Fore.RED}_______________________________ NEXT GEN _______________________________ \n{Style.RESET_ALL}")
    if firstTimeGeneration:
        currentGeneration = generateRandomGeneration(False)
        firstTimeGeneration = False
    else:
        currentGeneration = [currentGeneration[i] for i in nextRoulette]

    currentGenDecimal = fromBinaryToDecimal(currentGeneration)
    currentAdaptation = calcAdaptation(fromBinaryToDecimal(currentGeneration))
    nextRoulette = choosingWithRoulette(currentAdaptation)
    currentGeneration = crossing(currentGeneration)
    currentGeneration = mutation(currentGeneration)

    debug(currentGenDecimal, "DECIMAL")
    debug(currentGeneration, "BINARY")
    debug(currentAdaptation, "ADAPTATION")
