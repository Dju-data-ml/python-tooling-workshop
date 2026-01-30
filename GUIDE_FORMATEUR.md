# Guide Formateur - Python Tooling Workshop

## 📦 Ce qui a été créé

Repo Git complet avec **7 branches progressives** + configuration GitHub Codespaces.

### Structure du repo

```
python-tooling-workshop/
├── README.md                    # Documentation principale
├── masterclass_plan.md          # Plan détaillé 2h30
├── .gitignore                   # Fichiers Python à ignorer
├── .devcontainer/              
│   └── devcontainer.json        # Config Codespaces (VSCode + extensions)
├── src/                         # Code source (créé dans les steps)
├── tests/                       # Tests (créé dans les steps)
└── STEP_XX_README.md            # Guide pour chaque étape
```

### Branches disponibles

| Branche | Contenu | Commit message |
|---------|---------|----------------|
| `main` | Point de départ (README + devcontainer) | Initial setup |
| `step-01-structure` | Structure de dossiers `src/` | feat: setup project structure |
| `step-02-dependencies` | `requirements.txt` + guide venv | feat: add dependencies |
| `step-03-implementation` | Classes Task + TaskManager | feat: implement classes |
| `step-04-linting` | `pyproject.toml` + Ruff config | chore: add ruff linting |
| `step-05-formatting` | Guide formatage | style: formatting guide |
| `step-06-git-workflow` | Guide Git + Conventional Commits | docs: git workflow |
| `step-07-cli` | CLI avec Rich + Click | feat: implement CLI |

---

## 🚀 Préparation de la masterclass

### Option 1 : Utiliser GitHub Codespaces (Recommandé)

#### Avant la séance

1. **Créer un repo GitHub** à partir de ce dossier :
   ```bash
   cd python-tooling-workshop
   gh repo create datascientest/python-tooling-workshop --public --source=. --push
   ```

2. **Tester le Codespace** :
   - Aller sur le repo GitHub
   - Cliquer "Code" → "Codespaces" → "New codespace"
   - Vérifier que l'environnement se lance correctement
   - Python 3.11, VSCode, extensions Ruff installées

3. **Préparer les apprenants** :
   - Leur envoyer le lien du repo
   - Leur demander de créer un compte GitHub (si pas déjà fait)
   - Vérifier qu'ils ont accès aux Codespaces (60h/mois gratuit)

#### Pendant la séance

**Workflow de démonstration :**

1. **Partage d'écran** : Votre Codespace
2. **Live coding** : Checkout de chaque branche
3. **Exercice pratique** : Les apprenants reproduisent dans leur Codespace
4. **Validation** : Vous passez voir leurs écrans

**Commandes clés à montrer :**
```bash
# Navigation entre branches
git branch -a
git checkout step-01-structure
git diff step-01-structure..step-02-dependencies

# Installation venv (step-02)
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Linting (step-04)
ruff check src/
ruff check --fix src/

# Formatage (step-05)
ruff format src/

# CLI (step-07)
python -m src.cli.main add "Test" "Description"
python -m src.cli.main list
```

### Option 2 : Docker + code-server (Backup)

Si Codespaces ne fonctionne pas, vous pouvez utiliser Docker :

```dockerfile
# Dockerfile
FROM python:3.11-slim
RUN apt-get update && apt-get install -y git
WORKDIR /workspace
COPY . .
CMD ["bash"]
```

Mais c'est plus complexe à setup pour les apprenants.

---

## 📋 Timing de la masterclass (2h30)

| Phase | Durée | Branche | Activité |
|-------|-------|---------|----------|
| **Intro** | 10 min | `main` | Présentation, fork, Codespace |
| **Structure** | 25 min | `step-01` | Démo structure → Pratique |
| **Dépendances** | 20 min | `step-02` | Démo venv → Installation |
| **Implémentation** | 20 min | `step-03` | Démo POO → Code classes |
| **PAUSE** | 10 min | - | ☕ |
| **Linting** | 20 min | `step-04` | Config Ruff → Détection erreurs |
| **Formatage** | 15 min | `step-05` | Formatage auto |
| **Git Workflow** | 20 min | `step-06` | Branches + PR |
| **CLI** | 15 min | `step-07` | Démo CLI interactive |
| **Conclusion** | 10 min | - | Recap + Questions |

### Adaptation possible

**Si le groupe est rapide** (tout le monde suit) :
- Ajouter step-08 avec pytest (15 min)
- Montrer pre-commit hooks
- Démo CI/CD avec GitHub Actions

**Si le groupe est lent** (beaucoup de questions) :
- Skipper step-06 (git workflow) → juste mentionner
- Ou skipper step-07 (CLI) → rester sur REPL
- Prioriser : structure → dépendances → linting → formatage

---

## 🎓 Conseils pédagogiques

### Énergie de la séance

**Alterner démo/pratique** :
- ⏱️ 10 min démo (vous codez)
- ⏱️ 15 min pratique (ils reproduisent)
- ⏱️ 5 min validation (questions + debugging collectif)

**Maintenir l'attention** :
- Faire des micro-breaks (2-3 min) entre phases
- Utiliser le chat/Slack pour questions asynchrones
- Montrer des erreurs volontairement (c'est formateur)
- Encourager l'entraide entre apprenants

### Gestion des différences de niveau

**Apprenants rapides** :
- Leur donner des défis bonus (dans les README)
- Les transformer en "helpers" pour les autres
- Leur suggérer d'explorer les branches suivantes

**Apprenants en difficulté** :
- Avoir un Codespace de secours déjà configuré
- Les mettre en binôme avec quelqu'un de plus rapide
- Privilégier la compréhension sur la vitesse

### Debugging collectif

**Erreurs classiques à anticiper** :

1. **Venv pas activé** :
   ```bash
   # Symptôme : imports qui échouent
   # Fix : vérifier le prompt (.venv)
   source .venv/bin/activate
   ```

2. **Mauvais working directory** :
   ```bash
   # Symptôme : "No module named src"
   # Fix : être à la racine du projet
   pwd  # Doit montrer /workspaces/python-tooling-workshop
   ```

3. **Git détaché** :
   ```bash
   # Symptôme : "detached HEAD"
   # Fix : checkout d'une branche
   git checkout step-XX-xxx
   ```

4. **Conflits de merge** :
   ```bash
   # Si un apprenant a modifié des fichiers
   git stash
   git checkout step-XX-xxx
   ```

---

## 📊 Évaluation des apprenants

### Livrables attendus

À la fin du workshop, chaque apprenant devrait avoir :

- [ ] Un repo forké avec toutes les branches
- [ ] Un Codespace fonctionnel
- [ ] Au moins 1 commit avec Conventional Commits
- [ ] Le code qui passe `ruff check` sans erreurs
- [ ] (Bonus) Une PR créée et mergée

### Points de validation rapides

**Pendant la séance** (checkpoints visuels) :
1. Step 01 : Montrer `tree` de la structure
2. Step 02 : Montrer `pip list` avec rich et click
3. Step 03 : Exécuter `python -m src.models.task` sans erreur
4. Step 04 : `ruff check src/` → 0 errors
5. Step 07 : Lancer `python -m src.cli.main list`

**Après la séance** (si évaluation formelle) :
- Demander un screenshot de leur CLI fonctionnel
- Vérifier leur historique Git (`git log --oneline`)
- Checker qu'ils ont bien compris la différence linting/formatting

---

## 🔧 Troubleshooting

### Codespaces ne démarre pas

**Solution 1** : Rebuild
```bash
# Dans Codespace
Cmd/Ctrl + Shift + P → "Rebuild Container"
```

**Solution 2** : Nouveau Codespace
- Supprimer l'actuel
- En créer un nouveau

**Solution 3** : Local fallback
- `git clone` du repo
- Setup local avec venv

### Extensions VSCode manquantes

Si Ruff ou Python extension ne s'installe pas :

```bash
# Installer manuellement
code --install-extension charliermarsh.ruff
code --install-extension ms-python.python
```

### Problèmes réseau/firewall

Certains établissements bloquent Codespaces.

**Solution** : Utiliser un hotspot mobile ou préparer un environnement local.

---

## 📚 Ressources pour aller plus loin

À mentionner en fin de séance :

1. **Documentation officielle** :
   - [Ruff](https://docs.astral.sh/ruff/)
   - [Click](https://click.palletsprojects.com/)
   - [Rich](https://rich.readthedocs.io/)

2. **Pratique** :
   - [Real Python](https://realpython.com/) - Tutoriels Python
   - [Python Packaging Guide](https://packaging.python.org/)
   - [The Hitchhiker's Guide to Python](https://docs.python-guide.org/)

3. **Communauté** :
   - Slack DataScientest #python-help
   - Stack Overflow [python] tag
   - GitHub Discussions sur le repo

---

## 🎯 Objectifs pédagogiques atteints

À la fin du workshop, les apprenants devraient :

### Savoirs (Connaissances)
- [x] Comprendre la différence code exploration vs production
- [x] Connaître les outils standards Python (venv, ruff, pytest)
- [x] Connaître Conventional Commits

### Savoir-faire (Compétences)
- [x] Structurer un projet Python modulaire
- [x] Utiliser venv et requirements.txt
- [x] Configurer et utiliser Ruff
- [x] Créer des branches Git et des PR
- [x] Créer une CLI avec Click/Rich

### Savoir-être (Attitudes)
- [x] Adopter une posture "code propre dès le départ"
- [x] Comprendre l'importance de la review de code
- [x] Être autonome sur les outils de qualité

---

## 🎤 Script de conclusion

> "Bravo à tous ! Vous avez maintenant les outils pour écrire du code Python production-ready.
> 
> Ces pratiques vont vous servir **immédiatement** :
> - Sprint 2 (SQL) : structure de projet pour accès BDD
> - Sprint 4 (API) : FastAPI avec cette même architecture
> - Sprint 5 (Docker) : vos requirements.txt sont déjà prêts
> - Sprint 6 (Git) : vous maîtrisez déjà les branches
> - Sprint 7+ (LLM/Agents) : code production pour agents IA
> 
> Le repo reste disponible comme template pour tous vos futurs projets.
> 
> N'hésitez pas à poser vos questions sur Slack #python-help.
> 
> Bon coding ! 🚀"

---

## 📝 Notes pour itération future

**Ce qui marche bien** :
- Structure progressive par branches
- Codespaces = zéro setup local
- Alternance démo/pratique

**Améliorations possibles** :
- Ajouter step-08 avec pytest (si temps)
- Vidéos de recap par step (asynchone)
- Quiz interactif sur Conventional Commits
- Badge GitHub "Python Tooling Certified" 🎖️

---

**Bon workshop ! 🎉**
