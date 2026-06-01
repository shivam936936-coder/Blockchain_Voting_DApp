import time
import hashlib
import json


#Creating a class named "Block" to handle block related operations.
class Block: 
    #Method to assign data to block variables.
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce=0
        self.hash256=""
        self.Proof_of_work()   #Calling proof of work function

    #Implementing the concept of Proof of work and finding suitable nonce to reach the hash target
    def Proof_of_work(self):
        hash256 = ""
        while (hash256[:3] != "000"):
            #combining all block data and creating a string
            str1= str(self.index)+ str(self.timestamp)+ str(self.data)+ self.previous_hash+ str(self.nonce)
            #Calling get_hash method to generate hash of the string and storing the returned value in 'hash256'
            hash256 = self.get_hash(str1)
            self.nonce+=1         #incrementing nonce by 1 until target is reached
        self.hash = hash256
        self.nonce -= 1

    #Method to generate hash of a string
    def get_hash(self, str1):
        #Converting the string into bytes and using "sha256" function of the 'haslib' module to generate hash and converting it into hexadecimal using "hexdigest"
        hash256 = hashlib.sha256(str1.encode()).hexdigest()
        return hash256
    
    #Method to convert the block data into a more readable and formatted dictionary
    def to_Dict(self):
        block={
            "Index":self.index ,
            "Timestamp":self.timestamp ,
            "Data":self.data ,
            "Previous Hash":self.previous_hash ,
            "Hash":self.hash ,
            "Nonce":self.nonce
        }
        return block


#Creating a class named "Blockchain" for handling all blockchain related operations
class Blockchain:
    #Method to create an empty list/Blockchain
    def __init__(self):
        self.chain = []
        n=input("Do you want to load the previous blockchain data from blockchain_data.json? (y/n): ")
        if n.lower() == "y":
            self.loadChain()
        elif n.lower() == "n":
            self.genesis_block()  #Calling genesis_block() 
        else:
            print("Invalid input!! Starting with an empty blockchain.")
            self.genesis_block()  #Calling genesis_block()

    #Method to create a genesis block for the blockchain
    def genesis_block(self):
        index = 0
        timestamp = int(time.time())
        data = "Genesis Block"
        previous_hash = "0"*64
        #Creating an object of the class Block named genesis_block
        genesis_block = Block(index, timestamp, data, previous_hash)
        #Converting to dictionary
        block = genesis_block.to_Dict()
        #Adding the block to the list/Blockchain
        self.chain.append(block)

    #Method to add blocks in the blockchain
    def add_block(self, voter_id,candidate):
        #Calling Hasvoted() to check if the voter has already voted and storing the returned value in "voted"
        voted=self.Hasvoted(voter_id)
        #If the voter has not voted, then add the block to the blockchain and return True, else print a message that the voter has already voted.
        if voted==False:
            index = len(self.chain)
            timestamp = int(time.time())
            data = {
                "Voter ID": voter_id,
                "Candidate": candidate
            }
            previous_hash = self.chain[-1]["Hash"]
            new_block = Block(index, timestamp, data, previous_hash)
            block = new_block.to_Dict()
            self.chain.append(block)
            print(voter_id, " has cast a vote for ", candidate)
        else:
            print(voter_id, " has already voted!!")

    #Method to check if a voter has already voted by searching for the voter ID in the blockchain
    def Hasvoted(self,voter_id):
        for block in self.chain[1:]:
            if voter_id == block["Data"]["Voter ID"]:
                return True
        return False

    #Method to check the validity of the blockchain by checking the hash of each block and comparing it with the stored hash and also checking for duplicate votes and invalid candidates.
    def isvalid(self):
        i=0
        validity=True
        for block in self.chain[1:]:
            prev_block=self.chain[i]
            str2=str(block["Index"])+str(block["Timestamp"])+str(block["Data"])+block["Previous Hash"]+str(block["Nonce"])
            temphash=hashlib.sha256(str2.encode()).hexdigest()
            if block["Hash"] == temphash:
                if prev_block["Hash"] == block["Previous Hash"]:
                    for block1 in self.chain[i+2:]:
                        if block["Data"]["Voter ID"] == block1["Data"]["Voter ID"]:
                            print("Duplicate Vote found at block indices: ",block["Index"]," and ",block1["Index"])
                            validity=False
                        elif block["Data"]["Candidate"] not in candis:
                            print("Invalid candidate found at block index: ",block["Index"])
                            validity=False
                else:
                    validity=False
            else:
                validity=False
            i+=1
        return validity
    
    #Method to display the blockchain in a more readable and formatted way
    def viewChain(self):
        for block in self.chain:
            print("\nGenesis Block:- ") if block["Index"]==0 else print("\nBlock:- ")
            print("\tIndex         : ",block["Index"])
            print("\tTimestamp     : ",block["Timestamp"])
            print("\tData          : ",block["Data"])
            print("\tPrevious Hash : ",block["Previous Hash"])
            print("\tHash          : ",block["Hash"])
            print("\tNonce         : ",block["Nonce"])

    #Method to count the votes for each candidate by traversing the blockchain and counting the votes for each candidate and printing the results.
    def CountVotes(self):
        if self.isvalid()==False:
            print("Tampered Blockchain!!\nVote counting aborted!")
            return False
        else:
            vc.clear()
            n=len(candis)
            for i in range(n):
                vc.append(0)
            for block in self.chain[1:]:
                i=candis.index(block["Data"]["Candidate"])
                vc[i] += 1
            print("Vote counting in progress...")
            time.sleep(2)   #Adding a delay of 2 seconds to simulate vote counting process for better user experience.
            print("Vote counting completed!")
            i=0
            while i<n:
                print(candis[i],": ",vc[i]," votes")
                i+=1
            return True
    
    #Method to declare the winner of the election by finding the candidate with the maximum votes and checking for ties.
    def D_winner(self):
        f=self.CountVotes()
        if f:
            maxindex=0
            tie=False
            j=0
            while j<len(vc):
                if vc[j]>vc[maxindex]:
                    maxindex=j
                j+=1
            k=0
            while k<len(vc):
                if vc[k]==vc[maxindex] and k!=maxindex:
                    tie=True
                    break
                k+=1
            if tie:
                print("Voting tied!")
            else:
                print("Winner: ",candis[maxindex])

    #Method to save the blockchain data to a JSON file named "blockchain_data.json" for persistence and future use.
    def saveChain(self):
        with open("blockchain_data.json", "w") as f:
            json.dump(self.chain, f, indent=4)
        f.close()
        print("Blockchain data saved to 'blockchain_data.json'\nExiting the program.")

    #Method to load the blockchain data from the JSON file "blockchain_data.json" and validate the data by checking the hash of each block and also checking for duplicate votes and invalid candidates. If any tampered data is found, it will start with an empty blockchain and create a genesis block.
    def loadChain(self):
        try:
            with open("blockchain_data.json", "r") as f:
                self.chain = json.load(f)
            f.close()
            for block in self.chain[1:]:
                reg_voters.append(block["Data"]["Voter ID"])
                if block["Data"]["Candidate"] not in candis:       
                    candis.append(block["Data"]["Candidate"])
            flag=self.isvalid()
            if flag==False:
                print("Tampered Blockchain data found in 'blockchain_data.json'!!\nStarting with an empty blockchain.")
                self.chain = []
                reg_voters.clear()
                candis.clear()
                self.genesis_block()
            else:
                print("Blockchain data loaded from 'blockchain_data.json'")
        except FileNotFoundError:
            print("No saved blockchain data found. Starting with an empty blockchain.")

#Creating empty lists for registered voters, candidates and vote count for each candidate.
reg_voters=[]
candis=[]
vc=[]

#Creating an object of the class Blockchain named "blockchain"
blockchain=Blockchain()

#Function to register voters by adding their voter ID to the list of registered voters if they are not already registered and printing a message accordingly.
def register_voter(voter_id):
    if voter_id not in reg_voters:
        reg_voters.append(voter_id)
        print(voter_id, " has been registered as a voter.")
    else:
        print(voter_id, " is already registered as a voter.")

#Function to register candidates by adding their name to the list of candidates if they are not already registered and printing a message accordingly.
def register_candidate(name):
    if name not in candis:
        candis.append(name)
        print(name, " has been registered as a candidate.")
    else:
        print(name, " is already registered as a candidate.")

#Taking input for candidates and registering them using the register_candidate() method until the user types 'done'.
if len(candis)==0:
    print("Declare the candidates for the election one by one and press Enter after each candidate. \nType 'done' when finished: ")
    while True:
        candidate_name = input("Candidate Name: ")
        if candidate_name.lower() == 'done':
            break
        register_candidate(candidate_name)


#Displaying the menu and taking input for user choices in an infinite loop until the user chooses to exit by entering '7'.
while True:
    time.sleep(1)   #Adding a delay of 1 second before displaying the menu again for better user experience.
    c=0
    print("\nMENU:")
    print("1.Register Voter")
    print("2.Cast your Vote")
    print("3.View Blockchain")
    print("4.Count Votes")
    print("5.Check Chain Validity")
    print("6.Declare Winner")
    print("7.Exit")
    c=input("Enter your choice: ")
    #Validating user input for menu choices and converting it to an integer if it is a valid choice, else setting it to 0 for invalid choice.
    if c in ['1','2','3','4','5','6','7']:
        c=int(c)
        pass
    else:
        c=0

    match c:
        case 0:
            print("Invalid Choice!!")

        case 1:
            voter_id = input("Create a voter ID (case sensitive): ")
            register_voter(voter_id)

        case 2:
            vid=input("Enter your Voter ID (case sensitive): ")
            if vid not in reg_voters:
                print(vid, " is not a valid voter!!\nPlease register as a voter first.")
            else:
                print("Candidates list:")
                j=0
                while j<len(candis):
                    print(j+1,". ",candis[j])
                    j+=1
                k=input("Enter candidate S.No. to cast your vote: ")
                if k.isdigit() and int(k) in range(1,len(candis)+1):
                    blockchain.add_block(vid, candis[int(k)-1])
                else:
                    print("Invalid S.No.!!")
                
        case 3:
            blockchain.viewChain()

        case 4:
            blockchain.CountVotes()
            
        case 5:
            valid=blockchain.isvalid()
            if valid==True:
                print("Valid Blockchain")
            else:
                print("Invalid Blockchain!")

        case 6:
            blockchain.D_winner()

        case 7:
            n=input("Do you want to save the blockchain data before exiting? (y/n): ")
            if n.lower() == "y":
                blockchain.saveChain()   #Saving the blockchain data to a JSON file before exiting.
            else:
                print("Exiting the program without saving.")
            break

    

