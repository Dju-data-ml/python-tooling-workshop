# Step 06: Workflow Git professionnel

## Objectif

Apprendre à utiliser Git avec un workflow de branches et pull requests.

## Installation des dépendances

```bash
# Avec UV (recommandé)
uv sync

# Ou méthode classique
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

## Git branching strategy

### Le problème sans branches

```
main → commit → commit → commit → commit
       (OK)    (OK)    (BUG!)  (FIX)
```

❌ Si un bug est introduit, difficile de revenir en arrière
❌ Plusieurs personnes ne peuvent pas travailler en parallèle
❌ Pas de review avant intégration

### La solution : Feature branches

```
main  → commit A ────────────→ merge feature
                   ↖           ↗
feature branch      commit B → commit C
                    (develop) (review)
```

✅ Développement isolé
✅ main reste toujours stable
✅ Review avant merge

## 🔄 Workflow classique

### 1. Créer une branche

```bash
# Depuis main
git checkout main
git pull origin main  # Être à jour

# Créer une nouvelle branche
git checkout -b feature/add-delete-functionality
```

**Convention de nommage :**
- `feature/` : Nouvelle fonctionnalité
- `fix/` : Correction de bug
- `refactor/` : Refactorisation
- `docs/` : Documentation
- `test/` : Ajout de tests

### 2. Développer la feature

```bash
# Modifier des fichiers
vim src/services/task_manager.py

# Voir les changements
git status
git diff

# Stager les fichiers
git add src/services/task_manager.py

# Commit avec message conventionnel
git commit -m "feat: add delete task functionality"
```

### 3. Pousser la branche

```bash
git push origin feature/add-delete-functionality
```

### 4. Créer une Pull Request (PR)

Sur GitHub :
1. Aller sur le repo
2. Cliquer "Compare & pull request"
3. Remplir titre et description
4. Assigner un reviewer
5. Créer la PR

### 5. Review et merge

- Reviewer commente le code
- Développeur fait des corrections
- Une fois approuvé : merge dans main
- Supprimer la branche feature

## ✍️ Conventional Commits

Format standard pour les messages de commit :

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types principaux

| Type | Utilisation | Exemple |
|------|-------------|---------|
| **feat** | Nouvelle fonctionnalité | `feat: add task deletion` |
| **fix** | Correction de bug | `fix: handle empty task list` |
| **docs** | Documentation | `docs: update README with setup` |
| **style** | Formatage (pas de changement logique) | `style: apply ruff formatting` |
| **refactor** | Refactorisation | `refactor: extract validation logic` |
| **test** | Ajout de tests | `test: add unit tests for TaskManager` |
| **chore** | Tâches techniques | `chore: update dependencies` |
| **perf** | Performance | `perf: optimize task search` |

### Exemples concrets

```bash
# ✅ Bon
git commit -m "feat: add filter tasks by status"
git commit -m "fix: prevent duplicate task IDs"
git commit -m "docs: add API documentation"

# ❌ Mauvais
git commit -m "changes"
git commit -m "fix stuff"
git commit -m "WIP"
```

### Avec scope (optionnel)

```bash
git commit -m "feat(cli): add color output to list command"
git commit -m "fix(models): handle None in task creation"
git commit -m "test(services): add TaskManager integration tests"
```

### Avantages

- 📚 Historique Git lisible
- 🤖 Génération automatique de changelog
- 🔍 Recherche facilitée : `git log --grep="feat"`
- 🎯 Compréhension rapide des changements

## 🔧 Exercice pratique

### Partie 1 : Créer une feature branch

```bash
# 1. Partir de main
git checkout main

# 2. Créer une branche pour ajouter une méthode
git checkout -b feature/count-by-status

# 3. Ajouter cette méthode dans TaskManager
def get_statistics(self) -> dict:
    """Get task statistics by status."""
    return {
        "total": self.count_tasks(),
        "todo": self.count_by_status(TaskStatus.TODO),
        "in_progress": self.count_by_status(TaskStatus.IN_PROGRESS),
        "done": self.count_by_status(TaskStatus.DONE),
    }

# 4. Commit
git add src/services/task_manager.py
git commit -m "feat: add task statistics method"

# 5. Push
git push origin feature/count-by-status
```

### Partie 2 : Créer une Pull Request

1. Aller sur GitHub
2. Vous devriez voir "Compare & pull request"
3. Titre : "Add task statistics method"
4. Description :
   ```markdown
   ## Description
   Adds a new method to get statistics about tasks grouped by status.
   
   ## Changes
   - Added `get_statistics()` method to TaskManager
   - Returns dict with total, todo, in_progress, and done counts
   
   ## Testing
   - Tested manually in Python REPL
   - Works as expected
   ```
5. Créer la PR

### Partie 3 : Merge

Une fois la PR approuvée (ou auto-appro si vous êtes seul) :
```bash
# Merger sur GitHub avec le bouton "Merge"
# Puis localement :
git checkout main
git pull origin main
git branch -d feature/count-by-status  # Supprimer la branche locale
```

## 🎨 Workflow visuel

```
1. main (à jour)
   ↓
2. git checkout -b feature/xyz
   ↓
3. [Développement + commits]
   ↓
4. git push origin feature/xyz
   ↓
5. [Créer PR sur GitHub]
   ↓
6. [Review + discussions]
   ↓
7. [Merge PR → main]
   ↓
8. git checkout main && git pull
```

## Bonnes pratiques

### À faire

- **Branches courtes :** Une feature = une branche
- **Commits atomiques :** Un commit = un changement logique
- **Messages clairs :** Suivre Conventional Commits
- **Pull avant push :** Toujours sync avec main
- **Review systématique :** Même pour vos propres projets (bon exercice)

### ❌ À éviter

- Commiter directement sur main
- Branches qui vivent des semaines
- Messages de commit vagues : "update", "fix", "changes"
- Commits massifs (500+ lignes)
- Ne jamais merge main dans votre branche feature

## 🔀 Résoudre des conflits

### Scénario

```
main:  A → B → C
              ↘
feature:       D → E
```

Si quelqu'un d'autre a merge quelque chose sur main pendant que vous travailliez :

### 📊 Situation initiale

```
main:     A ── B ── C
                ↘
feature:        D ── E
```

**Problème :** main a avancé avec le commit C, mais votre branche part de B.

### Étape 1 : Mettre de côté vos changements

```bash
git stash
```

**Ce que ça fait :**
```
main:     A ── B ── C
                ↘
feature:        D ── E
stash:           [vos changements non commités]
```

### Étape 2 : Mettre à jour main

```bash
git checkout main
git pull origin main
```

**Ce que ça fait :**
```
main:     A ── B ── C ── F  (F = nouveaux commits sur main)
                ↘
feature:        D ── E
```

### Étape 3 : Rebasé votre branche

```bash
git checkout feature/xyz
git rebase main
```

**Ce que ça fait :**
```
Avant rebase:
main:     A ── B ── C ── F
                ↘
feature:        D ── E

Après rebase:
main:     A ── B ── C ── F
                           ↘
feature:                D' ── E'
```

**Explication simple :** Git prend vos commits D et E, les "décolle" de B, et les "recolle" après F.

### Étape 4 : Résoudre les conflits (si nécessaire)

```bash
# Si Git dit : CONFLICT (content): Merge conflict in fichier.py
# Éditez le fichier pour résoudre
git add fichier.py
git rebase --continue
```

**Exemple de conflit :**
```python
<<<<<<< HEAD  (version de main)
def calculate_total(items):
    return sum(items)
=======
def calculate_total(items, tax=0.2):  # votre version
    return sum(items) * (1 + tax)
>>>>>>> feature/xyz
```

**Résolution :**
```python
def calculate_total(items, tax=0.2):
    return sum(items) * (1 + tax)
```

### Étape 5 : Récupérer vos changements et pousser

```bash
git stash pop  # Récupérer vos changements stashés
git push origin feature/xyz --force-with-lease
```

**Résultat final :**
```
main:     A ── B ── C ── F
                           ↘
feature:                D' ── E' ── [vos changements]
```

---

### 🔄 Alternative : Merge (plus simple mais historique moins propre)

```bash
git checkout feature/xyz
git merge main
```

**Ce que ça fait :**
```
Avant merge:
main:     A ── B ── C ── F
                ↘
feature:        D ── E

Après merge:
main:     A ── B ── C ── F
                ↘
feature:        D ── E ── M  (M = merge commit)
```

**Rebase vs Merge :**
- **Rebase :** Historique linéaire, plus propre à lire ✅
- **Merge :** Historique exact, plus facile à comprendre ❌

## 🎓 GitFlow (aperçu)

Pour de gros projets, on utilise souvent GitFlow :

```
main (production)
  ↓
develop (intégration)
  ↓
feature/xyz (développement)
```

Vous verrez ça au Sprint 6 de la formation !

## Points de validation

- [ ] Vous savez créer une branche
- [ ] Vous suivez Conventional Commits
- [ ] Vous avez créé au moins une PR
- [ ] Vous comprenez le workflow branches → PR → merge

## 📚 Ressources

- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)

## 💾 Commit

Cette étape est particulière : c'est vous qui créez vos branches !

Exercice : créez une branche avec une petite amélioration de votre choix et faites une PR.

## Prochaine étape

→ **Step 07: CLI avec Rich et Click**

Vous allez créer une vraie interface en ligne de commande interactive.
