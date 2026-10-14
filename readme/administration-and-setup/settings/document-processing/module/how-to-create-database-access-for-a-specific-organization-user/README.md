# Comment créer un accès à la base de données pour un utilisateur spécifique de l'organisation

### **1. Se connecter à Docbits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Allez sur la page de connexion de votre application.
2. Saisissez vos identifiants (nom d'utilisateur et mot de passe) pour vous connecter.

### **2. Accéder aux paramètres** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Une fois connecté, repérez l'icône **Settings** (engrenage ⚙️) dans la barre latérale gauche.
2. Cliquez sur **Settings** pour ouvrir le panneau de configuration du système.

### **3. Ouvrir le module Document Processing** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. Dans **Settings**, repérez la section **Document Processing**.
2. Sous **Document Processing**, trouvez l'option **Module** et cliquez dessus.
   * La page de configuration du module concerné s'ouvre. Vous pouvez y procéder à la création de l'utilisateur pour la base de données.

### 4. Étapes pour activer et accéder à l'utilisateur AI Document et base de données : <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Activer les fonctionnalités** :
   * Utilisez les commutateurs sur la droite pour activer ou désactiver des fonctionnalités spécifiques :
     * **AI Document Warehouse** : activez-le pour autoriser l'accès aux fonctionnalités liées à l'IA.
     * **DB Access** : activez-le pour accorder à l'utilisateur l'accès à la base de données.
2. **Identifiants de la base de données** :
   * Le tableau de bord fournit les informations de connexion à la base de données suivantes :
     * **Username** : un nom d'utilisateur unique est affiché.
     * **Password** : veillez à stocker ou à copier le mot de passe de manière sécurisée.
     * **Database** : le nom de la base de données.
     * **Host** : le nom d'hôte.
     * **Port** : le port.
     * **SSL Mode :** la connexion nécessite `sslmode=require` pour une communication sécurisée.
3. **Copier les identifiants** :
   * Utilisez les icônes de copie à côté de chaque champ pour copier rapidement les identifiants et les utiliser dans votre client de base de données ou votre application.
4. **Connexion via DBeaver** :
   * Connexion via l'hôte
     * choisissez PostgreSQL
     * Renseignez les informations requises
     * passez à l'onglet SSL et cochez Use SSL. Descendez jusqu'à SSL mode et sélectionnez require
   * Connexion via l'URL
     * Renseignez les informations requises :\n - remplacez Host par l'hôte fourni\n - remplacez Port par le port fourni\n - remplacez Database par la base de données fournie\n - pour Username, sélectionnez le nom d'utilisateur fourni\n - pour Password, sélectionnez le mot de passe fourni
5. **Tester la connexion** :
   * Cliquez sur le bouton **"Test Connection"** pour vérifier que les identifiants et les informations de connexion sont corrects.
   * Si le test réussit, poursuivez avec la connexion.
6. **Explorer la base de données** :
   * Une fois connecté, accédez à la section **schema** ou **tables** de votre client de base de données.
   * Vérifiez les tables disponibles.
