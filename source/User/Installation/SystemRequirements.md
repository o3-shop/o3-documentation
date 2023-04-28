# System Requirements

You can run O3-Shop on different server systems.

The choice of a suitable hosting package depends, for example, on the number of articles, the expected visitors to the shop and the number of orders.

You have the following options:

- For a small shop with a few hundred articles, a few visitors per month and a manageable order volume, a shared hosting system is sufficient.
- For larger shops, choose a managed server system.
- If the load increases, a server farm with load balancing and a database cluster is recommended.

You will find advice and support in choosing the right system from our hosting partners. They provide solutions specially tailored to the O3-Shop.

---

For the operation of the O3-Shop, your system must meet the following system requirements.

## Webserver

- Apache versions 2.2 or 2.4 (on Linux)
- 750 MB free webspace
- Installed extension *mod_rewrite*

:::{hint}
  After the installation you will be taken to the web-based setup of the shop.

  Before you can run the setup, the system checks whether the system requirements are met.

  It is possible that under **Server Configuration** the Apache *mod_rewrite* module is marked as faulty, although you have installed the module.

  One reason for this is often the setting for *AllowOverride* in the Apache configuration of the vHost.

  If you have Apache 2.3.9, make sure *AllowOverride* has the value *None*.
:::

A decoder (Zend Guard Loader, ionCube Loader, ...) is not required, as O3-Shop is unencrypted.

## Database

- MySQL 5.5 or 5.7
- MariaDB (tested with MariaDB 10.4)

The database user needs sufficient authorisation to be able to create a database during the installation, if it does not already exist. The authorisation must also allow the creation of views.

The transaction isolation level must be left at the default value *REPEATABLE READ* of the InnoDB Storage Engine on the server side.

## PHP

- PHP versions 7.4, 8.0 or 8.1
- A *memory_limit* of 60 MB, but at least 32 MB, is recommended.
- The PHP setting *session.auto_start* in the ***php.ini*** file should be disabled (OFF)
- File uploads should be enabled in PHP
- Enabled *allow_url_fopen* and *fsockopen* on port 80
- Apache server variables *REQUEST_URI* or *SCRIPT_URI* must be present
- *ini_set* allowed

PHP extensions that must be installed:

- *GD LIB version 2.x*
- *PDO_MySQL*
- *BC Math*
- *JSON*
- *iconv*
- *tokenizer*
- *mbstring*
- *cURL*
- *SOAP*
- *DOM*

:::{note}
  For PHP 8 operation, it is strongly recommended to set PHP's error_reporting to `error_reporting = E_ALL & ~E_NOTICE & ~E_WARNING & ~E_DEPRECATED`, otherwise you will get a lot of warnings.
:::

## Composer

The installation of O3-Shop is no longer based on packed and downloadable installation packages, but is carried out with the help of Composer. Composer is a dependency manager for PHP, a tool that takes dependencies of program components of a project into account while installing the files of this project into a defined directory.

Composer is required for the installation of the O3-Shop and changes in the autoloading of files (not at runtime).

The requirements for Composer can be found at [https://getcomposer.org/doc/00-intro.md#system-requirements](https://getcomposer.org/doc/00-intro.md#system-requirements).

For installation instructions, see the Getting Started section of the Composer pages at [https://getcomposer.org](https://getcomposer.org).

- Composer 2.2

:::{attention}
   A Composer version newer than 2.2 is not supported.

   For example, install Composer version 2.2 as follows:

   ```
   composer selfupdate --2.2
   ```
:::


## OpenSSL

OpenSSL is required for the modules belonging to a compilation.

- *openssl* >= 1.0.1
