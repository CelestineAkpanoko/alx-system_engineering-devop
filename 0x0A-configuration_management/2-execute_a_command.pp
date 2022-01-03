# Creates a puppet manifest that kills killmenow process

exec { 'pkill -f killmenow':
  path => '/usr/bin/:/usr/local/bin:/bin/',
}
