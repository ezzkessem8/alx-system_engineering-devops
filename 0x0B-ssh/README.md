# 0x0B-ssh

## Description
This project focuses on SSH configuration and automation. The goal is to set up secure connections to servers using SSH keys and manage the configuration using both Bash scripts and Puppet manifests. The tasks cover a range of skills including generating SSH keys, configuring SSH clients, and using Puppet to automate these configurations.

## Tasks

### 0. Use a private key
**Script:** `0-use_a_private_key`

This task involves writing a Bash script to connect to a server using a specific private key without needing to type a password. The connection is established using the `ssh` command with single-character flags only.

### 1. Create an SSH key pair
**Script:** `1-create_ssh_key_pair`

This task requires creating a 4096-bit RSA key pair named `school` using a Bash script. The private key must be protected by the passphrase `betty`.

### 2. Client configuration file
**Script:** `2-ssh_config`

In this task, a script is written to configure the SSH client to use the private key `~/.ssh/school` and disable password authentication. The configuration ensures that connections to the server are secure and do not require a password.

### 3. Let me in!
**Script:** `3-setup_authorized_keys`

This task involves adding a given SSH public key to the `authorized_keys` file on the server for the `ubuntu` user. This setup allows secure access to the server using the SSH key.

### 4. Client configuration file (w/ Puppet)
**File:** `100-puppet_ssh_config.pp`

This advanced task involves using Puppet to automate the setup of the SSH client configuration. The Puppet manifest ensures that the SSH client is configured to use a specific private key and to refuse password authentication.

## Usage
1. **Make sure all scripts are executable:**
    ```bash
    chmod +x 0-use_a_private_key 1-create_ssh_key_pair 2-ssh_config 3-setup_authorized_keys
    ```

2. **Run each script as required:**
    ```bash
    ./0-use_a_private_key
    ./1-create_ssh_key_pair
    ./2-ssh_config
    ./3-setup_authorized_keys
    ```

3. **Apply the Puppet manifest:**
    ```bash
    sudo puppet apply 100-puppet_ssh_config.pp
    ```

## Notes
- Ensure that the SSH private key (`~/.ssh/school`) exists and is correctly configured.
- The Puppet manifest assumes the use of Puppet on a system with access to modify SSH configuration files.

## Environment
- **OS:** Ubuntu 20.04 LTS
- **Editors:** vi, vim, emacs

## Author
[Your Name] - Developer and Maintainer of the 0x0B-ssh project.
