# 0x0C-web_server

## Description
This project focuses on setting up and configuring a web server using Nginx on an Ubuntu server. It includes tasks such as transferring files to the server, installing and configuring Nginx, setting up domain names, and configuring custom error pages and redirections.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does
- You can’t use `systemctl` for restarting a process

## Tasks

### 0. Transfer a file to your server
**File:** `0-transfer_file`

Write a Bash script that transfers a file from the client to a server using SCP.

Requirements:
- Accepts 4 parameters:
  1. The path to the file to be transferred
  2. The IP of the server
  3. The username SCP connects with
  4. The path to the SSH private key that SCP uses
- Displays usage information if less than 4 parameters are passed
- Transfers the file to the user's home directory
- Disables strict host key checking

Example:
```bash
./0-transfer_file some_page.html 54.173.46.154 ubuntu ~/.ssh/school
```
1. Install nginx web server
File: 1-install_nginx_web_server

Write a Bash script that installs Nginx on the server, ensures it is listening on port 80, and serves a page with the string "Hello World!".

Requirements:

Install Nginx
Create an HTML page at /var/www/html/index.html with the content "Hello World!"
Start Nginx
Allow Nginx through the firewall
Example:

```bash
./1-install_nginx_web_server
```
2. Setup a domain name
File: 2-setup_a_domain_name

Provide the domain name that points to your server's IP address.

Requirements:

Provide only the domain name (e.g., exampledomain.tech)
Configure DNS records with an A entry pointing to the server's IP address
Example:

```bash
echo "exampledomain.tech" > 2-setup_a_domain_name
```
3. Redirection
File: 3-redirection

Write a Bash script that configures Nginx to redirect /redirect_me to another page with a 301 status code.

Requirements:

Configure Nginx to redirect /redirect_me to a specific URL with a 301 status code
Write the commands to automatically configure a new Ubuntu machine
Example:

```bash
./3-redirection
```
4. Not found page 404
File: 4-not_found_page_404

Write a Bash script that configures Nginx to serve a custom 404 page with the content "Ceci n'est pas une page".

Requirements:

The page must return an HTTP 404 error code
The page must contain the string "Ceci n'est pas une page"
Write the commands to automatically configure a new Ubuntu machine
Example:

```bash
./4-not_found_page_404
```
Usage
Make sure all scripts are executable:

bash
Copy code
chmod +x 0-transfer_file 1-install_nginx_web_server 3-redirection 4-not_found_page_404
Run each script as required:

```bash
./0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
./1-install_nginx_web_server
./3-redirection
./4-not_found_page_404
```
Environment
OS: Ubuntu 16.04 LTS
Editors: vi, vim, emacs
Author
[Ezra Kessem] - Developer and Maintainer of the 0x0C-web_server project.

```vbnet
*This README file provides an overview of the project, detailed descriptions of each task,
```
