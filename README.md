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


# Using `pre-commit` for a Django app

#### 1. Install `pre-commit` Requirements.txt

	pre-commit>=3.3.0
	black==23.7.0
	isort==5.12.0
	flake8==6.0.0
	flake8-django==0.1.0


#### 2. Create `.pre-commit-config.yaml` in your project root

	repos:
	  - repo: https://github.com/psf/black
	    rev: 23.7.0  # or latest stable version
	    hooks:
	      - id: black
	        language_version: python3

	  - repo: https://github.com/PyCQA/isort
	    rev: 5.12.0
	    hooks:
	      - id: isort
	        language_version: python3

	  - repo: https://github.com/PyCQA/flake8
	    rev: 6.0.0
	    hooks:
	      - id: flake8
	        additional_dependencies: [flake8-django]
	        language_version: python3

#### 3. Install the Git hook scripts

	pre-commit install
	pre-commit run --all-files

#### Embed this in you code
At the bottom of `manage.py`, just before `main()` or anywhere after imports:

	import subprocess
	import sys

	if len(sys.argv) > 1 and sys.argv[1] == "precommit":
	    subprocess.run(["pre-commit", "run", "--all-files"], check=True)
	    sys.exit(0)


#### ### Final Setup Command Checklist

	pip install -r requirements.txt         # install dev tools
	pre-commit install                      # install the Git hook
	pre-commit run --all-files              # (optional) fix all files now
	python manage.py precommit             # run hooks manually later


