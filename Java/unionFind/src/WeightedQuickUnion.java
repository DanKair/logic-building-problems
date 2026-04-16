public class WeightedQuickUnion {
    // Key idea of Data Structure: Make smaller tree under bigger tree (which has more elements belonging to it)
    public int[] id;  // parent[i] = parent of i
    public int[] size; // size[i] = number of elements in subtree rooted at i
    public int count;

    // Constructor: set id for each object to itself
    public WeightedQuickUnion(int n) {
        id = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            id[i] = i;  // sets id of each object to itself (e.g element with id of 0 has value 0 and etc)
            size[i] = 1; // size of each element by default is 1
        }
    }

    // root = the final node in the chain (the one pointing to itself)
    // chase parent pointers until reach root
    // (depth of i array accesses)
    private int root(int i) {   // find operation
        while (i != id[i]) { // checking if i is its own parent. If it's not, that means it's not the root, so we need to keep moving up to the next parent.
            i = id[i]; // Follow the parent of i
        }

        return i;
    }

    public boolean connected(int p, int q) {
        return root(p) == root(q);
    }

    public void union(int p, int q) {
        int i = root(p);
        int j = root(q);

        // if i and j has same root value, then they're already connected
        if (i == j) return;
        if (size[i] < size[j]) {
            // change 1st root point 2nd (smaller to larger one)
            id[i] = j;
            // append size of "loser's" elements
            size[j] += size[i];
        }

        else {
            // NOTE: Doesn't make child elements to also point to the new root
            // Only makes root point to new root
            id[j] = i;
            size[i] += size[j];
        }
    }

    public void displayQUnion(){
        for (int item: id){
            System.out.print(item + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        WeightedQuickUnion wq = new WeightedQuickUnion(5);
        wq.displayQUnion();
        wq.union(1, 2);
        wq.displayQUnion();
        wq.union(2, 3); // 3 should go under 1, because smaller tree goes below larget tree
        wq.displayQUnion();
        wq.union(0, 4);
        wq.displayQUnion();
        wq.union(3, 4);
        wq.displayQUnion();
    }


}
