require 'awesome_print'
require 'set'

class Vertex
  attr_accessor :name, :neighbors, :weights

  def initialize(name)
    @name = name
    @neighbors = []
    @weights = []
  end
end

class Graph
  attr_accessor :vertices

  def initialize
    @vertices = []
  end

  def add_vertex(name)
    @vertices << Vertex.new(name)
  end

  def find_vertex_by_name(name)
    vertices.each do |v|
      return v if v.name == name
    end
    nil
  end

  def count
    vertices.length
  end

  def add_edge(start_name, end_name, weight = nil, undirected = true)
    from = vertices.index { |v| v.name == start_name }
    to   = vertices.index { |v| v.name == end_name }
    vertices[from].neighbors[to] = true
    vertices[from].weights[to] = weight if weight
    if undirected
      vertices[to].neighbors[from] = true
      vertices[to].weights[from] = weight if weight
    end
  end

end



path='../dataset-1/*'
# path='../dataset-1/*01_10*'

start=Time.now

graphs=[]
Dir[path].each do |file|
  # g = Hash.new { |h,k| h[k] = {} } # 1
  # g=Set.new # 2
  g=Graph.new
  File.foreach(file).drop(1).each do |line|
    e1,e2,w=line.split ' '
    # 1
    # g[e1][e2]=w
    # g[e2][e1]=w

    # 2
    # g.add({[e1,e2].to_set => w})
    g.add_vertex(e1)
    g.add_vertex(e1)
    g.add_edge(e1, e2, w)
  end
  graphs << g
end

#ap graphs

endt=Time.now

puts "Time: #{endt-start}, with #{graphs.count} graphs"