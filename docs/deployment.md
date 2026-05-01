Deployment uses:

- systemd to manage FastAPI service
- nginx as reverse proxy

App runs on port 8000 internally.
Nginx exposes it on port 80.

Service auto-restarts on failure and system reboot.
