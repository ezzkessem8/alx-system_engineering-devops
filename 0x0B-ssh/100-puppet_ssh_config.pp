# 100-puppet_ssh_config.pp
# Puppet manifest to configure SSH client to use a private key and disable password authentication

file { '/home/ubuntu/.ssh':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => template('ssh_config.erb'),
}

file_line { 'Declare identity file':
  path  => '/home/ubuntu/.ssh/config',
  line  => '  IdentityFile ~/.ssh/school',
  match => '^\\s*IdentityFile\\s+.*$',
}

file_line { 'Turn off passwd auth':
  path  => '/home/ubuntu/.ssh/config',
  line  => '  PasswordAuthentication no',
  match => '^\\s*PasswordAuthentication\\s+.*$',
}

# Puppet template for SSH configuration
file { '/etc/puppetlabs/code/environments/production/modules/ssh_config/templates/ssh_config.erb':
  ensure  => file,
  content => @("EOF"),
Host 91440-web-01
  HostName 54.173.46.154
  User ubuntu
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
| EOF
}
