# Step 01: Structure de projet Python

## 🎯 Objectif

Apprendre à organiser un projet Python de manière modulaire et maintenable.

## 📁 Structure créée

```
python-tooling-workshop/
├── README.md              # Documentation principale
├── .gitignore            # Fichiers à ignorer par Git
├── src/                  # Code source de l'application
│   ├── __init__.py       # Fait de src un package Python
│   ├── models/           # Modèles de données (classes métier)
│   │   └── __init__.py
│   ├── services/         # Logique métier et services
│   │   └── __init__.py
│   └── cli/             # Interface en ligne de commande
│       └── __init__.py
└── tests/               # Tests unitaires et d'intégration
    └── __init__.py
```

## 💡 Concepts clés

### Architecture en couches

Le projet est organisé en couches logiques :

1. **models/** : Les structures de données (classes `Task`, enums, etc.)
   - Aucune logique métier complexe
   - Juste la représentation des données

2. **services/** : La logique métier
   - Opérations CRUD sur les tasks
   - Règles de gestion
   - Validation

3. **cli/** : L'interface utilisateur
   - Interaction avec le terminal
   - Affichage des résultats
   - Parsing des commandes

### Le fichier `__init__.py`

Ce fichier (même vide) transforme un dossier en **package Python**.

**Sans `__init__.py`:**
```python
# ❌ Ne fonctionne pas
from models.task import Task
```

**Avec `__init__.py`:**
```python
# ✅ Fonctionne
from src.models.task import Task
```

### Pourquoi `src/` ?

- Évite les conflits de noms avec les packages installés
- Structure claire : tout le code source est dans `src/`
- Facilite l'installation du package plus tard
- Convention moderne en Python

### Le dossier `tests/`

- Miroir de la structure `src/`
- Un fichier de test par module : `test_task.py`, `test_task_manager.py`
- Convention : préfixer les tests par `test_`

## 🏗️ À reproduire

### 1. Créer la structure de dossiers

```bash
mkdir -p src/models src/services src/cli tests
```

### 2. Créer les fichiers `__init__.py`

```bash
touch src/__init__.py
touch src/models/__init__.py
touch src/services/__init__.py
touch src/cli/__init__.py
touch tests/__init__.py
```

**Astuce:** Ces fichiers peuvent rester vides pour l'instant.

### 3. Vérifier la structure

```bash
tree -I '__pycache__|.git|.venv'
```

Vous devriez voir :
```
.
├── README.md
├── .gitignore
├── src
│   ├── __init__.py
│   ├── cli
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   └── services
│       └── __init__.py
└── tests
    └── __init__.py
```

### 4. Premier commit

```bash
git add .
git commit -m "feat: setup project structure"
```

## ✅ Points de validation

- [ ] Tous les dossiers sont créés
- [ ] Chaque package Python a son `__init__.py`
- [ ] La structure est commité dans Git
- [ ] Vous comprenez le rôle de chaque dossier

## 🔍 Aller plus loin

### Variantes de structure

Il existe d'autres conventions :

**Structure "flat"** (petits projets) :
```
project/
├── task.py
├── task_manager.py
└── main.py
```

**Structure "src layout"** (ce qu'on utilise) :
```
project/
├── src/
│   └── package/
└── tests/
```

**Structure "application"** (très gros projets) :
```
project/
├── src/
│   ├── domain/
│   ├── application/
│   ├── infrastructure/
│   └── presentation/
```

Pour ce workshop, on utilise le "src layout" car c'est :
- Un bon équilibre clarté/complexité
- Préparation à Docker et packaging
- Standard dans l'industrie

## 🚀 Prochaine étape

➡️ **Step 02: Environnements virtuels et dépendances**

Vous allez apprendre à isoler vos dépendances Python avec `venv`.
