# Spécification - Répartition du code et Livraison aux coéquipiers

Ce document décrit le plan pour isoler le travail de chaque membre de l'équipe Magnus Carlsen et réinitialiser le dépôt d'Ezechiel avec sa partie uniquement, tout en créant un dossier de livraison pour ses coéquipiers.

## 1. Objectifs
- Nettoyer le dépôt principal d'Ezechiel (`C:\Users\djebe\chessgame-magnus-carlsen`) pour ne conserver que ses fondations (`position.py`, `piece.py`, les tests associés et les squelettes de classes de `specific_pieces.py`).
- Créer un répertoire externe de livraison (`C:\Users\djebe\.gemini\antigravity\scratch\delivery_to_teammates`) contenant les travaux finis des coéquipiers (Matthias, Antonin, Maxime) avec des instructions individualisées pour qu'ils commitent eux-mêmes leur partie depuis leur machine.

## 2. Structure des dossiers de livraison
Un dossier externe sera structuré avec les répertoires et fichiers suivants :

### Dossier Global
`C:\Users\djebe\.gemini\antigravity\scratch\delivery_to_teammates`

#### Sous-dossier : `1_Matthias_Rossier`
- Fichiers :
  - `board.py`
  - `tests/test_board.py`
  - `code_pieces_matthias.py` (Classes `Pawn` et `Rook`)
- Fichier d'instructions : `README.md` (Explique comment créer la branche `feature/board-matthias`, ajouter ses fichiers, insérer ses pièces dans `specific_pieces.py`, lancer ses tests unitaires, et commiter sous son identité).

#### Sous-dossier : `2_Antonin_Robert`
- Fichiers :
  - `chess.py`
  - `tests/test_chess.py`
  - `code_pieces_antonin.py` (Classes `Bishop` et `Knight`)
- Fichier d'instructions : `README.md` (Explique comment créer la branche `feature/engine-antonin`, ajouter ses fichiers, insérer ses pièces dans `specific_pieces.py`, lancer ses tests unitaires, et commiter sous son identité).

#### Sous-dossier : `3_Maxime_Lotens`
- Fichiers :
  - `player.py`
  - `tests/test_player.py`
  - `code_pieces_maxime.py` (Classes `King` et `Queen`, logique de sauvegarde JSON)
- Fichier d'instructions : `README.md` (Explique comment créer la branche `feature/player-maxime`, ajouter ses fichiers, insérer ses pièces dans `specific_pieces.py`, lancer ses tests unitaires, et commiter sous son identité).

#### Sous-dossier : `4_Ezechiel_Integration_Finale`
- Fichiers :
  - `gui.py`
  - `images/` (Sprites des pièces d'échecs)
  - `tests/test_specific_pieces.py` (Validation globale de toutes les pièces)
- Fichier d'instructions : `README.md` (Étapes pour qu'Ezechiel fusionne les branches de ses camarades sur `main`, ajoute la GUI à la fin et valide l'ensemble du projet).

## 3. Plan d'action pour le dépôt d'Ezechiel
Le dépôt local `C:\Users\djebe\chessgame-magnus-carlsen` subira les modifications suivantes :
- Conserver `README.md`, `.gitignore`, `position.py`, `piece.py`, `tests/test_position.py`, `tests/test_piece.py`.
- Recréer `specific_pieces.py` avec uniquement des squelettes de classes vides (`Pawn`, `Rook`, `Bishop`, `Knight`, `Queen`, `King` héritant de `Piece` et levant `NotImplementedError` ou contenant `pass`).
- Supprimer tous les autres fichiers (`board.py`, `chess.py`, `gui.py`, `player.py`, `tests/test_board.py`, `tests/test_chess.py`, `tests/test_player.py`, `tests/test_specific_pieces.py`, dossier `images/`).
- Commiter cette base propre sur la branche `feature/fondations-ezechiel` (ou directement sur la branche principale) avec l'identité d'Ezechiel.
