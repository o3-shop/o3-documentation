# Run setup

To get your O3-Shop ready to go, run the web-based setup.

## Start setup

Make sure that configuration parameters can be written during the setup and start the setup.

1. Open a shell and change to the shop's directory.

```
cd /var/www/oxideshop/source
```

2. Make sure that the following files are not write-protected:

- ***.htaccess***
- ***config.inc.php***

3. Open a browser and go to `www.yourshopurl.de/setup`.

  Replace `www.yourshopurl.de` with the URL where your O3-Shop will be accessible.

  The setup will start.

## Requirements

Coloured symbols indicate whether the system requirements are met:

- ![](../../../assets/install_pass.png) The prerequisite is fulfilled.
- ![](../../../assets/install_pmin.png) The prerequisite is not or only partially fulfilled. The O3-Shop still works and can be installed.
- ![](../../../assets/install_fail.png) The prerequisite is not fulfilled. The O3-Shop does not work without this prerequisite and cannot be installed.
- ![](../../../assets/install_null.png) The prerequisite could not be checked.

1. Select the language for the installation.
2. Make sure that all system requirements are fulfilled in order to install the O3-Shop and operate it without problems. In case of configuration problems, contact your hosting partner or Internet Service Provider (ISP).
3. As soon as all system requirements are met (there are no red marks), press the **Start Setup** button.

## Welcome

1. Set the main delivery country and language of the shop. You can always add more delivery countries and/or languages later.
2. Recommended: Activate the checkbox for regular check for updates.
3. Select the Start shop installation button.

## Licence conditions

Check the licence conditions and accept them.

## Database

Create a database or integrate an existing database.

**Database Hostname or IP Address**

  You have the following options:

  - If the database and web server are on the same server, leave the default value localhost. This is the default for most shops.
  - If your database is outsourced, enter the host name or IP address of your database server.

**Database Name**

  You have the following options:

  - Enter the name of your outsourced database.
  - If you do not have a database yet, enter a name for a database that the system creates during setup.

**Database user name** and **database password**

  Enter the access data for the database and keep it in a safe place.

**Demo data**

Decide whether you want to install the shop pre-configured with sample items.

Demo data is recommended if you want to familiarise yourself with the shop in a test installation first.

You can delete the demo data at any time if you want to fill the shop with your own articles.

If you do not yet have a database, select the **Create database now** button.

If you have integrated an existing database, a message appears that the database will be overwritten and that the required tables and data will now be saved in this database.

## Directories & Login

If necessary, adjust the directory settings and set the login data for the administration area of the shop.

Make a note of the following settings and keep the data in a safe place:

**Shop URL**

  Displays the URL under which your eShop will be accessible.

**Directory on the server to the shop**

  Indicates the internal path to the shop on the server (for example /var/www/oxideshop/source/).

  Adjust the path, for example, if you have several shops.

  You need the path in the last step of the setup.

**Directory on the server to the TMP directory**

  Names the directory in which the shop's temporary files, for example for Smarty or SEO cache, are stored.

  Background: Some modules ask you from time to time to delete temporary files manually.

**Administrator e-mail** and **administrator password**

  Enter the administrator's e-mail address and password.

  Use this data to log in to the administration area after the setup.

## Finish

For security reasons, set the *config.inc.php* file to *read-only* mode. Test the shop.

1. Open the console of your system and change to the shop's directory (/var/www/ocideshop/source/).
2. Execute the following command:
```
chmod 0444 config.inc.php
```
3. Open the shop as a customer and as an administrator:
4. The link **To shop** takes you to the start page of your shop.
5. The link **To shop administration** leads you to the administration area.
