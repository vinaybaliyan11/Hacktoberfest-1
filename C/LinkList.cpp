#include<iostream>

using namespace std;

struct node{
    int data;
    node* next;
};
node *A;


void insertNode(int val){
    node *temp = new node();
    temp -> data = val;
    temp -> next = NULL;
    node* temp1 = A;
    while(temp1-> next != NULL){
        temp1= temp1-> next ;
    } temp1-> next = temp;
}

void showList(){
    node* temp1=A;
    /*while(temp1-> next != NULL){
        temp1= temp1-> next;
        cout << temp1-> data << " -> ";
        */
    for (node* temp= head; temp!=NULL; temp=temp->next){
        cout << temp1-> data << " -> ";
    }

    }cout << endl;
}



void deleteMin(){
    // 98 5 7 2 9 6 887 55 0
    node *head=A;

    node *temp=head; //for traversal
    node *prev=NULL;

    node *mini=head; //for getting the smallest element
    node *minPrev=NULL; // for list bridging

    while(temp!=NULL){
        if(temp->data < mini->data){
            minPrev=prev;
            mini=temp;
        }
        prev=temp;
        temp=temp->next;

    }
    if(minPrev==NULL)
        head=mini->next;
    else
        minPrev->next=mini->next;

    cout<<"element to delete is "<<mini->data<<"\n";
    delete mini;

    showList();
}

int main(){
    A = NULL;
    node *temp = new node();
    temp -> data = 2;
    temp -> next= NULL;
    A = temp;
    cout << "how many values?" << endl;
    int n,v;
    cin >> n ;
    cout << "enter values" << endl;
    for (int i =0; i<n;i++){
        cin >> v;
        insertNode(v);
    }
    showList();
    //delete
    // Search
    // length
    // mid

}
