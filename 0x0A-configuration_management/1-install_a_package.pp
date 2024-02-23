# Install flask from pip3

class { 'python':
  ensure => 'present',
}

package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/bin',
  require => [Class['python'], Package['python3-pip']],
}

exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install Werkzeug',
  path    => '/usr/bin',
  require => [Class['python'], Package['python3-pip']],
}
