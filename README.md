# pre-commit-Hooks
Frontend &amp; Backend

##### basic frontend project setup using **React** with **Husky**, **ESLint**, and **Prettier**, along with **pre-commit hooks** to enforce code quality.

### ✅ Stack:

-   React (Vite or CRA — we'll use **Vite** for speed)
    
-   ESLint
    
-   Prettier
    
-   Husky
    
-   lint-staged (for efficient pre-commit formatting)

##  📁 Project Setup Guide

1. **Create the Vite Project**

		npm create vite@latest my-frontend-app --template react
		cd my-frontend-app
		npm install

2. **Install Dev Dependencies**

		npm install -D eslint prettier husky lint-staged

3. **Configure ESLint**

a minimal `.eslintrc.cjs` :

		module.exports = {
		  env: {
		    browser: true,
		    es2021: true,
		  },
		  extends: [
		    'eslint:recommended',
		    'plugin:react/recommended',
		    'prettier',
		  ],
		  parserOptions: {
		    ecmaFeatures: {
		      jsx: true,
		    },
		    ecmaVersion: 'latest',
		    sourceType: 'module',
		  },
		  plugins: ['react'],
		  rules: {},
		  settings: {
		    react: {
		      version: 'detect',
		    },
		  },
		};


4. **Add Prettier Config**
`.prettierrc` file :

		{
		  "singleQuote": true,
		  "semi": true,
		  "trailingComma": "es5"
		}
And `.prettierignore`:
	
	node_modules
	dist
	build

#### 5. **Setup Husky + lint-staged**

	npm install --save-dev husky
	npx husky init

in the  '.husky/pre-commit'

	npm test
	prettier $(git diff --cached --name-only --diff-filter=ACMR | sed 's| |\\ |g') --write --ignore-unknown
	git update-index --again
	npx lint-staged

In `package.json`, add:

	"lint-staged": {
	  "*.{js,jsx,ts,tsx}": [
	    "eslint --fix",
	    "prettier --write"
	  ]
	}



