# casino-emulator

#### Application for solving [the Multi-Armed Bandit problem](https://en.wikipedia.org/wiki/Multi-armed_bandit). Considered two ways of solving:

- Epsilon greedy
- Thompson sampling

#### There are three strategies to run programm (should be set in docker-compose.yaml in the player service)

- epsilon_greedy
- thompson_sampling
- all


##### Path to the dice probability distributions:
```
src/dice_emulator/probability_distributions.json
```

##### To start application you should run:
```
docker-compose up
```
