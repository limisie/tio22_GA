# Genetic Algorithm for Graph Coloring
A genetic algorithm was implemented to solve the graph coloring problem. The algorithm was compared to other algorithms for the Mycielski-4 and Mycielski-5 graphs. See `Algorytm genetyczny - problem kolorowania grafu.ipynb` for the research.

## Methods 
The genetic algorithm employs three main operators

**Selection**: This operator identifies individuals to be included in the next generation. Several selection strategies are available, including:
- Random selection,
- Tournament selection,
- Roulette Wheel selection,
- Universal stochastic sampling (SUS).

 **Crossover**: This operator combines two parent individuals to form new offspring. Various crossover strategies are available, including:
- Single-point crossover,
- Multipoint crossover,
- Uniform crossover.

 **Mutation**: This operator introduces random changes to individuals to maintain genetic diversity. Different mutation strategies are available, including: 
- Random,
- Swap,
- Inversion,
- Scramble.

## Experiments

General genetic algorithm experiments:
- effect of population size,
- influence of crossover operator,
- impact of mutation operator,
- evolution dynamics.

Research on genetic operators:
- differences between selection operators,
- differences between crossover operators,
- differences between mutation operators.

Comparing results with Graph Coloring benchmarks.
