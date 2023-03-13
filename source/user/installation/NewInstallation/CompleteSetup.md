# Complete the installation

## Setup directory

After successful installation, the **/setup** directory is automatically deleted. This is to prevent the setup from being called up again at a later time. Check whether the deletion of the directory was successful.

## File and directory rights

For error-free operation, the shop requires write permissions for some directories (file permissions on 777 or 775). Please make sure that the write permissions for the directories **/source/out/pictures**, **/source/out/media**, **/source/log**, **/source/export**, **/source/tmp** and **/var** are set, if necessary also recursively in all subdirectories.

The **.htaccess** and **config.inc.php** files from the main directory must be write-protected after the setup has been completed (file rights set to 444).