Creating a Child Theme
======================

A child theme (often “child-theme”) is an additional theme for an existing theme in o3-shop.
It takes over the design and functions of the so-called parent theme, but allows you to make your own changes without directly changing the original theme.

This is important because updates to the parent theme would otherwise override your adjustments.

We name our child theme simply *child*. The ``type`` stays the same as with a standard theme. As ``target-directory`` we also use our theme's name and the ``assets-directory`` begins with ``out`` followed by the name again. Currently it's just a normal theme installable via Composer.

composer.json
-------------

theme.php
---------
Create a `theme.php` file in the root of the child folder.

```php
declare(strict_types=1);

$aTheme = [
    'id' => 'child',
    'title' => 'CHILD',
    'description' => 'A child theme from o3-shop.',
    'parentTheme' => 'o3-shop',
    'parentVersions' => ['1.1.0','1.3.0'],
];
```
As ``id``, ``title`` and ``description`` you set the usual things but what's new now are the keys ``parentTheme`` and ``parentVersions``. These two array keys make the theme a child theme.

- ``parentTheme`` is a string and must contain the ``id`` of the parent theme.
- ``parentVersions`` is an array and must contain at least one compatible version of the corresponding parent theme.

In this example we use our current o3-theme and support versions 1.1.0 as well as 1.3.0.

If you wish, you can also add theme setting as usual.

Overwrite Templates
-------------------

Overwriting assets follows the same principle. Let's take the image ``logo.svg`` as an example in o3-theme:


    your_project_name
      ├── de
      ├── en
      ├── out
      .  └── o3-theme
      .     └── img
      .        ├── logo.svg
      .        └── ...
      └── tpl

And so we use the same structure for CHILD:



    child
      ├── de
      ├── en
      ├── out
      .  └── child
      .     └── img
      .        └── logo.svg
      └── tpl

While ``logo.svg`` is now loading from CHILD all other assets still coming from o3-theme.

Overwrite Translations
----------------------

Last thing you can overwrite are translations but this time you must use a little bit different structure. The original parent theme uses ``lang.php`` files in corresponding language directories like ``en`` for english or ``de`` for german.



    o3-theme
      ├── de
      .  └── lang.php
      ├── en
      .  └── lang.php
      └── ...

You now use the same directory structure again but name the files ``cust_lang.php``.


    child
      ├── de
      .  └── cust_lang.php
      ├── en
      .  └── cust_lang.php
      └── ...

Inside the ``cust_lang.php`` files you can change single translations. So the file may contain a few translations like follows:



    $sLangName = 'English';

    $aLang = [
        'charset' => 'UTF-8'

        'TRUST_BADGES' => 'Our Trust Badges',
        'SOCIAL_MEDIA' => 'Social Platforms',
    ];

important

If some changes do not take effect directly, take care to update the template cache:

    ```bash
    ./vendor/bin/oe-console oe:cache:clear
    ```

Load development files
-------------------------

Create Views Folder and Copy Files

```bash
mkdir your_project_name/source/Application/views/child
cp -r your_project_name/vendor/o3-shop/o3-theme/* your_project_name/source/Application/views/child
```

Create Out Folder child and Copy Files

```bash
mkdir your_project_name/source/out/child
cp -r your_project_name/vendor/o3-shop/o3-theme/out/o3-theme* your_project_name/source/out/child
```       
