def reverse_in_place(arr)
  (arr.length / 2).times do |i|
    arr[i], arr[-1-i] = arr[-1-i], arr[i]
  end
end

def diag_flip(arr)
  (arr.length - 1).times do |col|
    ((col + 1)..(arr.length - 1)).each do |row|
      arr[row][col], arr[col][row] = arr[col][row], arr[row][col]
    end
  end
end

def rotate(arr)
  diag_flip(arr)
  arr.each { |row| reverse_in_place(row) }
end

arr = [%w(a b c d), %w(e f g h), %w(i j k l), %w(m n o p)]
rotate(arr)

p arr
