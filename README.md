# Python Tooling Workshop

Workshop pratique pour maîtriser les outils et bonnes pratiques Python en production.

## Comment utiliser ce workshop

Ce workshop est organisé en **branches progressives**. Chaque branche contient une étape spécifique avec son propre README.

### Navigation entre les étapes

```bash
# Voir toutes les branches disponibles
git branch -a

# Passer à une étape spécifique
git checkout step-01-structure

# Voir les différences entre deux étapes
git diff step-01-structure..step-02-dependencies
```

### Étapes du workshop

| Branche | Contenu |
|---------|---------|
| **step-01-structure** | Structure de projet Python modulaire |
| **step-02-dependencies** | Environnements virtuels et dépendances |
| **step-03-implementation** | Implémentation des classes POO |
| **step-04-linting** | Linting et qualité de code avec Ruff |
| **step-05-formatting** | Formatage automatique du code |
| **step-06-git-workflow** | Workflow Git professionnel |
| **step-07-cli** | Interface CLI avec Rich et Click |

### Démarrage rapide

1. **Choisissez votre étape** :
   ```bash
   git checkout step-01-structure  # Pour commencer
   ```

2. **Lisez le README** de la branche pour les instructions détaillées

3. **Suivez les exercices** pas à pas

### Prérequis

- Python 3.10+
- Git
- [UV](https://docs.astral.sh/uv/) (recommandé) ou pip/venv
- Un éditeur de code (VSCode recommandé)

### Installation des dépendances (à partir de step-02)

```bash
# Avec UV (recommandé)
uv sync

# Ou méthode classique
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

### Pour les formateurs

Voir [docs/masterclass_plan.md](./docs/masterclass_plan.md) pour le plan détaillé de la formation.


**Commencez par :** `git checkout step-01-structure`
