#!/usr/bin/env ruby

phone_number = ARGV[0]

# Remove any non-digit characters from the input
phone_number.gsub!(/\D/, '')

# Check if the phone number is exactly 10 digits long
if phone_number.length == 10
  puts phone_number
end
