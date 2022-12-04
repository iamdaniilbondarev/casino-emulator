# casino-emulator

#### Приложение, которое решает задачу многорукого бандита на примере игральных кубиков. Рассмотрены два способа:

- [Epsilon greedy](https://en.wikipedia.org/wiki/Greedy_algorithm)
- [Thompson sampling](https://en.wikipedia.org/wiki/Thompson_sampling)

#### Есть три различные стратегии при запуске (задается в файле docker-compose.yaml в сервисе player)

- epsilon_greedy
- thompson_sampling
- all


##### Вероятностные распределния для кубиков расположены в *src/dice_emulator/probability_distributions.json*

##### Для запуска приложения следует в терминале ввести команду *docker-compose up*
