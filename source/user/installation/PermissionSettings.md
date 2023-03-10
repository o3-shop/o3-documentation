# Permission settings

Read and write access is required for the directories listed below and their subdirectories:

- `/source/export`
- /source/log/
- /source/out/pictures/
- /source/out/media/
- /source/tmp/
- /var/

also the CLI (Command Line Interface) user needs read and write access to the /var/ directory.

Regarding the browser-based setup, the HTTP server must have write access to the following directory and these files:

- /source/Setup
- /source/config.inc.php
- /source/.htaccess

After completing the installation, remove the write permissions for the file "config.inc.php".
