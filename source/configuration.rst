Configuration
-------------


Root
^^^^

Hide GRUB menu
""""""""""""""

.. code-block:: ini
   :caption: /etc/default/grub

   GRUB_TIMEOUT_STYLE=hidden
   GRUB_TIMEOUT=0
   GRUB_CMDLINE_LINUX_DEFAULT="quiet loglevel=0"


.. code-block:: console

   $ update-grub

Improve `agetty` legibility
"""""""""""""""""""""""""""

.. code-block:: ini
   :caption: /etc/default/console-setup

   # Change the console font settings
   FONTFACE="Terminus"
   FONTSIZE="32x16"

Install the essentials
""""""""""""""""""""""

.. code-block:: console

   $ apt-get update
   $ apt-get upgrade

   $ apt-get install sudo zsh vim \
   zsh-syntax-highlighting cmus tmux mpv \
   alsa-tools alsa-utils i3 i3blocks rofi xinit \
   xorg curl git thunar sshfs terminator starship \
   xbindkeys unclutter feh killall ncdu btop \
   zsh-syntax-highlighting gtk-theme-switch \
   taskwarrior vit jackd2 qjackctl pulseaudio \
   pulseaudio-module-jack pavucontrol pulsemixer \
   a2jmidid python3-venv python3-pip pipx \
   xclip tig

   $ usermod -aG sudo <username>
   $ chsh <username> -s /bin/zsh
   $ chsh -s /bin/zsh


User
^^^^

Fetch the dotfiles and assets
"""""""""""""""""""""""""""""

.. code-block:: console

   mkdir ~/System
   cd ~/System
   git clone https://github.com/hugligit/dotfiles.git
   git clone https://github.com/hugligit/assets.git
   sh ~/System/dotfiles/stow_all.sh
   sh ~/System/assets/stow_all.sh
   fc-cache -f -v

   # The documentation can only be built after 
   # python venv is set up correctly
   git clone https://github.com/hugligit/configure-debian-docs.git install-info



zsh
"""

.. code-block:: console

   sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

vim
"""

.. code-block:: console

   mkdir - .vim/pack/minpac/opt
   cd .vim/pack/minpac/opt
   git clone https://github.com/k-takata/minpac.git
   # vim: PackUpdate

tmux
""""

.. code-block:: console

   git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
   # tmux update plugins: leader I

sound
"""""

Find the right card and set it in `~/.asoundrc`

.. code-block:: console

  aplay -l

.. code-block:: console
   :caption: ~/.asoundrc

   defaults.pcm.card 2
   defaults.ctl.card 2

Start jack server, jack sink for pulseaudio and
midi bridge between jack and alsa.

.. code-block:: console

   # TEST: jackd -d alsa -d hw:2,0 -p 128 -n 3 -r 48000
   pactl load-module module-jack-sink
   pactl load-module module-jack-source
   # send PA to Jack sink in pavucontrol
   a2jmidid -e

python virtual environments
"""""""""""""""""""""""""""

Debian doesn't like installing pip modules outside
the virtual environments. For projects requiring
other modules the venv has to be activated:

.. code-block:: console

   python3 -m venv .venv # (or venv or anywhere else)
   source .venv/bin/activate

Then it is possible to install modules and do the
work:

.. code-block:: console
   
   python -m pip install <python-module>

The finished product can be installed so that it
works even without active venv. This only works
when there is a valid toml file in the project
root:

.. code-block:: console

   deactivate
   python3 -m pipx ensurepath
   pipx install .

.. code-block:: toml
   :caption: sample.toml

   [project]
   name = "lemon_curry"
   
   # pip freeze
   version = "0.1.0" # required :(
   dependencies = [
           # can be obtained with `pip freeze`
           "prompt_toolkit==3.0.51",
           "Pygments==2.19.2",
           ]
   
   
   [project.scripts]
   # command name = script_file:entry_function
   lemon_curry = "sample:main" 
   # say-hi = "hello:main" # another hypothetical one

bluetooth
"""""""""

# sudo apt install --no-install-recommends bluez bluez-tools blueman

github
""""""

Once only
.........

.. code-block:: console

   # Generate a new SSH key (ed25519 is recommended)
   ssh-keygen -t ed25519 -C "your_email@example.com"
   
   # Copy public key
   cat ~/.ssh/id_ed25519.pub

   xclip -sel clip < ~/.ssh/id_ed25519.pub

For each terminal session
.........................

.. code-block:: console

   # Start ssh-agent
   eval "$(ssh-agent -s)"
   
   # Add key to agent
   ssh-add ~/.ssh/id_ed25519
   

Add existing repositories to github
...................................

Add remote alias that points to the githup repository

.. code-block:: console

   git remote add origin git@github.com:USERNAME/REPO.git
   git remote -v
   git push -u origin main   # or master, matching your local branch

Simple `pull` and `push` commands are sufficient from then on.

.. code-block:: console

   git add .
   git commit -m "message"
   git push
   git pull

Github CLI setup
................

.. code-block:: console

   # Install
   (type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y)) \
   && sudo mkdir -p -m 755 /etc/apt/keyrings \
   && out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
   && cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
   && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
   && sudo mkdir -p -m 755 /etc/apt/sources.list.d \
   && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
   && sudo apt update \
   && sudo apt install gh -y

   # Completion
   mkdir ~/.oh-my-zsh/.completions # needs to be more robust
   gh completion -s zsh > ~/.oh-my-zsh/completions/_gh
   fpath=(~/.oh-my-zsh/completions $fpath)
   autoload -Uz compinit && compinit

   # One off authentication
   gh auth login


