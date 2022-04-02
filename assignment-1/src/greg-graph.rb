require 'awesome_print'
require 'set'
require 'algorithms'

include Containers

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

def prim(g, s)
  inf=1/0.0
  # g.each{|i| i.merge({:parent => nil, :key => inf})}
  q=MinHeap.new
  g.each do |k,v| 
    v.merge!({:parent => nil, :key => [inf]})
    q.push(v[:key], k)
  end
  ap q.min
  g['2'][:key][0]=3
  q.change_key('2', 3)
  ap q.min
  
  # Q=[(g[i]['key'], i) for i in list(g.keys())]
  # g[s]['key'][0]=0
  # heapq.heapify(Q)

  # while len(Q)>0
  #     u=hpop(Q)
  #     print('adjacent of ', u, ' are ', g[u[1]])
  #     for v in [item for item in g[u[1]] if item!='key' and item !='parent']
  #         for key, i in Q
  #             # print(i,'==',v,' and ',int(g[u[1]][v]),' < ', key[0])
  #             if i==v and int(g[u[1]][v])<key[0]
  #                 key[0]=int(g[u[1]][v])
  #                 g[v]['parent']=u[1]
  #     heapq.heapify(Q)
end


path='../dataset-1/*'
# path='../dataset-1/*01_10*'
GC.disable
start=Time.now


graphs=[]
num_exec=1

Dir[path].each do |file|
  g = Hash.new { |h,k| h[k] = {} } # 1
  # g=Set.new # 2
  # g=Graph.new
  File.foreach(file).drop(1).each do |line|
    e1,e2,w=line.split ' '
    # 1
    g[e1][e2]=w
    g[e2][e1]=w

    # 2
    # g.add({[e1,e2].to_set => w})
    
    # 3
    # g.add_vertex(e1)
    # g.add_vertex(e1)
    # g.add_edge(e1, e2, w)
  end
  # graphs << g
  GC.disable
  start=Time.now
  num_exec.times{prim(g,1)}
  endt=Time.now
  GC.enable
  graphs << (endt-start)/num_exec
end

#ap graphs

endt=Time.now
GC.enable

# puts "Time: #{endt-start}, with #{graphs.count} graphs"
puts "Averages: #{graphs}"
