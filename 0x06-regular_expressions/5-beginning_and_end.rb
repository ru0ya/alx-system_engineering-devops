#!/usr/bin/env ruby
#matches a string starting with 'h' and ends with 'n'
x = ARGV[0]
puts x.scan(/h.n/).join
