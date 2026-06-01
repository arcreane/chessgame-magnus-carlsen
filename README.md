# Projet Jeu d'Echecs - Equipe Magnus Carlsen

## Objectif du projet
Nous devons developper un jeu d'echecs en Python.Le code doit utiliser l'approche orientee objet et respecter l'encapsulation

## Outils de l'equipe
- Trello : https://trello.com/invite/b/69ce374b58a5bfc5ac761c23/ATTI3d4647f549d493639df8966ffb7d71433E237B91/chessi
- GitHub : Pour sauvegarder et partager le code

## Regles de travail (Git et GitHub)
Pour avoir tous les points sur la methode de travail, chaque membre de l'equipe doit respecter ceci :
- Noms des branches : Creer une branche par fonctionnalite, par exemple feature/piece-roi ou fix/bug-deplacement 
- Commits : Tous les membres doivent faire des commits reguliers.
- Messages de commit : Utiliser des messages clairs en anglais, par exemple feat: add King movement ou fix: correct checkmate

## Ce que nous devons developper
- Les classes communes : Position, Board, Player, AIPlayer et Chess.
- Les pieces : Creer une classe abstraite Piece , puis developper le Roi, la Reine, le Fou, le Cavalier, la Tour et le Pion. Chaque membre doit coder au moins un deplacement de piece.
- Les tests : Chaque classe doit etre testee avec UnitTest et inclure des tests a la fin de son fichier.
- La sauvegarde : Le jeu doit pouvoir enregistrer et recharger une partie dans un fichier.

## Membres de l'equipe
- Ezechiel DJEBE : Gestion du projet et fondations :
  - Mise en place de GitHub, du README et du .gitignore.
  - Implementation de la classe Position.
  - Implementation de la classe abstraite Piece.
    
- Matthias ROSSIER : Gestion du plateau et de l'espace de jeu :
  - Implementation de la classe Board (initialisation et gestion des cases).
  - Developpement des deplacements pour le Pion et la Tour.
  - Mise en place des tests fonctionnels pour ces modules.
    
- Antonin ROBERT : Logique de jeu et moteur principal : 
  - Implementation de la classe Chess (boucle de jeu et changement de joueur).
  - Developpement des deplacements pour le Fou et le Cavalier.
  - Gestion de la detection de l'echec et mat (isCheckMate)
    
- Maxime LOTENS :Interaction joueurs et intelligence artificielle :
  - Implementation des classes Player et AIPlayer (mouvements aleatoires).
  - Developpement des deplacements pour le Roi et la Reine.
  - Fonctionnalite de sauvegarde et restauration de la partie.

