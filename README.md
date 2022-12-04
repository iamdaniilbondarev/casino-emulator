# casino-emulator

#### Приложение, которое решает задачу [многорукого бандита](https://en.wikipedia.org/wiki/Multi-armed_bandit) на примере игральных кубиков. Рассмотрены два способа:

- Epsilon greedy
- Thompson sampling

#### Есть три различные стратегии при запуске (задается в файле docker-compose.yaml в сервисе player)

- epsilon_greedy
- thompson_sampling
- all


##### Вероятностные распределния для кубиков расположены:
```
src/dice_emulator/probability_distributions.json
```

##### Для запуска приложения следует в терминале ввести команду:
```
docker-compose up
```
