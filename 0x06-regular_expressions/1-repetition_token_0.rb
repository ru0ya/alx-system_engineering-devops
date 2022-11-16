#!/usr/bin/env ruby
#character 't'matches a specified number of strings

x = ARGV[0]
puts x.scan(/hbt{2, 5}n/).join

