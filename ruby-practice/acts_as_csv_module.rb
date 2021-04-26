module ActsAsCsv
    
    def self.included(base)
        base.extend ClassMethods
    end

    module ClassMethods
        def acts_as_csv
            include IstanceMethods
        end
    end

    module InstanceMethods
        
        def read
            @csv_contents = []
            filename = self.class.to_s.downcase + '.txt'
        end
    end
end