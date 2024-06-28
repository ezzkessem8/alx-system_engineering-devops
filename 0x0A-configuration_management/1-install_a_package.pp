# Install flask
# Using ensure attribute to specify the version
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
