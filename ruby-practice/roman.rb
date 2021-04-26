#This class demonstrates how overriding method_missing can lead to interesting behavior.
class Roman
    def self.method_missing name, *args
        r = name.to_s
        r.gsub!("IV", "IIII")
        r.gsub!("IX", "VIIII")
        r.gsub!("XL", "XXXX")
        r.gsub!("XC", "LXXXX")

        (r.count('I') +
        r.count('V') * 5 +
        r.count('X') * 10 +
        r.count('L') * 50 +
        r.count('C') * 100)
    end
end

puts Roman.X
puts Roman.XC
puts Roman.XII
puts Roman.XIV
puts Roman.Dog_It_Up