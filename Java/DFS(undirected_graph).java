import java.util.*;
class Graph{
    int ver;
    int adjMatrix[][];
    Graph(int v){
        ver = v;
        adjMatrix = new int[ver][ver];
    }
    public void addEdge(int u, int v){
        adjMatrix[u][v] = 1;
        adjMatrix[v][u] = 1;
    }
    public  void printMatrix(){
        for(int i = 0; i < adjMatrix.length; i++){
            for(int j = 0; j < adjMatrix.length; j++){
                System.out.print(adjMatrix[i][j]+" ");
            }
            System.out.println();
        }
         
    }
    public void DFS(int source,boolean[] visited){
        System.out.print(source + " ");
        visited[source] = true;
        for(int i = 0; i < adjMatrix.length; i++){
            if(adjMatrix[source][i] == 1 && !visited[i]){
                visited[i] = true;
                DFS(i,visited);
            }
        }
    }
    
}
public class Main{
    public static void main(String[] args){
        Graph g = new Graph(4);
        g.addEdge(0,1);
        g.addEdge(0,2);
        g.addEdge(1,3);
        g.printMatrix();
        boolean visited[] = new boolean[4];
        for(int j = 0; j < 4; j++){
            if(!visited[j]){
                g.DFS(j,visited);
            }
        }
    }
}
