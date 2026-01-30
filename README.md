# Python Tooling Workshop

Workshop pratique pour maîtriser les outils et bonnes pratiques Python en production.

## 📚 Vue d'ensemble

Ce workshop vous guide étape par étape dans la création d'un **Task Manager CLI** en Python, en appliquant les meilleures pratiques de développement professionnel.

### Ce que vous allez apprendre

- Structurer un projet Python modulaire
- Gérer les dépendances avec `venv` et `requirements.txt`
- Utiliser le linting et le formatage automatique (Ruff)
- Appliquer un workflow Git professionnel avec branches
- Créer une CLI interactive avec Rich et Click
- Écrire des tests unitaires avec pytest

## Structure du workshop

Le projet est organisé en **branches progressives**. Chaque branche représente une étape du développement :

```
main                    → Point de départ (ce README)
  ↓
step-01-structure       → Structure de projet Python
  ↓
step-02-dependencies    → Environnements virtuels et dépendances
  ↓
step-03-implementation  → Code fonctionnel (classes POO)
  ↓
step-04-linting         → Linting avec Ruff
  ↓
step-05-formatting      → Formatage automatique
  ↓
step-06-git-workflow    → Workflow Git avec branches et PR
  ↓
step-07-cli             → Interface CLI avec Rich/Click
  ↓
step-08-tests           → Tests unitaires avec pytest
```

## Démarrage rapide

### Option 1: GitHub Codespaces (Recommandé)

1. Cliquez sur le "Code" → "Codespaces" → "Create codespace"
2. Attendez que l'environnement soit prêt (2-3 minutes)
3. Vous avez VSCode dans votre navigateur avec tout configuré 

### Option 2: Local

**Prérequis:**
- Python 3.10+
- Git
- VSCode (recommandé)

**Installation:**
```bash
# Cloner le repo
git clone https://github.com/[username]/python-tooling-workshop.git
cd python-tooling-workshop

# Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate

# Installer les dépendances (après checkout d'une branche avec requirements.txt)
pip install -r requirements.txt
```

## 📖 Guide d'utilisation

### Naviguer entre les étapes

```bash
# Voir toutes les branches disponibles
git branch -a

# Passer à une étape spécifique
git checkout step-01-structure

# Voir les différences entre deux étapes
git diff step-01-structure..step-02-dependencies
```

### Workflow recommandé

1. **Checkout** de la branche de l'étape
2. **Lire** le README de cette étape
3. **Reproduire** le code dans votre propre branche
4. **Tester** que ça fonctionne
5. **Commit** vos changements
6. **Passer** à l'étape suivante

## Pour les formateurs

### Structure pédagogique

- **Durée totale:** 2h30
- **Format:** Démonstration → Pratique → Validation
- **Rythme:** 15-20 min par étape

### Plan détaillé

Voir [../docs/masterclass_plan.md](./../docs/masterclass_plan.md) pour le timing et le contenu de chaque phase.

## Technologies utilisées

- **Python 3.10+** - Langage de programmation
- **Rich** - Affichage stylé dans le terminal
- **Click** - Framework pour créer des CLI
- **Ruff** - Linter et formatteur ultra-rapide
- **pytest** - Framework de tests
- **Git** - Gestion de versions

## Ressources

- [Documentation Ruff](https://docs.astral.sh/ruff/)
- [Guide pytest](https://docs.pytest.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Real Python - Project Structure](https://realpython.com/python-application-layouts/)

## Contribution

Ce projet est un support pédagogique. Les suggestions d'amélioration sont les bienvenues via issues ou PR !

## Licence

MIT - Libre d'utilisation pour l'éducation et la formation.

---

**Bon workshop **
