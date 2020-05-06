from maze.generation.growingtree import GrowingTree
from maze.mazedata.board import Board
from maze.mazedata.constants import *
import random
from math import sqrt


class GeneticSolver():
    """Solve the maze using a genetic algorithm.

    TODO: Improve description

    Attributes:
        board (Board): the pre-made maze to solve
        pop_size (int): the size of the population
        population (int[][]): the current population, represented as
            lists of ints encoding organism movement
        mutation_chance (float): chance of mutation on
            reproduction (default: 50%)
        move_limit (int): maximum number of moves an organism can make
        min_score (int): minimum acceptable score for an organism (default: 2)
        seed (int): seed for randomness (default: None)
    """

    def __init__(self, board, size, chance=0.5, min_score=2, seed=None):
        self.board = board
        random.seed(seed)
        self.pop_size = size
        self.mutation_chance = chance  # pre-made maze to solve
        self.min_score = min_score
        self.move_limit = int(sqrt(self.board.height * self.board.width) * 3)

        # initialize population
        self.population = [[random.randint(0, 4) for i
                            in range(self.move_limit)] for j
                           in range(self.pop_size)]
        # sort population by fitness
        self.population.sort(key=lambda g: self.fitness(g))

    def fitness(self, organism):
        """Determine the fitness of the given organism

        Use manhattan distance (d = |(x2-x1)| + |(y2-y1)|) as well as a
        "penalties" to determine fitness. Lower numbers = better fitness.
        Penalties are determined by 2 factors:
            - Number of moves that run into a wall
            - Number of moves that do nothing

        Organisms are given as lists of numbers, representing their
        DNA. Each DNA list contains integer genes, which corresond to
        movements on the board.

        Args:
            organism (int[]): the organism to be tested.

        Returns:
            The fitness score for the given organism
        """
        # reset the player location
        self.board.reset_player()

        # Encodes the genes into movements:
        # 0 = No Movement
        # 1 = Move Up
        # 2 = Move Down
        # 3 = Move Right
        # 4 = Move Left
        gene_encoder = {
            0: (0, 0),
            1: NORTH,
            2: SOUTH,
            3: EAST,
            4: WEST
        }

        # Initial penalties
        penalties = 0

        for g in organism:
            d = gene_encoder.get(g, (0, 0))
            move = self.board.move_player(d)
            if (not move):
                penalties += 1

        finish = self.board.end_node
        end = self.board.player

        return abs(finish[0] - end[0]) + abs(finish[1] - end[1]) + penalties

    def breed(self, first_parent, second_parent):
        """Breed the two organisms

        Breeds two parent organism and returns a new child organism.
        The DNA of the new organism is comprised of some
        combination of the two parents DNA. There is also a change
        gene mutation that is dependent on the mutation chance
        attribute passed in on class construction.

        Args:
            first_parent (int[]): DNA representing the first parent
            second_parent (int[]): DNA representing the second parent

        Returns:
            (int[]): Possibly mutated new organism
        """
        crossover_point = random.randint(0, self.move_limit - 1)

        offspring = first_parent[:crossover_point]
        offspring.extend(second_parent[crossover_point:])

        return self.mutate(offspring)

    def mutate(self, offspring):
        """Mutate the given organism DNA

        Mutates the DNA based on self.mutation_chance. If the gene
        gets mutated, a single gene will be changed into another random
        gene.

        Args:
            offspring (int[]): DNA to possibly mutate

        Returns:
            int[]: DNA that has been mutated
        """
        if (random.random() <= self.mutation_chance):
            offspring[random.randint(0, self.move_limit-1)
                      ] = random.randint(0, 4)
        return offspring

    def new_population(self):
        """Make a new population using the fittest parents

        Removes half (TODO: make this variable) of the current
        population and repopulates using the existing members as the
        parents.

        Note: Assumes that self.population is already sorted in order
        of increasing score (decreasing fitness)
        """
        # create new population
        fittest = self.population[:int(self.pop_size / 2)]
        new_population = []
        new_population.extend(fittest)

        while (len(new_population) < self.pop_size):
            # choose 2 parents (does allow for asexual reprod)
            first = random.choice(fittest)
            second = random.choice(fittest)
            child = self.breed(first, second)

            new_population.append(child)

        # replace the old population
        self.population = new_population
        self.population.sort(key=lambda g: self.fitness(g))

    def simulate(self):
        """Simulate the population and evolution

        Runs the genetic algorithm, terminating when the fittest member
        of the population can complete the maze with a score that is
        <= self.min_score

        Returns:
            (int[]): The DNA of the fittest organism that can complete
                the maze in the "best" way.
        """
        generations = 0
        while (self.fitness(self.population[0]) > self.min_score):
            self.new_population()
            generations += 1

        print("Satisfactory solution found in ", generations, " generations.")
        return self.population[0]
