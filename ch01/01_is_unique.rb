def is_unique(str)
  sorted_str = str.split('').sort()
  (sorted_str.length - 1).times do |i|
    return false if sorted_str[i] == sorted_str[i+1]
  end

  true
end

puts is_unique("asdfghjklwertyuio")
puts is_unique("asdfa")
