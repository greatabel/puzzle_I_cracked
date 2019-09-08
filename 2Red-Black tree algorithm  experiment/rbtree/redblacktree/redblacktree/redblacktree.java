package redblacktree;

import java.io.*;

/*------本段代码实现的功能是插入（红黑树涉及树的调整：左旋、右旋等），删除，搜索（指定Key值节点）-----*/

public class redblacktree{
	
	public Node root;
	public Node nil= new Node();
	
	//初始化叶点
	private  void InitNil(){
		 nil.NData=0;
		 nil.color=true;  //叶子节点都必须是黑的
		 nil.leftChild=null;
		 nil.rightChild=null;
		 
	}
	
	
	//设置根节点
	private void setRoot(Node node){
    this.root=node;		
	}
	
	
	
	
	
	
	private Node getMin(Node node){
		while(node.leftChild !=nil)
			node=node.leftChild ;
		return node;
	}
	
	
	/*----------------------小的public---------------*/
	public  Node getRoot(){
		return this.root;
		
	}
	
	public void preOrder(){
		preOrderRBTree(this.root,1);
		
	}
	//插入属性值
	public void rbInsert(int i)
	{
		InitNil();
		Node node=new Node();
		node.NData =i;
		Insert(node);
		node.color=false;  //默认执red
		node.leftChild =nil;
		node.rightChild =nil;
		rbInsertAdjustment(node);
		
		
	}
	
	//下面实现rank（T，x）的相关代码
	public int size(Node node)
	{ if(node==nil) return 0;
	else  return size(node.leftChild )+size(node.rightChild )+1;
	
	}
	public int OSRank(int x)
	{ int r;
	Node y;
	r=size(search(x).leftChild )+1;
	y=search(x);
	while(y!=this.root)
	{ if(y==y.parent.rightChild)
		 r=r+size(y.parent.leftChild )+1;
	    y=y.parent ;
	}
	    return r;
	}
	
	
	/*-----------------------按照数值找节点---------------*/
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
	
	
	public Node rbDelete(int i){
		Node node;
		node=search(i);
		if(node==null) return null;
		else return (rbDelete(node));
	}
	
	
	
	
	
	
	
	
	
	/*--------------------------------------------*/
	//红黑树的饿节点的插入操作
	public void Insert(Node node)
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
	
	
	
	
	//前序遍历红黑树
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
	    
	    
	         }//end of preOrderRBTree
	
	
	//红黑树进行左旋转
	private void leftRotate(Node node){
		Node temp;
       temp=node.rightChild ;
       
       node.rightChild =temp.leftChild ;
       /*------------1---------------*/
       if(temp.leftChild !=nil)
    	   temp.leftChild .parent =node;
           temp.parent =node.parent ;
       /*------------2当前节点没有父母节点，即是自己是新插入的第一，或者以前树被删除空--------------*/
       if(node.parent ==nil) this.setRoot(temp);
       else if(node==node.parent .leftChild )
    	      node.parent .leftChild =temp;
       else node.parent .rightChild =temp;
       temp.leftChild =node;
       node.parent =temp;
                    }
	
	private void rightRotate(Node node){
		Node tempa;
		tempa=node.leftChild ;
		
		node.leftChild =tempa.rightChild ;
		if(tempa.rightChild !=nil) tempa.rightChild .parent =node;
		tempa.parent=node.parent ;
		
		if(node.parent ==nil) this.setRoot(tempa);
		else if (node==node.parent .leftChild ) node.parent .leftChild =tempa;
		else node.parent .rightChild =tempa;
		tempa.rightChild =node;
		node.parent =tempa;
	}

	//红黑树插入后的调整
	private void rbInsertAdjustment(Node node){
		while(node.parent .color == false)
		{
			if(node.parent ==node.parent .parent .leftChild )
			{ Node temp=node.parent .parent .rightChild ;
			if(temp.color ==false){
				node.parent.color =true;
				temp.color =true;
				node.parent .parent .color =false;
				node=node.parent .parent ;
                        		}
			else          {
				if(node==node.parent .rightChild ){
					node=node.parent ;
					leftRotate(node);
				                                  }
				node.parent .color =true;
				node.parent .parent .color =false;
				rightRotate(node.parent .parent );
				
			              }
			                 }
			else {
				Node temp=node.parent .parent .leftChild ;
				if(temp.color ==false){
					node.parent .color =true;
					temp.color =true;
					node.parent .parent .color =false;
					node=node.parent .parent ;
				}
				else{
					if(node==node.parent.leftChild ){
						node=node.parent ;
						rightRotate(node);
					}
					node.parent .color =true;
					node.parent .parent .color =false;
					leftRotate(node.parent .parent );
				}
			}
		}
		this.getRoot().color=true;
	}
	//查找后继
	private Node getSuccessor(Node node){
        if (node.rightChild != nil) return getMin(node.rightChild);
        Node y = node.parent;
        while((y != nil) && (y.rightChild == node)){
            node = y;
            y = y.parent;
        }
        return y;
    }
	
	
	//节点删除
	private Node rbDelete(Node node){
        Node y, x;
        if ((node.leftChild == nil) || (node.rightChild == nil))
            y = node;
        else y = getSuccessor(node);
        if (y.leftChild != nil) x = y.leftChild;
        else x = y.rightChild;
        x.parent = y.parent;
        if (y.parent == nil) setRoot(x);
        else if (y == y.parent.leftChild) y.parent.leftChild = x;
        else y.parent.rightChild = x;
        if(y != node) node.NData  = y.NData;
        if (y.color == true) rbDeleteAdjust(x);
        return y;
    }
	
	
	
	
	//删除后调整为红黑树
	 private void rbDeleteAdjust(Node node){
	        while(node != getRoot() && node.color == true)
	            if(node == node.parent.leftChild){
	                Node y = node.parent.rightChild;
	                if(y.color == false){
	                    y.color = true;
	                    node.parent.color = false;
	                    leftRotate(node.parent);
	                    y = node.parent.rightChild;
	                }
	                if ((y.leftChild.color == true) && (y.rightChild.color == true)){
	                    y.color = false;
	                    node = node.parent;
	                }
	                else if(y.rightChild.color == true){
	                    y.leftChild.color = true;
	                    y.color = false;
	                    rightRotate(y);
	                    y = node.parent.rightChild;
	                    }
	                y.color = node.parent.color;
	                node.parent.color = true;
	                y.rightChild.color = true;
	                leftRotate(node.parent);
	                node = getRoot();
	            }
	            else{
	                Node y = node.parent.leftChild;
	                if(y.color == false){
	                    y.color = true;
	                    node.parent.color = false;
	                    rightRotate(node.parent);
	                    y = node.parent.leftChild;
	                }
	                if ((y.rightChild.color == true) && (y.leftChild.color == true)){
	                    y.color = false;
	                    node = node.parent;
	                }
	                else if(y.leftChild.color == true){
	                    y.rightChild.color = true;
	                    y.color = false;
	                    leftRotate(y);
	                    y = node.parent.leftChild;
	                    }
	                y.color = node.parent.color;
	                node.parent.color = true;
	                y.leftChild.color = true;
	                rightRotate(node.parent);
	                node = getRoot();
	            }
	        node.color = true;
	    }
	 
	 
	//求出红黑树的黑高度
	public int bDepth(){
		Node mynode=this.root ;
		Node p=mynode;
		Node[] Stack1;
		Stack1=new Node[10];
		int[] Stack2;
		Stack2=new int[10];
		
		int curdepth,maxdepth=0,top=-1;
		if(mynode!=null){
	  curdepth=1;
	  do{
		  while(p!=null)
		  {Stack1[++top]=p;
		  Stack2[top]=curdepth;
		  
		  if(p.color==true)
		  {p=p.leftChild ;
		   curdepth++;
		  }
		  else p=p.leftChild ;
		   
		  } //end of WHILE
		  p=Stack1[top];
		  curdepth=Stack2[top--];
		  if(p.leftChild ==null && p.rightChild ==null)
			   if(curdepth>maxdepth)
				   maxdepth=curdepth;
		  if(p.color==true)
		  {
		  p=p.rightChild ;
		  curdepth++;
		  }
		  else p=p.rightChild ;
	  
		  
	  }while(!(p==null && top==-1));//end of DO
		}// end of IF 
  return(maxdepth);
	
	} //end of BLACK Height
	
	
	

	
}//end of the whole red-black tree class


















































	
	
	
	