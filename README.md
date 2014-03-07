# fixhub

**Note**: I am no longer using or maintaining fixhub.

Recently, GitHub introduced [Octicons](https://github.com/blog/1106-say-hello-to-octicons), which broke GitHub for users browsing the web with their own fonts (e.g., *Allow pages to choose their own fonts* set to **no** in Firefox).
fixhub replaces several of the Octicon font glyphs with PNG images or text labels so you can use GitHub with your own fonts.

# Screenshots

The following before-and-after screenshots demonstrate some of fixhub's features.

## User bar
*before*

![user bar before](https://github.com/davidlazar/fixhub/raw/ef82bbea6482377c47d0a9dfee1640a3273ffb34/screenshots/userbar-before.png)

*after*

![user bar after](https://github.com/davidlazar/fixhub/raw/ef82bbea6482377c47d0a9dfee1640a3273ffb34/screenshots/userbar-after.png)

## Repository list
*before*

![repo before](https://github.com/davidlazar/fixhub/raw/ef82bbea6482377c47d0a9dfee1640a3273ffb34/screenshots/repo-before.png)

*after*

![repo after](https://github.com/davidlazar/fixhub/raw/ef82bbea6482377c47d0a9dfee1640a3273ffb34/screenshots/repo-after.png)

## File list
*before*

![files before](https://github.com/davidlazar/fixhub/raw/ef82bbea6482377c47d0a9dfee1640a3273ffb34/screenshots/files-before.png)

*after*

![files after](https://github.com/davidlazar/fixhub/raw/ef82bbea6482377c47d0a9dfee1640a3273ffb34/screenshots/files-after.png)

## User activity
*before*

![activity before](https://github.com/davidlazar/fixhub/raw/ef82bbea6482377c47d0a9dfee1640a3273ffb34/screenshots/activity-before.png)

*after*

![activity after](https://github.com/davidlazar/fixhub/raw/ef82bbea6482377c47d0a9dfee1640a3273ffb34/screenshots/activity-after.png)

# Usage

fixhub is a [Greasemonkey](https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/) script.

To install and use:

1. Generate the CSS used to replace the current GitHub icons:

    `$ python gencss.py > fixhub-icons.css`

2. With Greasemonkey enabled in Firefox, install the fixhub user script:

    `$ firefox fixhub.user.js`

# Icons

fixhub uses icons from the following free icon sets:

* [Silk icons](http://www.famfamfam.com/lab/icons/silk/) by famfamfam
* [Iconic](http://somerandomdude.com/work/iconic/) by Some Random Dude
* [Wireframe Toolbar icon set](http://www.gentleface.com/free_icon_set.html) by Gentleface

Thanks to the authors of these icons.

# License

All non-icon files are MIT licensed.
