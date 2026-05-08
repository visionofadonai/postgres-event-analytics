Rate limiting added for protection:
* from accidental flooding
* from abuse
* from runaway requests


Readiness checks added for 
* confirming app is alive
* verifying DB reachable
* connection pool is functioning

CORS added to handle browser-based clients from breaking

Error handling improved to keep leaking the following to clients:
* stack traces
* SQL errors
* internal paths
* DB info
