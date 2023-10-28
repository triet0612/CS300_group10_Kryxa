## Note for development

### Backend is a JSON api using FastAPI in Python

*Migrate database:*
```
// create bin/ folder in KryxaAPI
run migrate.py
```

*Debug python:*
```
run main.py in KryxaAPI/
```

### Frontend is a single-page application using Svelte framework

Single page app will be build to www folder in this same directory, backend will serve it as single page app.

*Before anything:*
```
npm install
```
*To debug frontend:*
```
npm run dev
```
*To build frontend:*
```
npm run build
```

### Workflow:

run migrate.py
run npm run build

run main.py for API
npm run dev to debug frontend (remember to run main.py for API first)