# Creates a puppet manifest that kills killmenow process

exec { 'pkill':
  command => 'pkill killmenow',
  provider => 'shell',
}
