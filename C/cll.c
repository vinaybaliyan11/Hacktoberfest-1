#include<stdio.h>
#include<stdlib.h>

struct node
{
    int digit;
    struct node *next;
};
void traverse(struct node *head)
{
    struct node *ptr=(struct node *)malloc(sizeof(struct node));
    ptr=head;
    while(1==1)
    {
        printf("Value in the node %d\n",ptr->digit);
        ptr=ptr->next;
        if(ptr==head)
        {
            break;
        }
    }
}
int search(struct node *head)
{
    struct node *ptr=(struct node *)malloc(sizeof(struct node));
    ptr=head;
    int sear;
    printf("Enter the no sear you want to search\n");
    scanf(" %d",&sear);

    while(1==1)
    {
        if(ptr->digit==sear)
        {
            return 1;
        }
        else
        {
            ptr=ptr->next;
            if(ptr==head)
            {
                return 0;
            }
        }
    }
}
int main()
{
    struct node *head=(struct node *)malloc(sizeof(struct node));
    struct node *s=(struct node *)malloc(sizeof(struct node));
    struct node *t=(struct node *)malloc(sizeof(struct node));
    struct node *f=(struct node *)malloc(sizeof(struct node));
    struct node *last=(struct node *)malloc(sizeof(struct node));

    head->digit=9;
    head->next=s;

    s->digit=26;
    s->next=t;

    t->digit=76;
    t->next=f;

    f->digit=96;
    f->next=last;

    last->digit=86;
    last->next=head;

    traverse(head);
    int r=search(head);
    if(r==1)
    {
        printf("Founded");
    }
    else{
        printf("Not found");
    }

    



    return 0;
}
