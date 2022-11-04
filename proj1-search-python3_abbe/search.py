# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    from util import Stack

    # iniciar la pila vacía 
    stackXY = Stack()

    visitados= [] # Estados visitados
    path = [] # Cada estado mantiene su camino desde el estado inicio

    # Vigila si el estado inicial es el objetivo #
    if problem.isGoalState(problem.getStartState()):
        return []

    # Empieza desde el inicio y encuentra una solución, el camino es una lista vacía #
    stackXY.push((problem.getStartState(),[]))

    while(True):

        # Condicion: no se puede encontrar una solución #
        if stackXY.isEmpty():
            return []

        # Obtener información del estado actual #
        xy,path = stackXY.pop() # Tomar posición y camino
        visitados.append(xy)

        # Esto funciona para el autograder    #
        # Comprobamos si el estado es un objetivo cuando encontramos sucesores #

        # Condicion final: alcanzar la meta #
        if problem.isGoalState(xy):
            return path

        # Obtener sucesores del estado actual #
        succ = problem.getSuccessors(xy)

        # Agregar nuevos estados en la pila y arreglar el camino #
        if succ:
            for item in succ:
                if item[0] not in visitados:

                # if item[0] not in visited and item[0] not in (state[0] for state in stackXY.list):
                #   if problem.isGoalState(item[0]):
                #       return path + [item[1]]

                    newPath = path + [item[1]] # Calcular nuevo camino
                    stackXY.push((item[0],newPath))
    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    from util import Queue

    # queueXY: ((x,y),[camino]) #
    queueXY = Queue()

    visitados = [] # Estados visitados
    path = [] # Cada estado mantiene su ruta/camino desde el estado inicial

    # Comprueba si el estado inicial es el estado objetivo #
    if problem.isGoalState(problem.getStartState()):
        return []

    # Comienza desde el principio y encuentra una solucion, la ruta/camino es una lista vacia #
    queueXY.push((problem.getStartState(),[]))

    while(True):

        # Condicion terminada: no pudo encontrar una solucion #
        if queueXY.isEmpty():
            return []

        # Obtener informacion del estado actual #
        xy,path = queueXY.pop() # Tomar posicion y camino
        visitados.append(xy)

        # Comment this and uncomment 179. This is only works for autograder
        # En las conferencias comprobamos si un estado es un objetivo cuando encontramos sucesores

        # Condicion terminada: alcanzar la meta #
        if problem.isGoalState(xy):
            return path

        # Obtenga sucesores del estado actual #
        succ = problem.getSuccessors(xy)

        # Agregue nuevos estados en la cola y arregle su ruta #
        if succ:
            for item in succ:
                if item[0] not in visitados and item[0] not in (state[0] for state in queueXY.list):

                    # Lectures code:
                    # Todas la implementaciones se ejecutan en autograder y en los comentarios que escribo
                    # El codigo apropiado que me ha enseñado en conferencias
                    # if problem.isGoalState(item[0]):
                    #   return path + [item[1]]

                    newPath = path + [item[1]] # Calcular nueva ruta
                    queueXY.push((item[0],newPath))
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    from util import PriorityQueue

    # queueXY: ((x,y),[camino],prioridad) #
    queueXY = PriorityQueue()

    visitados = [] # Estados visitados
    path = [] # Cada estado mantiene su camino desde el estado inicial

    # Comprueba si el estado inicial es el estado objetivo #
    if problem.isGoalState(problem.getStartState()):
        return []

    # Comienza desde el principio y encuentra una solucion, la ruta es una lista vacia #
    # con la prioridad mas barata, costo                                       #
    queueXY.push((problem.getStartState(),[]),0)

    while(True):

        # Condicion terminada: no pudo encontra una solucion #
        if queueXY.isEmpty():
            return []

        # Obtener informacion del estado actual #
        xy,path = queueXY.pop() # Tomar posicion y camino
        visitados.append(xy)

        # This only works for autograder    #
        # En las conferencias comprobamos si un estado es un objetivo cuando encontramos sucesores #

        # Condicion terminada: alcanzar la meta #
        if problem.isGoalState(xy):
            return path

        # Obtener sucesores del estado actual #
        succ = problem.getSuccessors(xy)

        # Agregue nuevos estados en la cola y arregle su ruta #
        if succ:
            for item in succ:
                if item[0] not in visitados and (item[0] not in (state[2][0] for state in queueXY.heap)):

                    #    Como algoritmos anteriores: deberiamos comprobar en este punto si el sucesor
                    #    es un estado objetivo para seguir el codigo de las conferencias

                    newPath = path + [item[1]]
                    pri = problem.getCostOfActions(newPath)

                    queueXY.push((item[0],newPath),pri)

                # Estado está en la cola. Compruebe si la ruta actual es más barata que la anterior #
                elif item[0] not in visitados and (item[0] in (state[2][0] for state in queueXY.heap)):
                    for state in queueXY.heap:
                        if state[2][0] == item[0]:
                            oldPri = problem.getCostOfActions(state[2][1])

                    newPri = problem.getCostOfActions(path + [item[1]])

                    if oldPri > newPri:
                    # El estado es mas barato con su nuevo padre-> actualizar y arreglar el padre #
                        newPath = path + [item[1]]
                        queueXY.update((item[0],newPath),newPri)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

from util import PriorityQueue
class MyPriorityQueueWithFunction(PriorityQueue):
    """
    Implements a priority queue with the same push/pop signature of the
    Queue and the Stack classes. This is designed for drop-in replacement for
    those two classes. The caller has to provide a priority function, which
    extracts each item's priority.
    """
    def  __init__(self, problem, priorityFunction):
        "priorityFunction (item) -> priority"
        self.priorityFunction = priorityFunction      # store the priority function
        PriorityQueue.__init__(self)        # super-class initializer
        self.problem = problem
    def push(self, item, heuristic):
        "Adds an item to the queue with priority from the priority function"
        PriorityQueue.push(self, item, self.priorityFunction(self.problem,item,heuristic))

# Calculate f(n) = g(n) + h(n) #
def f(problem,state,heuristic):

    return problem.getCostOfActions(state[1]) + heuristic(state[0],problem)

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    # queueXY: ((x,y),[camino]) #
    queueXY = MyPriorityQueueWithFunction(problem,f)

    path = [] # Cada estado mantiene su camino desde el estado inicial
    visitados = [] # Estados visitados


    # Compruebe si el estado inicial es el estado objetivo #
    if problem.isGoalState(problem.getStartState()):
        return []

    # Agregue el estado inicial. La ruta es una lista vacia #
    element = (problem.getStartState(),[])

    queueXY.push(element,heuristic)

    while(True):

        # Condicion terminada. no pudo encontrar una solucion #
        if queueXY.isEmpty():
            return []

        # Obtenga informacion del estado actual #
        xy,path = queueXY.pop() # Tomar posicion y camino

        # El estado ya ha sido visitado. Un camino con menor costo ha sido previamente
        # encontrado. Sobrepasar este estado
        if xy in visitados:
            continue

        visitados.append(xy)

        # Condicion terminada: alcanzar la meta #
        if problem.isGoalState(xy):
            return path

        # Obtener sucesores del estado actual #
        succ = problem.getSuccessors(xy)

        # Agregue nuevos estados en la cola y arregle su ruta #
        if succ:
            for item in succ:
                if item[0] not in visitados:

                    # Como algoritmos anteriores: deberiamos comprobar este punto si el sucesor
                    # es un estado objetivo para seguir el codigo de las conferencias

                    newPath = path + [item[1]] # Arreglar la ruta
                    element = (item[0],newPath)
                    queueXY.push(element,heuristic)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
