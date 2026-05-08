Deployment uses:

- systemd to manage FastAPI service
- nginx as reverse proxy

App runs on port 8000 internally.
Nginx exposes it on port 80.

Service auto-restarts on failure and system reboot.

Security-related additions:

- CORS middleware enabled
- basic API rate limiting added
- internal exception leakage reduced
- database-backed health endpoint implemented
