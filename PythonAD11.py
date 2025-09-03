#Python Genetic Algorithm for Optimization

#Write a Python program to implement a genetic algorithm for solving optimization problems.

# Import the random module for generating random numbers
import random
# Import the numpy module for numerical operations
import numpy as np

# Problem definition: Example function to optimize (e.g., Rastrigin function)
def rastrigin(x):
    # Define the constant A
    A = 10
    # Compute the Rastrigin function value for the input x
    return A * len(x) + sum([(xi**2 - A * np.cos(2 * np.pi * xi)) for xi in x])

# GA Parameters
# Set the population size
population_size = 100
# Set the genome length (number of genes in a chromosome)
genome_length = 10
# Set the crossover rate
crossover_rate = 0.8
# Set the mutation rate
mutation_rate = 0.01
# Set the number of generations
num_generations = 100
# Define the bounds for the gene values
bounds = [-5.12, 5.12]

# Initialization
def initialize_population(pop_size, genome_len, bounds):
    # Generate a population of random individuals within the given bounds
    return [np.random.uniform(bounds[0], bounds[1], genome_len) for _ in range(pop_size)]

# Fitness function
def evaluate_fitness(population):
    # Evaluate the fitness of each individual in the population using the Rastrigin function
    return [rastrigin(individual) for individual in population]

# Selection (Tournament Selection)
def tournament_selection(population, fitness, tournament_size=3):
    # Initialize the list of selected individuals
    selected = []
    # Select individuals based on tournament selection
    for _ in range(len(population)):
        # Choose random aspirants for the tournament
        aspirants = [random.randint(0, len(population) - 1) for _ in range(tournament_size)]
        # Select the individual with the best fitness among the aspirants
        selected.append(min(aspirants, key=lambda aspirant: fitness[aspirant]))
    # Return the selected individuals
    return [population[i] for i in selected]

# Crossover (Single Point Crossover)
def single_point_crossover(parent1, parent2):
    # Perform crossover with a given probability
    if random.random() < crossover_rate:
        # Choose a random crossover point
        point = random.randint(1, len(parent1) - 1)
        # Create children by combining the parents at the crossover point
        child1 = np.concatenate([parent1[:point], parent2[point:]])
        child2 = np.concatenate([parent2[:point], parent1[point:]])
        # Return the children
        return child1, child2
    # If no crossover, return the parents as is
    return parent1, parent2

# Mutation
def mutate(individual, mutation_rate, bounds):
    # Mutate each gene with a given probability
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            # Replace the gene with a random value within the bounds
            individual[i] = np.random.uniform(bounds[0], bounds[1])
    # Return the mutated individual
    return individual

# Genetic Algorithm
def genetic_algorithm():
    # Initialize the population
    population = initialize_population(population_size, genome_length, bounds)
    
    # Iterate over the number of generations
    for generation in range(num_generations):
        # Evaluate the fitness of the population
        fitness = evaluate_fitness(population)
        
        # Selection
        # Select individuals based on their fitness
        selected_population = tournament_selection(population, fitness)
        
        # Crossover
        # Create the next generation through crossover
        next_population = []
        for i in range(0, len(selected_population), 2):
            parent1 = selected_population[i]
            parent2 = selected_population[min(i + 1, len(selected_population) - 1)]
            child1, child2 = single_point_crossover(parent1, parent2)
            next_population.extend([child1, child2])
        
        # Mutation
        # Mutate the individuals in the next generation
        population = [mutate(individual, mutation_rate, bounds) for individual in next_population]
        
        # Evaluation
        # Re-evaluate the fitness of the new population
        fitness = evaluate_fitness(population)
        # Find the best fitness and corresponding individual
        best_fitness = min(fitness)
        best_individual = population[fitness.index(best_fitness)]
        
        # Print the best fitness of the current generation
        print(f'Generation {generation + 1}: Best Fitness = {best_fitness}')
    
    # Return the best individual found
    return best_individual

# Uncomment the line below to run the genetic algorithm
best_solution = genetic_algorithm()
# Print the best solution found
print("Best solution found:", best_solution)


