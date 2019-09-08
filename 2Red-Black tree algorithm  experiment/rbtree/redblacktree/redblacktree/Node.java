package redblacktree;

import java.io.*;
/*-------Node类实现的主要是定义节点的属性和相关操作，以便于其他类调用--------*/
public class Node{
	 int NData;                 //储存节点数据值
	 Node parent;              //节点的父母节点
	 Node leftChild;           //节点的左孩子节点
	 Node rightChild;          //节点的右孩子节点
	 boolean color;            //节点的颜色

	 
 //设置节点的数值
  public void setNode(int i){
	  this.NData=i;
  }
 //输出节点相关信息
  public void displayNode(){
	  System.out.println("Data:"+this.NData+";color:"+this.color);
  }
 //取得节点的属性值
  public int getValue(){
	  return this.NData;
  }
  //取得节点的颜色
  public String getColor(){
	  if(this.color==true) return "B";
	  else return "R";
  }
  
  
}












