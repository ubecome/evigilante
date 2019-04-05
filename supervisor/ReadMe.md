#bringup

- L’objectif est de lire et d’exécuter un patrolling, à partir d'un fichier de conf param.yaml en JSON format .

#Start Tutorial

##Description
- Ce projet contient plusieurs repertoires :
[config] : Contient un input file patrol.yaml avec une liste de points atteignable de la carte du turtlesim.
[msg] : Contient les 3 Msg : Goal.msg, Patrol.msg et Patrolling.msg qui  devrait contenir les listes des Goal et du Patrol.
[launch] : Contient un launch File qui permet de lancer le node Turtlesim , faire l'appel des paramètres server rosparam dans l’environement ROS ainsi que de lancer les scripts de supervision.
[AlbumPhoto] : Contient quelques exemples de simulation du Turtlesim_node.
[src] : Contient les fichiers sources.
[supervisor] : Contient des outils de supervision python :

1. yamlreader.py :

Un script python qui permet à la fois de jouer le rôle d’un ParserYaml et un Talker . Cet noeud permet d'extraire les données d’un fichier patrol.yaml puis le transmettre vers le message crée /bringup/Goal.msg.

2. custom_listener.py :

Un noeud Listener afin de verifier que les valeurs sont bien transmis a travers un topic vers le message .

3. gotogoal.py :

Cette noeud combine le Listener des goals et le controle du Turtlesim . Donc,il récupére les valeurs et le transmettre au message comme un Goal Point et le transmettre vers un topic au Turtlesim afin de bouger.
#Avant de Tester le code
On doit rendre les 3 scripts exucutables :

$ chmod u+x ~/catkin_ws/src/bringup/supervisor/yamlreader.py
$ chmod u+x ~/catkin_ws/src/bringup/supervisor/custom_listener.py
$ chmod u+x ~/catkin_ws/src/bringup/supervisor/gotogoal.py


#Testing the code
Ouvrer le terminal, run:
$ roscore

dans un autre terminal, run:

$ cd catkin_ws/
$ source devel/setup.bash
$ roslaunch bringup software_bringup.launch 

 Cela va lancer le Turtlsim node ainsi les parametres server rosparam. Vous devez trouvez une chose similaire a ca :
[====================================================== OutputConsole==========================================================================]
started roslaunch server http://tayssir-VirtualBox:41975/

SUMMARY
========

PARAMETERS
 * /duration_minutes: 66
 * /goals: [{'action': 'SNAP...
 * /name: Data center patro...
 * /rosdistro: melodic
 * /rosversion: 1.14.3

NODES
  /
    Gotogoal_Listener (bringup/gotogoal.py)
    Talker (bringup/yamlreader.py)
    turtle_bringup (turtlesim/turtlesim_node)

ROS_MASTER_URI=http://localhost:11311

process[turtle_bringup-1]: started with pid [5216]
process[Gotogoal_Listener-2]: started with pid [5217]
process[Talker-3]: started with pid [5218]
======Start Listener===========
Loading Yaml File :

{'duration_minutes': 66, 'name': 'Data center patrolling', 'goals': [{'action': 'SNAP', 'position': {'y': 10, 'x': 0}, 'id': '0'}, {'action': 'TEMP', 'position': {'y': 10, 'x': 10}, 'id': '1'}, {'action': 'TURN', 'position': {'y': 20, 'x': 10}, 'id': '2'}]}

=================
Parsing Yaml File : 
=================
name : Data center patrolling

duration_minutes : 66
Goal point #1  id = 0  , x = 0 y = 10
=================
id: 0
pose: 
  x: 0
  y: 10
  theta: 0.0
  linear_velocity: 0.0
  angular_velocity: 0.0
twist: 
  linear: 
    x: 0.0
    y: 0.0
    z: 0.0
  angular: 
    x: 0.0
    y: 0.0
    z: 0.0
Goal point #2  id = 1  , x = 10 y = 10
=================
id: 1
pose: 
  x: 10
  y: 10
  theta: 0.0
  linear_velocity: 0.0
  angular_velocity: 0.0
twist: 
  linear: 
    x: 0.0
    y: 0.0
    z: 0.0
  angular: 
    x: 0.0
    y: 0.0
    z: 0.0
10.0 10.0
Goal point Received :  id = 1  , x = 10.0 , y = 10.0
10.0 10.0
Goal point #3  id = 2  , x = 10 y = 20
=================
id: 2
pose: 
  x: 10
  y: 20
  theta: 0.0
  linear_velocity: 0.0
  angular_velocity: 0.0
twist: 
  linear: 
    x: 0.0
    y: 0.0
    z: 0.0
  angular: 
    x: 0.0
    y: 0.0
    z: 0.0
======================================================Finish===========================================================
[Talker-3] process has finished cleanly


[==================================================================================================================================================]


#Fin Tutorial


