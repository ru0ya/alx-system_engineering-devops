#!/usr/bin/env ruby
#regular expression that only matches capital letters

x = ARGV[0]
puts x.scan(/[A-Z]*/).join
