#updating a configuration file
file{ '~/.ssh/school':
ensure                 => 'file',
mode                   => '0600',
user                   => 'ubuntu',
PasswordAuthentication => 'no',
}




