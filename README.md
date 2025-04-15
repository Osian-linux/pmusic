# pmusic
Polybar module which display what is currently plaing

# __Dependencies:__

__```playerctl```:__

Install on ```Arch Linux```:

```~# pacman -S playerctl```

Install on ```Ubuntu\Debian```:

```~# apt install playerctl```

__Install:__

run ```install.sh``` and add this lines to polybar config:

```
[module/pmusic]
type = custom/script
exec = ~/.polybar-scripts/pmusic/pmusic.sh
interval = 2
```

# __Screenshots:__
![image](https://github.com/user-attachments/assets/aeac1243-b7d6-4d63-a8c0-e4dd3534e3c3)
