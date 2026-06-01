# 🗳️ Blockchain-Based Voting System

A simple blockchain implementation in Python designed to simulate a secure voting system.  
This project demonstrates how blockchain concepts like **immutability**, **proof of work**, and **hash validation** can be applied to ensure transparency and integrity in elections.

---

## 📌 Features
- **Genesis Block Creation**: Initializes the blockchain with a genesis block.
- **Proof of Work**: Implements a basic PoW mechanism requiring hashes to start with `"000"`.
- **Voter Registration**: Ensures only registered voters can cast votes.
- **Candidate Registration**: Allows dynamic candidate declaration before voting begins.
- **Vote Casting**: Prevents duplicate votes by checking voter IDs.
- **Blockchain Validation**: Detects tampering, duplicate votes, and invalid candidates.
- **Vote Counting**: Tallies votes for each candidate with simulated delay for realism.
- **Winner Declaration**: Announces the winner or detects ties.
- **Persistence**: Saves and loads blockchain data from `blockchain_data.json`.

---

## 🛠️ Tech Stack
- **Language**: Python 3
- **Libraries**: 
  - `hashlib` → SHA-256 hashing
  - `time` → timestamps and delays
  - `json` → persistence of blockchain data

---

## 🚀 How It Works
1. **Register Candidates**: Enter candidate names until typing `done`.
2. **Register Voters**: Create unique voter IDs.
3. **Cast Votes**: Voters select candidates by serial number.
4. **View Blockchain**: Inspect blocks with details like index, timestamp, hash, and nonce.
5. **Count Votes**: Tally votes securely if blockchain is valid.
6. **Check Validity**: Verify chain integrity and detect tampering.
7. **Declare Winner**: Announce election results.
8. **Save/Load Blockchain**: Persist data across sessions.

---

## ▶️ Usage
Run the script in your terminal.
Follow the interactive menu:
MENU:
1. Register Voter
2. Cast your Vote
3. View Blockchain
4. Count Votes
5. Check Chain Validity
6. Declare Winner
7. Exit

---

## 🔒 Security Highlights
- 1.Proof of Work ensures computational effort for block creation.
- 2.Hash Validation prevents tampering with block data.
- 3.Duplicate Vote Detection maintains fairness.
- 4.Candidate Validation ensures only registered candidates receive votes.

---

⚠️ Disclaimer
This project is for educational purposes only.
It demonstrates blockchain concepts in a voting context but is not production-ready for real elections.
