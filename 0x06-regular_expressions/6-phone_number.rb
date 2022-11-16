#!/usr/bin/env ruby
#mathes a 10 digit phone number
x = ARGV[0]
puts x.scan(/^[0-9]{10}$/).join
