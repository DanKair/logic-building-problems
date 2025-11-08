public class QuickUnion {

    public int[] id;

    // Constructor: set id for each object to itself
    public QuickUnion(int n){
        id = new int[n]; // created new array "id" size of n
        for (int i = 0; i < n; i++){
            id[i] = i; // sets id of each object to itself (e.g element with id of 0 has value 0 and etc)
        }
    }

    // chase parent pointers until reach root
    // (depth of i array accesses)
    private int root(int i) {   // find operation
        while (i != id[i]) { // checking if i is its own parent. If it's not, that means it's not the root, so we need to keep moving up to the next parent.
            i = id[i]; // Follow the parent of i
        }

        return i;
    }

    // check if p and q have same root
    // (depth of p and q array accesses)
    public boolean connected(int p, int q) {
        return root(p) == root(q);
    }

    // change root of p to point to root of q (depth of p and q array acceses)
    public void union(int p, int q) {
        int i = root(p);
        int j = root(q);

        id[i] = j;  // Make the root of p point to the root of q
    }

    public void displayQUnion(){
        for (int item: id){
            System.out.print(item + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        QuickUnion qu = new QuickUnion(5);
        qu.union(1, 3); // 3 becomes root of 1
        qu.union(3, 4); // 4 -> 3 -> 1
        System.out.println(qu.connected(3, 1));
        qu.displayQUnion();
    }
}
