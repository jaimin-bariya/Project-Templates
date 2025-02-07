# Electron - Template



```
my-electron-app/  
├── public/  
│   ├── index.html  
│   ├── favicon.ico  
│   └── manifest.json  
│  
├── src/                  # React frontend with Vite (renderer process)  
│   ├── assets/  
│   │   ├── images/  
│   │   ├── fonts/  
│   │   └── styles/  
│   │       ├── variables.css  
│   │       ├── global.css  
│   │       └── index.js  
│   ├── components/  
│   │   ├── Header.jsx  
│   │   ├── Footer.jsx  
│   │   ├── Button.jsx  
│   │   └── Card/  
│   │       ├── Card.jsx  
│   │       ├── Card.module.css  
│   │       └── Card.test.jsx  
│   ├── data/  
│   │   ├── blogData.js  
│   │   ├── navLinks.js  
│   │   ├── featureList.js  
│   │   └── index.js  
│   ├── hooks/  
│   │   ├── useFetch.js  
│   │   ├── useAuth.js  
│   │   └── index.js  
│   ├── pages/  
│   │   ├── Home.jsx  
│   │   ├── About.jsx  
│   │   ├── Contact.jsx  
│   │   └── index.js  
│   ├── services/  
│   │   ├── api.js  
│   │   ├── authService.js  
│   │   └── index.js  
│   ├── store/  
│   │   ├── store.js  
│   │   ├── userContext.js  
│   │   └── index.js  
│   ├── utils/  
│   │   ├── formatDate.js  
│   │   ├── validateInput.js  
│   │   └── index.js  
│   ├── router/  
│   │   ├── AppRouter.jsx  
│   │   ├── PrivateRoute.jsx  
│   │   └── index.js  
│   ├── App.jsx        # React entry point 
│   ├── main.jsx  
│   └── index.jsx  
│  
├── main/              # Electron backend (main process)  
│   ├── main.js  
│   ├── preload.js  
│   └── electron.config.js  
│  
├── dist/              # Build output for React  
│  
├── node_modules/      # Project dependencies  
│  
├── package.json  
├── vite.config.js      # Vite configuration file  
├── electron-builder.json  # Electron build config  
├── README.md              #  Documentation  
└── .gitignore
```

