# SoftwareArchitectureAnonymousChat

Anonymous chat for Software Architecture course

## Code structure

1. Routers for the websocket and /messages/count are located in the folder "routes".
2. In the file "connections.py" there is ConnectionManager for websockets logic.
3. In the file main.py there is basic configuration of project, and we start server using this file.
4. Index.html is the client code.

## How to run the project

1. Run main.py

```shell
python main.py
```

2. Run index.html several times, one instance for one client.

## How to run tests

1. Install cypress.

```shell
npm install cypress
```

2. Write in console.

```shell
npx cypress open
```

3. Go to the E2E Testing and open Electron.

4. In specs tab choose quality-attributes.cy.js and that's it.

Maintainability test:

1. Use command

```shell
radon mi -s "<filename>.py"
```
