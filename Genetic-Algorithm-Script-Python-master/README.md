# Genetic-Algorithm-Script-Python

Written by Konrad Bernaszuk <konradbernaszuk@gmail.com>, December 2018.

# Genetic algorithm with roulette wheel selection
The following program contains a genetic algorithm written as script in python. It was a task from the university.

:package: Installation:

1. Git clone

  ``` git clone https://github.com/Skrzyniec/Genetic-Algorithm-Script-Python.git ```

2. Open project PyCharm or any other ide.

3. Navigate to the /src/ and run from genetic.py

4. Clean build and run.
 
 
:page_facing_up: About:

1. Important settings

``` 
parser.add_argument('-ch', '--numberOfChromosomes', type=int, required=False)
parser.add_argument('-pm', '--mutationPropa', required=False)
parser.add_argument('-pk', '--crossingPropa', required=False)
parser.add_argument('-max', '--maximumIterations', required=False)
parser.add_argument('-f', '--listOfArgs', required=False)
```
- parser, for arguments -f is divided with "," list of args for this funtion

```adaptation[j] = (listOfINTArgs[0] * pow(i, 3)) + (listOfINTArgs[1] * pow(i, 2)) + (listOfINTArgs[2] * i) + listOfINTArgs[3]```

for instance:

``` -ch 6 -pm 1 -pk 80 -max 1000 -f 1,2,4,2 ```

where ```-f 1,2,4,2``` == f(x) = 1 * x^3 +  2 * x^2 +  4 * x + 2

rest of args is easy to understand by they names.


2. The Algorithm

    - Generating the initial population.
    - Calculation of its adaptation for the function f (x).
    - Creating next individuals using the roulette wheel method.
    - Assign generation of new x values for each individual and their binary representation.
    - Execution of crossing in a random place of intersection for unique pairs using the "crossing" method.
    - Performing a mutation at random for each bit of each individual using the "mutation" method.
    - Assigning new X values and binary representation.
    - Calculation of the adaptation value for the individuals thus created.
    - Repeat from point c to the desired stop condition (NUMBER OF ITERATIONS).
