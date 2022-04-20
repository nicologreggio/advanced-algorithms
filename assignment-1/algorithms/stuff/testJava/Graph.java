package testJava;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.AbstractMap;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.SortedMap;
import java.util.TreeMap;
import java.util.concurrent.ConcurrentSkipListMap;



class Graph{
  public static void main(String[] args) {
    File folder=new File("./testJava/dataset");
    for(var f:folder.listFiles()){
      try {
        var graph=readGraph(f);
        System.out.println(graph);
      } catch (IOException e) {
        e.printStackTrace();
      }
    }
  }

  static Map<Integer, Map<Integer, Integer>> readGraph(File f) throws IOException{
    Map<Integer, Map<Integer, Integer>> r=new HashMap<>();
    Files.lines(Paths.get(f.getAbsolutePath())).skip(1).forEach(l->{
      int[] e=Arrays.stream(l.split(" ")).mapToInt(Integer::parseInt).toArray();
      if(!r.containsKey(e[0])){
        r.put(e[0], new HashMap<>());
      }
      r.get(e[0]).put(e[1], e[2]);

      if(!r.containsKey(e[1])){
        r.put(e[1], new HashMap<>());
      }
      r.get(e[1]).put(e[0], e[2]);
    });

    return r;
  }

  static void prim(Map<Integer, Map<Integer, Integer>> g, int s){
    SortedMap<Integer, Integer> q=new ConcurrentSkipListMap<>();
    SortedMap<Integer, Integer> q2=new ConcurrentSkipListMap<>();
    Map<Integer, Integer> parents=new HashMap<>();
    g.forEach((k, v)->{
      if(k==s){
        q.put(0, k);
      }
      else{
        q.put(Integer.MAX_VALUE, k);
      }
      parents.put(k, null);
    });

  }
}