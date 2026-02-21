#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

// create an easy way to store uuid and weight simultaneously
struct Crate {
public:
	string uuid;
	int weight;
	Crate(string uuid, int weight) : uuid(uuid), weight(weight) {};
};

class Shelf {
public:
	Crate** arr = new Crate* [4]();
	int weight = 0;
	int lastIndex = 0;

	// Each stack should be stored in a node
	Shelf* next = nullptr;

	// adds a crate to the arr
	void addCrate(Crate* crate) {
		arr[lastIndex++] = crate;
		this->weight += crate->weight;
	}

	// checks if the array can contain the given crate
	bool canAddCrate(const Crate* crate) {
		if (lastIndex == 4) return false;
		if (crate->weight + this->weight > 1000) return false;
		return true;
	}
};

class ArrivalQueueNode {
	// LL containing all the crates
public:
	Crate* crate;
	ArrivalQueueNode* next;
	ArrivalQueueNode(ArrivalQueueNode* next) : next(next) {
		crate = nullptr;
	}
	ArrivalQueueNode() {
		crate = nullptr;
		next = nullptr;
	}
};

class Warehouse {
public:
	// not used, but required
	vector<Crate*> sortingFloor = vector<Crate*>();

	// the 10 shelves must be an array-based stack, but this is redundant
	// because shelves must form a node-backed LL with eachother
	// so this is the implementation of the node-backed LL version
	Shelf* shelvesHead = nullptr;

	// instantiate the arrival queue
	ArrivalQueueNode* arrivalQueueHead = new ArrivalQueueNode();

	// constructor
	Warehouse(vector<Crate*> &crates) {

		// instantiate 10 shelves per warehouse
		for (int i = 0; i < 10; i++) {
			Shelf* currentShelf = this->shelvesHead;
			Shelf* nextShelf = new Shelf();
			nextShelf->next = currentShelf;
			this->shelvesHead = nextShelf;
		}

		// populate the arrivalQueue with all elements from the vector argument
		for (int i = crates.size()-1; i >= 0; i--){
			arrivalQueueHead->crate = crates[i];
			arrivalQueueHead = new ArrivalQueueNode(arrivalQueueHead);
		}

		// get rid of queue node with no value from the loop
		arrivalQueueHead = arrivalQueueHead->next;

		// start populating the shelves with elements from the arrival queue
		this->emptyArrivalQueue();
	}

	// move all elements from arrival queue to shelves
	void emptyArrivalQueue() {
		// get a copy of first shelf pointer
		Shelf* copyShelvesHead = shelvesHead;

		// run until queue is empty
		while (arrivalQueueHead != nullptr) {
			// get crate
			Crate* crate = arrivalQueueHead->crate;
			if (copyShelvesHead->canAddCrate(crate)) {
				// if crate can be added, add it and advance the queue
				copyShelvesHead->addCrate(crate);
				arrivalQueueHead = arrivalQueueHead->next;
			}
			else {
				// if crate cannot be added, go to next shelf and check again
				copyShelvesHead = copyShelvesHead->next;
			}
		}
	}

	// validator
	string validate() {
		string msg = " ";
		Shelf* shelf = this->shelvesHead;

		// iterate through all shelves
		while (shelf != nullptr) {
			msg += "|";

			// if the weight is under the limit, print "Good"
			// otherwise, print "Bad"
			msg += (shelf->weight <= 1000 ? "  Good   " : "   Bad   ");

			// advance shelf pointer
			shelf = shelf->next;
		}
		return msg;
	}
};

int main()
{
	// temporary storage for crates
	// for optimisation can directly add crates to warehouse queue
	vector<Crate*> crates = vector<Crate*>();

	// check if file exists
	ifstream file("crates.txt");
	if (!file) {
		cerr << "File not found!" << endl;
		return -1;
	}
	
	// read all lines from file
	// then create crates from the data
	// and add them to the temporary storage
	int weight;
	string uuid;
	while (file >> weight >> uuid) {
		crates.push_back(new Crate(uuid, weight));
	}

	// instantiate warehouse
	Warehouse w = Warehouse(crates);

	// make a copy of the head of the shelves linked list
	Shelf* head = w.shelvesHead;

	// print the uuid and weight of each crate
	// or lines if the space is empty
	for (int i = 3; i >= 0; i--) {
		Shelf* headCopy = head;
		cout << " ";
		while (headCopy != nullptr) {
			string message = "| ------- ";
			if (headCopy->arr[i] != nullptr) {
				string uuid = headCopy->arr[i]->uuid;
				string weight = to_string(headCopy->arr[i]->weight);
				message = "| " + uuid + " " + weight;
				message += string(5 - weight.length(), ' ');
			}
			cout << message;
			headCopy = headCopy->next;
		}
		cout << endl;
	}

	// validate output
	cout << w.validate() << endl;

	// end program
	return 0;
}
