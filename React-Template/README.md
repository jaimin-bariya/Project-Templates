# React-Templates


```
src/
│
├── assets/          # Static files like images, fonts, and icons
│   ├── images/
│   ├── fonts/
│   └── styles/      # Global CSS or SCSS files
│       ├── variables.css
│       ├── global.css
│       └── index.js # Centralized export for styles
│
├── components/      # Reusable components
│   ├── Header.jsx
│   ├── Footer.jsx
│   ├── Button.jsx
│   ├── Card/
│   │   ├── Card.jsx
│   │   ├── Card.module.css
│   │   └── Card.test.jsx
│   └── index.js     # Centralized export for components
│
├── data/            # Static data used throughout the app
│   ├── blogData.js   # Blog posts, articles, etc.
│   ├── navLinks.js   # Navbar menu links
│   ├── featureList.js  # Features list for landing pages
│   └── index.js      # Centralized export for data files
│
├── pages/           # Top-level pages (used for routing)
│   ├── Home.jsx
│   ├── About.jsx
│   ├── Contact.jsx
│   └── index.js      # Centralized export for pages
│
├── hooks/           # Custom React hooks
│   ├── useFetch.js
│   ├── useAuth.js
│   └── index.js      # Centralized export for hooks
│
├── services/        # API service files
│   ├── api.js
│   ├── authService.js
│   └── index.js      # Centralized export for services
│
├── store/           # State management (if using Redux, Context API, etc.)
│   ├── store.js
│   ├── userContext.js
│   └── index.js      # Centralized export for store files
│
├── utils/           # Utility/helper functions
│   ├── formatDate.js
│   ├── validateInput.js
│   └── index.js      # Centralized export for utilities
│
├── router/          # React Router setup (if applicable)
│   ├── AppRouter.jsx
│   ├── PrivateRoute.jsx
│   └── index.js      # Centralized export for router files
│
├── App.jsx          # Main application component
├── index.jsx        # Application entry point
└── styles/          # Global styling
    ├── variables.css
    ├── mixins.scss
    └── index.js      # Centralized export for styles

```
