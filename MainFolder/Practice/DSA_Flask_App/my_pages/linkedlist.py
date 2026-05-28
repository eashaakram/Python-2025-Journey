import streamlit as st

from my_pages.utils import home_button

st.markdown("---")

# -----------------------------
# DRAW LINKED LIST
# -----------------------------
def draw_linked_list(llist):

    st.subheader("Linked List Visualization")

    if not llist or len(llist) == 0:
        st.warning("Linked List is empty")
        return

    cols = st.columns(len(llist))

    for i, value in enumerate(llist):

        with cols[i]:

            # NODE BOX
            st.markdown(
                f"""
                <div style="
                    border:2px solid #00FFFF;
                    padding:15px;
                    text-align:center;
                    border-radius:10px;
                    background-color:#1E1E1E;
                    color:white;
                    font-size:22px;
                    font-weight:bold;
                ">
                    {value}
                </div>
                """,
                unsafe_allow_html=True
            )

            # ARROW (except last node)
            if i != len(llist) - 1:
                st.markdown("➡")


# -----------------------------
# MAIN PAGE
# -----------------------------
def show_linked_list():

    home_button()

    st.title("Linked List Visualizer 🔗")

    # INIT
    if "llist" not in st.session_state:
        st.session_state.llist = [10, 20, 30]

    draw_linked_list(st.session_state.llist)
    st.markdown("---")

    # ---------------- INSERT ----------------
    st.subheader("Insert Node")

    value = st.number_input("Enter Value", step=1, key="ll_insert")

    position = st.number_input(
        "Position (0 = start, -1 = end)",
        step=1,
        value=-1,
        key="ll_pos"
    )

    if st.button("Insert Node"):

        if position == -1 or position >= len(st.session_state.llist):
            st.session_state.llist.append(value)
        elif position <= 0:
            st.session_state.llist.insert(0, value)
        else:
            st.session_state.llist.insert(position, value)

        st.rerun()

    st.markdown("---")

    # ---------------- DELETE ----------------
    st.subheader("Delete Node")

    del_pos = st.number_input(
        "Delete Position (0 based)",
        step=1,
        key="del_pos"
    )

    if st.button("Delete Node"):

        if len(st.session_state.llist) > 0 and del_pos < len(st.session_state.llist):
            st.session_state.llist.pop(del_pos)
            st.rerun()
        else:
            st.warning("Invalid position or empty list")

    st.markdown("---")

    # ---------------- COMPLEXITY ----------------
    st.subheader("Time Complexity")

    st.table({
        "Operation": ["Insert", "Delete", "Search"],
        "Complexity": ["O(n)", "O(n)", "O(n)"]
    })

    st.markdown("---")

    # ---------------- CODE VIEW ----------------
    with st.expander("View C++ Code"):

        st.code("""
#include<iostream>
using namespace std;
struct Node{
	int data;
	Node* next;
	
};
//Function
Node* Insert_Front(Node* head, int info){  //value humna integer ma bheji iss lia int info
	Node* newNode = new Node();
	newNode->data = info;
	newNode->next = head;
	head = newNode;
	
	cout<<"Insert at front position "<<info<<endl;
	return head;
	}
Node* Insert_End(Node* head, int value){
	Node* newNode = new Node();
	newNode->data = value;
	newNode->next = NULL;
	
	if(head == NULL){
		head = newNode;
		}
	else{
		Node* current = head;
		while(current->next != NULL){
			current = current->next;
		}
		current->next = newNode;
		}
	cout<<"Insert at end: "<<value<<endl;
	return head;
		
}
Node* Delete_Front(Node* head){
	if(head == NULL){
		cout<<"List is already empty"<<endl;
		return NULL;
	}
	Node* temp = head;
	head = head->next;
	cout<<"Delete from front "<<temp->data<<endl;
	delete temp;
	return head;
}
Node* Delete_End(Node* head){
	if(head == NULL){
		cout<<"List is already empty"<<endl;
		return NULL;
	}
	if(head->next == NULL){
		cout<<"Delete from end"<<head->data<<endl;
		delete head;
		return NULL;
	}
	Node* current = head;
	while(current->next->next != NULL){
		current = current->next;//null tk phonchaya
	}
	cout<<"Delete from end "<<current->next->data<<endl;
	delete current->next;
	current->next = NULL;
	return head;
}
void Display(Node* head){
	Node* current = head;
	if(head == NULL){
		cout<<"List is empty"<<endl;
		return;
	}
	
	cout<<"Data in the linked list: ";
	while(current != NULL){
		cout<<current->data<<" -> ";
		current = current->next;
	}
	cout<<endl;
}

int main(){
	Node* head = NULL;
	int choice, value;
	
	while(true){
		cout<<"1.Insert at first position"<<endl;
		cout<<"2.Insert at last position"<<endl;
		cout<<"3.Delete at first position"<<endl;
		cout<<"4.Delete at last position"<<endl;
		cout<<"5.Display the list"<<endl;
		cout<<"6.Exit"<<endl;
		
		cout<<"Enter your choice: ";
		cin>>choice;
		
		switch(choice){
			case 1:
				cout<<"Enter value to insert at front: ";
				cin>>value;
				head = Insert_Front(head, value);
				break;
			case 2:
				cout<<"Enter value to insert at last: ";
				cin>>value;
				head = Insert_End(head, value);
				break;
			case 3:
				head = Delete_Front(head);
				break;
			case 4:
				head = Delete_End(head);
				break;
			case 5:
				Display(head);
				break;
			case 6:
				cout<<"Exit Program..."<<endl;
				return 0;
			default:
				cout<<"Invalid choice"<<endl;
		}
	}
}
        """)