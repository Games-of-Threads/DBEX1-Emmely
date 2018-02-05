# Define a function
import os.path
import pickle


# Define a class
class STORE:
    
    def __init__(self, dbname):
        self.dbname = "./" + dbname + "/" +dbname
        if not os.path.exists(dbname):
            os.makedirs(dbname)
        self.memory = {}
        #TODO If Database exist the open the database
        if ( os.path.isfile( self.dbname ) ):
            self.memory = pickle.load( open( self.dbname, "rb" ) )
        else:
            pickle.dump( self.memory, open( self.dbname , "wb" ) )

    def tell_me_about_the_store(self):
        print("This key value store has the name <" + self.dbname + ">.")
        print("The in-memory dictonary is persisted in a file named <" + self.dbname + ">.")
        print("This key value store is persisted on disk in up to ten files named <" + self.dbname + "_[0-9]_store > .")

    def put_val(self, key, value):
        suffix = str(hash( key ))[-1]
        disk_file = self.dbname + "_" + suffix +"_store"  
        self.memory[key] = ''
        store = {}
        if ( os.path.isfile( disk_file ) ):
            store = pickle.load( open( disk_file , "rb" ) )
            print("The store existed .")

        else:
            print("The store created .")
        store[key] = value
        print(store)
        print( "The " + value + " stored in key -> " + key)
        pickle.dump( store, open( disk_file , "wb" ) )
        
    def read_val(self, key):
        suffix = str(hash( key ))[-1]
        disk_file = self.dbname + "_" + suffix +"_store"  
        if key in self.memory:
            if( len(self.memory[key]) > 0 ):
                print( self.memory[key] )
                return self.memory[key]
            else:            
                store = {}
                if ( os.path.isfile( disk_file) ):
                    store = pickle.load( open( disk_file , "rb" ) )
                    print("The store existed in" + disk_file)
                    if( len(store[key]) > 0 ):
                        print( store[key] )
                        self.memory[key] = store[key]
                        return store[key]
                    else:
                        print('key not found')
        else:
            print('No key in memory');
    def delete_val(self, key):
        suffix = str(hash( key ))[-1]
        disk_file = self.dbname + "_" + suffix +"_store"  
        if key in self.memory:
            del self.memory[key]           
        store = {}
        if ( os.path.isfile( disk_file) ):           
            store = pickle.load( open( disk_file , "rb" ) )
            if key in store:
                del store[key]
                pickle.dump( store, open( disk_file , "wb" ) )

        else:
            print('key not found. Nothing was deleted')
   
    def print_all(self):
        z = {}
        for suffix in range(10):
            disk_file = self.dbname + "_" + str(suffix) +"_store"             
            if ( os.path.isfile( disk_file) ):
                store = pickle.load( open( disk_file , "rb" ) )
                if( len( store ) > 0 ):
                    z.update( store )
        print(z)
        return z