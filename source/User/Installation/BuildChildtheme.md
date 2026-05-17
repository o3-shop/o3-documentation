#### Creating a Child Theme

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

3. theme.php
Create a `theme.php` file in the root of the child folder.

```php
declare(strict_types=1);

$aTheme = [
    'id' => 'o3-shop-child',
    'title' => 'CHILD',
    'description' => 'A child theme from o3-shop.',
    'parentTheme' => 'o3-shop',
    'parentVersions' => ['1.1.0','1.3.0'],
];
```

> **Important:**
> - <THEME_NAME> = Name of the theme used when a child theme is active. Default: o3-theme
> - <THEME_NAME> in packagist.json ändern.
> - Copy the entire `o3-theme` directory, not just its contents
> - The target should be `source/out/o3-theme/`, not `source/out/` directly