# Prepare installation

Create the prerequisites for the new installation of the O3-Shop.

## Install Composer

The installation of O3-Shop is no longer based on packed and downloadable installation packages, but is carried out with the help of Composer. Composer is a dependency manager for PHP, a tool that takes dependencies of program components of a project into account while installing the files of this project into a defined directory.

For a new installation of the O3-Shop you need Composer. See under [Server and System Requirements](SystemRequirements.md) section [Composer](SystemRequirements.md#composer).

For installation instructions, see the Getting Started section of the Composer pages at [https://getcomposer.org](https://getcomposer.org).

## Provide shop files

The shop files are provided by Composer. The shop files are stored in a subdirectory that is specified in the command with **your_project_name**. This is based on the directory in which the command is issued in the shell. The parameter **--no-dev** is specified if the development-related files are not needed.

```
composer create-project --no-dev o3-shop/o3-shop your_project_name
```

```{note}
Use a different version constraint to install a different project version.

- leave empty for the latest official release ever
- e.g. `1.2` for the latest official release of the 1.0 branch
- `dev-b-1.x-ce-nightly` for the latest development versions of the 1.x branch. This is intended for development and testing purposes and should not be used for productive use!
```

After Composer has finished its work, the new directory named *your_project_name* exists. This is the root directory of the project and contains all files needed for the installation of the O3-Shop.

## Configure Apache

The root directory must now be moved to a directory that the HTTP server can access. The document root directory of Apache must point to the ***/source*** directory of the main directory.

## Adjusting file and directory permissions

The HTTP server requires read and write access for the following directories and their subdirectories at runtime:

- `/source/export`
- `/source/log/`
- `/source/out/pictures/`
- `/source/out/media/`
- `/source/tmp/`
- `/var/`

In addition, the CLI user (Command Line Interface) also needs read and write access for the directory `/var/`.

For the web-based setup, the HTTP server must have write access to the following directory and these files:

- `/source/Setup`
- `/source/config.inc.php`
- `/source/.htaccess`

## Create database

O3-Shop requires a MySQL / MariaDB database to store items, categories, customer and order data and other information.

Most web hosts offer database access via a special website, such as phpMyAdmin. If you need help with this, please contact your hosting partner or Internet Service Provider (ISP).

Create a new MySQL or MariaDB database. You can choose the name of the database freely, for example `o3_shop`.

Remember the name of the database and the access data to the database (user name and password).

You will need this data to run the setup after the installation.
