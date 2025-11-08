public class QuickFind {
    public int[] id; // Initialized empty array

    // Constructor that assigns each object to their corresponding id
    public QuickFind(int n){
        id = new int[n]; // created new array "id" size of n
        for (int i = 0; i < n; i++){
            id[i] = i; // sets id of each object to itself (e.g element with id of 0 has value 0 and etc)
        }
    }

    public boolean connected(int p, int q){
        // Checks whether p and q are in same component
        return id[p] == id[q];
    }

    public void union(int p, int q){
        int elementWithPid = id[p]; // stores the value of elements that has same id value as p
        int elementsWithQid = id[q];

        for (int i = 0; i < id.length; i++){
            if (id[i] == elementWithPid){
                // Change first element (p) to second element's value (q)
                id[i] = elementsWithQid;

            }

            // if(id[i] == id[p]) Doesn't work properly, only handles 1 element value change, not many values
        }

    }

    public void displayQFindArray(){
        for (int item: id){
            System.out.print(item + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        QuickFind quickFind = new QuickFind(5);
        quickFind.displayQFindArray();
        quickFind.union(4 ,3);
        System.out.println(quickFind.connected(4, 3));
        quickFind.displayQFindArray();
        quickFind.union(3, 1);
        quickFind.displayQFindArray();
        quickFind.union(1, 0);
        quickFind.displayQFindArray();

    }
}
