#include<iostream>
#include<queue>
#include<malloc.h>
using namespace std;

struct node{
  int data;
  node *left;
  node *right;
};

void levelOrder(struct node *root){
  if(root == NULL) return;

  queue<node *>Q;
  Q.push(root)

  while(!Q.empty()){
    struct node* curr = Q.front()
      cout<< curr->data <<" ";
      if(curr->left != NULL) Q.push(curr-> left);
        if(curr->right != NULL) Q.push(curr-> right);

        Q.pop()
  }
}