import random

def sum_fitness(population):
	result = 0
	for individual in population:
		result += individual.get_fitness()

	return result

def selection_probability(population):
    sum_fitness_population = sum_fitness(population)
    min_q = 0 # xác xuất tích lũy
    max_q = 0
    probability = []
    for i in range(0, len(population)):
        p = population[i].get_fitness()/sum_fitness_population
        max_q += p
        probability.append([min_q, max_q])
        min_q = max_q

    return probability

def selection_chromosomes(population):
    probability = selection_probability(population)
    
    num_random = random.random()
    for i in range (0, len(probability)):
            if probability[i][0] <= num_random and probability[i][1] >= num_random:
                individual_choice = population[i]
                break

    return individual_choice
       