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

1. Create Views Folder and Copy Files

```bash
mkdir <DOCUMENT_ROOT>/source/Application/views/<THEME_NAME>
cp -r <DOCUMENT_ROOT>/vendor/o3-shop/o3-theme/* <DOCUMENT_ROOT>/source/Application/views/<THEME_NAME>
```

2. Create Out Folder <THEME_NAME> and Copy Files

```bash
mkdir <DOCUMENT_ROOT>/source/out/<THEME_NAME>
cp -r <DOCUMENT_ROOT>/vendor/o3-shop/o3-theme/out/o3-theme* <DOCUMENT_ROOT>/source/out/<THEME_NAME>
```





> **Important:**
> - <THEME_NAME> = Name of the theme used when a child theme is active. Default: o3-theme
> - <THEME_NAME> in packagist.json ändern.
> - Copy the entire `o3-theme` directory, not just its contents
> - The target should be `source/out/o3-theme/`, not `source/out/` directly