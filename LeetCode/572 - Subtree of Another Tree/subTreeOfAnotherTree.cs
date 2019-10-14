/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public bool IsSubtree(TreeNode s, TreeNode t) {
        if(s == null)
            return t == null;
        if (Match(s, t))
            return true;
        else
            
            return IsSubtree(s.left, t) || IsSubtree(s.right, t);
    }
    public bool Match(TreeNode s, TreeNode t)
    {
        if(!(s!=null && t!=null))
            return s == null && t == null;
        if(s.val == t.val)
            return Match(s.left, t.left) && Match(s.right, t.right);
        return false;
    }
}