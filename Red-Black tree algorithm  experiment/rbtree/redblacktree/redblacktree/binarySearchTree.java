package redblacktree;

public class binarySearchTree extends redblacktree{
	
	private Node root;
	public Node nil= new Node();
	
	//初始化叶点
	private  void InitNil(){
		 nil.NData=0;
		 nil.color=true;  //叶子节点都必须是黑的
		 nil.leftChild=null;
		 nil.rightChild=null;
		 
	}
	
	public void preOrder(){
		preOrderRBTree(this.root,1);
		
	}
	
	public void BSTInsert(int i)
	{
		InitNil();
		Node node=new Node();
		node.NData =i;
		BSTInsert(node);
		node.color=false;  //默认执red
		node.leftChild =nil;
		node.rightChild =nil;
		
				
	}
	
	
	public void BSTInsert(Node node)
	{
		//空树的时候
		if(root==null){
			root=node;
			root.parent=nil;
			
		}
		else
		{
			Node begin =root;
			Node parent;
			while(true){
			parent=begin;
			if(node.NData< begin.NData)
			{ //当要插入节点的属性值比当前的头节点的属性值小的时候，我们往左边插入
				begin=begin.leftChild;
				if(begin==nil)
				{ //已经下移到了最底下了
					begin.leftChild=node;
					node.parent=parent;
					return ;
				}
				
			} 
			else{
				//当要插入的在右边时候
				begin=begin.rightChild;
				if(begin==nil)
				{ 
					parent.rightChild=node;
				node.parent=parent;
				return ;
				}
			}
			}//end of while
			
			
		}//end of else
		
	}
	
	
	
	private void preOrderRBTree(Node root,int level){
		
		if(root != null)
			
			System.out.println("(" + root.NData + root.getColor() + ",");
		        if(root.leftChild == nil) 
		        { for(int i=0;i<level;i++) System.out.print("  "); 
		        	System.out.println("NIL,");
		        }
		        else {
		           preOrderRBTree(root.leftChild,level++);
		           for(int i=0;i<level;i++) System.out.print("  "); 
		           System.out.println(",");
		           }
		        for(int i=0;i<level;i++) System.out.print("  "); 
		        if(root.rightChild == nil) 
		        {	 for(int i=0;i<level;i++) System.out.print("  "); 
		        	System.out.println("NIL)");
		        }
		        else{
		           preOrderRBTree(root.rightChild,level++);
		           for(int i=0;i<level;i++) System.out.print("  "); 
		           System.out.println(")");
		           }
		    
		    
		         }//
	
	
	public Node search(int key){
		if(root==null) return null;
		else {
			Node temp=root;
			while(temp.NData !=key)
			{if(key<temp.NData )
				temp=temp.leftChild ;
			else
				temp=temp.rightChild ;
			if(temp==nil)
				return null;
			}
			return temp;
		}
	}
	
}