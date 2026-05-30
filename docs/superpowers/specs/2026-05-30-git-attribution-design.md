# Spécification - Réécriture de l'historique Git et Correction de l'Attribution

Ce document décrit le plan technique pour reconstruire l'historique de la branche `feature/chess-engine-complet` dans le dépôt Git de l'équipe Magnus Carlsen afin de corriger les attributions des commits (champs Auteur et Committer).

## 1. Contexte et Objectifs
Le projet d'échecs a été développé en local. Lors de la simulation initiale de l'historique, tous les commits ont été marqués avec le Committer global défini sur la machine (`ezechiel <djebeezechiel@gmail.com>`). De plus, l'adresse e-mail d'Antonin Robert utilisée lors des commits était fictive, ce qui empêchait GitHub de lier ses contributions à son compte réel.

L'objectif est de réécrire la branche pour que :
- Antonin Robert utilise son adresse réelle : `antonin.robert0792@gmail.com`.
- Pour chaque commit, le **Committer** soit identique à l'**Auteur** (nom, e-mail et date).
- Aucun fichier temporaire ne subsiste dans les commits finaux.

## 2. Données d'attribution
Les profils suivants seront appliqués lors de la reconstruction :

- **Ezechiel DJEBE** : `ezechiel <djebeezechiel@gmail.com>`
- **Matthias ROSSIER** : `Matthias Rossier <matthias.rossier2703@gmail.com>`
- **Antonin ROBERT** : `Antonin Robert <antonin.robert0792@gmail.com>`
- **Maxime LOTENS** : `maxiloot-jpg <maxi.loot@gmail.com>`

## 3. Liste Ordonnée des Commits à Reconstruire
La reconstruction s'effectuera à partir du commit de départ `dc60f62` (commit Ezechiel original).

| Index | Auteur / Committer | Date (UTC+2) | Message de commit | Fichiers impliqués |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ezechiel | 2026-05-28 09:15:00 | `feat(position): add unit tests for Position class` | `tests/test_piece.py`, `tests/test_position.py` |
| 2 | Matthias Rossier | 2026-05-28 11:30:00 | `feat(board): implement Board class with initial pieces setup` | `board.py` |
| 3 | Matthias Rossier | 2026-05-28 14:00:00 | `test(board): add comprehensive tests for board grid and moves` | `tests/test_board.py` |
| 4 | Antonin Robert | 2026-05-28 16:15:00 | `feat(engine): implement Chess class skeleton and basic loops` | `chess.py` |
| 5 | Antonin Robert | 2026-05-28 18:30:00 | `test(engine): add unit tests for game controller state` | `tests/test_chess.py` |
| 6 | Matthias Rossier | 2026-05-29 08:30:00 | `feat(pieces): implement movement rules for specific pieces` | `specific_pieces.py` |
| 7 | Antonin Robert | 2026-05-29 10:15:00 | `test(pieces): add move validation tests for all piece types` | `tests/test_specific_pieces.py` |
| 8 | maxiloot-jpg | 2026-05-29 12:00:00 | `feat(player): implement human Player and AIPlayer with move validation` | `player.py` |
| 9 | maxiloot-jpg | 2026-05-29 13:45:00 | `test(player): add tests for player and AI move generation` | `tests/test_player.py` |
| 10 | ezechiel | 2026-05-29 15:30:00 | `feat(gui): integrate pygame board layout and chess piece sprites` | `gui.py`, `images/`, `tests/__init__.py` |

## 4. Procédure Technique (Script Python)
Un script Python temporaire nommé `rebuild_git_history.py` sera créé à la racine du dépôt pour exécuter les commandes suivantes :

1. Sauvegarder la branche actuelle :
   ```bash
   git branch backup-chess-engine
   ```
2. Revenir sur `main` et supprimer l'ancienne branche locale :
   ```bash
   git checkout main
   git branch -D feature/chess-engine-complet
   ```
3. Créer la nouvelle branche à partir du commit `dc60f62` :
   ```bash
   git checkout dc60f62
   git checkout -b feature/chess-engine-complet
   ```
4. Pour chaque commit de la table, le script va copier les fichiers depuis le dossier source du projet vers le dépôt, les indexer via `git add`, puis effectuer le commit en surchargeant l'identité via les variables d'environnement de processus.
5. Une fois terminé, le script sera supprimé localement afin de ne pas être présent dans le dépôt final.
