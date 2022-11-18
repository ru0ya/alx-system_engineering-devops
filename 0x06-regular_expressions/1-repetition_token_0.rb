#!/usr/bin/env ruby
#regular expression that matches given string

x = ARGV[0]
puts x.match(/hbt{2, 5}n/).join
