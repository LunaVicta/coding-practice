class Tree
    attr_accessor :children, :node_name
    def initialize(hashmap)
        @children = []
        hashmap.each_pair do
            |key, value|
            @node_name = key
            value.each_pair { |k,v| @children.append(Tree.new({k => v}))}
        end
    end

    def visit_all(&block)
        visit &block
        children.each {|c| c.visit_all &block}
    end

    def visit(&block)
        block.call self
    end
end
family = Tree.new({"grandpa"=>{"dad"=>{"child 1"=>{}, "child 2"=>{}}, "uncle"=>{"child 3"=>{}, "child 4"=>{}}}})
family.visit_all {|node| puts node.node_name}