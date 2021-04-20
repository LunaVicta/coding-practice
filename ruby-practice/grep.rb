puts "Enter a file name: "
fileName = gets.chomp
puts "Enter a search string: "
searchString = gets.chomp
puts
puts
File.open(fileName, 'r') do |f|
    line = 0
    f.each do
        |l|
        if l.include? searchString
            puts l
            puts line
        end
        line += 1
    end
end