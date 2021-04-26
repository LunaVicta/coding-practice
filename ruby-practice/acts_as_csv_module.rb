module ActsAsCsv
    def self.included(base)
      base.extend ClassMethods
    end
    
    module ClassMethods
      def acts_as_csv
        include InstanceMethods
      end
    end
    
    module InstanceMethods
      def read
        @csv_contents = []
        filename = self.class.to_s.downcase + '.txt'
        file = File.new(filename)
        @headers = file.gets.chomp.split(', ')
  
        file.each do |row|
          @csv_contents << row.chomp.split(', ')
        end
      end

      class CsvRow
          def initialize(headers, contents)
              @headers = headers
              @row_contents = contents
          end
          def self.method_missing name, *args
              h = name.to_s
              @row_contents[@headers.index(h)]
          end
      end

      def each(&block)
           
      end
      
      attr_accessor :headers, :csv_contents
      def initialize
        read 
      end
    end
  end
  
  class RubyCsv  # no inheritance! You can mix it in
    include ActsAsCsv
    acts_as_csv
  end
  
  m = RubyCsv.new
  puts m.headers.inspect
  puts m.csv_contents.inspect