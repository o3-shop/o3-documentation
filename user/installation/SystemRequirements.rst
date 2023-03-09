# O3-Shop

## System requirements

- Apache versions 2.2 or 2.4 (on Linux)
- 500 MB free webspace
- Installed extension mod_rewrite
- 1 database (MySQL 5.5 or 5.7, alternatively MariaDB (tested with MariaDB 10.4))
- PHP versions 8.0, 8.1 or 7.4
- We recommend a memory_limit of 60 MB, but at least 32 MB.
- The PHP setting session.auto_start in the php.ini file should be deactivated (OFF).
- File uploads should be enabled in PHP
- Enabled allow_url_fopen and fsockopen on port 80
- Apache server variables REQUEST_URI or SCRIPT_URI must be present
- ini_set allowed
- PHP extensions that must be installed:
  - GD LIB version 2.x
  - PDO_MySQL
  - BC Math
  - JSON
  - iconv
  - tokenizer
  - mbstring
  - cURL
  - SOAP
  - DOM
- openssl >= 1.0.1
