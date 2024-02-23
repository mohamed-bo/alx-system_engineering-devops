# Install flask from pip

package { 'pip':
  ensure => 'installed',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
