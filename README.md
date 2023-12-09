<div align="center"> <image src="./telegramScreenshot.png" height="400px" width="auto"> </div>
<h1 align="center"> tmate sender</h1>
<br>

## INSTALLATION

### Install dependencies

Debian & Ubuntu etc.:
`sudo apt install tmate curl tmux`

Arch and derivatives:
`sudo pacman -S tmate curl tmux`

## quick setup
```bash
git clone url && cd amogusmate
python -m venv .venv && source .venv/bin/activate
pip3 install argparse
sudo python install.py --install --systemd
```

## Uninstall
```bash
sudo python amogusmate.py --uninstall
```


### TO DO 
- [X] Use systemd than cron job
- [X] Add install.py
- [X] Add systemd service
- [X] Add install/uninstall option
- [ ] Script explanation
- [ ] Write usecase
- [ ] Port amogusmate to python
- [ ] Reformat Message to be more readable