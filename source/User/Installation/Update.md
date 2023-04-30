# Update

## Update metapackage version in the composer.json file

Open a terminal window and navigate to the main store directory.

Execute following Composer command to update. Match the name with the version you want to udpate to (in the example 1.1):

```
composer require --no-update o3-shop/shop-metapackage-ce:v1.2
```

## Update dependencies

Update all required libraries executing the Composer command:

```
composer update --no-plugins --no-scripts --no-dev
```

Only specify the **--no-dev parameter** if you don’t need the development related files.


## Perform the update running the scripts

```
composer update --no-dev
```

```{note}
The update will overwrite any changes you may have made to modules or themes in the source directory.

Background: During a store update, Composer first loads the new data into the **vendor** directory. Then the data is copied to the **source** directory. This replaces the files of the store, the modules and the themes.

Your individual customizations of the O3-Shop or changes to third-party modules are only safe from being overwritten by the update if you have made the changes through one of the shop's extension options (component, module, child theme).
```

```{attention}
During the update you will be asked which packages may be overwritten.

To ensure that only compatible and tested packages are installed and to avoid inconsistencies and malfunctions caused by incorrectly implemented modules or themes, you have to confirm the queries with *Yes*.
```

## Empty ***tmp*** directory

To ensure that the cached items do not contain incompatibilities, empty the **tmp** directory:

```
rm -rf source/tmp/*
```

## Migrate database

```
vendor/bin/oe-eshop-db_migrate migrations:migrate
```

## Regenerate database views

Depending on the changes and store edition, the store may go into maintenance mode after the update.
To prevent this, regenerate the database views with the following command:

```
vendor/bin/oe-eshop-db_views_regenerate
```
