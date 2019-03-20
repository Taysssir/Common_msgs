#common_msgs

- L’objectif est de lire et d’exécuter un patrolling, à partir d'un fichier de conf param.yaml en JSON format. Cela , ce fait sur 3 étapes :

#Start Tutorial

##Description
- Ce projet contient plusieurs repertoires :
[config] : Contient un input file patrol.yaml avec une liste de points atteignable de la carte du turtlesim.
[msg] : Contient les 3 Msg : Goal.msg, Patrol.msg et Patrolling.msg qui  devrait contenir les listes des Goal et du Patrol.
[launch] : Contient un launch File qui permet de lancer le node Turtlesim ainsi que faire l'appel des paramètres server rosparam dans l’environement ROS.
[src] : Contient 3 scripts python :

1. yamlreader.py :

Un script python qui permet à la fois de jouer le rôle d’un ParserYaml et un Talker . Cet noeud permet d'extraire les données d’un fichier patrol.yaml puis le transmettre vers le message crée /common_msgs/Goal.msg.

2. custom_listener.py :

Un noeud Listener afin de verifier que les valeurs sont bien transmis a travers un topic vers le message .

3. gotogoal.py :

Cette noeud combine le Listener des goals et le controle du Turtlesim . Donc,il récupére les valeurs et le transmettre au message comme un Goal Point et le transmettre vers un topic au Turtlesim afin de bouger.
#Avant de Tester le code
On doit rendre les 3 scripts exucutables :

$ chmod u+x ~/catkin_ws/src/common_msgs/src/yamlreader.py
$ chmod u+x ~/catkin_ws/src/common_msgs/src/custom_listener.py
$ chmod u+x ~/catkin_ws/src/common_msgs/src/gotogoal.py


#Testing the code
Ouvrer le terminal, run:
$ roscore

dans un autre terminal, run:

$ cd catkin_ws/
$ source devel/setup.bash
$ roslaunch common_msgs yamlreader.launch

 Cela va lancer le Turtlsim node ainsi les parametres server rosparam. Vous devez trouvez une chose similaire a ca :
================================================================
started roslaunch server http://tayssir-VirtualBox:39097/

SUMMARY

PARAMETERS
 * /duration_minutes: 66
 * /goals: [{'action': 'SNAP...
 * /name: Data center patro...
 * /rosdistro: melodic
 * /rosversion: 1.14.3

NODES
  /
    tartoula (turtlesim/turtlesim_node)

ROS_MASTER_URI=http://localhost:11311

process[tartoula-1]: started with pid [4432]

================================================================

Maintenant, on veut Lancer le Listener.Deux choix sont possible: Soit lancer custom_listener.py,Soit gotogal.py :

* Verifier que les valeurs sont bien transmis a travers un topic vers le message :dans un autre terminal, run:

$ cd catkin_ws/
$ source devel/setup.bash
$ rosrun common_msgs custom_listener.py

Vous devez trouvez une chose similaire a ca :

======Start Listener===========
0.0 10.0
Goal point Received :  id = 0  , x = 0.0 , y = 10.0
10.0 10.0
Goal point Received :  id = 1  , x = 10.0 , y = 10.0
10.0 20.0
Goal point Received :  id = 2  , x = 10.0 , y = 20.0
==============================

* Récupére les valeurs a travers le Listener et le transmettre au message comme un Goal Point puis le transmettre vers un topic au Turtlesim afin de bouger :dans un autre terminal, run:

$ cd catkin_ws/
$ source devel/setup.bash
~/catkin_ws/src/common_msgs/src$ python gotogoal.py

Dans cette point,le Turtlesim passe au premier GoalPoint puis reste dans un tour boucle infinie.(je suis en train de chercher une solution afin de résoudre ce problème).VOus trouvez une capture de simulation Turtlesim pour cette point dans ce package.

Puis, on doit lancer le parser et le Talker pour transmettre les donnees :dans un autre terminal, run:

$ cd catkin_ws/
$ source devel/setup.bash
$rosrun  common_msgs yamlreader.py

```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
[=================================Remaraue 1=======================================================================================]
- Il vaut mieux de lancer le Listener et le Talker en meme temps ou bien successivement pour s`assurer qu'il capte tous les valeurs.
[===================================================================================================================================] 

``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

Vous devez trouvez ca :


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
...
...
#Fin Tutorial


