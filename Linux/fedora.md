# Initial Setup

## open-ssh

Installed but not running / enabled by default.

```
systemctl enable sshd
systemctl start sshd
```

## Setup my user

Fedora (for me) has a few bugs right of the bat, my username "mem" is allowed but silently fails due to the existing group "mem".

Its not ideal but for consistency with my other installs I rename the existing group "mem" to "memsys"

```
# create my user
useradd -m -G wheel mem

# set password
passwd mem
```

## sudoers

Modify the sudoers entry for wheel

```%wheel  ALL=(ALL)       NOPASSWD: ALL```
