# Step 08: Tests et Intégration Continue (CI)

## Objectif

Apprendre à valider la qualité du code avec des tests unitaires et à automatiser ces vérifications avec GitHub Actions.

## Installation des dépendances

```bash
# Installer pytest et pytest-cov avec UV
uv sync
```

## 🧪 Tests unitaires avec Pytest

### Structure des tests
```
tests/
├── __init__.py
├── test_task.py          # Tests du modèle Task
└── test_task_manager.py  # Tests de la logique TaskManager
```

### Exécuter les tests

```bash
# Lancer tous les tests
uv run pytest

# Lancer avec le rapport de couverture (coverage)
uv run pytest --cov=src tests/
```

### Pourquoi tester ?
- **Confiance** : Vérifier que le code fait ce qu'on attend.
- **Non-régression** : S'assurer qu'une modification ne casse pas l'existant.
- **Documentation** : Les tests servent d'exemple d'utilisation.

## 🚀 GitHub Actions (CI)

Le fichier `.github/workflows/ci.yml` automatise les vérifications à chaque `push` ou `pull request`.

### Workflow automatisé :
1. **Linting** : Vérification du style avec Ruff.
2. **Formatting** : Vérification du formatage avec Ruff.
3. **Tests** : Exécution de tous les tests unitaires.

### Avantages de la CI :
- **Qualité garantie** : On ne merge que du code qui passe les tests.
- **Feedback rapide** : On sait immédiatement si on a cassé quelque chose.

## À reproduire

### 1. Créer le dossier de tests
```bash
mkdir tests
touch tests/__init__.py tests/test_task.py tests/test_task_manager.py
```

### 2. Écrire vos tests
Utilisez `pytest.fixture` pour préparer un environnement de test propre (ex: un `TaskManager` vide).

### 3. Configurer la CI
Créez le fichier `.github/workflows/ci.yml` pour automatiser vos tests sur GitHub.

## Points de validation

- [ ] `uv run pytest` passe au vert (all tests passed)
- [ ] La couverture de code est satisfaisante
- [ ] Le workflow GitHub Actions est configuré
- [ ] Ruff est intégré dans la CI

## Commit

```bash
git add .
git commit -m "feat: add unit tests and GitHub Actions CI"
```

## Prochaine étape

Félicitations ! Vous avez terminé le workshop. Votre projet est maintenant professionnel, testé et automatisé.
