#!/usr/bin/env ruby
# To match pattern hbttn, hbtttn, hbttttn or hbtttttn
puts ARGV[0].scan(/hbt{2,5}n/).join
