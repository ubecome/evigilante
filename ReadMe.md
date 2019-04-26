#patrolling_sim

##Description
- Le package patrolling_sim, est un framework basé sur ROS pour la simulation et l'analyse comparative d'algorithmes MRP, utilisé ces dernières années pour étudier le problème de la patrouille. Le cadre proposé permet aux chercheurs d'exécuter, de comparer, d'analyser et d'intégrer de nouveaux algorithmes dans des bancs d'essai de simulation couramment adoptés. Ainsi, il met l’accent sur la coordination entre équipes multi-robots et facilite la préparation d’expériences MRS dans le monde physique avec ROS, en imitant la mise en place d’expériences simulées et en réutilisant le code source

## Dependencies

* Ubuntu 16
* ROS keintec
* [http://wiki.ros.org/patrolling_sim]

#Start Tutorial

1. Installez ROS Kinetic Kame en suivant les instructions fournies à:

[http://wiki.ros.org/kinetic/Installation/Ubuntu]

2. Installez les dépendances nécessaires, en tapant dans le terminal:

$ sudo apt install ros-kinetic-move-base ros-kinetic- amcl ros-kinetic-map-server

3. Configurez votre espace de travail ROS Catkin en tapant dans le terminal:

$ cd ∼/catkin_ws
$ catkin_make
$ source devel/setup.bash

4. Téléchargez et compilez patrolling_sim:

$ cd src
$ git clone https://github.com/davidbsp/patrolling_sim $ 
$ catkin_make

Après avoir téléchargé et compilé avec succès le package patrolling_sim, on peut facilement initier et configurer des expériences de patrouille multi-robots en exécutant le script start_experiment.py

$ rosrun patrolling_sim start_experiment.py

5. Résultat:

Le script déclenche une interface de configuration utilisateur GUI Programming pour Python. Cela permet de configurer facilement des missions de patrouille simulées à l'aide de ROS et de Stage. En particulier, l'interface de configuration permet aux utilisateurs de choisir entre différentes cartes d'environnement, la taille des équipes de robots, des algorithmes de patrouille, des modes de localisation, des modes de navigation, des temps d'attente pour atteindre les objectifs de patrouille et même différents types de terminaux. En raison de l’extensibilité et de la souplesse de la structure de patrouille, l’utilisateur peut facilement ajouter des cartes supplémentaires et des algorithmes de patrouille ...

#Fin Tutorial