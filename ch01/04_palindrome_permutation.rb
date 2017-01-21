def pal_perm(str)
  char_counts = Hash.new(0)

  str.split('').select { |c| ('a'..'z').include? c.downcase }.each do |c2|
    char_counts[c2.downcase] += 1
  end

  num_odd = char_counts.values.count {|n| n.odd?}
  [0, 1].include? num_odd
end

puts pal_perm("TacCat")
