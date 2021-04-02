number = rand(10)
guess = 100
until guess == number
  puts "Guess a number"
  guess = gets.to_i
  puts "Too high" if guess>number
  puts "Too low" if guess<number
end
puts "Correct! It was #{number}."
