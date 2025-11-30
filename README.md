# Assistant Personnel Intelligent CLI

Un puissant assistant personnel en ligne de commande qui vous aide à gérer les tâches, les notes et les rappels avec résumé de texte alimenté par l'IA.

## Fonctionnalités

- 📝 **Gestion des Tâches**: Créer, lister, compléter et supprimer des tâches avec des catégories
- 📓 **Prise de Notes**: Ajouter des notes avec résumé automatique alimenté par l'IA en utilisant le NLP
- ⏰ **Rappels**: Définir des rappels basés sur le temps avec des notifications console
- 🔍 **Recherche**: Rechercher dans vos notes efficacement
- 🎨 **Interface CLI Riche**: Belle interface de terminal avec des tableaux et des panneaux

## Prérequis

- Python 3.8 ou supérieur
- Gestionnaire de paquets pip

## Installation

1. Clonez le dépôt:
```bash
git clone https://github.com/mhammadzahi/intelligent-personal-assistant-cli.git
cd intelligent-personal-assistant-cli
```

2. Créez et activez un environnement virtuel:
```bash
python3 -m venv env
source env/bin/activate  # Sur Windows: env\Scripts\activate
```

3. Installez les dépendances:
```bash
pip install -r requirements.txt
```

4. Téléchargez le modèle de langue spaCy (si non téléchargé automatiquement):
```bash
python -m spacy download en_core_web_sm
```

## Utilisation

### Gestion des Tâches

#### Ajouter une Tâche
```bash
python main.py task add "Acheter des courses"
python main.py task add "Terminer le rapport de projet" --category work
```

#### Lister Toutes les Tâches
```bash
python main.py task list
```

#### Marquer une Tâche comme Terminée
```bash
python main.py task done 1
```

#### Supprimer une Tâche
```bash
python main.py task delete 1
```

### Gestion des Notes

#### Ajouter une Note
L'assistant générera automatiquement un résumé en utilisant le NLP:
```bash
python main.py note add "Notes de Réunion" "Aujourd'hui, nous avons discuté de la feuille de route du quatrième trimestre. Les points clés incluent le lancement de la nouvelle fonctionnalité en décembre, l'embauche de deux développeurs supplémentaires et l'augmentation du budget marketing. L'équipe a accepté le calendrier."
```

#### Lister Toutes les Notes
```bash
python main.py note list
```

#### Rechercher des Notes
Rechercher dans les titres et le contenu des notes:
```bash
python main.py note search "feuille de route"
python main.py note search "réunion"
```

#### Supprimer une Note
```bash
python main.py note delete 1
```

### Gestion des Rappels

#### Ajouter un Rappel
Les rappels utilisent le format `AAAA-MM-JJ HH:MM`:
```bash
python main.py reminder add "Rendez-vous chez le médecin" "2025-12-15 10:30"
python main.py reminder add "Appeler maman" "2025-12-01 18:00"
```

#### Lister Tous les Rappels
```bash
python main.py reminder list
```

#### Supprimer un Rappel
```bash
python main.py reminder delete 1
```

#### Notifications de Rappels
Les rappels sont automatiquement vérifiés lorsque vous lancez l'application. Si des rappels sont dus, ils seront affichés comme des notifications console.

## Structure du Projet

```
intelligent-personal-assistant-cli/
├── main.py              # Point d'entrée CLI et gestion des commandes
├── controllers.py       # Logique métier pour les tâches, notes et rappels
├── models.py           # Modèles de données (Task, Note, Reminder)
├── database.py         # Connexion et initialisation de la base de données SQLite
├── nlp_utils.py        # Utilitaires de résumé de texte NLP
├── notifications.py    # Système de notification des rappels
├── utils.py            # Fonctions d'aide (analyse de date, formatage)
├── requirements.txt    # Dépendances Python
└── README.md          # Ce fichier
```

## Stockage des Données

L'application utilise SQLite pour la persistance des données. Le fichier de base de données (`assistant.db`) est automatiquement créé dans le répertoire du projet lors de la première exécution.

### Schéma de la Base de Données

**Table des Tâches:**
- `id`: Clé primaire
- `title`: Titre de la tâche
- `category`: Catégorie de la tâche (par défaut: "general")
- `status`: Statut de la tâche ("pending" ou "done")
- `created_at`: Horodatage

**Table des Notes:**
- `id`: Clé primaire
- `title`: Titre de la note
- `content`: Contenu complet de la note
- `summary`: Résumé généré par l'IA
- `created_at`: Horodatage

**Table des Rappels:**
- `id`: Clé primaire
- `title`: Titre du rappel
- `due_date`: Date et heure d'échéance
- `status`: Statut du rappel ("pending")
- `created_at`: Horodatage

## Exemples

### Exemple de Flux de Travail Complet

```bash
# Ajouter quelques tâches
python main.py task add "Préparer la présentation" --category work
python main.py task add "Aller à la salle de sport" --category personal
python main.py task add "Examiner les pull requests" --category work

# Lister toutes les tâches
python main.py task list

# Marquer une tâche comme terminée
python main.py task done 1

# Ajouter une note détaillée avec résumé automatique
python main.py note add "Idées de Projet" "Nous avons fait un brainstorming de plusieurs idées pour le prochain trimestre. Premièrement, implémenter une version d'application mobile de notre plateforme. Deuxièmement, ajouter des recommandations alimentées par l'IA. Troisièmement, améliorer l'expérience d'intégration avec des tutoriels interactifs. L'équipe était plus enthousiaste à propos des fonctionnalités d'IA."

# Lister les notes pour voir le résumé
python main.py note list

# Rechercher des notes spécifiques
python main.py note search "IA"

# Définir des rappels
python main.py reminder add "Standup d'équipe" "2025-12-01 09:00"
python main.py reminder add "Soumettre la feuille de temps" "2025-12-01 17:00"

# Lister les rappels
python main.py reminder list

# Supprimer les éléments terminés
python main.py task delete 1
python main.py note delete 1
python main.py reminder delete 1
```

## Fonctionnalités en Détail

### Résumé Alimenté par l'IA

Lorsque vous ajoutez une note, l'application utilise les capacités NLP de spaCy pour:
1. Analyser le contenu du texte
2. Calculer les fréquences des mots (en excluant les mots vides)
3. Noter les phrases en fonction des mots-clés importants
4. Extraire les phrases les plus pertinentes
5. Générer un résumé concis

Cela vous aide à examiner rapidement vos notes sans lire tout le contenu.

### Catégories de Tâches

Organisez vos tâches avec des catégories personnalisées:
- `work`: Tâches professionnelles
- `personal`: Courses personnelles
- `shopping`: Listes de courses
- `general`: Tâches diverses (par défaut)

### Notifications de Rappels

L'application vérifie les rappels dus à chaque fois qu'elle est lancée. Si des rappels ont dépassé leur date d'échéance, ils seront affichés de manière visible dans un panneau de notification.

## Dépendances

- **rich**: Formatage de terminal et tableaux magnifiques
- **spacy**: Traitement du langage naturel pour le résumé de texte
- **en_core_web_sm**: Modèle de langue anglaise pour spaCy

## Conseils

1. **Utilisez des guillemets** pour les arguments multi-mots:
   ```bash
   python main.py task add "Ceci est une tâche multi-mots"
   ```

2. **Le format de date** pour les rappels doit être `AAAA-MM-JJ HH:MM`:
   ```bash
   python main.py reminder add "Réunion" "2025-12-25 14:30"
   ```

3. **La recherche est insensible à la casse** et recherche à la fois dans les titres et le contenu:
   ```bash
   python main.py note search "projet"
   ```

4. **Les ID de tâches** sont affichés lors de la liste - utilisez-les pour les opérations done/delete

## Dépannage

### Modèle spaCy Non Trouvé
Si vous obtenez une erreur concernant un modèle spaCy manquant:
```bash
python -m spacy download en_core_web_sm
```

### Erreurs d'Importation
Assurez-vous d'avoir activé l'environnement virtuel:
```bash
source env/bin/activate  # Sur Windows: env\Scripts\activate
```

### Erreurs de Base de Données
Si vous rencontrez des problèmes de base de données, vous pouvez supprimer `assistant.db` pour recommencer (cela supprimera toutes vos données).

## Contribution

Les contributions sont les bienvenues! N'hésitez pas à soumettre une Pull Request.

## Licence

Ce projet est open source et disponible sous la licence MIT.

## Auteur

Mohammad Hammad Zahi (@mhammadzahi)

## Support

Pour les problèmes, questions ou suggestions, veuillez ouvrir un issue sur GitHub.
