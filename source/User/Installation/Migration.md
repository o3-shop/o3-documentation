# Migrate from OXID eShop

In principle, a migration between the OXID eShop and O3-Shop is possible, but we recommend a new installation to get a clean installation.

The migration keeps your data: it swaps the shop's code from the `oxid-esales/*` packages to `o3-shop/*` and then upgrades the database schema in place. **Make a full backup first — the database changes are not reversible.**

## Requirements for a migration

Please ensure that **all** requirements are met:
- You start with an error-free Composer installation of the OXID eShop version 6.4.3 **Community Edition**.
  For older shop versions, please perform the update offered by OXID eSales to version 6.4.3 **before** you start the migration. Newer OXID shops (> 6.4.3) cannot be migrated.
  The migration only supports Community Editions. The migration of Professional or Enterprise Editions is not supported.
- The OXID eShop was installed via the package 'oxid-esales/oxideshop-project'. Check if 'oxid-esales/oxideshop-project' is mentioned as *name* in the file composer.json, located in the main directory of your shop. If you use a different package composition, please check its components manually to determine if they can be replaced.
- PHP 7.4 – 8.2 and Composer 2.2.x are available.
- You have made a full backup of your installation (Files and Database) before proceeding with a migration.
- **If your database runs on MySQL 8.0, complete the [MySQL 8 pre-step](#mysql-8-pre-step) below _before_ migrating.**

(mysql-8-pre-step)=
## MySQL 8 pre-step (MySQL 8.0 only)

MySQL 8.0 removed the `ENCODE()` / `DECODE()` functions that OXID used to encrypt two
columns:

- `oxconfig.OXVARVALUE`
- `oxuserpayments.OXVALUE`

The migrations that decode these columns skip themselves on MySQL 8, which would leave
the data encrypted and break the shop. You must therefore decode these columns
**before** migrating, on an engine that still provides `DECODE()` — MariaDB or
MySQL 5.7 (for example against a MariaDB copy of the database, before the data lives on
MySQL 8):

```sql
-- Run on MariaDB / MySQL 5.7 — NOT on MySQL 8 (DECODE() does not exist there).
SET SESSION sql_mode = '';  -- decoded values are latin1-encoded, not valid UTF-8

ALTER TABLE oxconfig ADD COLUMN `OXVARVALUE_UNENC` text;
UPDATE oxconfig SET `OXVARVALUE_UNENC` = DECODE(OXVARVALUE, 'fq45QS09_fqyx09239QQ') WHERE 1;
ALTER TABLE oxconfig MODIFY COLUMN `OXVARVALUE` text;
UPDATE oxconfig SET `OXVARVALUE` = `OXVARVALUE_UNENC` WHERE 1;
ALTER TABLE oxconfig DROP COLUMN `OXVARVALUE_UNENC`;

ALTER TABLE oxuserpayments ADD COLUMN `OXVALUE_UNENC` text;
UPDATE oxuserpayments SET `OXVALUE_UNENC` = DECODE(OXVALUE, 'fq45QS09_fqyx09239QQ') WHERE 1;
ALTER TABLE oxuserpayments MODIFY COLUMN `OXVALUE` text;
UPDATE oxuserpayments SET `OXVALUE` = `OXVALUE_UNENC` WHERE 1;
ALTER TABLE oxuserpayments DROP COLUMN `OXVALUE_UNENC`;
```

`fq45QS09_fqyx09239QQ` is the shop's default configuration key.

Because the decoded `OXVARVALUE` / `OXVALUE` bytes are latin1 (not valid UTF-8), MySQL 8's
default strict `sql_mode` would **reject** them on import (`ER_TRUNCATED_WRONG_VALUE`, error
1366) and silently truncate exactly the data this step is meant to preserve. So when you move
the decoded database back onto MySQL 8, disable strict mode for the import:

```bash
# on the MariaDB (or MySQL 5.7) copy, after running the decode SQL above:
mysqldump --no-tablespaces --single-transaction <database> > decoded.sql

# import into the MySQL 8 target with strict mode off so the latin1 bytes are accepted:
mysql --init-command="SET SESSION sql_mode=''" <database> < decoded.sql
```

The database views are regenerated during the migration, so they do not need to be
transferred. On **MariaDB** or **MySQL 5.7** you can skip this whole pre-step — the
migrations decode the columns for you.

## Perform migration

### Replace packages

Open a terminal window and navigate to the main store directory and replace the OXID
packages with their O3-Shop counterparts. O3-Shop is pulled in through the
`o3-shop/shop-metapackage-ce` package, which carries the full component set — this mirrors
the `oxid-esales/oxideshop-metapackage-ce` you remove immediately afterwards:

```
composer require -W o3-shop/shop-metapackage-ce:^1.6 --no-scripts --no-plugins
composer remove oxid-esales/oxideshop-metapackage-ce --no-scripts --no-plugins
composer update --no-interaction
```

Confirm all overwrite requests with `y`.

Development tools (only if your installation uses them):

```
composer remove oxid-esales/testing-library oxid-esales/oxideshop-ide-helper --dev --no-scripts --no-plugins
composer require o3-shop/testing-library:^1.0 o3-shop/shop-ide-helper:^1.0 --dev --no-scripts --no-plugins
```

In the case of additional packages installed by OXID or individual compositions of the
shop project, check which packages need to be replaced from *oxid-esales* to *o3-shop*
(see the [package overview](#package-overview) below).

### Data migration

Run the database migrations from the shop's main directory:

```
vendor/bin/oe-eshop-db_migrate migrations:migrate
```

```{warning}
Pass **only** `migrations:migrate`. The second argument to `oe-eshop-db_migrate` is the
*edition filter*, not an option — a value such as `--no-interaction` there is read as an
edition, matches nothing, and silently skips every migration. Non-interactive mode is
already the default.
```

Then regenerate the database views (a separate, mandatory step):

```
vendor/bin/oe-eshop-db_views_generate
```

Finally, clear the compiled cache:

```
rm -rf source/tmp/*
```

### Verify the migration

O3-Shop provides two console commands to inspect and validate the migration state:

```
# current version, latest available, and any pending/unknown migrations
bin/oe-console oe:migrate:status

# pass/fail health check — exits with a non-zero code on any problem
bin/oe-console oe:migrate:verify
```

`oe:migrate:verify` confirms the migration-tracking table is present, there are no
pending migrations, the database views are present and queryable, and no
`oxid-esales/*` packages remain in `composer.lock`. A successful `oe:migrate:verify` is
the signal that the migration completed.

## What the data migration does

The cumulative `migrations:migrate` step brings the 6.4.3 schema up to the current
O3-Shop release. `oe:migrate:status` lists the authoritative set for your target
version; the main steps are:

| Migration | What it does |
|:----------|:-------------|
| Decode `oxconfig.OXVARVALUE` | Decrypts the config values (skipped on MySQL 8 — see the pre-step). |
| Decode `oxuserpayments.OXVALUE` | Decrypts stored payment values (skipped on MySQL 8). |
| `oxcontents.OXISPLAIN` | Adds the column and backfills it for "plain" content items. |
| Rights & roles tables | Creates `o3rightsroles`, `o3rightsroleselements`, `o3object2role`. |
| `OXNODELETE` flag | Adds the protective flag to `oxactions` and `oxcontents`. |
| Revocation (§ 356a BGB) | Creates `o3revocation` and seeds the revocation notice CMS snippet. |

## After migrating

- **Theme.** O3-Shop ships the **o3-theme** and **wave** themes; it does not ship
  OXID's `azure` theme. If your shop's configured theme is not available after the
  migration, the storefront will not render until you activate a shipped theme
  (Admin → Extensions → Themes). The admin panel itself is unaffected.
- **Revocation (§ 356a BGB).** A default-off CMS snippet and the `o3revocation` table
  are created. Review the snippet and activate the feature if it is required for your
  market.
- **Custom modules.** OXID modules that have an O3-Shop counterpart (e.g. PayPal, GDPR
  opt-in, Usercentrics) must be swapped from *oxid-esales* to *o3-shop* as well; third
  party modules are the operator's responsibility.

(package-overview)=
## Overview of the packages replaced by O3-Shop

Requiring `o3-shop/o3-shop` resolves the full O3-Shop component set transitively, so you
normally do not install these individually. This mapping is a reference for custom
compositions:

| OXID package                                      | OXID version | O3-Shop package                          |
|:--------------------------------------------------|-------------:|:-----------------------------------------|
| oxid-esales/oxideshop-project                     | dev-b-6.0-ce | o3-shop/o3-shop                          |
| oxid-esales/oxideshop-ce                          | 6.10.3       | o3-shop/shop-ce                          |
| oxid-esales/oxideshop-composer-plugin             | 5.2.2        | o3-shop/shop-composer-plugin             |
| oxid-esales/oxideshop-facts                       | 2.4.0        | o3-shop/shop-facts                       |
| oxid-esales/oxideshop-unified-namespace-generator | 2.2.0        | o3-shop/shop-unified-namespace-generator |
| oxid-esales/oxideshop-doctrine-migration-wrapper  | 3.3.0        | o3-shop/shop-doctrine-migration-wrapper  |
| oxid-esales/oxideshop-db-views-generator          | 1.3.0        | o3-shop/shop-db-views-generator          |
| oxid-esales/codeception-page-objects              | 2.3.0        | o3-shop/codeception-page-objects         |
| oxid-esales/codeception-modules                   | 1.4.2        | o3-shop/codeception-modules              |
| oxid-esales/wave-theme                            | 1.6.2        | o3-shop/wave-theme                       |
| oxid-esales/flow-theme                            | 3.8.1        | o3-shop/o3-theme                         |
| oxid-esales/oxideshop-demodata-installer          | 1.3.0        | o3-shop/shop-demodata-installer          |
| oxid-esales/oxideshop-demodata-ce                 | 6.0.4        | o3-shop/shop-demodata-ce                 |
| oxid-esales/paypal-module                         | 6.4.1        | o3-shop/paypal-module                    |
| oxid-esales/gdpr-optin-module                     | 2.3.3        | o3-shop/gdpr-optin-module                |
| oxid-professional-services/usercentrics           | 1.2.1        | o3-shop/usercentrics                     |
| oxid-esales/testing-library                       | 8.1.0        | o3-shop/testing-library                  |
| oxid-esales/oxideshop-ide-helper                  | 4.1.0        | o3-shop/shop-ide-helper                  |
| oxid-esales/developer-tools                       | 1.1.0        | o3-shop/developer-tools                  |
| oxid-esales/php-selenium                          | 1.0.5        | o3-shop/php-selenium                     |
| oxid-esales/mink-selenium-driver                  | 1.1.2        | o3-shop/mink-selenium-driver             |
