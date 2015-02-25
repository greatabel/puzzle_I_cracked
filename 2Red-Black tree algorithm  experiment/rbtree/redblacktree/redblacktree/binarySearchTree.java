package redblacktree;

public class binarySearchTree extends redblacktree{
	
	private Node root;
	public Node nil= new Node();
	
	//��ʼ��Ҷ��
	private  void InitNil(){
		 nil.NData=0;
		 nil.color=true;  //Ҷ�ӽڵ㶼�����Ǻڵ�
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
		node.color=false;  //Ĭ��ִred
		node.leftChild =nil;
		node.rightChild =nil;
		
				
	}
	
	
	public void BSTInsert(Node node)
	{
		//������ʱ��
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
			{ //��Ҫ����ڵ������ֵ�ȵ�ǰ��ͷ�ڵ������ֵС��ʱ����������߲���
				begin=begin.leftChild;
				if(begin==nil)
				{ //�Ѿ����Ƶ����������
					begin.leftChild=node;
					node.parent=parent;
					return ;
				}
				
			} 
			else{
				//��Ҫ��������ұ�ʱ��
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