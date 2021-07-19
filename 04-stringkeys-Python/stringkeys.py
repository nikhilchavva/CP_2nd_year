def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        d=self.calculate_hash_value(string)
        self.table.insert(d,string)
        return -1
        
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        d=self.calculate_hash_value(string)
        if(self.table[d]==None or self.table[d]!=string):
            return -1
        else:
            return d
       
    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        Hash=(ord(string[0])*100)+ ord(string[1])
        return Hash